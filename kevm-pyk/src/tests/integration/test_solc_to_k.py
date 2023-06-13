from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from kevm_pyk.kompile import KompileTarget, kevm_kompile

if TYPE_CHECKING:
    from typing import Callable, Final


EXAMPLES_DIR: Final = (Path(__file__).parent / 'test-data/examples').resolve(strict=True)
TEST_DATA: Final = tuple(EXAMPLES_DIR.glob('*.sol'))


@pytest.mark.parametrize(
    'contract_file',
    TEST_DATA,
    ids=[contract_file.name for contract_file in TEST_DATA],
)
def test_solc_to_k(contract_file: Path, bin_runtime: Callable, tmp_path: Path) -> None:
    # Given
    definition_dir = tmp_path / 'kompiled'
    main_file, main_module_name = bin_runtime(contract_file)

    # When
    kevm_kompile(
        target=KompileTarget.HASKELL,
        output_dir=definition_dir,
        main_file=main_file,
        main_module=main_module_name,
        syntax_module=main_module_name,
    )
