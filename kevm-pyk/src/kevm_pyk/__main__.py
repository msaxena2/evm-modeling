from __future__ import annotations

import json
import logging
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import TYPE_CHECKING

from pathos.pools import ProcessPool  # type: ignore
from pyk.cli.utils import file_path
from pyk.cterm import CTerm
from pyk.kast.outer import KApply, KRewrite, KSort, KToken
from pyk.kcfg import KCFG
from pyk.kore.tools import PrintOutput, kore_print
from pyk.ktool.kompile import LLVMKompileType
from pyk.ktool.krun import KRunOutput
from pyk.prelude.ml import is_top, mlAnd
from pyk.proof import APRProof
from pyk.proof.equality import EqualityProof
from pyk.proof.show import APRProofShow
from pyk.proof.tui import APRProofViewer
from pyk.utils import BugReport, single

from .cli import KEVMCLIArgs, node_id_like
from .config import INCLUDE_DIR, KEVM_LIB
from .gst_to_kore import SORT_ETHEREUM_SIMULATION, gst_to_kore, kore_pgm_to_kore
from .kevm import KEVM, KEVMSemantics, kevm_node_printer
from .kompile import KompileTarget, kevm_kompile
from .utils import ensure_ksequence_on_k_cell, get_apr_proof_for_spec, kevm_prove, legacy_explore, print_failure_info

if TYPE_CHECKING:
    from argparse import Namespace
    from collections.abc import Callable, Iterable
    from typing import Any, Final, TypeVar

    from pyk.kast.outer import KClaim
    from pyk.kcfg.kcfg import NodeIdLike
    from pyk.proof.proof import Proof

    T = TypeVar('T')

_LOGGER: Final = logging.getLogger(__name__)
_LOG_FORMAT: Final = '%(levelname)s %(asctime)s %(name)s - %(message)s'


def _ignore_arg(args: dict[str, Any], arg: str, cli_option: str) -> None:
    if arg in args:
        if args[arg] is not None:
            _LOGGER.warning(f'Ignoring command-line option: {cli_option}')
        args.pop(arg)


def main() -> None:
    sys.setrecursionlimit(15000000)
    parser = _create_argument_parser()
    args = parser.parse_args()
    logging.basicConfig(level=_loglevel(args), format=_LOG_FORMAT)

    executor_name = 'exec_' + args.command.lower().replace('-', '_')
    if executor_name not in globals():
        raise AssertionError(f'Unimplemented command: {args.command}')

    execute = globals()[executor_name]
    execute(**vars(args))


# Command implementation


def exec_version(**kwargs: Any) -> None:
    version_file = KEVM_LIB / 'version'
    version = version_file.read_text().strip()
    print(f'KEVM Version: {version}')


def exec_kompile(
    output_dir: Path | None,
    main_file: Path,
    emit_json: bool,
    includes: list[str],
    main_module: str | None,
    syntax_module: str | None,
    target: KompileTarget | None = None,
    read_only: bool = False,
    ccopts: Iterable[str] = (),
    o0: bool = False,
    o1: bool = False,
    o2: bool = False,
    o3: bool = False,
    debug: bool = False,
    enable_llvm_debug: bool = False,
    llvm_library: bool = False,
    verbose: bool = False,
    **kwargs: Any,
) -> None:
    if target is None:
        target = KompileTarget.LLVM

    optimization = 0
    if o1:
        optimization = 1
    if o2:
        optimization = 2
    if o3:
        optimization = 3

    kevm_kompile(
        target,
        output_dir=output_dir,
        main_file=main_file,
        main_module=main_module,
        syntax_module=syntax_module,
        includes=includes,
        emit_json=emit_json,
        read_only=read_only,
        ccopts=ccopts,
        optimization=optimization,
        enable_llvm_debug=enable_llvm_debug,
        llvm_kompile_type=LLVMKompileType.C if llvm_library else LLVMKompileType.MAIN,
        debug=debug,
        verbose=verbose,
    )


def exec_prove_legacy(
    spec_file: Path,
    definition_dir: Path | None = None,
    includes: Iterable[str] = (),
    bug_report: bool = False,
    save_directory: Path | None = None,
    spec_module: str | None = None,
    claim_labels: Iterable[str] | None = None,
    exclude_claim_labels: Iterable[str] = (),
    debug: bool = False,
    debugger: bool = False,
    max_depth: int | None = None,
    max_counterexamples: int | None = None,
    branching_allowed: int | None = None,
    haskell_backend_args: Iterable[str] = (),
    **kwargs: Any,
) -> None:
    _ignore_arg(kwargs, 'md_selector', f'--md-selector: {kwargs["md_selector"]}')

    if definition_dir is None:
        definition_dir = KompileTarget.HASKELL.definition_dir

    kevm = KEVM(definition_dir, use_directory=save_directory)

    include_dirs = [Path(include) for include in includes]
    include_dirs += [INCLUDE_DIR]

    final_state = kevm.prove_legacy(
        spec_file=spec_file,
        includes=include_dirs,
        bug_report=bug_report,
        spec_module=spec_module,
        claim_labels=claim_labels,
        exclude_claim_labels=exclude_claim_labels,
        debug=debug,
        debugger=debugger,
        max_depth=max_depth,
        max_counterexamples=max_counterexamples,
        branching_allowed=branching_allowed,
        haskell_backend_args=haskell_backend_args,
    )
    final_kast = mlAnd([state.kast for state in final_state])
    print(kevm.pretty_print(final_kast))
    if not is_top(final_kast):
        raise SystemExit(1)


def exec_prove(
    spec_file: Path,
    includes: Iterable[str],
    definition_dir: Path | None = None,
    bug_report: bool = False,
    save_directory: Path | None = None,
    spec_module: str | None = None,
    claim_labels: Iterable[str] | None = None,
    exclude_claim_labels: Iterable[str] = (),
    reinit: bool = False,
    max_depth: int = 1000,
    max_iterations: int | None = None,
    workers: int = 1,
    simplify_init: bool = True,
    break_every_step: bool = False,
    break_on_jumpi: bool = False,
    break_on_calls: bool = True,
    kore_rpc_command: str | Iterable[str] | None = None,
    use_booster: bool = False,
    smt_timeout: int | None = None,
    smt_retry_limit: int | None = None,
    trace_rewrites: bool = False,
    failure_info: bool = True,
    auto_abstract_gas: bool = False,
    **kwargs: Any,
) -> None:
    _ignore_arg(kwargs, 'md_selector', f'--md-selector: {kwargs["md_selector"]}')
    md_selector = 'k & ! node'

    if definition_dir is None:
        definition_dir = KompileTarget.HASKELL.definition_dir

    if smt_timeout is None:
        smt_timeout = 300
    if smt_retry_limit is None:
        smt_retry_limit = 10

    br = BugReport(spec_file.with_suffix('.bug_report')) if bug_report else None
    kevm = KEVM(definition_dir, use_directory=save_directory, bug_report=br)

    include_dirs = [Path(include) for include in includes]
    include_dirs += [INCLUDE_DIR]

    _LOGGER.info(f'Extracting claims from file: {spec_file}')
    claims = kevm.get_claims(
        spec_file,
        spec_module_name=spec_module,
        include_dirs=include_dirs,
        md_selector=md_selector,
        claim_labels=claim_labels,
        exclude_claim_labels=exclude_claim_labels,
    )

    if not claims:
        raise ValueError(f'No claims found in file: {spec_file}')

    if kore_rpc_command is None:
        kore_rpc_command = ('kore-rpc-booster',) if use_booster else ('kore-rpc',)
    elif isinstance(kore_rpc_command, str):
        kore_rpc_command = kore_rpc_command.split()

    def is_functional(claim: KClaim) -> bool:
        claim_lhs = claim.body
        if type(claim_lhs) is KRewrite:
            claim_lhs = claim_lhs.lhs
        return not (type(claim_lhs) is KApply and claim_lhs.label.name == '<generatedTop>')

    def _init_and_run_proof(claim: KClaim) -> tuple[bool, list[str] | None]:
        with legacy_explore(
            kevm,
            kcfg_semantics=KEVMSemantics(auto_abstract_gas=auto_abstract_gas),
            id=claim.label,
            bug_report=br,
            kore_rpc_command=kore_rpc_command,
            smt_timeout=smt_timeout,
            smt_retry_limit=smt_retry_limit,
            trace_rewrites=trace_rewrites,
        ) as kcfg_explore:
            proof_problem: Proof
            if is_functional(claim):
                if (
                    save_directory is not None
                    and not reinit
                    and EqualityProof.proof_exists(claim.label, save_directory)
                ):
                    proof_problem = EqualityProof.read_proof_data(save_directory, claim.label)
                else:
                    proof_problem = EqualityProof.from_claim(claim, kevm.definition, proof_dir=save_directory)
            else:
                if (
                    save_directory is not None
                    and not reinit
                    and APRProof.proof_data_exists(claim.label, save_directory)
                ):
                    proof_problem = APRProof.read_proof_data(save_directory, claim.label)

                else:
                    _LOGGER.info(f'Converting claim to KCFG: {claim.label}')
                    kcfg, init_node_id, target_node_id = KCFG.from_claim(kevm.definition, claim)

                    new_init = ensure_ksequence_on_k_cell(kcfg.node(init_node_id).cterm)
                    new_target = ensure_ksequence_on_k_cell(kcfg.node(target_node_id).cterm)

                    _LOGGER.info(f'Computing definedness constraint for initial node: {claim.label}')
                    new_init = kcfg_explore.cterm_assume_defined(new_init)

                    if simplify_init:
                        _LOGGER.info(f'Simplifying initial and target node: {claim.label}')
                        new_init, _ = kcfg_explore.cterm_simplify(new_init)
                        new_target, _ = kcfg_explore.cterm_simplify(new_target)
                        if CTerm._is_bottom(new_init.kast):
                            raise ValueError(
                                'Simplifying initial node led to #Bottom, are you sure your LHS is defined?'
                            )
                        if CTerm._is_top(new_target.kast):
                            raise ValueError(
                                'Simplifying target node led to #Bottom, are you sure your RHS is defined?'
                            )

                    kcfg.replace_node(init_node_id, new_init)
                    kcfg.replace_node(target_node_id, new_target)

                    proof_problem = APRProof(
                        claim.label, kcfg, [], init_node_id, target_node_id, {}, proof_dir=save_directory
                    )

            passed = kevm_prove(
                kevm,
                proof_problem,
                kcfg_explore,
                max_depth=max_depth,
                max_iterations=max_iterations,
                break_every_step=break_every_step,
                break_on_jumpi=break_on_jumpi,
                break_on_calls=break_on_calls,
            )
            failure_log = None
            if not passed:
                failure_log = print_failure_info(proof_problem, kcfg_explore)

            return passed, failure_log

    results: list[tuple[bool, list[str] | None]]
    if workers > 1:
        with ProcessPool(ncpus=workers) as process_pool:
            results = process_pool.map(_init_and_run_proof, claims)
    else:
        results = []
        for claim in claims:
            results.append(_init_and_run_proof(claim))

    failed = 0
    for claim, r in zip(claims, results, strict=True):
        passed, failure_log = r
        if passed:
            print(f'PROOF PASSED: {claim.label}')
        else:
            failed += 1
            print(f'PROOF FAILED: {claim.label}')
            if failure_info and failure_log is not None:
                for line in failure_log:
                    print(line)

    if failed:
        sys.exit(failed)


def exec_prune_proof(
    definition_dir: Path,
    spec_file: Path,
    node: NodeIdLike,
    includes: Iterable[str] = (),
    save_directory: Path | None = None,
    spec_module: str | None = None,
    claim_labels: Iterable[str] | None = None,
    exclude_claim_labels: Iterable[str] = (),
    **kwargs: Any,
) -> None:
    _ignore_arg(kwargs, 'md_selector', f'--md-selector: {kwargs["md_selector"]}')
    md_selector = 'k & ! node'

    if save_directory is None:
        raise ValueError('Must pass --save-directory to prune-proof!')

    _LOGGER.warning(f'definition_dir: {definition_dir}')
    kevm = KEVM(definition_dir, use_directory=save_directory)

    include_dirs = [Path(include) for include in includes]
    include_dirs += [INCLUDE_DIR]

    _LOGGER.info(f'Extracting claims from file: {spec_file}')
    claim = single(
        kevm.get_claims(
            spec_file,
            spec_module_name=spec_module,
            include_dirs=include_dirs,
            md_selector=md_selector,
            claim_labels=claim_labels,
            exclude_claim_labels=exclude_claim_labels,
        )
    )

    apr_proof = APRProof.read_proof_data(save_directory, claim.label)
    node_ids = apr_proof.prune(node)
    _LOGGER.info(f'Pruned nodes: {node_ids}')
    apr_proof.write_proof_data()


def exec_show_kcfg(
    definition_dir: Path,
    spec_file: Path,
    save_directory: Path | None = None,
    includes: Iterable[str] = (),
    claim_labels: Iterable[str] | None = None,
    exclude_claim_labels: Iterable[str] = (),
    spec_module: str | None = None,
    md_selector: str | None = None,
    nodes: Iterable[NodeIdLike] = (),
    node_deltas: Iterable[tuple[NodeIdLike, NodeIdLike]] = (),
    to_module: bool = False,
    minimize: bool = True,
    failure_info: bool = False,
    sort_collections: bool = False,
    pending: bool = False,
    failing: bool = False,
    **kwargs: Any,
) -> None:
    kevm = KEVM(definition_dir)
    include_dirs = [Path(include) for include in includes]
    include_dirs += [INCLUDE_DIR]
    proof = get_apr_proof_for_spec(
        kevm,
        spec_file,
        save_directory=save_directory,
        spec_module_name=spec_module,
        include_dirs=include_dirs,
        md_selector=md_selector,
        claim_labels=claim_labels,
        exclude_claim_labels=exclude_claim_labels,
    )

    if pending:
        nodes = list(nodes) + [node.id for node in proof.pending]
    if failing:
        nodes = list(nodes) + [node.id for node in proof.failing]

    node_printer = kevm_node_printer(kevm, proof)
    proof_show = APRProofShow(kevm, node_printer=node_printer)

    res_lines = proof_show.show(
        proof,
        nodes=nodes,
        node_deltas=node_deltas,
        to_module=to_module,
        minimize=minimize,
        sort_collections=sort_collections,
    )

    if failure_info:
        with legacy_explore(kevm, kcfg_semantics=KEVMSemantics(), id=proof.id) as kcfg_explore:
            res_lines += print_failure_info(proof, kcfg_explore)

    print('\n'.join(res_lines))


def exec_view_kcfg(
    definition_dir: Path,
    spec_file: Path,
    save_directory: Path | None = None,
    includes: Iterable[str] = (),
    claim_labels: Iterable[str] | None = None,
    exclude_claim_labels: Iterable[str] = (),
    spec_module: str | None = None,
    md_selector: str | None = None,
    **kwargs: Any,
) -> None:
    kevm = KEVM(definition_dir)
    include_dirs = [Path(include) for include in includes]
    include_dirs += [INCLUDE_DIR]
    proof = get_apr_proof_for_spec(
        kevm,
        spec_file,
        save_directory=save_directory,
        spec_module_name=spec_module,
        include_dirs=include_dirs,
        md_selector=md_selector,
        claim_labels=claim_labels,
        exclude_claim_labels=exclude_claim_labels,
    )

    node_printer = kevm_node_printer(kevm, proof)
    proof_view = APRProofViewer(proof, kevm, node_printer=node_printer)

    proof_view.run()


def exec_run(
    input_file: Path,
    expand_macros: bool,
    depth: int | None,
    output: KRunOutput,
    schedule: str,
    mode: str,
    chainid: int,
    target: KompileTarget | None = None,
    save_directory: Path | None = None,
    debugger: bool = False,
    **kwargs: Any,
) -> None:
    if target is None:
        target = KompileTarget.LLVM

    _ignore_arg(kwargs, 'definition_dir', f'--definition: {kwargs["definition_dir"]}')
    kevm = KEVM(target.definition_dir, use_directory=save_directory)

    try:
        json_read = json.loads(input_file.read_text())
        kore_pattern = gst_to_kore(json_read, schedule, mode, chainid)
    except json.JSONDecodeError:
        pgm_token = KToken(input_file.read_text(), KSort('EthereumSimulation'))
        kast_pgm = kevm.parse_token(pgm_token)
        kore_pgm = kevm.kast_to_kore(kast_pgm, sort=KSort('EthereumSimulation'))
        kore_pattern = kore_pgm_to_kore(kore_pgm, SORT_ETHEREUM_SIMULATION, schedule, mode, chainid)

    kevm.run_kore(
        kore_pattern,
        depth=depth,
        term=True,
        expand_macros=expand_macros,
        output=output,
        check=True,
        debugger=debugger,
    )


def exec_kast(
    input_file: Path,
    output: PrintOutput,
    schedule: str,
    mode: str,
    chainid: int,
    target: KompileTarget | None = None,
    save_directory: Path | None = None,
    **kwargs: Any,
) -> None:
    if target is None:
        target = KompileTarget.LLVM

    _ignore_arg(kwargs, 'definition_dir', f'--definition: {kwargs["definition_dir"]}')
    kevm = KEVM(target.definition_dir, use_directory=save_directory)

    try:
        json_read = json.loads(input_file.read_text())
        kore_pattern = gst_to_kore(json_read, schedule, mode, chainid)
    except json.JSONDecodeError:
        pgm_token = KToken(input_file.read_text(), KSort('EthereumSimulation'))
        kast_pgm = kevm.parse_token(pgm_token)
        kore_pgm = kevm.kast_to_kore(kast_pgm)
        kore_pattern = kore_pgm_to_kore(kore_pgm, SORT_ETHEREUM_SIMULATION, schedule, mode, chainid)

    output_text = kore_print(kore_pattern, kevm.definition_dir, output)
    print(output_text)


# Helpers


def _create_argument_parser() -> ArgumentParser:
    def list_of(elem_type: Callable[[str], T], delim: str = ';') -> Callable[[str], list[T]]:
        def parse(s: str) -> list[T]:
            return [elem_type(elem) for elem in s.split(delim)]

        return parse

    kevm_cli_args = KEVMCLIArgs()
    parser = ArgumentParser(prog='kevm-pyk')

    command_parser = parser.add_subparsers(dest='command', required=True)

    command_parser.add_parser('version', help='Print KEVM version and exit.', parents=[kevm_cli_args.logging_args])

    kevm_kompile_args = command_parser.add_parser(
        'kompile',
        help='Kompile KEVM specification.',
        parents=[kevm_cli_args.logging_args, kevm_cli_args.k_args, kevm_cli_args.kompile_args],
    )
    kevm_kompile_args.add_argument('main_file', type=file_path, help='Path to file with main module.')
    kevm_kompile_args.add_argument(
        '--target', type=KompileTarget, help='[llvm|haskell|haskell-standalone|node|foundry]'
    )
    kevm_kompile_args.add_argument(
        '-o', '--output-definition', type=Path, dest='output_dir', help='Path to write kompiled definition to.'
    )

    prove_args = command_parser.add_parser(
        'prove',
        help='Run KEVM proof.',
        parents=[
            kevm_cli_args.logging_args,
            kevm_cli_args.parallel_args,
            kevm_cli_args.k_args,
            kevm_cli_args.kprove_args,
            kevm_cli_args.rpc_args,
            kevm_cli_args.smt_args,
            kevm_cli_args.explore_args,
            kevm_cli_args.spec_args,
        ],
    )
    prove_args.add_argument(
        '--reinit',
        dest='reinit',
        default=False,
        action='store_true',
        help='Reinitialize CFGs even if they already exist.',
    )
    prove_args.add_argument(
        '--use-booster',
        dest='use_booster',
        default=False,
        action='store_true',
        help="Use the booster RPC server instead of kore-rpc. Requires calling kompile with '--target haskell-booster' flag",
    )

    prune_proof_args = command_parser.add_parser(
        'prune-proof',
        help='Remove a node and its successors from the proof state.',
        parents=[
            kevm_cli_args.logging_args,
            kevm_cli_args.k_args,
            kevm_cli_args.spec_args,
        ],
    )
    prune_proof_args.add_argument('node', type=node_id_like, help='Node to remove CFG subgraph from.')

    command_parser.add_parser(
        'prove-legacy',
        help='Run KEVM proof using the legacy kprove binary.',
        parents=[
            kevm_cli_args.logging_args,
            kevm_cli_args.k_args,
            kevm_cli_args.spec_args,
            kevm_cli_args.kprove_legacy_args,
        ],
    )

    command_parser.add_parser(
        'view-kcfg',
        help='Display tree view of CFG',
        parents=[kevm_cli_args.logging_args, kevm_cli_args.k_args, kevm_cli_args.spec_args],
    )

    command_parser.add_parser(
        'show-kcfg',
        help='Display tree show of CFG',
        parents=[
            kevm_cli_args.logging_args,
            kevm_cli_args.k_args,
            kevm_cli_args.kcfg_show_args,
            kevm_cli_args.spec_args,
            kevm_cli_args.display_args,
        ],
    )

    run_args = command_parser.add_parser(
        'run',
        help='Run KEVM test/simulation.',
        parents=[
            kevm_cli_args.logging_args,
            kevm_cli_args.target_args,
            kevm_cli_args.evm_chain_args,
            kevm_cli_args.k_args,
        ],
    )
    run_args.add_argument('input_file', type=file_path, help='Path to input file.')
    run_args.add_argument(
        '--output',
        default=KRunOutput.PRETTY,
        type=KRunOutput,
        choices=list(KRunOutput),
    )
    run_args.add_argument(
        '--expand-macros',
        dest='expand_macros',
        default=True,
        action='store_true',
        help='Expand macros on the input term before execution.',
    )
    run_args.add_argument(
        '--no-expand-macros',
        dest='expand_macros',
        action='store_false',
        help='Do not expand macros on the input term before execution.',
    )
    run_args.add_argument(
        '--debugger',
        dest='debugger',
        action='store_true',
        help='Run GDB debugger for execution.',
    )

    kast_args = command_parser.add_parser(
        'kast',
        help='Run KEVM program.',
        parents=[
            kevm_cli_args.logging_args,
            kevm_cli_args.target_args,
            kevm_cli_args.evm_chain_args,
            kevm_cli_args.k_args,
        ],
    )
    kast_args.add_argument('input_file', type=file_path, help='Path to input file.')
    kast_args.add_argument(
        '--output',
        default=PrintOutput.KORE,
        type=PrintOutput,
        choices=list(PrintOutput),
    )

    return parser


def _loglevel(args: Namespace) -> int:
    if args.debug:
        return logging.DEBUG

    if args.verbose:
        return logging.INFO

    return logging.WARNING


if __name__ == '__main__':
    main()
