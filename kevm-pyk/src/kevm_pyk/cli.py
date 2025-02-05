from __future__ import annotations

import logging
from argparse import ArgumentParser
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING, Any

from pyk.cli.args import (
    BugReportOptions,
)
from pyk.cli.args import DisplayOptions as PykDisplayOptions
from pyk.cli.args import (
    KCLIArgs,
    KDefinitionOptions,
    KompileOptions,
    LoggingOptions,
    Options,
    ParallelOptions,
    SaveDirOptions,
    SMTOptions,
    SpecOptions,
)
from pyk.cli.utils import file_path
from pyk.kore.rpc import FallbackReason
from pyk.kore.tools import PrintOutput
from pyk.ktool.krun import KRunOutput

from .kompile import KompileTarget
from .utils import arg_pair_of

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Final, TypeVar

    from pyk.kcfg.kcfg import NodeIdLike

    T = TypeVar('T')

_LOGGER: Final = logging.getLogger(__name__)


def list_of(elem_type: Callable[[str], T], delim: str = ';') -> Callable[[str], list[T]]:
    def parse(s: str | list[str]) -> list[T]:
        s_list = s.split(delim) if not isinstance(s, list) else s
        return [elem_type(elem) for elem in s_list]

    return parse


def node_id_like(s: str) -> NodeIdLike:
    try:
        return int(s)
    except ValueError:
        return s


def generate_options(args: dict[str, Any]) -> LoggingOptions:
    command = args['command']
    match command:
        case 'version':
            return VersionOptions(args)
        case 'kompile-spec':
            return KompileSpecOptions(args)
        case 'prove':
            return ProveOptions(args)
        case 'prune':
            return PruneOptions(args)
        case 'section-edge':
            return SectionEdgeOptions(args)
        case 'show-kcfg':
            return ShowKCFGOptions(args)
        case 'view-kcfg':
            return ViewKCFGOptions(args)
        case 'kast':
            return KastOptions(args)
        case 'run':
            return RunOptions(args)
        case _:
            raise ValueError(f'Unrecognized command: {command}')


def get_option_string_destination(command: str, option_string: str) -> str:
    option_string_destinations = {}
    match command:
        case 'version':
            option_string_destinations = VersionOptions.from_option_string()
        case 'kompile-spec':
            option_string_destinations = KompileSpecOptions.from_option_string()
        case 'prove':
            option_string_destinations = ProveOptions.from_option_string()
        case 'prune':
            option_string_destinations = PruneOptions.from_option_string()
        case 'section-edge':
            option_string_destinations = SectionEdgeOptions.from_option_string()
        case 'show-kcfg':
            option_string_destinations = ShowKCFGOptions.from_option_string()
        case 'view-kcfg':
            option_string_destinations = ViewKCFGOptions.from_option_string()
        case 'kast':
            option_string_destinations = KastOptions.from_option_string()
        case 'run':
            option_string_destinations = RunOptions.from_option_string()

    return option_string_destinations.get(option_string, option_string.replace('-', '_'))


def get_argument_type_setter(command: str, option_string: str) -> Callable[[str], Any]:
    def func(par: str) -> str:
        return par

    option_types = {}
    match command:
        case 'version':
            option_types = VersionOptions.get_argument_type()
        case 'kompile-spec':
            option_types = KompileSpecOptions.get_argument_type()
        case 'prove':
            option_types = ProveOptions.get_argument_type()
        case 'prune':
            option_types = PruneOptions.get_argument_type()
        case 'section-edge':
            option_types = SectionEdgeOptions.get_argument_type()
        case 'show-kcfg':
            option_types = ShowKCFGOptions.get_argument_type()
        case 'view-kcfg':
            option_types = ViewKCFGOptions.get_argument_type()
        case 'kast':
            option_types = KastOptions.get_argument_type()
        case 'run':
            option_types = RunOptions.get_argument_type()

    return option_types.get(option_string, func)


def _create_argument_parser() -> ArgumentParser:
    kevm_cli_args = KEVMCLIArgs()
    config_args = ConfigArgs()
    parser = ArgumentParser(prog='kevm-pyk')

    command_parser = parser.add_subparsers(dest='command', required=True)

    command_parser.add_parser(
        'version', help='Print KEVM version and exit.', parents=[kevm_cli_args.logging_args, config_args.config_args]
    )

    kevm_kompile_spec_args = command_parser.add_parser(
        'kompile-spec',
        help='Kompile KEVM specification.',
        parents=[kevm_cli_args.logging_args, kevm_cli_args.k_args, kevm_cli_args.kompile_args, config_args.config_args],
    )
    kevm_kompile_spec_args.add_argument('main_file', type=file_path, help='Path to file with main module.')
    kevm_kompile_spec_args.add_argument('--target', type=KompileTarget, help='[haskell|maude]')

    kevm_kompile_spec_args.add_argument(
        '--debug-build', dest='debug_build', help='Enable debug symbols in LLVM builds.'
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
            kevm_cli_args.bug_report_args,
            kevm_cli_args.smt_args,
            kevm_cli_args.explore_args,
            kevm_cli_args.spec_args,
            config_args.config_args,
        ],
    )
    prove_args.add_argument(
        '--reinit',
        dest='reinit',
        default=None,
        action='store_true',
        help='Reinitialize CFGs even if they already exist.',
    )
    prove_args.add_argument(
        '--max-frontier-parallel',
        type=int,
        help='Maximum worker threads to use on a single proof to explore separate branches in parallel.',
    )

    prune_args = command_parser.add_parser(
        'prune',
        help='Remove a node and its successors from the proof state.',
        parents=[kevm_cli_args.logging_args, kevm_cli_args.k_args, kevm_cli_args.spec_args, config_args.config_args],
    )
    prune_args.add_argument('node', type=node_id_like, help='Node to remove CFG subgraph from.')

    section_edge_args = command_parser.add_parser(
        'section-edge',
        help='Break an edge into sections.',
        parents=[kevm_cli_args.logging_args, kevm_cli_args.k_args, kevm_cli_args.spec_args, config_args.config_args],
    )
    section_edge_args.add_argument('edge', type=arg_pair_of(str, str), help='Edge to section in CFG.')
    section_edge_args.add_argument('--sections', type=int, help='Number of sections to make from edge (>= 2).')

    command_parser.add_parser(
        'view-kcfg',
        help='Explore a given proof in the KCFG visualizer.',
        parents=[kevm_cli_args.logging_args, kevm_cli_args.k_args, kevm_cli_args.spec_args, config_args.config_args],
    )

    command_parser.add_parser(
        'show-kcfg',
        help='Print the CFG for a given proof.',
        parents=[
            kevm_cli_args.logging_args,
            kevm_cli_args.k_args,
            kevm_cli_args.kcfg_show_args,
            kevm_cli_args.spec_args,
            kevm_cli_args.display_args,
            config_args.config_args,
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
            config_args.config_args,
        ],
    )
    run_args.add_argument('input_file', type=file_path, help='Path to input file.')
    run_args.add_argument(
        '--output',
        type=KRunOutput,
        choices=list(KRunOutput),
    )
    run_args.add_argument(
        '--expand-macros',
        dest='expand_macros',
        default=None,
        action='store_true',
        help='Expand macros on the input term before execution.',
    )
    run_args.add_argument(
        '--no-expand-macros',
        dest='expand_macros',
        default=None,
        action='store_false',
        help='Do not expand macros on the input term before execution.',
    )
    run_args.add_argument(
        '--debugger',
        dest='debugger',
        default=None,
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
            config_args.config_args,
        ],
    )
    kast_args.add_argument('input_file', type=file_path, help='Path to input file.')
    kast_args.add_argument(
        '--output',
        type=PrintOutput,
        choices=list(PrintOutput),
    )

    return parser


class KOptions(KDefinitionOptions):
    definition_dir: Path | None
    depth: int | None

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'definition_dir': None,
            'depth': None,
        }

    @staticmethod
    def from_option_string() -> dict[str, str]:
        return KDefinitionOptions.from_option_string() | {
            'definition': 'definition_dir',
        }

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return KDefinitionOptions.get_argument_type()


class RPCOptions(Options):
    log_succ_rewrites: bool
    log_fail_rewrites: bool
    kore_rpc_command: str | None
    use_booster: bool
    fallback_on: list[FallbackReason]
    post_exec_simplify: bool
    interim_simplification: int | None
    port: int | None
    maude_port: int | None
    use_booster_dev: bool

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'log_succ_rewrites': True,
            'log_fail_rewrites': False,
            'kore_rpc_command': None,
            'use_booster': True,
            'fallback_on': [],
            'post_exec_simplify': False,
            'interim_simplification': None,
            'port': None,
            'maude_port': None,
            'use_booster_dev': False,
        }

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return {'fallback-on': list_of(FallbackReason, delim=',')}


class ExploreOptions(Options):
    break_every_step: bool
    break_on_jumpi: bool
    break_on_jump: bool
    break_on_calls: bool
    break_on_storage: bool
    break_on_basic_blocks: bool
    break_on_load_program: bool
    max_depth: int
    max_iterations: int | None
    failure_info: bool
    auto_abstract_gas: bool
    counterexample_info: bool
    fail_fast: bool
    force_sequential: bool

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'break_every_step': False,
            'break_on_jump': False,
            'break_on_jumpi': False,
            'break_on_calls': False,
            'break_on_storage': False,
            'break_on_basic_blocks': False,
            'break_on_load_program': False,
            'max_depth': 1000,
            'max_iterations': None,
            'failure_info': True,
            'auto_abstract_gas': False,
            'counterexample_info': True,
            'fail_fast': True,
            'force_sequential': False,
        }

    @staticmethod
    def from_option_string() -> dict[str, str]:
        return {
            'symbolic-immutables': 'break_on_load_program',
            'failure-information': 'failure_info',
            'no-failure-information': 'no_failure_info',
        }


class KProveOptions(Options):
    debug_equations: list[str]
    fast_check_subsumption: bool
    direct_subproof_rules: bool
    maintenance_rate: int
    assume_defined: bool
    optimize_kcfg: bool

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'debug_equations': [],
            'fast_check_subsumption': False,
            'direct_subproof_rules': False,
            'maintenance_rate': 1,
            'assume_defined': False,
            'optimize_kcfg': False,
        }


class KCFGShowOptions(Options):
    nodes: list[NodeIdLike]
    node_deltas: list[tuple[NodeIdLike, NodeIdLike]]
    failure_info: bool
    to_module: bool
    pending: bool
    failing: bool
    counterexample_info: bool

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'nodes': [],
            'node_deltas': [],
            'failure_info': False,
            'to_module': False,
            'pending': False,
            'failing': False,
            'counterexample_info': False,
        }

    @staticmethod
    def from_option_string() -> dict[str, str]:
        return {
            'counterexample-information': 'counterexample_info',
            'no-counterexample-information': 'no_counterexample_info',
            'node': 'nodes',
            'node-delta': 'node_deltas',
        }

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return {
            'node': list_of(node_id_like, delim=','),
            'node-delta': list_of(arg_pair_of(node_id_like, node_id_like)),
        }


class TargetOptions(Options):
    target: str | None

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'target': None,
        }


class EVMChainOptions(Options):
    schedule: str
    chainid: int
    mode: str
    usegas: bool

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'schedule': 'CANCUN',
            'chainid': 1,
            'mode': 'NORMAL',
            'usegas': True,
        }

    @staticmethod
    def from_option_string() -> dict[str, str]:
        return {
            'no-gas': 'no_usegas',
        }


class DisplayOptions(PykDisplayOptions):
    sort_collections: bool

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'sort_collections': False,
        }

    @staticmethod
    def from_option_string() -> dict[str, str]:
        return PykDisplayOptions.from_option_string()

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return PykDisplayOptions.get_argument_type()


class KGenOptions(Options):
    requires: list[str]
    imports: list[str]

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'requires': [],
            'imports': [],
        }

    @staticmethod
    def from_option_string() -> dict[str, str]:
        return {
            'require': 'requires',
            'module-import': 'imports',
        }

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return {
            'require': list_of(str),
            'module-import': list_of(str),
        }


class VersionOptions(LoggingOptions):
    @staticmethod
    def from_option_string() -> dict[str, str]:
        return LoggingOptions.from_option_string()

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return LoggingOptions.get_argument_type()


class KompileSpecOptions(LoggingOptions, KOptions, KompileOptions):
    main_file: Path
    target: KompileTarget
    debug_build: bool

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'target': KompileTarget.HASKELL,
            'debug_build': False,
        }

    @staticmethod
    def from_option_string() -> dict[str, str]:
        return LoggingOptions.from_option_string() | KOptions.from_option_string() | KompileOptions.from_option_string()

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return (
            LoggingOptions.get_argument_type()
            | KOptions.get_argument_type()
            | KompileOptions.get_argument_type()
            | {'target': KompileTarget, 'main_file': file_path}
        )


class ProveOptions(
    LoggingOptions,
    ParallelOptions,
    KOptions,
    RPCOptions,
    BugReportOptions,
    SMTOptions,
    ExploreOptions,
    SpecOptions,
    KProveOptions,
):
    reinit: bool
    max_frontier_parallel: int

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'reinit': False,
            'max_frontier_parallel': 1,
        }

    @staticmethod
    def from_option_string() -> dict[str, str]:
        return (
            LoggingOptions.from_option_string()
            | ParallelOptions.from_option_string()
            | KOptions.from_option_string()
            | RPCOptions.from_option_string()
            | BugReportOptions.from_option_string()
            | SMTOptions.from_option_string()
            | ExploreOptions.from_option_string()
            | SpecOptions.from_option_string()
            | KProveOptions.from_option_string()
        )

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return (
            LoggingOptions.get_argument_type()
            | ParallelOptions.get_argument_type()
            | KOptions.get_argument_type()
            | RPCOptions.get_argument_type()
            | BugReportOptions.get_argument_type()
            | SMTOptions.get_argument_type()
            | ExploreOptions.get_argument_type()
            | SpecOptions.get_argument_type()
            | KProveOptions.get_argument_type()
        )


class PruneOptions(LoggingOptions, KOptions, SpecOptions):
    node: NodeIdLike

    @staticmethod
    def from_option_string() -> dict[str, str]:
        return LoggingOptions.from_option_string() | KOptions.from_option_string() | SpecOptions.from_option_string()

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return (
            LoggingOptions.get_argument_type()
            | KOptions.get_argument_type()
            | SpecOptions.get_argument_type()
            | {
                'node': node_id_like,
            }
        )


class SectionEdgeOptions(
    LoggingOptions,
    KOptions,
    RPCOptions,
    SMTOptions,
    SpecOptions,
    BugReportOptions,
):
    edge: tuple[str, str]
    sections: int

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'sections': 2,
        }

    @staticmethod
    def from_option_string() -> dict[str, str]:
        return (
            LoggingOptions.from_option_string()
            | KOptions.from_option_string()
            | RPCOptions.from_option_string()
            | SMTOptions.from_option_string()
            | SpecOptions.from_option_string()
            | BugReportOptions.from_option_string()
        )

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return (
            LoggingOptions.get_argument_type()
            | KOptions.get_argument_type()
            | RPCOptions.get_argument_type()
            | SMTOptions.get_argument_type()
            | SpecOptions.get_argument_type()
            | BugReportOptions.get_argument_type()
            | {
                'edge': arg_pair_of(str, str),
            }
        )


class ShowKCFGOptions(
    LoggingOptions,
    KCFGShowOptions,
    KOptions,
    SpecOptions,
    DisplayOptions,
):
    @staticmethod
    def from_option_string() -> dict[str, str]:
        return (
            LoggingOptions.from_option_string()
            | KCFGShowOptions.from_option_string()
            | KOptions.from_option_string()
            | SpecOptions.from_option_string()
            | DisplayOptions.from_option_string()
        )

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return (
            LoggingOptions.get_argument_type()
            | KCFGShowOptions.get_argument_type()
            | KOptions.get_argument_type()
            | SpecOptions.get_argument_type()
            | DisplayOptions.get_argument_type()
        )


class ViewKCFGOptions(
    LoggingOptions,
    KOptions,
    SpecOptions,
):
    @staticmethod
    def from_option_string() -> dict[str, str]:
        return LoggingOptions.from_option_string() | KOptions.from_option_string() | SpecOptions.from_option_string()

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return LoggingOptions.get_argument_type() | KOptions.get_argument_type() | SpecOptions.get_argument_type()


class RunOptions(
    LoggingOptions,
    KOptions,
    EVMChainOptions,
    TargetOptions,
    SaveDirOptions,
):
    input_file: Path
    output: KRunOutput
    expand_macros: bool
    debugger: bool

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'output': KRunOutput.PRETTY,
            'expand_macros': True,
            'debugger': False,
        }

    @staticmethod
    def from_option_string() -> dict[str, str]:
        return (
            LoggingOptions.from_option_string()
            | KOptions.from_option_string()
            | EVMChainOptions.from_option_string()
            | TargetOptions.from_option_string()
            | SaveDirOptions.from_option_string()
        )

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return (
            LoggingOptions.get_argument_type()
            | KOptions.get_argument_type()
            | EVMChainOptions.get_argument_type()
            | TargetOptions.get_argument_type()
            | SaveDirOptions.get_argument_type()
            | {
                'input_file': file_path,
                'output': KRunOutput,
            }
        )


class KastOptions(
    LoggingOptions,
    TargetOptions,
    EVMChainOptions,
    KOptions,
    SaveDirOptions,
):
    input_file: Path
    output: PrintOutput

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'output': PrintOutput.KORE,
        }

    @staticmethod
    def from_option_string() -> dict[str, str]:
        return (
            LoggingOptions.from_option_string()
            | TargetOptions.from_option_string()
            | EVMChainOptions.from_option_string()
            | KOptions.from_option_string()
            | SaveDirOptions.from_option_string()
        )

    @staticmethod
    def get_argument_type() -> dict[str, Callable]:
        return (
            LoggingOptions.get_argument_type()
            | KOptions.get_argument_type()
            | EVMChainOptions.get_argument_type()
            | TargetOptions.get_argument_type()
            | SaveDirOptions.get_argument_type()
            | {
                'input_file': file_path,
            }
        )


class ConfigArgs:
    @cached_property
    def config_args(self) -> ArgumentParser:
        args = ArgumentParser(add_help=False)
        args.add_argument(
            '--config-file',
            dest='config_file',
            type=file_path,
            default=Path('./kevm-pyk.toml'),
            help='Path to Pyk config file.',
        )
        args.add_argument(
            '--config-profile',
            dest='config_profile',
            default='default',
            help='Config profile to be used.',
        )
        return args


class KEVMCLIArgs(KCLIArgs):
    @cached_property
    def target_args(self) -> ArgumentParser:
        args = ArgumentParser(add_help=False)
        args.add_argument('--target', choices=['llvm', 'haskell', 'haskell-standalone', 'foundry'])
        return args

    @cached_property
    def k_args(self) -> ArgumentParser:
        args = super().definition_args
        args.add_argument('--depth', type=int, help='Maximum depth to execute to.')
        return args

    @cached_property
    def kprove_args(self) -> ArgumentParser:
        args = ArgumentParser(add_help=False)
        args.add_argument(
            '--debug-equations',
            type=list_of(str, delim=','),
            help='Comma-separated list of equations to debug.',
        )
        args.add_argument(
            '--fast-check-subsumption',
            dest='fast_check_subsumption',
            default=None,
            action='store_true',
            help='Use fast-check on k-cell to determine subsumption (experimental).',
        )
        args.add_argument(
            '--direct-subproof-rules',
            dest='direct_subproof_rules',
            default=None,
            action='store_true',
            help='For passing subproofs, construct lemmas directly from initial to target state.',
        )
        args.add_argument(
            '--maintenance-rate',
            dest='maintenance_rate',
            type=int,
            help='The number of proof iterations performed between two writes to disk and status bar updates. Note that setting to >1 may result in work being discarded if proof is interrupted.',
        )
        args.add_argument(
            '--assume-defined',
            dest='assume_defined',
            default=None,
            action='store_true',
            help='Use the implication check of the Booster (experimental).',
        )
        args.add_argument(
            '--optimize-kcfg',
            dest='optimize_kcfg',
            default=None,
            action='store_true',
            help='Optimize the constructed KCFG on-the-fly.',
        )
        return args

    @cached_property
    def kprove_legacy_args(self) -> ArgumentParser:
        args = ArgumentParser(add_help=False)
        args.add_argument(
            '--bug-report',
            default=None,
            action='store_true',
            help='Generate a haskell-backend bug report for the execution.',
        )
        args.add_argument(
            '--debugger',
            dest='debugger',
            default=None,
            action='store_true',
            help='Launch proof in an interactive debugger.',
        )
        args.add_argument(
            '--max-depth',
            dest='max_depth',
            type=int,
            help='The maximum number of computational steps to prove.',
        )
        args.add_argument(
            '--max-counterexamples',
            type=int,
            dest='max_counterexamples',
            help='Maximum number of counterexamples reported before a forcible stop.',
        )
        args.add_argument(
            '--branching-allowed',
            type=int,
            dest='branching_allowed',
            help='Number of branching events allowed before a forcible stop.',
        )
        args.add_argument(
            '--haskell-backend-arg',
            dest='haskell_backend_args',
            action='append',
            help='Arguments passed to the Haskell backend execution engine.',
        )
        return args

    @cached_property
    def evm_chain_args(self) -> ArgumentParser:
        schedules = (
            'DEFAULT',
            'FRONTIER',
            'HOMESTEAD',
            'TANGERINE_WHISTLE',
            'SPURIOUS_DRAGON',
            'BYZANTIUM',
            'CONSTANTINOPLE',
            'PETERSBURG',
            'ISTANBUL',
            'BERLIN',
            'LONDON',
            'MERGE',
            'SHANGHAI',
            'CANCUN',
        )
        modes = ('NORMAL', 'VMTESTS')

        args = ArgumentParser(add_help=False)
        args.add_argument(
            '--schedule',
            choices=schedules,
            help=f"schedule to use for execution [{'|'.join(schedules)}].",
        )
        args.add_argument('--chainid', type=int, help='chain ID to use for execution.')
        args.add_argument(
            '--mode',
            choices=modes,
            help="execution mode to use [{'|'.join(modes)}].",
        )
        args.add_argument(
            '--no-gas', default=None, action='store_false', dest='usegas', help='omit gas cost computations.'
        )
        return args

    @cached_property
    def display_args(self) -> ArgumentParser:
        args = super().display_args
        args.add_argument(
            '--sort-collections',
            dest='sort_collections',
            default=None,
            action='store_true',
            help='Sort collections before outputting term.',
        )
        return args

    @cached_property
    def rpc_args(self) -> ArgumentParser:
        args = ArgumentParser(add_help=False)
        args.add_argument(
            '--no-log-rewrites',
            dest='log_succ_rewrites',
            default=None,
            action='store_false',
            help='Do not log traces of any simplification and rewrite rule application.',
        )
        args.add_argument(
            '--log-fail-rewrites',
            dest='log_fail_rewrites',
            default=None,
            action='store_true',
            help='Log traces of all simplification and rewrite rule applications.',
        )
        args.add_argument(
            '--kore-rpc-command',
            dest='kore_rpc_command',
            type=str,
            help='Custom command to start RPC server.',
        )
        args.add_argument(
            '--use-booster',
            dest='use_booster',
            default=None,
            action='store_true',
            help='Use the booster RPC server instead of kore-rpc.',
        )
        args.add_argument(
            '--no-use-booster',
            dest='use_booster',
            default=None,
            action='store_false',
            help='Do not the booster RPC server instead of kore-rpc.',
        )
        args.add_argument(
            '--use-booster-dev',
            dest='use_booster_dev',
            default=None,
            action='store_true',
            help='Use the development booster RPC server instead of kore-rpc.',
        )
        args.add_argument(
            '--fallback-on',
            dest='fallback_on',
            type=list_of(FallbackReason, delim=','),
            help='Comma-separated reasons to fallback from booster to kore, only usable with --use-booster. Options [Branching,Aborted,Stuck].',
        )
        args.add_argument(
            '--post-exec-simplify',
            dest='post_exec_simplify',
            default=None,
            action='store_true',
            help='Always simplify states with kore backend after booster execution, only usable with --use-booster.',
        )
        args.add_argument(
            '--no-post-exec-simplify',
            dest='post_exec_simplify',
            default=None,
            action='store_false',
            help='Do not simplify states with kore backend after booster execution, only usable with --use-booster.',
        )
        args.add_argument(
            '--interim-simplification',
            dest='interim_simplification',
            type=int,
            help='Max number of steps to execute before applying simplifier to term in booster backend, only usable with --use-booster.',
        )
        args.add_argument(
            '--port',
            dest='port',
            type=int,
            help='Use existing RPC server on named port.',
        )
        args.add_argument(
            '--maude-port',
            dest='maude_port',
            type=int,
            help='Use existing Maude RPC server on named port.',
        )
        return args

    @cached_property
    def explore_args(self) -> ArgumentParser:
        args = ArgumentParser(add_help=False)
        args.add_argument(
            '--break-every-step',
            dest='break_every_step',
            default=None,
            action='store_true',
            help='Store a node for every EVM opcode step (expensive).',
        )
        args.add_argument(
            '--break-on-jumpi',
            dest='break_on_jumpi',
            default=None,
            action='store_true',
            help='Store a node for every EVM jumpi opcode.',
        )
        args.add_argument(
            '--break-on-jump',
            dest='break_on_jump',
            default=None,
            action='store_true',
            help='Store a node for every EVM jump opcode.',
        )
        args.add_argument(
            '--break-on-calls',
            dest='break_on_calls',
            default=None,
            action='store_true',
            help='Store a node for every EVM call made.',
        )
        args.add_argument(
            '--no-break-on-calls',
            dest='break_on_calls',
            default=None,
            action='store_false',
            help='Do not store a node for every EVM call made (default).',
        )
        args.add_argument(
            '--break-on-storage',
            dest='break_on_storage',
            default=None,
            action='store_true',
            help='Store a node for every EVM SSTORE/SLOAD made.',
        )
        args.add_argument(
            '--break-on-basic-blocks',
            dest='break_on_basic_blocks',
            default=None,
            action='store_true',
            help='Store a node for every EVM basic block (implies --break-on-calls).',
        )
        args.add_argument(
            '--symbolic-immutables',
            dest='break_on_load_program',
            default=None,
            action='store_true',
            help='Enable support for symbolic immutable variables in Solidity code.',
        )
        args.add_argument(
            '--max-depth',
            dest='max_depth',
            type=int,
            help='Maximum number of K steps before the state is saved in a new node in the CFG. Branching will cause this to happen earlier.',
        )
        args.add_argument(
            '--max-iterations',
            dest='max_iterations',
            type=int,
            help='Number of times to expand the next pending node in the CFG.',
        )
        args.add_argument(
            '--failure-information',
            dest='failure_info',
            default=None,
            action='store_true',
            help='Show failure summary for all failing tests (default).',
        )
        args.add_argument(
            '--no-failure-information',
            dest='failure_info',
            default=None,
            action='store_false',
            help='Do not show failure summary for failing tests.',
        )
        args.add_argument(
            '--auto-abstract-gas',
            dest='auto_abstract_gas',
            default=None,
            action='store_true',
            help='Automatically extract gas cell when infinite gas is enabled.',
        )
        args.add_argument(
            '--counterexample-information',
            dest='counterexample_info',
            default=None,
            action='store_true',
            help='Show models for failing nodes (default).',
        )
        args.add_argument(
            '--no-counterexample-information',
            dest='counterexample_info',
            default=None,
            action='store_false',
            help='Do not show models for failing nodes.',
        )
        args.add_argument(
            '--fail-fast',
            dest='fail_fast',
            default=None,
            action='store_true',
            help='Stop execution on other branches if a failing node is detected (default).',
        )
        args.add_argument(
            '--force-sequential',
            dest='force_sequential',
            default=None,
            action='store_true',
            help='Use sequential, single-threaded proof loop.',
        )
        args.add_argument(
            '--no-fail-fast',
            dest='fail_fast',
            default=None,
            action='store_false',
            help='Continue execution on other branches if a failing node is detected.',
        )
        return args

    @cached_property
    def k_gen_args(self) -> ArgumentParser:
        args = ArgumentParser(add_help=False)
        args.add_argument(
            '--require',
            dest='requires',
            action='append',
            help='Extra K requires to include in generated output.',
        )
        args.add_argument(
            '--module-import',
            dest='imports',
            action='append',
            help='Extra modules to import into generated main module.',
        )
        return args

    @cached_property
    def kcfg_show_args(self) -> ArgumentParser:
        args = ArgumentParser(add_help=False)
        args.add_argument(
            '--node',
            type=node_id_like,
            dest='nodes',
            action='append',
            help='List of nodes to display as well.',
        )
        args.add_argument(
            '--node-delta',
            type=arg_pair_of(node_id_like, node_id_like),
            dest='node_deltas',
            action='append',
            help='List of nodes to display delta for.',
        )
        args.add_argument(
            '--failure-information',
            dest='failure_info',
            default=None,
            action='store_true',
            help='Show failure summary for cfg.',
        )
        args.add_argument(
            '--no-failure-information',
            dest='failure_info',
            default=None,
            action='store_false',
            help='Do not show failure summary for cfg.',
        )
        args.add_argument(
            '--to-module', dest='to_module', default=None, action='store_true', help='Output edges as a K module.'
        )
        args.add_argument(
            '--pending', dest='pending', default=None, action='store_true', help='Also display pending nodes.'
        )
        args.add_argument(
            '--failing', dest='failing', default=None, action='store_true', help='Also display failing nodes.'
        )
        args.add_argument(
            '--counterexample-information',
            dest='counterexample_info',
            default=None,
            action='store_true',
            help="Show models for failing nodes. Should be called with the '--failure-information' flag.",
        )
        return args
