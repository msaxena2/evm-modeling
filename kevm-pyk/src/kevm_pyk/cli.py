from __future__ import annotations

import logging
from argparse import ArgumentParser
from functools import cached_property
from typing import TYPE_CHECKING, Any

from pyk.cli.args import DisplayOptions, KDefinitionOptions, Options
from pyk.kore.rpc import FallbackReason

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Final, TypeVar

    T = TypeVar('T')

_LOGGER: Final = logging.getLogger(__name__)


def list_of(elem_type: Callable[[str], T], delim: str = ';') -> Callable[[str], list[T]]:
    def parse(s: str) -> list[T]:
        return [elem_type(elem) for elem in s.split(delim)]

    return parse


class KEVMDisplayOptions(DisplayOptions):
    sort_collections: bool

    @staticmethod
    def default() -> dict[str, Any]:
        return {'sort_collections': False}

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument(
            '--sort-collections',
            dest='sort_collections',
            action='store_true',
            help='Sort collections before outputting term.',
        )


class KOptions(KDefinitionOptions):
    depth: int | None

    @staticmethod
    def default() -> dict[str, Any]:
        return {'depth': None}

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument('--depth', type=int, help='Maximum depth to execute to.')


class KProveOptions(Options):
    debug_equations: list[str]
    always_check_subsumption: bool
    fast_check_subsumption: bool

    @staticmethod
    def default() -> dict[str, Any]:
        return {'always_check_subsumption': True, 'fast_check_subsumption': False, 'debug_equations': []}

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument(
            '--debug-equations',
            type=list_of(str, delim=','),
            help='Comma-separate list of equations to debug.',
        )
        parser.add_argument(
            '--always-check-subsumption',
            dest='always_check_subsumption',
            action='store_true',
            help='Check subsumption even on non-terminal nodes.',
        )
        parser.add_argument(
            '--no-always-check-subsumption',
            dest='always_check_subsumption',
            action='store_false',
            help='Do not check subsumption on non-terminal nodes.',
        )
        parser.add_argument(
            '--fast-check-subsumption',
            dest='fast_check_subsumption',
            action='store_true',
            help='Use fast-check on k-cell to determine subsumption.',
        )


class RPCOptions(Options):
    trace_rewrites: bool
    kore_rpc_command: str | None
    use_booster: bool
    fallback_on: list[FallbackReason] | None
    post_exec_simplify: bool
    interim_simplification: int | None
    port: int | None
    maude_port: int | None

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'trace_rewrites': False,
            'use_booster': False,
            'post_exec_simplify': True,
            'kore_rpc_command': None,
            'interim_simplification': None,
            'port': None,
            'maude_port': None,
            'fallback_on': None,
        }

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument(
            '--trace-rewrites',
            dest='trace_rewrites',
            action='store_true',
            help='Log traces of all simplification and rewrite rule applications.',
        )
        parser.add_argument(
            '--kore-rpc-command',
            dest='kore_rpc_command',
            type=str,
            help='Custom command to start RPC server',
        )
        parser.add_argument(
            '--use-booster',
            dest='use_booster',
            action='store_true',
            help='Use the booster RPC server instead of kore-rpc.',
        )
        parser.add_argument(
            '--fallback-on',
            dest='fallback_on',
            type=list_of(FallbackReason, delim=','),
            help='Comma-separated reasons to fallback from booster to kore, only usable with --use-booster. Options [Branching,Aborted,Stuck].',
        )
        parser.add_argument(
            '--post-exec-simplify',
            dest='post_exec_simplify',
            action='store_true',
            help='Always simplify states with kore backend after booster execution, only usable with --use-booster.',
        )
        parser.add_argument(
            '--no-post-exec-simplify',
            dest='post_exec_simplify',
            action='store_false',
            help='Do not simplify states with kore backend after booster execution, only usable with --use-booster.',
        )
        parser.add_argument(
            '--interim-simplification',
            dest='interim_simplification',
            type=int,
            help='Max number of steps to execute before applying simplifier to term in booster backend, only usable with --use-booster.',
        )
        parser.add_argument(
            '--port',
            dest='port',
            type=int,
            help='Use existing RPC server on named port',
        )
        parser.add_argument(
            '--maude-port',
            dest='maude_port',
            type=int,
            help='Use existing Maude RPC server on named port',
        )


class ExploreOptions(Options):
    break_every_step: bool
    break_on_jumpi: bool
    break_on_calls: bool
    break_on_storage: bool
    break_on_basic_blocks: bool
    max_depth: int
    max_iterations: int | None
    failure_info: bool
    auto_abstract_gas: bool
    counterexample_info: bool
    fail_fast: bool

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'break_every_step': False,
            'break_on_jumpi': False,
            'break_on_calls': False,
            'break_on_storage': False,
            'break_on_basic_blocks': False,
            'max_depth': 1000,
            'failure_info': True,
            'counterexample_info': True,
            'fail_fast': True,
            'max_iterations': None,
            'auto_abstract_gas': False,
        }

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument(
            '--break-every-step',
            dest='break_every_step',
            action='store_true',
            help='Store a node for every EVM opcode step (expensive).',
        )
        parser.add_argument(
            '--break-on-jumpi',
            dest='break_on_jumpi',
            action='store_true',
            help='Store a node for every EVM jump opcode.',
        )
        parser.add_argument(
            '--break-on-calls',
            dest='break_on_calls',
            action='store_true',
            help='Store a node for every EVM call made.',
        )
        parser.add_argument(
            '--no-break-on-calls',
            dest='break_on_calls',
            action='store_false',
            help='Do not store a node for every EVM call made.',
        )
        parser.add_argument(
            '--break-on-storage',
            dest='break_on_storage',
            action='store_true',
            help='Store a node for every EVM SSTORE/SLOAD made.',
        )
        parser.add_argument(
            '--break-on-basic-blocks',
            dest='break_on_basic_blocks',
            action='store_true',
            help='Store a node for every EVM basic block (implies --break-on-calls).',
        )
        parser.add_argument(
            '--max-depth',
            dest='max_depth',
            type=int,
            help='Maximum number of K steps before the state is saved in a new node in the CFG. Branching will cause this to happen earlier.',
        )
        parser.add_argument(
            '--max-iterations',
            dest='max_iterations',
            type=int,
            help='Number of times to expand the next pending node in the CFG.',
        )
        parser.add_argument(
            '--failure-information',
            dest='failure_info',
            action='store_true',
            help='Show failure summary for all failing tests',
        )
        parser.add_argument(
            '--no-failure-information',
            dest='failure_info',
            action='store_false',
            help='Do not show failure summary for failing tests',
        )
        parser.add_argument(
            '--auto-abstract-gas',
            dest='auto_abstract_gas',
            action='store_true',
            help='Automatically extract gas cell when infinite gas is enabled',
        )
        parser.add_argument(
            '--counterexample-information',
            dest='counterexample_info',
            action='store_true',
            help='Show models for failing nodes.',
        )
        parser.add_argument(
            '--no-counterexample-information',
            dest='counterexample_info',
            action='store_false',
            help='Do not show models for failing nodes.',
        )
        parser.add_argument(
            '--fail-fast',
            dest='fail_fast',
            action='store_true',
            help='Stop execution on other branches if a failing node is detected.',
        )
        parser.add_argument(
            '--no-fail-fast',
            dest='fail_fast',
            action='store_false',
            help='Continue execution on other branches if a failing node is detected.',
        )


class KProveLegacyOptions(Options):
    bug_report: bool
    debugger: bool
    max_depth: int | None
    max_counterexamples: int | None
    branching_allowed: int | None
    haskell_backend_args: list[str]

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'bug_report': False,
            'debugger': False,
            'max_depth': None,
            'max_counterexamples': None,
            'branching_allowed': None,
            'haskell_backend_args': [],
        }

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument(
            '--bug-report',
            action='store_true',
            help='Generate a haskell-backend bug report for the execution.',
        )
        parser.add_argument(
            '--debugger',
            dest='debugger',
            action='store_true',
            help='Launch proof in an interactive debugger.',
        )
        parser.add_argument(
            '--max-depth',
            dest='max_depth',
            type=int,
            help='The maximum number of computational steps to prove.',
        )
        parser.add_argument(
            '--max-counterexamples',
            type=int,
            dest='max_counterexamples',
            help='Maximum number of counterexamples reported before a forcible stop.',
        )
        parser.add_argument(
            '--branching-allowed',
            type=int,
            dest='branching_allowed',
            help='Number of branching events allowed before a forcible stop.',
        )
        parser.add_argument(
            '--haskell-backend-arg',
            dest='haskell_backend_args',
            action='append',
            help='Arguments passed to the Haskell backend execution engine.',
        )


class TargetOptions(Options):
    target: str

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'target': 'llvm',
        }

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
        parser.add_argument('--target', choices=['llvm', 'haskell', 'haskell-standalone', 'foundry'])


class EVMChainOptions(Options):
    schedule: str
    chainid: int
    mode: str
    usegas: bool

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'schedule': 'SHANGHAI',
            'chainid': 1,
            'mode': 'NORMAL',
            'usegas': False,
        }

    @staticmethod
    def update_args(parser: ArgumentParser) -> None:
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
        )
        modes = ('NORMAL', 'VMTESTS')

        parser.add_argument(
            '--schedule',
            choices=schedules,
            help=f"schedule to use for execution [{'|'.join(schedules)}]",
        )
        parser.add_argument('--chainid', type=int, help='chain ID to use for execution')
        parser.add_argument(
            '--mode',
            choices=modes,
            help="execution mode to use [{'|'.join(modes)}]",
        )
        parser.add_argument('--no-gas', action='store_false', dest='usegas', help='omit gas cost computations')


class KEVMCLIArgs:
    requires: list[str]
    imports: list[str]

    @staticmethod
    def default() -> dict[str, Any]:
        return {
            'requires': [],
            'imports': [],
        }

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
