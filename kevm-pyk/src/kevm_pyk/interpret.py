from __future__ import annotations

import json
import logging
import sys
from argparse import ArgumentParser
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import TYPE_CHECKING

from pyk.cli_utils import file_path
from pyk.kore.prelude import int_dv
from pyk.kore.tools import kore_print
from pyk.ktool.krun import KRunOutput, _krun

from .cli import evm_chain_args, k_args, shared_args
from .gst_to_kore import _mode_to_kore, _schedule_to_kore, gst_to_kore

if TYPE_CHECKING:
    from argparse import Namespace
    from typing import Final


_LOGGER: Final = logging.getLogger(__name__)
_LOG_FORMAT: Final = '%(levelname)s %(asctime)s %(name)s - %(message)s'


def main() -> None:
    sys.setrecursionlimit(15000000)
    args = _parse_args()
    _exec_interpret(
        args.definition_dir,
        args.input_file,
        args.parser,
        args.expand_macros,
        args.depth,
        args.output,
        args.schedule,
        args.mode,
        args.chainid,
        args.unparse,
    )


def _exec_interpret(
    definition_dir: Path,
    input_file: Path,
    parser: str | None,
    expand_macros: str,
    depth: int | None,
    output: KRunOutput,
    schedule: str,
    mode: str,
    chainid: int,
    unparse: bool,
) -> None:
    if input_file.suffix == '.json':
        _LOGGER.info('Using gst_to_kore on JSON input.')
        pgm = json.loads(input_file.read_text())
        pgm_kore = gst_to_kore(pgm, schedule, mode, chainid)
        with NamedTemporaryFile('w', delete=False) as ntf:
            ntf.write(pgm_kore.text)
            ntf.flush()
            _LOGGER.info('Invoking krun.')
            krun_result = _krun(
                definition_dir=definition_dir,
                input_file=Path(ntf.name),
                depth=depth,
                term=True,
                no_expand_macros=not expand_macros,
                parser='cat',
                output=KRunOutput.KORE,
                check=False,
            )
    else:
        _LOGGER.info('Reading input directly with K parser.')
        cmap = {
            'MODE': _mode_to_kore(mode).text,
            'SCHEDULE': _schedule_to_kore(schedule).text,
            'CHAINID': int_dv(chainid).text,
        }
        pmap = {'MODE': 'cat', 'SCHEDULE': 'cat', 'CHAINID': 'cat'}
        _LOGGER.info('Invoking krun.')
        krun_result = _krun(
            definition_dir=definition_dir,
            input_file=input_file,
            depth=depth,
            term=False,
            no_expand_macros=not expand_macros,
            parser=parser,
            cmap=cmap,
            pmap=pmap,
            output=KRunOutput.KORE,
            check=False,
        )
    if krun_result.returncode != 0 or unparse:
        if output == KRunOutput.NONE:
            pass
        else:
            _LOGGER.info('Unparsing output.')
            print(kore_print(krun_result.stdout, definition_dir, output.value))
    _LOGGER.info('Finished.')
    sys.exit(krun_result.returncode)


def _parse_args() -> Namespace:
    parser = ArgumentParser(
        description='Inpterpret an EVM program (GeneralStateTest or custom KEVM format)',
        parents=[shared_args(), k_args(), evm_chain_args()],
    )
    parser.add_argument('input_file', type=file_path, help='Path to input file.')
    parser.add_argument('--parser', default=None, type=str, help='Parser to use for $PGM.')
    parser.add_argument(
        '--unparse', dest='unparse', default=True, action='store_true', help='Unparse the output in all cases.'
    )
    parser.add_argument(
        '--no-unparse', dest='unparse', action='store_false', help='Do not unparse the output on success cases.'
    )
    parser.add_argument(
        '--output',
        default=KRunOutput.PRETTY,
        type=KRunOutput,
        help='Output format to use, one of [pretty|program|kast|binary|json|latex|kore|none].',
    )
    parser.add_argument(
        '--expand-macros',
        dest='expand_macros',
        default=True,
        action='store_true',
        help='Expand macros on the input term before execution.',
    )
    parser.add_argument(
        '--no-expand-macros',
        dest='expand_macros',
        action='store_false',
        help='Do not expand macros on the input term before execution.',
    )
    return parser.parse_args()


if __name__ == '__main__':
    main()
