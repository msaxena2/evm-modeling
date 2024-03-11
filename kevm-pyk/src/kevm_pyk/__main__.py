from __future__ import annotations

import contextlib
import graphlib
import json
import logging
import os
import sys
import tempfile
import time
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING

from pathos.pools import ProcessPool  # type: ignore
from pyk.cli.args import (
    BugReportOptions,
    KompileOptions,
    LoggingOptions,
    ParallelOptions,
    SaveDirOptions,
    SMTOptions,
    SpecOptions,
)
from pyk.cli.cli import CLI, Command
from pyk.cli.utils import file_path
from pyk.cterm import CTerm
from pyk.kast.outer import KApply, KRewrite, KSort, KToken
from pyk.kcfg import KCFG
from pyk.kdist import kdist
from pyk.kore.tools import PrintOutput, kore_print
from pyk.ktool.kompile import LLVMKompileType
from pyk.ktool.krun import KRunOutput
from pyk.prelude.ml import is_top, mlOr
from pyk.proof.implies import EqualityProof
from pyk.proof.reachability import APRProof
from pyk.proof.show import APRProofShow
from pyk.proof.tui import APRProofViewer
from pyk.utils import FrozenDict, hash_str, single

from . import VERSION, config
from .cli import (
    EVMChainOptions,
    ExploreOptions,
    KEVMDisplayOptions,
    KOptions,
    KProveLegacyOptions,
    KProveOptions,
    RPCOptions,
    TargetOptions,
)
from .gst_to_kore import SORT_ETHEREUM_SIMULATION, gst_to_kore, kore_pgm_to_kore
from .kevm import KEVM, KEVMSemantics, kevm_node_printer
from .kompile import KompileTarget, kevm_kompile
from .utils import (
    arg_pair_of,
    claim_dependency_dict,
    ensure_ksequence_on_k_cell,
    get_apr_proof_for_spec,
    legacy_explore,
    print_failure_info,
    run_prover,
)

if TYPE_CHECKING:
    from argparse import ArgumentParser
    from collections.abc import Callable, Iterable, Iterator
    from typing import Any, Final, TypeVar

    from pyk.kast.outer import KClaim
    from pyk.kcfg.kcfg import NodeIdLike
    from pyk.kcfg.tui import KCFGElem
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

    kevm_cli = CLI(
        (
            KastCommand,
            KompileSpecCommand,
            ProveLegacyCommand,
            ProveCommand,
            PruneCommand,
            RunCommand,
            ShowKCFGCommand,
            VersionCommand,
            ViewKCFGCommand,
        )
    )
    command = kevm_cli.get_command()
    assert isinstance(command, LoggingOptions)
    logging.basicConfig(level=_loglevel(command), format=_LOG_FORMAT)
    command.exec()


class KompileSpecCommand(Command, KOptions, KompileOptions, LoggingOptions):
    main_file: Path
    target: KompileTarget
    output_dir: Path
    debug_build: bool

    @staticmethod
    def name() -> str:
        return 'kompile-spec'

    @staticmethod
    def help_str() -> str:
        return 'Kompile KEVM specification.'

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'debug_build': False,
            'output_dir': Path(),
            'target': KompileTarget.HASKELL,
        }

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument('main_file', type=file_path, help='Path to file with main module.')
        parser.add_argument('--target', type=KompileTarget, help='[haskell|maude]')
        parser.add_argument(
            '-o', '--output-definition', type=Path, dest='output_dir', help='Path to write kompiled definition to.'
        )
        parser.add_argument('--debug-build', dest='debug_build', help='Enable debug symbols in LLVM builds.')

    def exec(self) -> None:
        if self.target not in [KompileTarget.HASKELL, KompileTarget.MAUDE]:
            raise ValueError(f'Can only call kevm kompile-spec with --target [haskell,maude], got: {self.target.value}')

        optimization = 0
        if self.o1:
            optimization = 1
        if self.o2:
            optimization = 2
        if self.o3:
            optimization = 3
        if self.debug_build:
            optimization = 0

        kevm_kompile(
            self.target,
            output_dir=self.output_dir,
            main_file=self.main_file,
            main_module=self.main_module,
            syntax_module=self.syntax_module,
            includes=self.includes,
            emit_json=self.emit_json,
            read_only=self.read_only,
            ccopts=self.ccopts,
            optimization=optimization,
            enable_llvm_debug=self.enable_llvm_debug,
            llvm_kompile_type=LLVMKompileType.C if self.llvm_library else LLVMKompileType.MAIN,
            debug_build=self.debug_build,
            debug=self.debug,
            verbose=self.verbose,
        )


class ShowKCFGCommand(Command, KOptions, SpecOptions, KEVMDisplayOptions, LoggingOptions):
    nodes: list[NodeIdLike]
    node_deltas: list[tuple[NodeIdLike, NodeIdLike]]
    failure_info: bool
    to_module: bool
    pending: bool
    failing: bool
    counterexample_info: bool

    @staticmethod
    def name() -> str:
        return 'show-kcfg'

    @staticmethod
    def help_str() -> str:
        return 'Print the CFG for a given proof.'

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'failure_info': False,
            'to_module': False,
            'pending': False,
            'failing': False,
            'counterexample_info': False,
            'nodes': [],
            'node_deltas': [],
        }

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument(
            '--node',
            type=node_id_like,
            dest='nodes',
            action='append',
            help='List of nodes to display as well.',
        )
        parser.add_argument(
            '--node-delta',
            type=arg_pair_of(node_id_like, node_id_like),
            dest='node_deltas',
            action='append',
            help='List of nodes to display delta for.',
        )
        parser.add_argument(
            '--failure-information',
            dest='failure_info',
            action='store_true',
            help='Show failure summary for cfg',
        )
        parser.add_argument(
            '--no-failure-information',
            dest='failure_info',
            action='store_false',
            help='Do not show failure summary for cfg',
        )
        parser.add_argument('--to-module', dest='to_module', action='store_true', help='Output edges as a K module.')
        parser.add_argument('--pending', dest='pending', action='store_true', help='Also display pending nodes')
        parser.add_argument('--failing', dest='failing', action='store_true', help='Also display failing nodes')
        parser.add_argument(
            '--counterexample-information',
            dest='counterexample_info',
            action='store_true',
            help="Show models for failing nodes. Should be called with the '--failure-information' flag",
        )

    def exec(self) -> None:
        if self.definition_dir is None:
            raise ValueError('Must pass --definition to show-kcfg!')

        kevm = KEVM(self.definition_dir)
        include_dirs = [Path(include) for include in self.includes]
        include_dirs += config.INCLUDE_DIRS
        proof = get_apr_proof_for_spec(
            kevm,
            self.spec_file,
            save_directory=self.save_directory,
            spec_module_name=self.spec_module,
            include_dirs=include_dirs,
            md_selector=self.md_selector,
            claim_labels=self.claim_labels,
            exclude_claim_labels=self.exclude_claim_labels,
        )

        nodes = []
        if self.pending:
            nodes = list(self.nodes) + [node.id for node in proof.pending]
        if self.failing:
            nodes = list(self.nodes) + [node.id for node in proof.failing]

        node_printer = kevm_node_printer(kevm, proof)
        proof_show = APRProofShow(kevm, node_printer=node_printer)

        res_lines = proof_show.show(
            proof,
            nodes=nodes,
            node_deltas=self.node_deltas,
            to_module=self.to_module,
            minimize=self.minimize,
            sort_collections=self.sort_collections,
        )

        if self.failure_info:
            with legacy_explore(kevm, kcfg_semantics=KEVMSemantics(), id=proof.id) as kcfg_explore:
                res_lines += print_failure_info(proof, kcfg_explore)

        print('\n'.join(res_lines))


def node_id_like(s: str) -> NodeIdLike:
    try:
        return int(s)
    except ValueError:
        return s


class ZeroProcessPool:
    def map(self, f: Callable[[Any], Any], xs: list[Any]) -> list[Any]:
        return [f(x) for x in xs]


class JSONEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, FrozenDict):
            return json.JSONEncoder.encode(self, dict(obj))
        return json.JSONEncoder.default(self, obj)


@dataclass(frozen=True)
class KClaimJob:
    claim: KClaim
    dependencies: frozenset[KClaimJob]

    @cached_property
    def digest(self) -> str:
        deps_digest = ''.join([dep.digest for dep in self.dependencies])
        claim_hash = hash_str(json.dumps(self.claim.to_dict(), sort_keys=True, cls=JSONEncoder))
        return hash_str(f'{claim_hash}{deps_digest}')

    def up_to_date(self, digest_file: Path | None) -> bool:
        if not isinstance(digest_file, Path) or not digest_file.exists():
            return False
        digest_dict = json.loads(digest_file.read_text())
        if 'claims' not in digest_dict:
            digest_dict['claims'] = {}
            digest_file.write_text(json.dumps(digest_dict, indent=4))
        if self.claim.label not in digest_dict['claims']:
            return False
        return digest_dict['claims'][self.claim.label] == self.digest

    def update_digest(self, digest_file: Path | None) -> None:
        if digest_file is None:
            return
        digest_dict = {}
        if digest_file.exists():
            digest_dict = json.loads(digest_file.read_text())
        if 'claims' not in digest_dict:
            digest_dict['claims'] = {}
        digest_dict['claims'][self.claim.label] = self.digest
        digest_file.write_text(json.dumps(digest_dict, indent=4))

        _LOGGER.info(f'Updated claim {self.claim.label} in digest file: {digest_file}')


def init_claim_jobs(spec_module_name: str, claims: list[KClaim]) -> frozenset[KClaimJob]:
    labels_to_claims = {claim.label: claim for claim in claims}
    labels_to_claim_jobs: dict[str, KClaimJob] = {}

    def get_or_load_claim_job(claim_label: str) -> KClaimJob:
        if claim_label not in labels_to_claim_jobs:
            if claim_label in labels_to_claims:
                claim = labels_to_claims[claim_label]
            elif f'{spec_module_name}.{claim_label}' in labels_to_claims:
                claim = labels_to_claims[f'{spec_module_name}.{claim_label}']
            else:
                raise ValueError(f'Claim with label {claim_label} not found.')
            deps = frozenset({get_or_load_claim_job(dep_label) for dep_label in claim.dependencies})
            claim_job = KClaimJob(claim, deps)
            labels_to_claim_jobs[claim_label] = claim_job
        return labels_to_claim_jobs[claim_label]

    return frozenset({get_or_load_claim_job(claim.label) for claim in claims})


@contextlib.contextmanager
def wrap_process_pool(workers: int) -> Iterator[ZeroProcessPool | ProcessPool]:
    if workers <= 1:
        yield ZeroProcessPool()
    else:
        with ProcessPool(ncpus=workers) as pp:
            yield pp


class ProveCommand(
    Command,
    KOptions,
    ParallelOptions,
    KProveOptions,
    BugReportOptions,
    SMTOptions,
    ExploreOptions,
    SpecOptions,
    RPCOptions,
    LoggingOptions,
):
    reinit: bool

    @staticmethod
    def name() -> str:
        return 'prove'

    @staticmethod
    def help_str() -> str:
        return 'Run KEVM proof.'

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'reinit': False,
        }

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument(
            '--reinit',
            dest='reinit',
            action='store_true',
            help='Reinitialize CFGs even if they already exist.',
        )

    def exec(self) -> None:
        md_selector = 'k'

        save_directory = self.save_directory if self.save_directory is not None else Path(tempfile.mkdtemp())
        digest_file = save_directory / 'digest'

        definition_dir = self.definition_dir if self.definition_dir is not None else kdist.get('evm-semantics.haskell')

        kevm = KEVM(definition_dir, use_directory=save_directory, bug_report=self.bug_report)

        include_dirs = [Path(include) for include in self.includes]
        include_dirs += config.INCLUDE_DIRS

        kore_rpc_command: Iterable[str]
        if self.kore_rpc_command is None:
            kore_rpc_command = ('kore-rpc-booster',) if self.use_booster else ('kore-rpc',)
        elif isinstance(self.kore_rpc_command, str):
            kore_rpc_command = self.kore_rpc_command.split()

        def is_functional(claim: KClaim) -> bool:
            claim_lhs = claim.body
            if type(claim_lhs) is KRewrite:
                claim_lhs = claim_lhs.lhs
            return not (type(claim_lhs) is KApply and claim_lhs.label.name == '<generatedTop>')

        llvm_definition_dir = definition_dir / 'llvm-library' if self.use_booster else None

        _LOGGER.info(f'Extracting claims from file: {self.spec_file}')
        all_claims = kevm.get_claims(
            self.spec_file,
            spec_module_name=self.spec_module,
            include_dirs=include_dirs,
            md_selector=md_selector,
            claim_labels=self.claim_labels,
            exclude_claim_labels=self.exclude_claim_labels,
        )
        if all_claims is None:
            raise ValueError(f'No claims found in file: {self.spec_file}')
        spec_module_name = (
            self.spec_module if self.spec_module is not None else os.path.splitext(self.spec_file.name)[0].upper()
        )
        all_claim_jobs = init_claim_jobs(spec_module_name, all_claims)
        all_claim_jobs_by_label = {c.claim.label: c for c in all_claim_jobs}
        claims_graph = claim_dependency_dict(all_claims, spec_module_name=spec_module_name)

        def _init_and_run_proof(claim_job: KClaimJob) -> tuple[bool, list[str] | None]:
            claim = claim_job.claim
            up_to_date = claim_job.up_to_date(digest_file)
            if up_to_date:
                _LOGGER.info(f'Claim is up to date: {claim.label}')
            else:
                _LOGGER.info(f'Claim reinitialized because it is out of date: {claim.label}')
            claim_job.update_digest(digest_file)
            with legacy_explore(
                kevm,
                kcfg_semantics=KEVMSemantics(auto_abstract_gas=self.auto_abstract_gas),
                id=claim.label,
                llvm_definition_dir=llvm_definition_dir,
                bug_report=self.bug_report,
                kore_rpc_command=kore_rpc_command,
                smt_timeout=self.smt_timeout,
                smt_retry_limit=self.smt_retry_limit,
                trace_rewrites=self.trace_rewrites,
                fallback_on=self.fallback_on,
                interim_simplification=self.interim_simplification,
                no_post_exec_simplify=(not self.post_exec_simplify),
            ) as kcfg_explore:
                proof_problem: Proof
                if is_functional(claim):
                    if not self.reinit and up_to_date and EqualityProof.proof_exists(claim.label, save_directory):
                        proof_problem = EqualityProof.read_proof_data(save_directory, claim.label)
                    else:
                        proof_problem = EqualityProof.from_claim(claim, kevm.definition, proof_dir=save_directory)
                else:
                    if not self.reinit and up_to_date and APRProof.proof_data_exists(claim.label, save_directory):
                        proof_problem = APRProof.read_proof_data(save_directory, claim.label)

                    else:
                        _LOGGER.info(f'Converting claim to KCFG: {claim.label}')
                        kcfg, init_node_id, target_node_id = KCFG.from_claim(kevm.definition, claim)

                        new_init = ensure_ksequence_on_k_cell(kcfg.node(init_node_id).cterm)
                        new_target = ensure_ksequence_on_k_cell(kcfg.node(target_node_id).cterm)

                        _LOGGER.info(f'Computing definedness constraint for initial node: {claim.label}')
                        new_init = kcfg_explore.cterm_symbolic.assume_defined(new_init)

                        _LOGGER.info(f'Simplifying initial and target node: {claim.label}')
                        new_init, _ = kcfg_explore.cterm_symbolic.simplify(new_init)
                        new_target, _ = kcfg_explore.cterm_symbolic.simplify(new_target)
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
                            claim.label,
                            kcfg,
                            [],
                            init_node_id,
                            target_node_id,
                            {},
                            proof_dir=save_directory,
                            subproof_ids=claims_graph[claim.label],
                            admitted=claim.is_trusted,
                        )

                if proof_problem.admitted:
                    proof_problem.write_proof_data()
                    _LOGGER.info(f'Skipping execution of proof because it is marked as admitted: {proof_problem.id}')
                    return True, None

                start_time = time.time()
                passed = run_prover(
                    proof_problem,
                    kcfg_explore,
                    max_depth=self.max_depth,
                    max_iterations=self.max_iterations,
                    cut_point_rules=KEVMSemantics.cut_point_rules(
                        self.break_on_jumpi,
                        self.break_on_calls,
                        self.break_on_storage,
                        self.break_on_basic_blocks,
                    ),
                    terminal_rules=KEVMSemantics.terminal_rules(self.break_every_step),
                    fail_fast=self.fail_fast,
                    always_check_subsumption=self.always_check_subsumption,
                    fast_check_subsumption=self.fast_check_subsumption,
                )
                end_time = time.time()
                _LOGGER.info(f'Proof timing {proof_problem.id}: {end_time - start_time}s')
                failure_log = None
                if not passed:
                    failure_log = print_failure_info(proof_problem, kcfg_explore)

                return passed, failure_log

        topological_sorter = graphlib.TopologicalSorter(claims_graph)
        topological_sorter.prepare()
        with wrap_process_pool(workers=self.workers) as process_pool:
            selected_results: list[tuple[bool, list[str] | None]] = []
            selected_claims = []
            while topological_sorter.is_active():
                ready = topological_sorter.get_ready()
                _LOGGER.info(f'Discharging proof obligations: {ready}')
                curr_claim_list = [all_claim_jobs_by_label[label] for label in ready]
                results: list[tuple[bool, list[str] | None]] = process_pool.map(_init_and_run_proof, curr_claim_list)
                for label in ready:
                    topological_sorter.done(label)
                selected_results.extend(results)
                selected_claims.extend(curr_claim_list)

        failed = 0
        for job, r in zip(selected_claims, selected_results, strict=True):
            passed, failure_log = r
            if passed:
                print(f'PROOF PASSED: {job.claim.label}')
            else:
                failed += 1
                print(f'PROOF FAILED: {job.claim.label}')
                if self.failure_info and failure_log is not None:
                    for line in failure_log:
                        print(line)

        if failed:
            sys.exit(failed)


class VersionCommand(Command, LoggingOptions):
    @staticmethod
    def name() -> str:
        return 'version'

    @staticmethod
    def help_str() -> str:
        return 'Print KEVM version and exit.'

    def exec(self) -> None:
        print(f'KEVM Version: {VERSION}')


class PruneCommand(Command, KOptions, SpecOptions, LoggingOptions):
    node: NodeIdLike

    @staticmethod
    def name() -> str:
        return 'prune-proof'

    @staticmethod
    def help_str() -> str:
        return 'Remove a node and its successors from the proof state.'

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument('node', type=node_id_like, help='Node to remove CFG subgraph from.')

    def exec(self) -> None:
        md_selector = 'k'

        if self.save_directory is None:
            raise ValueError('Must pass --save-directory to prune-proof!')

        if self.definition_dir is None:
            raise ValueError('Must pass --definition to prune-proof!')

        kevm = KEVM(self.definition_dir, use_directory=self.save_directory)

        include_dirs = [Path(include) for include in self.includes]
        include_dirs += config.INCLUDE_DIRS

        _LOGGER.info(f'Extracting claims from file: {self.spec_file}')
        claim = single(
            kevm.get_claims(
                self.spec_file,
                spec_module_name=self.spec_module,
                include_dirs=include_dirs,
                md_selector=md_selector,
                claim_labels=self.claim_labels,
                exclude_claim_labels=self.exclude_claim_labels,
            )
        )

        apr_proof = APRProof.read_proof_data(self.save_directory, claim.label)
        node_ids = apr_proof.prune(self.node)
        print(f'Pruned nodes: {node_ids}')
        apr_proof.write_proof_data()


class ProveLegacyCommand(Command, KOptions, SpecOptions, KProveLegacyOptions, LoggingOptions):
    bug_report_legacy: bool

    @staticmethod
    def name() -> str:
        return 'prove-legacy'

    @staticmethod
    def help_str() -> str:
        return 'Run KEVM proof using the legacy kprove binary.'

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'bug_report_legacy': False,
        }

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument('--bug-report-legacy', action='store_true', help='Generate a legacy bug report.')

    def exec(self) -> None:
        definition_dir = self.definition_dir
        if definition_dir is None:
            definition_dir = kdist.get('evm-semantics.haskell')

        kevm = KEVM(definition_dir, use_directory=self.save_directory)

        include_dirs = [Path(include) for include in self.includes]
        include_dirs += config.INCLUDE_DIRS

        final_state = kevm.prove_legacy(
            spec_file=self.spec_file,
            includes=include_dirs,
            bug_report=self.bug_report_legacy,
            spec_module=self.spec_module,
            claim_labels=self.claim_labels,
            exclude_claim_labels=self.exclude_claim_labels,
            debug=self.debug,
            debugger=self.debugger,
            max_depth=self.max_depth,
            max_counterexamples=self.max_counterexamples,
            branching_allowed=self.branching_allowed,
            haskell_backend_args=self.haskell_backend_args,
        )
        final_kast = mlOr([state.kast for state in final_state])
        print(kevm.pretty_print(final_kast))
        if not is_top(final_kast):
            raise SystemExit(1)


class ViewKCFGCommand(Command, KOptions, SpecOptions, LoggingOptions):
    @staticmethod
    def name() -> str:
        return 'view-kcfg'

    @staticmethod
    def help_str() -> str:
        return 'Explore a given proof in the KCFG visualizer.'

    def exec(self) -> None:
        if self.definition_dir is None:
            raise ValueError('Must pass --definition to view-kcfg!')

        kevm = KEVM(self.definition_dir)
        include_dirs = [Path(include) for include in self.includes]
        include_dirs += config.INCLUDE_DIRS
        proof = get_apr_proof_for_spec(
            kevm,
            self.spec_file,
            save_directory=self.save_directory,
            spec_module_name=self.spec_module,
            include_dirs=include_dirs,
            md_selector=self.md_selector,
            claim_labels=self.claim_labels,
            exclude_claim_labels=self.exclude_claim_labels,
        )

        node_printer = kevm_node_printer(kevm, proof)

        def custom_view(element: KCFGElem) -> list[str]:
            if type(element) is KCFG.Edge:
                return list(element.rules)
            if type(element) is KCFG.NDBranch:
                return list(element.rules)
            return []

        proof_view = APRProofViewer(proof, kevm, node_printer=node_printer, custom_view=custom_view)

        proof_view.run()


class RunCommand(Command, KOptions, TargetOptions, EVMChainOptions, SaveDirOptions, LoggingOptions):
    input_file: Path
    output: KRunOutput
    expand_macros: bool
    debugger: bool

    @staticmethod
    def name() -> str:
        return 'run'

    @staticmethod
    def help_str() -> str:
        return 'Run KEVM test/simulation.'

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'output': KRunOutput.PRETTY,
            'expand_macros': True,
            'debugger': False,
        }

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument('input_file', type=file_path, help='Path to input file.')
        parser.add_argument(
            '--output',
            type=KRunOutput,
            choices=list(KRunOutput),
        )
        parser.add_argument(
            '--expand-macros',
            dest='expand_macros',
            action='store_true',
            help='Expand macros on the input term before execution.',
        )
        parser.add_argument(
            '--no-expand-macros',
            dest='expand_macros',
            action='store_false',
            help='Do not expand macros on the input term before execution.',
        )
        parser.add_argument(
            '--debugger',
            dest='debugger',
            action='store_true',
            help='Run GDB debugger for execution.',
        )

    def exec(self) -> None:
        target_fqn = f'evm-semantics.{self.target}'

        kevm = KEVM(kdist.get(target_fqn), use_directory=self.save_directory)

        try:
            json_read = json.loads(self.input_file.read_text())
            kore_pattern = gst_to_kore(json_read, self.schedule, self.mode, self.chainid, self.usegas)
        except json.JSONDecodeError:
            pgm_token = KToken(self.input_file.read_text(), KSort('EthereumSimulation'))
            kast_pgm = kevm.parse_token(pgm_token)
            kore_pgm = kevm.kast_to_kore(kast_pgm, sort=KSort('EthereumSimulation'))
            kore_pattern = kore_pgm_to_kore(
                kore_pgm, SORT_ETHEREUM_SIMULATION, self.schedule, self.mode, self.chainid, self.usegas
            )

        kevm.run(
            kore_pattern,
            depth=self.depth,
            term=True,
            expand_macros=self.expand_macros,
            output=self.output,
            check=True,
            debugger=self.debugger,
        )


class KastCommand(Command, TargetOptions, EVMChainOptions, SaveDirOptions, LoggingOptions):
    input_file: Path
    output: PrintOutput

    @staticmethod
    def name() -> str:
        return 'kast'

    @staticmethod
    def help_str() -> str:
        return 'Run KEVM program.'

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'output': PrintOutput.KORE,
        }

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument('input_file', type=file_path, help='Path to input file.')
        parser.add_argument(
            '--output',
            type=PrintOutput,
            choices=list(PrintOutput),
        )

    def exec(self) -> None:
        target_fqn = f'evm-semantics.{self.target}'

        kevm = KEVM(kdist.get(target_fqn), use_directory=self.save_directory)

        try:
            json_read = json.loads(self.input_file.read_text())
            kore_pattern = gst_to_kore(json_read, self.schedule, self.mode, self.chainid, self.usegas)
        except json.JSONDecodeError:
            pgm_token = KToken(self.input_file.read_text(), KSort('EthereumSimulation'))
            kast_pgm = kevm.parse_token(pgm_token)
            kore_pgm = kevm.kast_to_kore(kast_pgm)
            kore_pattern = kore_pgm_to_kore(
                kore_pgm, SORT_ETHEREUM_SIMULATION, self.schedule, self.mode, self.chainid, self.usegas
            )

        output_text = kore_print(kore_pattern, definition_dir=kevm.definition_dir, output=self.output)
        print(output_text)


class SectionEdgeCommand(Command, LoggingOptions, KOptions, SpecOptions, RPCOptions, BugReportOptions, SMTOptions):
    edge: tuple[str, str]
    sections: int
    use_booster: bool

    @staticmethod
    def name() -> str:
        return 'section-edge'

    @staticmethod
    def help_str() -> str:
        return 'Break an edge into sections.'

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'sections': 2,
            'use-booster': False,
        }

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument('edge', type=arg_pair_of(str, str), help='Edge to section in CFG.')
        parser.add_argument('--sections', type=int, help='Number of sections to make from edge (>= 2).')
        parser.add_argument(
            '--use-booster',
            dest='use_booster',
            action='store_true',
            help="Use the booster RPC server instead of kore-rpc. Requires calling kompile with '--target haskell-booster' flag",
        )

    def exec(self) -> None:
        md_selector = 'k'

        if self.save_directory is None:
            raise ValueError('Must pass --save-directory to section-edge!')

        kore_rpc_command: Iterable[str]
        if self.kore_rpc_command is None:
            kore_rpc_command = ('kore-rpc-booster',) if self.use_booster else ('kore-rpc',)
        elif isinstance(self.kore_rpc_command, str):
            kore_rpc_command = self.kore_rpc_command.split()

        if self.definition_dir is None:
            raise ValueError('Must pass --definition to section-edge!')

        kevm = KEVM(self.definition_dir, use_directory=self.save_directory)
        llvm_definition_dir = self.definition_dir / 'llvm-library' if self.use_booster else None

        include_dirs = [Path(include) for include in self.includes]
        include_dirs += config.INCLUDE_DIRS

        claim = single(
            kevm.get_claims(
                self.spec_file,
                spec_module_name=self.spec_module,
                include_dirs=include_dirs,
                md_selector=md_selector,
                claim_labels=self.claim_labels,
                exclude_claim_labels=self.exclude_claim_labels,
            )
        )

        proof = APRProof.read_proof_data(self.save_directory, claim.label)
        source_id, target_id = self.edge
        with legacy_explore(
            kevm,
            kcfg_semantics=KEVMSemantics(),
            id=proof.id,
            bug_report=self.bug_report,
            kore_rpc_command=kore_rpc_command,
            smt_timeout=self.smt_timeout,
            smt_retry_limit=self.smt_retry_limit,
            trace_rewrites=self.trace_rewrites,
            llvm_definition_dir=llvm_definition_dir,
        ) as kcfg_explore:
            kcfg, _ = kcfg_explore.section_edge(
                proof.kcfg, source_id=int(source_id), target_id=int(target_id), logs=proof.logs, sections=self.sections
            )
        proof.write_proof_data()


# Helpers


def _loglevel(args: LoggingOptions) -> int:
    if args.debug:
        return logging.DEBUG

    if args.verbose:
        return logging.INFO

    return logging.WARNING


if __name__ == '__main__':
    main()
