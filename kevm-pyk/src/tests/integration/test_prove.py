from __future__ import annotations

import logging
import sys
from typing import TYPE_CHECKING, NamedTuple

import pytest
from pyk.cterm import CTerm

from kevm_pyk import config
from kevm_pyk.__main__ import exec_prove
from kevm_pyk.kevm import KEVM
from kevm_pyk.kompile import KompileTarget, kevm_kompile

from ..utils import REPO_ROOT
from .utils import TEST_DATA_DIR, gen_bin_runtime

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path
    from typing import Any, Final

    from pyk.utils import BugReport
    from pytest import LogCaptureFixture, TempPathFactory


sys.setrecursionlimit(10**8)

TEST_DIR: Final = REPO_ROOT / 'tests'
SPEC_DIR: Final = TEST_DIR / 'specs'


# -------------------
# Test specifications
# -------------------


def spec_files(dir_name: str, glob: str) -> tuple[Path, ...]:
    test_dir = SPEC_DIR / dir_name
    res = tuple(test_dir.glob(glob))
    assert res
    return res


BENCHMARK_TESTS: Final = spec_files('benchmarks', '*-spec.k')
FUNCTIONAL_TESTS: Final = spec_files('functional', '*-spec.k')
OPCODES_TESTS: Final = spec_files('opcodes', '*-spec.k')
ERC20_TESTS: Final = spec_files('erc20', '*/*-spec.k')
BIHU_TESTS: Final = spec_files('bihu', '*-spec.k')
EXAMPLES_TESTS: Final = spec_files('examples', '*-spec.k') + spec_files('examples', '*-spec.md')
MCD_TESTS: Final = spec_files('mcd', '*-spec.k')
OPTIMIZATION_TESTS: Final = (SPEC_DIR / 'opcodes/evm-optimizations-spec.md',)

ALL_TESTS: Final = sum(
    [
        BENCHMARK_TESTS,
        FUNCTIONAL_TESTS,
        OPCODES_TESTS,
        ERC20_TESTS,
        BIHU_TESTS,
        EXAMPLES_TESTS,
        MCD_TESTS,
        OPTIMIZATION_TESTS,
    ],
    (),
)


def exclude_list(exclude_file: Path) -> list[Path]:
    res = [REPO_ROOT / test_path for test_path in exclude_file.read_text().splitlines()]
    assert res
    return res


FAILING_PYK_TESTS: Final = exclude_list(TEST_DIR / 'failing-symbolic.pyk')
FAILING_BOOSTER_TESTS: Final = exclude_list(TEST_DIR / 'failing-symbolic.haskell-booster')
FAILING_TESTS: Final = exclude_list(TEST_DIR / 'failing-symbolic.haskell')


# -----------
# Kompilation
# -----------


KOMPILE_MAIN_FILE: Final = {
    'benchmarks/functional-spec.k': 'functional-spec.k',
    'bihu/functional-spec.k': 'functional-spec.k',
    'examples/solidity-code-spec.md': 'solidity-code-spec.md',
    'examples/erc20-spec.md': 'erc20-spec.md',
    'examples/erc721-spec.md': 'erc721-spec.md',
    'examples/storage-spec.md': 'storage-spec.md',
    'examples/sum-to-n-spec.k': 'sum-to-n-spec.k',
    'examples/sum-to-n-foundry-spec.k': 'sum-to-n-foundry-spec.k',
    'functional/infinite-gas-spec.k': 'infinite-gas-spec.k',
    'functional/evm-int-simplifications-spec.k': 'evm-int-simplifications-spec.k',
    'functional/int-simplifications-spec.k': 'int-simplifications-spec.k',
    'functional/lemmas-no-smt-spec.k': 'lemmas-no-smt-spec.k',
    'functional/lemmas-spec.k': 'lemmas-spec.k',
    'functional/merkle-spec.k': 'merkle-spec.k',
    'functional/storageRoot-spec.k': 'storageRoot-spec.k',
    'mcd/functional-spec.k': 'functional-spec.k',
    'opcodes/evm-optimizations-spec.md': 'evm-optimizations-spec.md',
}

KOMPILE_MAIN_MODULE: Final = {
    'benchmarks/functional-spec.k': 'FUNCTIONAL-SPEC-SYNTAX',
    'bihu/functional-spec.k': 'FUNCTIONAL-SPEC-SYNTAX',
    'erc20/functional-spec.k': 'FUNCTIONAL-SPEC-SYNTAX',
    'mcd/functional-spec.k': 'FUNCTIONAL-SPEC-SYNTAX',
    'opcodes/evm-optimizations-spec.md': 'EVM-OPTIMIZATIONS-SPEC-LEMMAS',
}

KOMPILE_CONTRACT: Final = {
    'examples/erc20-spec.md': TEST_DATA_DIR / 'examples/ERC20.sol',
    'examples/erc721-spec.md': TEST_DATA_DIR / 'examples/ERC721.sol',
    'examples/storage-spec.md': TEST_DATA_DIR / 'examples/Storage.sol',
}


class Target(NamedTuple):
    main_file: Path
    main_module_name: str
    contract_file: Path | None
    use_booster: bool

    def __call__(self, output_dir: Path) -> KompiledTarget:
        definition_subdir = 'kompiled' if not self.use_booster else 'kompiled-booster'
        definition_dir = output_dir / definition_subdir

        include_dir: Path | None
        if self.contract_file:
            include_dir = output_dir / 'include'
            include_dir.mkdir()
            gen_bin_runtime(self.contract_file, output_dir=include_dir)
        else:
            include_dir = None

        result = KompiledTarget(definition_dir, include_dir)
        target = KompileTarget.HASKELL if not self.use_booster else KompileTarget.HASKELL_BOOSTER

        kevm_kompile(
            output_dir=definition_dir,
            target=target,
            main_file=self.main_file,
            main_module=self.main_module_name,
            syntax_module=self.main_module_name,
            includes=result.includes,
            debug=True,
        )

        return result


class KompiledTarget(NamedTuple):
    definition_dir: Path
    include_dir: Path | None

    @property
    def include_dirs(self) -> list[Path]:
        if self.include_dir:
            return [self.include_dir]
        return []

    @property
    def includes(self) -> list[str]:
        return [str(include_dir) for include_dir in self.include_dirs]


@pytest.fixture(scope='module')
def kompiled_target_for(tmp_path_factory: TempPathFactory) -> Callable[[Path, bool], KompiledTarget]:
    cache_dir = tmp_path_factory.mktemp('target')
    cache: dict[Target, KompiledTarget] = {}

    def kompile(spec_file: Path, use_booster: bool) -> KompiledTarget:
        target = _target_for_spec(spec_file, use_booster=use_booster)

        if target not in cache:
            output_dir = cache_dir / f'{target.main_file.stem}-{len(cache)}'
            output_dir.mkdir()
            cache[target] = target(output_dir)

        return cache[target]

    return kompile


def _target_for_spec(spec_file: Path, use_booster: bool) -> Target:
    spec_file = spec_file.resolve()
    spec_id = str(spec_file.relative_to(SPEC_DIR))
    spec_root = SPEC_DIR / spec_file.relative_to(SPEC_DIR).parents[-2]
    main_file = spec_root / KOMPILE_MAIN_FILE.get(spec_id, 'verification.k')
    main_module_name = KOMPILE_MAIN_MODULE.get(spec_id, 'VERIFICATION')

    main_id = str(main_file.relative_to(SPEC_DIR))
    contract_file = KOMPILE_CONTRACT.get(main_id)

    return Target(main_file, main_module_name, contract_file, use_booster)


# ---------
# Pyk tests
# ---------


@pytest.mark.parametrize(
    'spec_file',
    ALL_TESTS,
    ids=[str(spec_file.relative_to(SPEC_DIR)) for spec_file in ALL_TESTS],
)
def test_pyk_prove(
    spec_file: Path,
    kompiled_target_for: Callable[[Path, bool], KompiledTarget],
    tmp_path: Path,
    caplog: LogCaptureFixture,
    use_booster: bool,
    bug_report: BugReport | None,
) -> None:
    caplog.set_level(logging.INFO)

    if (not use_booster and spec_file in FAILING_PYK_TESTS) or (use_booster and spec_file in FAILING_BOOSTER_TESTS):
        pytest.skip()

    # Given
    log_file = tmp_path / 'log.txt'
    use_directory = tmp_path / 'kprove'
    use_directory.mkdir()

    # When
    try:
        target = kompiled_target_for(spec_file, use_booster)
        exec_prove(
            spec_file=spec_file,
            definition_dir=target.definition_dir,
            includes=[str(include_dir) for include_dir in config.INCLUDE_DIRS] + target.includes,
            save_directory=use_directory,
            smt_timeout=300,
            smt_retry_limit=10,
            md_selector='foo',  # TODO Ignored flag, this is to avoid KeyError
            use_booster=use_booster,
            bug_report=bug_report,
        )
    except BaseException:
        raise
    finally:
        log_file.write_text(caplog.text)


# ------------
# Legacy tests
# ------------


PROVE_ARGS: Final[dict[str, Any]] = {
    'functional/lemmas-no-smt-spec.k': {
        'haskell_args': ['--smt=none'],
    },
}


@pytest.mark.parametrize(
    'spec_file',
    FAILING_PYK_TESTS,
    ids=[str(spec_file.relative_to(SPEC_DIR)) for spec_file in FAILING_PYK_TESTS],
)
def test_kprove_prove(
    spec_file: Path,
    kompiled_target_for: Callable[[Path, bool], KompiledTarget],
    tmp_path: Path,
    caplog: LogCaptureFixture,
    bug_report: BugReport | None,
) -> None:
    caplog.set_level(logging.INFO)

    if spec_file in FAILING_TESTS:
        pytest.skip()

    # Given
    spec_id = str(spec_file.relative_to(SPEC_DIR))
    args = PROVE_ARGS.get(spec_id, {})
    if 'haskell_args' not in args:
        args['haskell_args'] = []
    args['haskell_args'] += ['--smt-timeout', '300']
    args['haskell_args'] += ['--smt-retry-limit', '10']

    log_file = tmp_path / 'log.txt'
    use_directory = tmp_path / 'kprove'
    use_directory.mkdir()

    # When
    try:
        target = kompiled_target_for(spec_file, False)
        kevm = KEVM(target.definition_dir, use_directory=use_directory)
        actual = kevm.prove(spec_file=spec_file, include_dirs=list(config.INCLUDE_DIRS) + target.include_dirs, **args)
    except BaseException:
        raise
    finally:
        log_file.write_text(caplog.text)

    # Then
    assert len(actual) == 1
    assert CTerm._is_top(actual[0].kast)
