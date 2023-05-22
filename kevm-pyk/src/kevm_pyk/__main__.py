from __future__ import annotations

import json
import logging
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import TYPE_CHECKING

from pyk.cli_utils import BugReport, file_path
from pyk.cterm import CTerm
from pyk.kast.outer import KDefinition, KFlatModule, KImport, KRequire
from pyk.kcfg import KCFG, KCFGExplore, KCFGShow, KCFGViewer
from pyk.kore.prelude import int_dv
from pyk.ktool.krun import KRunOutput, _krun
from pyk.prelude.ml import is_bottom
from pyk.proof import APRProof

from .cli import KEVMCLIArgs
from .foundry import (
    Foundry,
    foundry_kompile,
    foundry_list,
    foundry_prove,
    foundry_remove_node,
    foundry_section_edge,
    foundry_show,
    foundry_simplify_node,
    foundry_step_node,
    foundry_to_dot,
)
from .gst_to_kore import _mode_to_kore, _schedule_to_kore
from .kevm import KEVM
from .kompile import KompileTarget, kevm_kompile
from .solc_to_k import Contract, contract_to_main_module, solc_compile
from .utils import arg_pair_of, ensure_ksequence_on_k_cell, get_apr_proof_for_spec, kevm_apr_prove

if TYPE_CHECKING:
    from argparse import Namespace
    from collections.abc import Callable, Iterable
    from typing import Any, Final, TypeVar

    from pyk.kcfg.tui import KCFGElem

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


def exec_compile(contract_file: Path, **kwargs: Any) -> None:
    res = solc_compile(contract_file)
    print(json.dumps(res))


def exec_kompile(
    target: KompileTarget,
    output_dir: Path | None,
    main_file: Path,
    emit_json: bool,
    includes: list[str],
    main_module: str | None,
    syntax_module: str | None,
    read_only: bool = False,
    ccopts: Iterable[str] = (),
    o0: bool = False,
    o1: bool = False,
    o2: bool = False,
    o3: bool = False,
    debug: bool = False,
    enable_llvm_debug: bool = False,
    **kwargs: Any,
) -> None:
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
        debug=debug,
    )


def exec_solc_to_k(
    definition_dir: Path,
    contract_file: Path,
    contract_name: str,
    main_module: str | None,
    requires: list[str],
    imports: list[str],
    **kwargs: Any,
) -> None:
    kevm = KEVM(definition_dir)
    empty_config = kevm.definition.empty_config(KEVM.Sorts.KEVM_CELL)
    solc_json = solc_compile(contract_file)
    contract_json = solc_json['contracts'][contract_file.name][contract_name]
    if 'sources' in solc_json and contract_file.name in solc_json['sources']:
        contract_source = solc_json['sources'][contract_file.name]
        for key in ['id', 'ast']:
            if key not in contract_json and key in contract_source:
                contract_json[key] = contract_source[key]
    contract = Contract(contract_name, contract_json, foundry=False)
    contract_module = contract_to_main_module(contract, empty_config, imports=['EDSL'] + imports)
    _main_module = KFlatModule(
        main_module if main_module else 'MAIN', [], [KImport(mname) for mname in [contract_module.name] + imports]
    )
    modules = (contract_module, _main_module)
    bin_runtime_definition = KDefinition(
        _main_module.name, modules, requires=[KRequire(req) for req in ['edsl.md'] + requires]
    )
    _kprint = KEVM(definition_dir, extra_unparsing_modules=modules)
    print(_kprint.pretty_print(bin_runtime_definition) + '\n')


def exec_foundry_kompile(
    definition_dir: Path,
    foundry_root: Path,
    md_selector: str | None = None,
    includes: Iterable[str] = (),
    regen: bool = False,
    rekompile: bool = False,
    requires: Iterable[str] = (),
    imports: Iterable[str] = (),
    ccopts: Iterable[str] = (),
    llvm_kompile: bool = True,
    debug: bool = False,
    llvm_library: bool = False,
    **kwargs: Any,
) -> None:
    _ignore_arg(kwargs, 'main_module', f'--main-module {kwargs["main_module"]}')
    _ignore_arg(kwargs, 'syntax_module', f'--syntax-module {kwargs["syntax_module"]}')
    _ignore_arg(kwargs, 'spec_module', f'--spec-module {kwargs["spec_module"]}')
    _ignore_arg(kwargs, 'o0', '-O0')
    _ignore_arg(kwargs, 'o1', '-O1')
    _ignore_arg(kwargs, 'o2', '-O2')
    _ignore_arg(kwargs, 'o3', '-O3')
    foundry_kompile(
        definition_dir=definition_dir,
        foundry_root=foundry_root,
        includes=includes,
        md_selector=md_selector,
        regen=regen,
        rekompile=rekompile,
        requires=requires,
        imports=imports,
        ccopts=ccopts,
        llvm_kompile=llvm_kompile,
        debug=debug,
        llvm_library=llvm_library,
    )


def exec_prove(
    definition_dir: Path,
    spec_file: Path,
    includes: list[str],
    bug_report: bool = False,
    save_directory: Path | None = None,
    spec_module: str | None = None,
    md_selector: str | None = None,
    claim_labels: Iterable[str] = (),
    exclude_claim_labels: Iterable[str] = (),
    max_depth: int = 1000,
    max_iterations: int | None = None,
    workers: int = 1,
    simplify_init: bool = True,
    break_every_step: bool = False,
    break_on_jumpi: bool = False,
    break_on_calls: bool = True,
    implication_every_block: bool = True,
    kore_rpc_command: str | Iterable[str] = ('kore-rpc',),
    smt_timeout: int | None = None,
    smt_retry_limit: int | None = None,
    trace_rewrites: bool = False,
    **kwargs: Any,
) -> None:
    br = BugReport(spec_file.with_suffix('.bug_report')) if bug_report else None
    kevm = KEVM(definition_dir, use_directory=save_directory, bug_report=br)

    _LOGGER.info(f'Extracting claims from file: {spec_file}')
    claims = kevm.get_claims(
        spec_file,
        spec_module_name=spec_module,
        include_dirs=[Path(i) for i in includes],
        md_selector=md_selector,
        claim_labels=claim_labels,
        exclude_claim_labels=exclude_claim_labels,
    )

    if isinstance(kore_rpc_command, str):
        kore_rpc_command = kore_rpc_command.split()

    with KCFGExplore(
        kevm,
        id='initializing',
        bug_report=br,
        kore_rpc_command=kore_rpc_command,
        smt_timeout=smt_timeout,
        smt_retry_limit=smt_retry_limit,
        trace_rewrites=trace_rewrites,
    ) as kcfg_explore:
        for claim in claims:
            _LOGGER.info(f'Converting claim to KCFG: {claim.label}')
            kcfg = KCFG.from_claim(kevm.definition, claim)

            new_init = ensure_ksequence_on_k_cell(kcfg.get_unique_init().cterm)
            new_target = ensure_ksequence_on_k_cell(kcfg.get_unique_target().cterm)

            _LOGGER.info(f'Computing definedness constraint for initial node: {claim.label}')
            new_init = kcfg_explore.cterm_assume_defined(new_init)

            if simplify_init:
                _LOGGER.info(f'Simplifying initial and target node: {claim.label}')
                _new_init, _ = kcfg_explore.cterm_simplify(new_init)
                _new_target, _ = kcfg_explore.cterm_simplify(new_target)
                if is_bottom(_new_init):
                    raise ValueError('Simplifying initial node led to #Bottom, are you sure your LHS is defined?')
                if is_bottom(_new_target):
                    raise ValueError('Simplifying target node led to #Bottom, are you sure your RHS is defined?')
                new_init = CTerm.from_kast(_new_init)
                new_target = CTerm.from_kast(_new_target)

            kcfg.replace_node(kcfg.get_unique_init().id, new_init)
            kcfg.replace_node(kcfg.get_unique_target().id, new_target)

            proof_problem = APRProof(claim.label, kcfg, {}, proof_dir=save_directory)

            result = kevm_apr_prove(
                kevm,
                claim.label,
                proof_problem,
                kcfg_explore,
                save_directory=save_directory,
                max_depth=max_depth,
                max_iterations=max_iterations,
                workers=workers,
                break_every_step=break_every_step,
                break_on_jumpi=break_on_jumpi,
                break_on_calls=break_on_calls,
                implication_every_block=implication_every_block,
                is_terminal=KEVM.is_terminal,
                extract_branches=KEVM.extract_branches,
                bug_report=br,
                kore_rpc_command=kore_rpc_command,
                smt_timeout=smt_timeout,
                smt_retry_limit=smt_retry_limit,
                trace_rewrites=trace_rewrites,
            )
            failed = 0
            if result:
                print(f'PROOF PASSED: {proof_problem.id}')
            else:
                failed += 1
                print(f'PROOF FAILED: {proof_problem.id}')
            sys.exit(failed)


def exec_show_kcfg(
    definition_dir: Path,
    spec_file: Path,
    save_directory: Path | None = None,
    includes: Iterable[str] = (),
    claim_labels: Iterable[str] = (),
    exclude_claim_labels: Iterable[str] = (),
    spec_module: str | None = None,
    md_selector: str | None = None,
    nodes: Iterable[str] = (),
    node_deltas: Iterable[tuple[str, str]] = (),
    to_module: bool = False,
    minimize: bool = True,
    **kwargs: Any,
) -> None:
    kevm = KEVM(definition_dir)
    apr_proof = get_apr_proof_for_spec(
        kevm,
        spec_file,
        save_directory=save_directory,
        spec_module_name=spec_module,
        include_dirs=[Path(i) for i in includes],
        md_selector=md_selector,
        claim_labels=claim_labels,
        exclude_claim_labels=exclude_claim_labels,
    )

    kcfg_show = KCFGShow(kevm)
    res_lines = kcfg_show.show(
        apr_proof.id,
        apr_proof.kcfg,
        nodes=nodes,
        node_deltas=node_deltas,
        to_module=to_module,
        minimize=minimize,
        node_printer=kevm.short_info,
    )
    print('\n'.join(res_lines))


def exec_view_kcfg(
    definition_dir: Path,
    spec_file: Path,
    save_directory: Path | None = None,
    includes: Iterable[str] = (),
    claim_labels: Iterable[str] = (),
    exclude_claim_labels: Iterable[str] = (),
    spec_module: str | None = None,
    md_selector: str | None = None,
    **kwargs: Any,
) -> None:
    kevm = KEVM(definition_dir)
    apr_proof = get_apr_proof_for_spec(
        kevm,
        spec_file,
        save_directory=save_directory,
        spec_module_name=spec_module,
        include_dirs=[Path(i) for i in includes],
        md_selector=md_selector,
        claim_labels=claim_labels,
        exclude_claim_labels=exclude_claim_labels,
    )

    viewer = KCFGViewer(apr_proof.kcfg, kevm, node_printer=kevm.short_info)
    viewer.run()


def exec_foundry_prove(
    foundry_root: Path,
    max_depth: int = 1000,
    max_iterations: int | None = None,
    reinit: bool = False,
    tests: Iterable[str] = (),
    exclude_tests: Iterable[str] = (),
    workers: int = 1,
    simplify_init: bool = True,
    break_every_step: bool = False,
    break_on_jumpi: bool = False,
    break_on_calls: bool = True,
    implication_every_block: bool = True,
    bmc_depth: int | None = None,
    bug_report: bool = False,
    kore_rpc_command: str | Iterable[str] = ('kore-rpc',),
    smt_timeout: int | None = None,
    smt_retry_limit: int | None = None,
    trace_rewrites: bool = False,
    **kwargs: Any,
) -> None:
    _ignore_arg(kwargs, 'main_module', f'--main-module: {kwargs["main_module"]}')
    _ignore_arg(kwargs, 'syntax_module', f'--syntax-module: {kwargs["syntax_module"]}')
    _ignore_arg(kwargs, 'definition_dir', f'--definition: {kwargs["definition_dir"]}')
    _ignore_arg(kwargs, 'spec_module', f'--spec-module: {kwargs["spec_module"]}')

    if isinstance(kore_rpc_command, str):
        kore_rpc_command = kore_rpc_command.split()

    results = foundry_prove(
        foundry_root=foundry_root,
        max_depth=max_depth,
        max_iterations=max_iterations,
        reinit=reinit,
        tests=tests,
        exclude_tests=exclude_tests,
        workers=workers,
        simplify_init=simplify_init,
        break_every_step=break_every_step,
        break_on_jumpi=break_on_jumpi,
        break_on_calls=break_on_calls,
        implication_every_block=implication_every_block,
        bmc_depth=bmc_depth,
        bug_report=bug_report,
        kore_rpc_command=kore_rpc_command,
        smt_timeout=smt_timeout,
        smt_retry_limit=smt_retry_limit,
        trace_rewrites=trace_rewrites,
    )
    failed = 0
    for pid, r in results.items():
        if r:
            print(f'PROOF PASSED: {pid}')
        else:
            failed += 1
            print(f'PROOF FAILED: {pid}')
    sys.exit(failed)


def exec_foundry_show(
    foundry_root: Path,
    test: str,
    nodes: Iterable[str] = (),
    node_deltas: Iterable[tuple[str, str]] = (),
    to_module: bool = False,
    minimize: bool = True,
    omit_unstable_output: bool = False,
    frontier: bool = False,
    stuck: bool = False,
    **kwargs: Any,
) -> None:
    output = foundry_show(
        foundry_root=foundry_root,
        test=test,
        nodes=nodes,
        node_deltas=node_deltas,
        to_module=to_module,
        minimize=minimize,
        omit_unstable_output=omit_unstable_output,
        frontier=frontier,
        stuck=stuck,
    )
    print(output)


def exec_foundry_to_dot(foundry_root: Path, test: str, **kwargs: Any) -> None:
    foundry_to_dot(foundry_root=foundry_root, test=test)


def exec_foundry_list(foundry_root: Path, **kwargs: Any) -> None:
    stats = foundry_list(foundry_root=foundry_root)
    print('\n'.join(stats))


def exec_run(
    definition_dir: Path,
    input_file: Path,
    term: bool,
    parser: str | None,
    expand_macros: str,
    depth: int | None,
    output: str,
    schedule: str,
    mode: str,
    chainid: int,
    **kwargs: Any,
) -> None:
    cmap = {
        'MODE': _mode_to_kore(mode).text,
        'SCHEDULE': _schedule_to_kore(schedule).text,
        'CHAINID': int_dv(chainid).text,
    }
    pmap = {'MODE': 'cat', 'SCHEDULE': 'cat', 'CHAINID': 'cat'}
    krun_result = _krun(
        definition_dir=definition_dir,
        input_file=input_file,
        depth=depth,
        term=term,
        no_expand_macros=not expand_macros,
        parser=parser,
        cmap=cmap,
        pmap=pmap,
        output=KRunOutput[output.upper()],
    )
    print(krun_result.stdout)
    sys.exit(krun_result.returncode)


def exec_foundry_view_kcfg(foundry_root: Path, test: str, **kwargs: Any) -> None:
    foundry = Foundry(foundry_root)
    apr_proofs_dir = foundry.out / 'apr_proofs'
    contract_name, test_name = test.split('.')
    proof_digest = foundry.proof_digest(contract_name, test_name)

    apr_proof = APRProof.read_proof(proof_digest, apr_proofs_dir)

    def _short_info(cterm: CTerm) -> Iterable[str]:
        return foundry.short_info_for_contract(contract_name, cterm)

    def _custom_view(elem: KCFGElem) -> Iterable[str]:
        return foundry.custom_view(contract_name, elem)

    viewer = KCFGViewer(apr_proof.kcfg, foundry.kevm, node_printer=_short_info, custom_view=_custom_view)
    viewer.run()


def exec_foundry_remove_node(foundry_root: Path, test: str, node: str, **kwargs: Any) -> None:
    foundry_remove_node(foundry_root=foundry_root, test=test, node=node)


def exec_foundry_simplify_node(
    foundry_root: Path,
    test: str,
    node: str,
    replace: bool = False,
    minimize: bool = True,
    bug_report: bool = False,
    smt_timeout: int | None = None,
    smt_retry_limit: int | None = None,
    trace_rewrites: bool = False,
    **kwargs: Any,
) -> None:
    pretty_term = foundry_simplify_node(
        foundry_root=foundry_root,
        test=test,
        node=node,
        replace=replace,
        minimize=minimize,
        bug_report=bug_report,
        smt_timeout=smt_timeout,
        smt_retry_limit=smt_retry_limit,
        trace_rewrites=trace_rewrites,
    )
    print(f'Simplified:\n{pretty_term}')


def exec_foundry_step_node(
    foundry_root: Path,
    test: str,
    node: str,
    repeat: int = 1,
    depth: int = 1,
    bug_report: bool = False,
    smt_timeout: int | None = None,
    smt_retry_limit: int | None = None,
    trace_rewrites: bool = False,
    **kwargs: Any,
) -> None:
    foundry_step_node(
        foundry_root=foundry_root,
        test=test,
        node=node,
        repeat=repeat,
        depth=depth,
        bug_report=bug_report,
        smt_timeout=smt_timeout,
        smt_retry_limit=smt_retry_limit,
        trace_rewrites=trace_rewrites,
    )


def exec_foundry_section_edge(
    foundry_root: Path,
    test: str,
    edge: tuple[str, str],
    sections: int = 2,
    replace: bool = False,
    bug_report: bool = False,
    smt_timeout: int | None = None,
    smt_retry_limit: int | None = None,
    trace_rewrites: bool = False,
    **kwargs: Any,
) -> None:
    foundry_section_edge(
        foundry_root=foundry_root,
        test=test,
        edge=edge,
        sections=sections,
        replace=replace,
        bug_report=bug_report,
        smt_timeout=smt_timeout,
        smt_retry_limit=smt_retry_limit,
        trace_rewrites=trace_rewrites,
    )


# Helpers


def _create_argument_parser() -> ArgumentParser:
    def list_of(elem_type: Callable[[str], T], delim: str = ';') -> Callable[[str], list[T]]:
        def parse(s: str) -> list[T]:
            return [elem_type(elem) for elem in s.split(delim)]

        return parse

    kevm_cli_args = KEVMCLIArgs()

    parser = ArgumentParser(prog='python3 -m kevm_pyk')

    command_parser = parser.add_subparsers(dest='command', required=True)

    kevm_kompile_args = command_parser.add_parser(
        'kompile',
        help='Kompile KEVM specification.',
        parents=[kevm_cli_args.shared_args, kevm_cli_args.k_args, kevm_cli_args.kompile_args],
    )
    kevm_kompile_args.add_argument('main_file', type=file_path, help='Path to file with main module.')
    kevm_kompile_args.add_argument(
        '--target', type=KompileTarget, help='[llvm|haskell|haskell-standalone|node|foundry]'
    )
    kevm_kompile_args.add_argument(
        '-o', '--output-definition', type=Path, dest='output_dir', help='Path to write kompiled definition to.'
    )

    _ = command_parser.add_parser(
        'prove',
        help='Run KEVM proof.',
        parents=[
            kevm_cli_args.shared_args,
            kevm_cli_args.k_args,
            kevm_cli_args.kprove_args,
            kevm_cli_args.rpc_args,
            kevm_cli_args.smt_args,
            kevm_cli_args.explore_args,
            kevm_cli_args.spec_args,
        ],
    )

    _ = command_parser.add_parser(
        'view-kcfg',
        help='Display tree view of CFG',
        parents=[kevm_cli_args.shared_args, kevm_cli_args.k_args, kevm_cli_args.spec_args],
    )

    _ = command_parser.add_parser(
        'show-kcfg',
        help='Display tree show of CFG',
        parents=[
            kevm_cli_args.shared_args,
            kevm_cli_args.k_args,
            kevm_cli_args.kcfg_show_args,
            kevm_cli_args.spec_args,
            kevm_cli_args.display_args,
        ],
    )

    run_args = command_parser.add_parser(
        'run',
        help='Run KEVM test/simulation.',
        parents=[kevm_cli_args.shared_args, kevm_cli_args.evm_chain_args, kevm_cli_args.k_args],
    )
    run_args.add_argument('input_file', type=file_path, help='Path to input file.')
    run_args.add_argument(
        '--term', default=False, action='store_true', help='<input_file> is the entire term to execute.'
    )
    run_args.add_argument('--parser', default=None, type=str, help='Parser to use for $PGM.')
    run_args.add_argument(
        '--output',
        default='pretty',
        type=str,
        help='Output format to use, one of [pretty|program|kast|binary|json|latex|kore|none].',
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

    solc_args = command_parser.add_parser('compile', help='Generate combined JSON with solc compilation results.')
    solc_args.add_argument('contract_file', type=file_path, help='Path to contract file.')

    solc_to_k_args = command_parser.add_parser(
        'solc-to-k',
        help='Output helper K definition for given JSON output from solc compiler.',
        parents=[kevm_cli_args.shared_args, kevm_cli_args.k_args, kevm_cli_args.k_gen_args],
    )
    solc_to_k_args.add_argument('contract_file', type=file_path, help='Path to contract file.')
    solc_to_k_args.add_argument('contract_name', type=str, help='Name of contract to generate K helpers for.')

    foundry_kompile = command_parser.add_parser(
        'foundry-kompile',
        help='Kompile K definition corresponding to given output directory.',
        parents=[
            kevm_cli_args.shared_args,
            kevm_cli_args.k_args,
            kevm_cli_args.k_gen_args,
            kevm_cli_args.kompile_args,
            kevm_cli_args.foundry_args,
        ],
    )
    foundry_kompile.add_argument(
        '--regen',
        dest='regen',
        default=False,
        action='store_true',
        help='Regenerate foundry.k even if it already exists.',
    )
    foundry_kompile.add_argument(
        '--rekompile',
        dest='rekompile',
        default=False,
        action='store_true',
        help='Rekompile foundry.k even if kompiled definition already exists.',
    )

    foundry_prove_args = command_parser.add_parser(
        'foundry-prove',
        help='Run Foundry Proof.',
        parents=[
            kevm_cli_args.shared_args,
            kevm_cli_args.k_args,
            kevm_cli_args.kprove_args,
            kevm_cli_args.smt_args,
            kevm_cli_args.rpc_args,
            kevm_cli_args.explore_args,
            kevm_cli_args.foundry_args,
        ],
    )
    foundry_prove_args.add_argument(
        '--test',
        type=str,
        dest='tests',
        default=[],
        action='append',
        help='Limit to only listed tests, ContractName.TestName',
    )
    foundry_prove_args.add_argument(
        '--exclude-test',
        type=str,
        dest='exclude_tests',
        default=[],
        action='append',
        help='Skip listed tests, ContractName.TestName',
    )
    foundry_prove_args.add_argument(
        '--reinit',
        dest='reinit',
        default=False,
        action='store_true',
        help='Reinitialize CFGs even if they already exist.',
    )
    foundry_prove_args.add_argument(
        '--bmc-depth',
        dest='bmc_depth',
        default=None,
        type=int,
        help='Max depth of loop unrolling during bounded model checking',
    )

    foundry_show_args = command_parser.add_parser(
        'foundry-show',
        help='Display a given Foundry CFG.',
        parents=[
            kevm_cli_args.shared_args,
            kevm_cli_args.k_args,
            kevm_cli_args.kcfg_show_args,
            kevm_cli_args.display_args,
            kevm_cli_args.foundry_args,
        ],
    )
    foundry_show_args.add_argument('test', type=str, help='Display the CFG for this test.')
    foundry_show_args.add_argument(
        '--omit-unstable-output',
        dest='omit_unstable_output',
        default=False,
        action='store_true',
        help='Strip output that is likely to change without the contract logic changing',
    )
    foundry_show_args.add_argument(
        '--frontier', dest='frontier', default=False, action='store_true', help='Also display frontier nodes'
    )
    foundry_show_args.add_argument(
        '--stuck', dest='stuck', default=False, action='store_true', help='Also display stuck nodes'
    )
    foundry_to_dot = command_parser.add_parser(
        'foundry-to-dot',
        help='Dump the given CFG for the test as DOT for visualization.',
        parents=[kevm_cli_args.shared_args, kevm_cli_args.foundry_args],
    )
    foundry_to_dot.add_argument('test', type=str, help='Display the CFG for this test.')

    command_parser.add_parser(
        'foundry-list',
        help='List information about CFGs on disk',
        parents=[kevm_cli_args.shared_args, kevm_cli_args.k_args, kevm_cli_args.foundry_args],
    )

    foundry_view_kcfg_args = command_parser.add_parser(
        'foundry-view-kcfg',
        help='Display tree view of CFG',
        parents=[kevm_cli_args.shared_args, kevm_cli_args.foundry_args],
    )
    foundry_view_kcfg_args.add_argument('test', type=str, help='View the CFG for this test.')

    foundry_remove_node = command_parser.add_parser(
        'foundry-remove-node',
        help='Remove a node and its successors.',
        parents=[kevm_cli_args.shared_args, kevm_cli_args.foundry_args],
    )
    foundry_remove_node.add_argument('test', type=str, help='View the CFG for this test.')
    foundry_remove_node.add_argument('node', type=str, help='Node to remove CFG subgraph from.')

    foundry_simplify_node = command_parser.add_parser(
        'foundry-simplify-node',
        help='Simplify a given node, and potentially replace it.',
        parents=[
            kevm_cli_args.shared_args,
            kevm_cli_args.smt_args,
            kevm_cli_args.rpc_args,
            kevm_cli_args.display_args,
            kevm_cli_args.foundry_args,
        ],
    )
    foundry_simplify_node.add_argument('test', type=str, help='Simplify node in this CFG.')
    foundry_simplify_node.add_argument('node', type=str, help='Node to simplify in CFG.')
    foundry_simplify_node.add_argument(
        '--replace', default=False, help='Replace the original node with the simplified variant in the graph.'
    )

    foundry_step_node = command_parser.add_parser(
        'foundry-step-node',
        help='Step from a given node, adding it to the CFG.',
        parents=[kevm_cli_args.shared_args, kevm_cli_args.rpc_args, kevm_cli_args.smt_args, kevm_cli_args.foundry_args],
    )
    foundry_step_node.add_argument('test', type=str, help='Step from node in this CFG.')
    foundry_step_node.add_argument('node', type=str, help='Node to step from in CFG.')
    foundry_step_node.add_argument(
        '--repeat', type=int, default=1, help='How many node expansions to do from the given start node (>= 1).'
    )
    foundry_step_node.add_argument(
        '--depth', type=int, default=1, help='How many steps to take from initial node on edge.'
    )

    foundry_section_edge = command_parser.add_parser(
        'foundry-section-edge',
        help='Given an edge in the graph, cut it into sections to get intermediate nodes.',
        parents=[kevm_cli_args.shared_args, kevm_cli_args.rpc_args, kevm_cli_args.smt_args, kevm_cli_args.foundry_args],
    )
    foundry_section_edge.add_argument('test', type=str, help='Section edge in this CFG.')
    foundry_section_edge.add_argument('edge', type=arg_pair_of(str, str), help='Edge to section in CFG.')
    foundry_section_edge.add_argument(
        '--sections', type=int, default=2, help='Number of sections to make from edge (>= 2).'
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
