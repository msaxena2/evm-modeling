from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from typing import Final
    from pyk.kast.inner import KInner

from pyk.kast.inner import KApply, KToken, KVariable
from pyk.prelude.collections import set_of
from pyk.prelude.utils import token

from kevm_pyk.kevm import KEVM, compute_jumpdests

TEST_DATA: Final = [
    ('single-ktoken', token(0), KToken('0x0', 'Int')),
    ('bytes-to-hex-empty', KApply('<k>', [token(b'')]), KApply('<k>', KToken('0x', 'Bytes'))),
    (
        'bytes-to-hex-nonempty',
        KApply('<k>', [token(b'\xa6\xb9c\x9d')]),
        KApply('<k>', KToken('0xa6b9639d', 'Bytes')),
    ),
    (
        'kast-to-hex',
        KApply(
            '<generatedTop>',
            KApply('<coinbase>', token(728815563385977040452943777879061427756277306518)),
            KApply('<pc>', token(100)),
            KApply('<output>', token(b'\x00\x00\x00\x3c\x60\xf5')),
            KApply('<program>', token(b'\xcc\xff\xff\xfac\x60\xf5')),
        ),
        KApply(
            '<generatedTop>',
            KApply('<coinbase>', KToken('0x7fa9385be102ac3eac297483dd6233d62b3e1496', 'Int')),
            KApply('<pc>', KToken('0x64', 'Int')),
            KApply('<output>', KToken('0x0000003c60f5', 'Bytes')),
            KApply('<program>', KToken('0xccfffffa6360f5', 'Bytes')),
        ),
    ),
]


@pytest.mark.parametrize(
    'test_id,input,result',
    TEST_DATA,
    ids=[test_id for test_id, *_ in TEST_DATA],
)
def test_kinner_to_hex(test_id: str, input: KInner, result: KInner) -> None:
    # When
    to_hex = KEVM.kinner_to_hex(input)
    # Then
    assert to_hex == result


JUMPDESTS_DATA: Final = [
    ('empty', [], set_of([])),
    (
        'with_buf',
        [
            token(
                b'`\xa0`@R4\x80\x15a\x00\x10W`\x00\x80\xfd[P`@Qa\x01\x038\x03\x80a\x01\x03\x839\x81\x01`@\x81\x90Ra\x00/\x91a\x007V[`\x80Ra\x00PV[`\x00` \x82\x84\x03\x12\x15a\x00IW`\x00\x80\xfd[PQ\x91\x90PV[`\x80Q`\x9ba\x00h`\x009`\x00`1\x01R`\x9b`\x00\xf3\xfe`\x80`@R4\x80\x15`\x0fW`\x00\x80\xfd[P`\x046\x10`(W`\x005`\xe0\x1c\x80c\xa5m\xfeJ\x14`-W[`\x00\x80\xfd[`S\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x81V[`@Q\x90\x81R` \x01`@Q\x80\x91\x03\x90\xf3\xfe\xa2dipfsX\"\x12 \xeb\xb3\x99\x11\xbe\x13L\xdeC\xcc\x01/\x849\xe7\xc5\x9aC\xf1\x0f\xf4\xdfE\x14Z\x80\x90(\xeb\xda\xee\xeadsolcC\x00\x08\r\x003'
            ),
            KEVM.buf(token(32), KVariable('VV0_x', 'Int')),
        ],
        set_of(
            [
                token(16),
                token(47),
                token(55),
                token(73),
                token(80),
                token(119),
                token(144),
                token(149),
                token(187),
            ]
        ),
    ),
    (
        'single_jumpdest',
        [
            token(b'['),
        ],
        set_of([token(0)]),
    ),
    (
        'multiple_bytes',
        [
            token(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00['),
            token(b'\x00\x00[\x00\x00'),
            token(b'\x00['),
        ],
        set_of([token(16), token(19), token(23)]),
    ),
    (
        'multiple_bufs',
        [
            KEVM.buf(token(32), KVariable('VV0_a', 'Int')),
            token(b'\x00\x00'),
            KEVM.buf(token(32), KVariable('VV0_x', 'Int')),
            token(b'\x00\x00[\x00\x00'),
            KEVM.buf(token(32), KVariable('VV0_y', 'Int')),
            token(b'\x00[[[\x00[\x00\x00'),
        ],
        set_of([token(68), token(104), token(105), token(106), token(108)]),
    ),
    ('jump_to_push', [token(bytes.fromhex('6001600055600A56605B5B'))], set_of([token(10)])),
]


@pytest.mark.parametrize(
    'test_id,input,expected',
    JUMPDESTS_DATA,
    ids=[test_id for test_id, *_ in JUMPDESTS_DATA],
)
def test_process_jumpdests(test_id: str, input: list[KInner], expected: KInner) -> None:
    # When
    result = compute_jumpdests(input)

    # Then
    assert result == expected
