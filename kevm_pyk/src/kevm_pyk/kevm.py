import logging
import os
import sys
from pathlib import Path
from subprocess import CalledProcessError
from typing import Any, Dict, Final, List, Optional

from pyk.cli_utils import run_process
from pyk.kast import KApply, KInner
from pyk.kastManip import flatten_label, getCell
from pyk.ktool import KProve, KRun
from pyk.ktool.kprint import paren
from pyk.prelude import intToken, stringToken

from .utils import add_include_arg

_LOGGER: Final = logging.getLogger(__name__)


# KEVM class


class KEVM(KProve, KRun):

    def __init__(self, definition_dir: Path, main_file: Optional[Path] = None, use_directory: Optional[Path] = None) -> None:
        # I'm going for the simplest version here, we can change later if there is an advantage.
        # https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way
        # Note that they say using `super` supports dependency injection, but I have never liked dependency injection anyway.
        KProve.__init__(self, definition_dir, use_directory=use_directory, main_file=main_file)
        KRun.__init__(self, definition_dir, use_directory=use_directory)
        KEVM._patch_symbol_table(self.symbol_table)

    @staticmethod
    def kompile(
        definition_dir: Path,
        main_file: Path,
        emit_json: bool = True,
        includes: List[str] = [],
        main_module_name: Optional[str] = None,
        syntax_module_name: Optional[str] = None,
        md_selector: Optional[str] = None,
        hook_namespaces: Optional[List[str]] = None,
        concrete_rules_file: Optional[Path] = None,
    ) -> 'KEVM':
        command = ['kompile', '--output-definition', str(definition_dir), str(main_file)]
        command += ['--backend', 'haskell']
        command += ['--main-module', main_module_name] if main_module_name else []
        command += ['--syntax-module', syntax_module_name] if syntax_module_name else []
        command += ['--md-selector', md_selector] if md_selector else []
        command += ['--hook-namespaces', ' '.join(hook_namespaces)] if hook_namespaces else []
        command += add_include_arg(includes)
        if concrete_rules_file and os.path.exists(concrete_rules_file):
            with open(concrete_rules_file, 'r') as crf:
                concrete_rules = ','.join(crf.read().split('\n'))
                command += ['--concrete-rules', concrete_rules]
        try:
            run_process(command, logger=_LOGGER)
        except CalledProcessError as err:
            sys.stderr.write(f'\nkompile stdout:\n{err.stdout}\n')
            sys.stderr.write(f'\nkompile stderr:\n{err.stderr}\n')
            sys.stderr.write(f'\nkompile returncode:\n{err.returncode}\n')
            sys.stderr.flush()
            raise
        return KEVM(definition_dir, main_file=main_file)

    @staticmethod
    def _patch_symbol_table(symbol_table: Dict[str, Any]) -> None:
        symbol_table['_orBool_']                                      = paren(symbol_table['_orBool_'])                                     # noqa
        symbol_table['_andBool_']                                     = paren(symbol_table['_andBool_'])                                    # noqa
        symbol_table['_impliesBool_']                                 = paren(symbol_table['_impliesBool_'])                                # noqa
        symbol_table['notBool_']                                      = paren(symbol_table['notBool_'])                                     # noqa
        symbol_table['_/Int_']                                        = paren(symbol_table['_/Int_'])                                       # noqa
        symbol_table['_*Int_']                                        = paren(symbol_table['_*Int_'])                                       # noqa
        symbol_table['_-Int_']                                        = paren(symbol_table['_-Int_'])                                       # noqa
        symbol_table['_+Int_']                                        = paren(symbol_table['_+Int_'])                                       # noqa
        symbol_table['#Or']                                           = paren(symbol_table['#Or'])                                          # noqa
        symbol_table['#And']                                          = paren(symbol_table['#And'])                                         # noqa
        symbol_table['#Implies']                                      = paren(symbol_table['#Implies'])                                     # noqa
        symbol_table['_Set_']                                         = paren(symbol_table['_Set_'])                                        # noqa
        symbol_table['_|->_']                                         = paren(symbol_table['_|->_'])                                        # noqa
        symbol_table['_Map_']                                         = paren(lambda m1, m2: m1 + '\n' + m2)                                # noqa
        symbol_table['_AccountCellMap_']                              = paren(lambda a1, a2: a1 + '\n' + a2)                                # noqa
        symbol_table['AccountCellMapItem']                            = lambda k, v: v                                                      # noqa
        symbol_table['_[_:=_]_EVM-TYPES_Memory_Memory_Int_ByteArray'] = lambda m, k, v: m + ' [ '  + k + ' := (' + v + '):ByteArray ]'      # noqa
        symbol_table['_[_.._]_EVM-TYPES_ByteArray_ByteArray_Int_Int'] = lambda m, s, w: '(' + m + ' [ ' + s + ' .. ' + w + ' ]):ByteArray'  # noqa
        symbol_table['_<Word__EVM-TYPES_Int_Int_Int']                 = paren(lambda a1, a2: '(' + a1 + ') <Word ('  + a2 + ')')            # noqa
        symbol_table['_>Word__EVM-TYPES_Int_Int_Int']                 = paren(lambda a1, a2: '(' + a1 + ') >Word ('  + a2 + ')')            # noqa
        symbol_table['_<=Word__EVM-TYPES_Int_Int_Int']                = paren(lambda a1, a2: '(' + a1 + ') <=Word (' + a2 + ')')            # noqa
        symbol_table['_>=Word__EVM-TYPES_Int_Int_Int']                = paren(lambda a1, a2: '(' + a1 + ') >=Word (' + a2 + ')')            # noqa
        symbol_table['_==Word__EVM-TYPES_Int_Int_Int']                = paren(lambda a1, a2: '(' + a1 + ') ==Word (' + a2 + ')')            # noqa
        symbol_table['_s<Word__EVM-TYPES_Int_Int_Int']                = paren(lambda a1, a2: '(' + a1 + ') s<Word (' + a2 + ')')            # noqa

    @staticmethod
    def halt() -> KApply:
        return KApply('#halt_EVM_KItem')

    @staticmethod
    def execute() -> KApply:
        return KApply('#execute_EVM_KItem')

    @staticmethod
    def jumpi() -> KApply:
        return KApply('JUMPI_EVM_BinStackOp')

    @staticmethod
    def jump() -> KApply:
        return KApply('JUMP_EVM_UnStackOp')

    @staticmethod
    def jumpi_applied(pc: KInner, cond: KInner) -> KApply:
        return KApply('____EVM_InternalOp_BinStackOp_Int_Int', [KEVM.jumpi(), pc, cond])

    @staticmethod
    def jump_applied(pc: KInner) -> KApply:
        return KApply('___EVM_InternalOp_UnStackOp_Int', [KEVM.jump(), pc])

    @staticmethod
    def pow256() -> KApply:
        return KApply('pow256_EVM-TYPES_Int', [])

    @staticmethod
    def range_uint(width: int, i: KInner) -> KApply:
        return KApply('#rangeUInt(_,_)_EVM-TYPES_Bool_Int_Int', [intToken(width), i])

    @staticmethod
    def range_sint(width: int, i: KInner) -> KApply:
        return KApply('#rangeSInt(_,_)_EVM-TYPES_Bool_Int_Int', [intToken(width), i])

    @staticmethod
    def range_address(i: KInner) -> KApply:
        return KApply('#rangeAddress(_)_EVM-TYPES_Bool_Int', [i])

    @staticmethod
    def range_bool(i: KInner) -> KApply:
        return KApply('#rangeBool(_)_EVM-TYPES_Bool_Int', [i])

    @staticmethod
    def range_bytes(width: KInner, ba: KInner) -> KApply:
        return KApply('#rangeBytes(_,_)_EVM-TYPES_Bool_Int_Int', [width, ba])

    @staticmethod
    def bool_2_word(cond: KInner) -> KApply:
        return KApply('bool2Word(_)_EVM-TYPES_Int_Bool', [cond])

    @staticmethod
    def size_bytearray(ba: KInner) -> KApply:
        return KApply('#sizeByteArray(_)_EVM-TYPES_Int_ByteArray', [ba])

    @staticmethod
    def inf_gas(g: KInner) -> KApply:
        return KApply('infGas', [g])

    @staticmethod
    def compute_valid_jumpdests(p: KInner) -> KApply:
        return KApply('#computeValidJumpDests(_)_EVM_Set_ByteArray', [p])

    @staticmethod
    def bin_runtime(c: KInner) -> KApply:
        return KApply('#binRuntime', [c])

    @staticmethod
    def hashed_location(compiler: str, base: KInner, offset: KInner, member_offset: int = 0) -> KApply:
        location = KApply('#hashedLocation(_,_,_)_HASHED-LOCATIONS_Int_String_Int_IntList', [stringToken(compiler), base, offset])
        if member_offset > 0:
            location = KApply('_+Int_', [location, intToken(member_offset)])
        return location

    @staticmethod
    def loc(accessor: KInner) -> KApply:
        return KApply('contract_access_loc', [accessor])

    @staticmethod
    def abi_calldata(name: str, args: List[KInner]) -> KApply:
        return KApply('#abiCallData(_,_)_EVM-ABI_ByteArray_String_TypedArgs', [stringToken(name), KEVM.typed_args(args)])

    @staticmethod
    def abi_selector(name: str) -> KApply:
        return KApply('abi_selector', [stringToken(name)])

    @staticmethod
    def abi_address(a: KInner) -> KApply:
        return KApply('#address(_)_EVM-ABI_TypedArg_Int', [a])

    @staticmethod
    def abi_bool(b: KInner) -> KApply:
        return KApply('#bool(_)_EVM-ABI_TypedArg_Int', [b])

    @staticmethod
    def abi_type(type: str, value: KInner) -> KApply:
        return KApply('abi_type_' + type, [value])

    @staticmethod
    def empty_typedargs() -> KApply:
        return KApply('.List{"_,__EVM-ABI_TypedArgs_TypedArg_TypedArgs"}_TypedArgs')

    @staticmethod
    def bytes_append(b1: KInner, b2: KInner) -> KApply:
        return KApply('_++__EVM-TYPES_ByteArray_ByteArray_ByteArray', [b1, b2])

    @staticmethod
    def account_cell(id: KInner, balance: KInner, code: KInner, storage: KInner, origStorage: KInner, nonce: KInner) -> KApply:
        return KApply('<account>', [KApply('<acctID>', [id]),
                                    KApply('<balance>', [balance]),
                                    KApply('<code>', [code]),
                                    KApply('<storage>', [storage]),
                                    KApply('<origStorage>', [origStorage]),
                                    KApply('<nonce>', [nonce])])

    @staticmethod
    def wordstack_len(constrainedTerm: KInner) -> int:
        return len(flatten_label('_:__EVM-TYPES_WordStack_Int_WordStack', getCell(constrainedTerm, 'WORDSTACK_CELL')))

    @staticmethod
    def parse_bytestack(s: KInner) -> KApply:
        return KApply('#parseByteStack(_)_SERIALIZATION_ByteArray_String', [s])

    @staticmethod
    def foundry_success() -> KApply:
        return KApply('foundry_success')

    @staticmethod
    def intlist(ints: List[KInner]) -> KApply:
        res = KApply('.List{"___HASHED-LOCATIONS_IntList_Int_IntList"}_IntList')
        for i in reversed(ints):
            res = KApply('___HASHED-LOCATIONS_IntList_Int_IntList', [i, res])
        return res

    @staticmethod
    def typed_args(args: List[KInner]) -> KApply:
        res = KApply('.List{"_,__EVM-ABI_TypedArgs_TypedArg_TypedArgs"}_TypedArgs')
        for i in reversed(args):
            res = KApply('_,__EVM-ABI_TypedArgs_TypedArg_TypedArgs', [i, res])
        return res
