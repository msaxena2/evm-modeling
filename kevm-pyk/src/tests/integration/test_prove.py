from __future__ import annotations

import logging
import sys
from typing import TYPE_CHECKING, NamedTuple

import pytest
from pyk.cterm import CTerm
from pyk.proof.reachability import APRProof

from kevm_pyk import config
from kevm_pyk.__main__ import ProveCommand
from kevm_pyk.kevm import KEVM
from kevm_pyk.kompile import KompileTarget, kevm_kompile

from ..utils import REPO_ROOT

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
KONTROL_TESTS: Final = spec_files('kontrol', '*-spec.k')

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
        KONTROL_TESTS,
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


class Target(NamedTuple):
    main_file: Path
    main_module_name: str

    def __call__(self, output_dir: Path) -> Path:
        return kevm_kompile(
            output_dir=output_dir / 'kompiled',
            target=KompileTarget.HASKELL,
            main_file=self.main_file,
            main_module=self.main_module_name,
            syntax_module=self.main_module_name,
            debug=True,
        )


@pytest.fixture(scope='module')
def kompiled_target_for(tmp_path_factory: TempPathFactory) -> Callable[[Path], Path]:
    cache_dir = tmp_path_factory.mktemp('target')
    cache: dict[Target, Path] = {}

    def kompile(spec_file: Path) -> Path:
        target = _target_for_spec(spec_file)

        if target not in cache:
            output_dir = cache_dir / f'{target.main_file.stem}-{len(cache)}'
            output_dir.mkdir()
            cache[target] = target(output_dir)

        return cache[target]

    return kompile


def _target_for_spec(spec_file: Path) -> Target:
    spec_file = spec_file.resolve()
    spec_id = str(spec_file.relative_to(SPEC_DIR))
    spec_root = SPEC_DIR / spec_file.relative_to(SPEC_DIR).parents[-2]
    main_file = spec_root / KOMPILE_MAIN_FILE.get(spec_id, 'verification.k')
    main_module_name = KOMPILE_MAIN_MODULE.get(spec_id, 'VERIFICATION')
    return Target(main_file, main_module_name)


# ---------
# Pyk tests
# ---------


class TParams:
    main_claim_id: str | None
    leaf_number: int | None
    break_on_calls: bool

    def __init__(
        self, main_claim_id: str | None = None, leaf_number: int | None = None, break_on_calls: bool = False
    ) -> None:
        self.main_claim_id = main_claim_id
        self.leaf_number = leaf_number
        self.break_on_calls = break_on_calls


TEST_PARAMS: dict[str, TParams] = {
    'mcd/vat-slip-pass-rough-spec.k': TParams(
        main_claim_id='VAT-SLIP-PASS-ROUGH-SPEC.Vat.slip.pass.rough',
        leaf_number=1,
    ),
}


for KONTROL_TEST in KONTROL_TESTS:
    TEST_PARAMS[f'kontrol/{KONTROL_TEST.name}'] = TParams(break_on_calls=True)


def leaf_number(proof: APRProof) -> int:
    non_target_leaves = [nd for nd in proof.kcfg.leaves if not proof.is_target(nd.id)]
    return len(non_target_leaves) + len(proof.kcfg.predecessors(proof.target))


@pytest.mark.parametrize(
    'spec_file',
    ALL_TESTS,
    ids=[str(spec_file.relative_to(SPEC_DIR)) for spec_file in ALL_TESTS],
)
def test_pyk_prove(
    spec_file: Path,
    kompiled_target_for: Callable[[Path], Path],
    tmp_path: Path,
    caplog: LogCaptureFixture,
    use_booster: bool,
    bug_report: BugReport | None,
    spec_name: str | None,
) -> None:
    caplog.set_level(logging.INFO)

    if (not use_booster and spec_file in FAILING_PYK_TESTS) or (use_booster and spec_file in FAILING_BOOSTER_TESTS):
        pytest.skip()

    if spec_name is not None and str(spec_file).find(spec_name) < 0:
        pytest.skip()

    # Given
    log_file = tmp_path / 'log.txt'
    use_directory = tmp_path / 'kprove'
    use_directory.mkdir()

    # When
    try:
        definition_dir = kompiled_target_for(spec_file)
        name = str(spec_file.relative_to(SPEC_DIR))
        break_on_calls = name in TEST_PARAMS and TEST_PARAMS[name].break_on_calls

        options = ProveCommand(
            {
                'spec_file': spec_file,
                'definition_dir': definition_dir,
                'includes': [str(include_dir) for include_dir in config.INCLUDE_DIRS],
                'save_directory': use_directory,
                'md_selector': 'foo',
                'use_booster': use_booster,
                'bug_report': bug_report,
                'break_on_calls': break_on_calls,
            }
        )

        options.exec()
        if name in TEST_PARAMS:
            params = TEST_PARAMS[name]
            if params.leaf_number is not None and params.main_claim_id is not None:
                apr_proof = APRProof.read_proof_data(
                    proof_dir=use_directory,
                    id=params.main_claim_id,
                )
                expected_leaf_number = params.leaf_number
                actual_leaf_number = leaf_number(apr_proof)
                assert expected_leaf_number == actual_leaf_number
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
    kompiled_target_for: Callable[[Path], Path],
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
        definition_dir = kompiled_target_for(spec_file)
        kevm = KEVM(definition_dir, use_directory=use_directory)
        actual = kevm.prove(spec_file=spec_file, include_dirs=list(config.INCLUDE_DIRS), **args)
    except BaseException:
        raise
    finally:
        log_file.write_text(caplog.text)

    # Then
    assert len(actual) == 1
    assert CTerm._is_top(actual[0].kast)
