import json
import logging
import sys
from pathlib import Path
from typing import Dict, Final, Iterable, List, Optional, Tuple, Union

from pyk.cli_utils import BugReport
from pyk.cterm import CTerm
from pyk.kast.inner import KApply, KInner, KLabel, KSequence, KSort, KToken, KVariable, build_assoc
from pyk.kast.manip import flatten_label, get_cell, split_config_from
from pyk.kast.outer import KFlatModule
from pyk.kcfg import KCFG
from pyk.kcfg.tui import KCFGElem
from pyk.ktool.kompile import KompileBackend, kompile
from pyk.ktool.kprint import SymbolTable, paren
from pyk.ktool.kprove import KProve
from pyk.ktool.krun import KRun
from pyk.prelude.kint import INT, intToken, ltInt
from pyk.prelude.ml import mlAnd, mlEqualsTrue
from pyk.prelude.string import stringToken

from .utils import byte_offset_to_lines

_LOGGER: Final = logging.getLogger(__name__)


# KEVM class


class KEVM(KProve, KRun):
    _srcmap_dir: Optional[Path]
    _contract_name: Optional[str]
    _contract_ids: Dict[int, str]
    _srcmaps: Dict[str, Dict[int, Tuple[int, int, int, str, int]]]
    _contract_srcs: Dict[str, List[str]]
    _contract_srcs_dir: Optional[Path]

    def __init__(
        self,
        definition_dir: Path,
        main_file: Optional[Path] = None,
        use_directory: Optional[Path] = None,
        kprove_command: str = 'kprove',
        krun_command: str = 'krun',
        extra_unparsing_modules: Iterable[KFlatModule] = (),
        bug_report: Optional[BugReport] = None,
        srcmap_dir: Optional[Path] = None,
        contract_name: Optional[str] = None,
        contract_srcs_dir: Optional[Path] = None,
    ) -> None:
        # I'm going for the simplest version here, we can change later if there is an advantage.
        # https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way
        # Note that they say using `super` supports dependency injection, but I have never liked dependency injection anyway.
        KProve.__init__(
            self,
            definition_dir,
            use_directory=use_directory,
            main_file=main_file,
            command=kprove_command,
            extra_unparsing_modules=extra_unparsing_modules,
            bug_report=bug_report,
        )
        KRun.__init__(
            self,
            definition_dir,
            use_directory=use_directory,
            command=krun_command,
            extra_unparsing_modules=extra_unparsing_modules,
            bug_report=bug_report,
        )
        self._srcmap_dir = srcmap_dir
        self._contract_name = contract_name
        self._contract_ids = {}
        self._srcmaps = {}
        self._contract_srcs = {}
        self._contract_srcs_dir = contract_srcs_dir
        if self._srcmap_dir is not None:
            self._contract_ids = {
                int(k): v for k, v in json.loads((self._srcmap_dir / 'contract_id_map.json').read_text()).items()
            }

    @staticmethod
    def kompile(
        definition_dir: Path,
        backend: KompileBackend,
        main_file: Path,
        emit_json: bool = True,
        includes: Iterable[str] = (),
        main_module_name: Optional[str] = None,
        syntax_module_name: Optional[str] = None,
        md_selector: Optional[str] = None,
        debug: bool = False,
        ccopts: Iterable[str] = (),
        llvm_kompile: bool = True,
        optimization: int = 0,
    ) -> 'KEVM':
        try:
            kompile(
                main_file=main_file,
                output_dir=definition_dir,
                backend=backend,
                emit_json=emit_json,
                include_dirs=[include for include in includes if Path(include).exists()],
                main_module=main_module_name,
                syntax_module=syntax_module_name,
                md_selector=md_selector,
                hook_namespaces=KEVM.hook_namespaces(),
                debug=debug,
                concrete_rules=KEVM.concrete_rules() if backend == KompileBackend.HASKELL else (),
                ccopts=ccopts,
                no_llvm_kompile=not llvm_kompile,
                opt_level=optimization or None,
            )
        except RuntimeError as err:
            sys.stderr.write(f'\nkompile stdout:\n{err.args[1]}\n')
            sys.stderr.write(f'\nkompile stderr:\n{err.args[2]}\n')
            sys.stderr.write(f'\nkompile returncode:\n{err.args[3]}\n')
            sys.stderr.flush()
            raise
        return KEVM(definition_dir, main_file=main_file)

    @classmethod
    def _patch_symbol_table(cls, symbol_table: SymbolTable) -> None:
        # fmt: off
        symbol_table['#Bottom']                                       = lambda: '#Bottom'
        symbol_table['_Map_']                                         = paren(lambda m1, m2: m1 + '\n' + m2)
        symbol_table['_AccountCellMap_']                              = paren(lambda a1, a2: a1 + '\n' + a2)
        symbol_table['.AccountCellMap']                               = lambda: '.Bag'
        symbol_table['AccountCellMapItem']                            = lambda k, v: v
        symbol_table['_<Word__EVM-TYPES_Int_Int_Int']                 = paren(lambda a1, a2: '(' + a1 + ') <Word ('  + a2 + ')')
        symbol_table['_>Word__EVM-TYPES_Int_Int_Int']                 = paren(lambda a1, a2: '(' + a1 + ') >Word ('  + a2 + ')')
        symbol_table['_<=Word__EVM-TYPES_Int_Int_Int']                = paren(lambda a1, a2: '(' + a1 + ') <=Word (' + a2 + ')')
        symbol_table['_>=Word__EVM-TYPES_Int_Int_Int']                = paren(lambda a1, a2: '(' + a1 + ') >=Word (' + a2 + ')')
        symbol_table['_==Word__EVM-TYPES_Int_Int_Int']                = paren(lambda a1, a2: '(' + a1 + ') ==Word (' + a2 + ')')
        symbol_table['_s<Word__EVM-TYPES_Int_Int_Int']                = paren(lambda a1, a2: '(' + a1 + ') s<Word (' + a2 + ')')
        paren_symbols = [
            '_|->_',
            '#And',
            '_andBool_',
            '_:__EVM-TYPES_WordStack_Int_WordStack',
            '#Implies',
            '_impliesBool_',
            '_&Int_',
            '_*Int_',
            '_+Int_',
            '_-Int_',
            '_/Int_',
            '_|Int_',
            '_modInt_',
            'notBool_',
            '#Or',
            '_orBool_',
            '_Set_',
            'typedArgs',
            '_up/Int__EVM-TYPES_Int_Int_Int',
            '_:_WS',
        ]
        for symb in paren_symbols:
            if symb in symbol_table:
                symbol_table[symb] = paren(symbol_table[symb])
        # fmt: on

    class Sorts:
        KEVM_CELL: Final = KSort('KevmCell')

    @staticmethod
    def hook_namespaces() -> List[str]:
        return ['JSON', 'KRYPTO', 'BLOCKCHAIN']

    @staticmethod
    def concrete_rules() -> List[str]:
        return [
            'EVM.allBut64th.pos',
            'EVM.Caddraccess',
            'EVM.Cbalance.new',
            'EVM.Cbalance.old',
            'EVM.Cextcodecopy.new',
            'EVM.Cextcodecopy.old',
            'EVM.Cextcodehash.new',
            'EVM.Cextcodehash.old',
            'EVM.Cextcodesize.new',
            'EVM.Cextcodesize.old',
            'EVM.Cextra.new',
            'EVM.Cextra.old',
            'EVM.Cgascap',
            'EVM.Cmem',
            'EVM.Cmodexp.new',
            'EVM.Cmodexp.old',
            'EVM.Csload.new',
            'EVM.Csstore.new',
            'EVM.Csstore.old',
            'EVM.Cstorageaccess',
            'EVM.ecrec',
            'EVM.#memoryUsageUpdate.some',
            'EVM.Rsstore.new',
            'EVM.Rsstore.old',
            'EVM-TYPES.#asByteStack',
            'EVM-TYPES.#asByteStackAux.recursive',
            'EVM-TYPES.#asWord.recursive',
            'EVM-TYPES.Bytes.range',
            'EVM-TYPES.bytesRange',
            'EVM-TYPES.mapWriteBytes.recursive',
            'EVM-TYPES.#padRightToWidth',
            'EVM-TYPES.padRightToWidthNonEmpty',
            'EVM-TYPES.#padToWidth',
            'EVM-TYPES.padToWidthNonEmpty',
            'EVM-TYPES.powmod.nonzero',
            'EVM-TYPES.powmod.zero',
            'EVM-TYPES.#range',
            'EVM-TYPES.signextend.invalid',
            'EVM-TYPES.signextend.negative',
            'EVM-TYPES.signextend.positive',
            'EVM-TYPES.upDivInt',
            'SERIALIZATION.addrFromPrivateKey',
            'SERIALIZATION.keccak',
            'SERIALIZATION.#newAddr',
            'SERIALIZATION.#newAddrCreate2',
        ]

    def srcmap_data(self, pc: int) -> Optional[Union[Tuple[int, int, int, str, int], Tuple[str, int, int]]]:
        if self._srcmap_dir is not None and self._contract_name is not None and self._contract_ids is not None:
            if self._contract_name not in self._srcmaps:
                _srcmap_pre = json.loads((self._srcmap_dir / f'{self._contract_name}.json').read_text())
                _srcmap: Dict[int, Tuple[int, int, int, str, int]] = {}
                for k, v in _srcmap_pre.items():
                    s, l, f, j, m = v
                    assert type(s) is int
                    assert type(l) is int
                    assert type(f) is int
                    assert type(j) is str
                    assert type(m) is int
                    _srcmap[int(k)] = (s, l, f, j, m)
                self._srcmaps[self._contract_name] = _srcmap
            _srcmap = self._srcmaps[self._contract_name]
            if pc in _srcmap:
                s, l, f, j, m = _srcmap[pc]
                if f in self._contract_ids:
                    contract_file = self._contract_ids[f]
                    if contract_file not in self._contract_srcs:
                        self._contract_srcs[contract_file] = (
                            (self._srcmap_dir.parent.parent / contract_file).read_text().split('\n')
                        )
                    _, start, end = byte_offset_to_lines(self._contract_srcs[contract_file], s, l)
                    return (self._contract_ids[f], start, end)
                else:
                    return (s, l, f, j, m)
            else:
                _LOGGER.warning(f'pc not found in srcmap: {pc}')
        return None

    def short_info(self, cterm: CTerm) -> List[str]:
        _, subst = split_config_from(cterm.config)
        k_cell = self.pretty_print(subst['K_CELL']).replace('\n', ' ')
        if len(k_cell) > 80:
            k_cell = k_cell[0:80] + ' ...'
        k_str = f'k: {k_cell}'
        ret_strs = [k_str]
        for cell, name in [('PC_CELL', 'pc'), ('CALLDEPTH_CELL', 'callDepth'), ('STATUSCODE_CELL', 'statusCode')]:
            if cell in subst:
                ret_strs.append(f'{name}: {self.pretty_print(subst[cell])}')
        _pc = get_cell(cterm.config, 'PC_CELL')
        if type(_pc) is KToken and _pc.sort == INT:
            srcmap = self.srcmap_data(int(_pc.token))
            ret_strs.append(f'src: {srcmap}')
        return ret_strs

    def solidity_src(self, pc: int) -> Iterable[str]:
        srcmap_data = self.srcmap_data(pc)
        if srcmap_data is not None:
            if len(srcmap_data) == 5:
                return [f'NO FILEMAP FOR SOURCEMAP: {srcmap_data}']
            elif len(srcmap_data) == 3:
                _path, start, end, *_ = srcmap_data
                assert type(_path) is str
                assert type(start) is int
                assert type(end) is int
                base_path = self._contract_srcs_dir if self._contract_srcs_dir is not None else Path('./')
                path = base_path / _path
                if path.exists() and path.is_file():
                    lines = path.read_text().split('\n')
                    prefix_lines = [f'   {l}' for l in lines[:start]]
                    actual_lines = [f' | {l}' for l in lines[start:end]]
                    suffix_lines = [f'   {l}' for l in lines[end:]]
                    return prefix_lines + actual_lines + suffix_lines
                else:
                    return [f'NO FILE FOR SOURCEMAP DATA: {srcmap_data}']
        return [f'NO SOURCEMAP DATA: {srcmap_data}']

    def custom_view(self, element: KCFGElem) -> Iterable[str]:
        if type(element) is KCFG.Node:
            pc_cell = get_cell(element.cterm.config, 'PC_CELL')
            if type(pc_cell) is KToken and pc_cell.sort == INT:
                return self.solidity_src(int(pc_cell.token))
        return ['NO DATA']

    @staticmethod
    def add_invariant(cterm: CTerm) -> CTerm:
        config, *constraints = cterm

        word_stack = get_cell(config, 'WORDSTACK_CELL')
        if type(word_stack) is not KVariable:
            word_stack_items = flatten_label('_:__EVM-TYPES_WordStack_Int_WordStack', word_stack)
            for i in word_stack_items[:-1]:
                constraints.append(mlEqualsTrue(KEVM.range_uint(256, i)))

        gas_cell = get_cell(config, 'GAS_CELL')
        if not (type(gas_cell) is KApply and gas_cell.label.name == 'infGas'):
            constraints.append(mlEqualsTrue(KEVM.range_uint(256, gas_cell)))
        constraints.append(mlEqualsTrue(KEVM.range_address(get_cell(config, 'ID_CELL'))))
        constraints.append(mlEqualsTrue(KEVM.range_address(get_cell(config, 'CALLER_CELL'))))
        constraints.append(mlEqualsTrue(KEVM.range_address(get_cell(config, 'ORIGIN_CELL'))))
        constraints.append(mlEqualsTrue(ltInt(KEVM.size_bytes(get_cell(config, 'CALLDATA_CELL')), KEVM.pow128())))

        return CTerm(mlAnd([config] + constraints))

    @staticmethod
    def extract_branches(cterm: CTerm) -> Iterable[KInner]:
        config, *constraints = cterm
        k_cell = get_cell(config, 'K_CELL')
        jumpi_pattern = KEVM.jumpi_applied(KVariable('###PCOUNT'), KVariable('###COND'))
        pc_next_pattern = KApply('#pc[_]_EVM_InternalOp_OpCode', [KEVM.jumpi()])
        branch_pattern = KSequence([jumpi_pattern, pc_next_pattern, KEVM.sharp_execute(), KVariable('###CONTINUATION')])
        if subst := branch_pattern.match(k_cell):
            cond = subst['###COND']
            if cond_subst := KEVM.bool_2_word(KVariable('###BOOL_2_WORD')).match(cond):
                cond = cond_subst['###BOOL_2_WORD']
            else:
                cond = KApply('_==Int_', [cond, intToken(0)])
            return [mlEqualsTrue(cond), mlEqualsTrue(KApply('notBool_', [cond]))]
        return []

    @staticmethod
    def is_terminal(cterm: CTerm) -> bool:
        config, *_ = cterm
        k_cell = get_cell(config, 'K_CELL')
        # <k> #halt </k>
        if k_cell == KEVM.halt():
            return True
        elif type(k_cell) is KSequence:
            # <k> #halt ~> CONTINUATION </k>
            if k_cell.arity == 2 and k_cell[0] == KEVM.halt() and type(k_cell[1]) is KVariable:
                # <callDepth> 0 </callDepth>
                if get_cell(config, 'CALLDEPTH_CELL') == intToken(0):
                    return True
        return False

    @staticmethod
    def halt() -> KApply:
        return KApply('#halt_EVM_KItem')

    @staticmethod
    def sharp_execute() -> KApply:
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
    def pow128() -> KApply:
        return KApply('pow128_WORD_Int', [])

    @staticmethod
    def pow256() -> KApply:
        return KApply('pow256_WORD_Int', [])

    @staticmethod
    def range_uint(width: int, i: KInner) -> KApply:
        return KApply('#rangeUInt(_,_)_WORD_Bool_Int_Int', [intToken(width), i])

    @staticmethod
    def range_sint(width: int, i: KInner) -> KApply:
        return KApply('#rangeSInt(_,_)_WORD_Bool_Int_Int', [intToken(width), i])

    @staticmethod
    def range_address(i: KInner) -> KApply:
        return KApply('#rangeAddress(_)_WORD_Bool_Int', [i])

    @staticmethod
    def range_bool(i: KInner) -> KApply:
        return KApply('#rangeBool(_)_WORD_Bool_Int', [i])

    @staticmethod
    def range_bytes(width: KInner, ba: KInner) -> KApply:
        return KApply('#rangeBytes(_,_)_WORD_Bool_Int_Int', [width, ba])

    @staticmethod
    def bool_2_word(cond: KInner) -> KApply:
        return KApply('bool2Word(_)_EVM-TYPES_Int_Bool', [cond])

    @staticmethod
    def size_bytes(ba: KInner) -> KApply:
        return KApply('lengthBytes(_)_BYTES-HOOKED_Int_Bytes', [ba])

    @staticmethod
    def inf_gas(g: KInner) -> KApply:
        return KApply('infGas', [g])

    @staticmethod
    def compute_valid_jumpdests(p: KInner) -> KApply:
        return KApply('#computeValidJumpDests(_)_EVM_Set_Bytes', [p])

    @staticmethod
    def bin_runtime(c: KInner) -> KApply:
        return KApply('binRuntime', [c])

    @staticmethod
    def hashed_location(compiler: str, base: KInner, offset: KInner, member_offset: int = 0) -> KApply:
        location = KApply(
            '#hashedLocation(_,_,_)_HASHED-LOCATIONS_Int_String_Int_IntList', [stringToken(compiler), base, offset]
        )
        if member_offset > 0:
            location = KApply('_+Int_', [location, intToken(member_offset)])
        return location

    @staticmethod
    def loc(accessor: KInner) -> KApply:
        return KApply('contract_access_loc', [accessor])

    @staticmethod
    def lookup(map: KInner, key: KInner) -> KApply:
        return KApply('#lookup(_,_)_EVM-TYPES_Int_Map_Int', [map, key])

    @staticmethod
    def abi_calldata(name: str, args: List[KInner]) -> KApply:
        return KApply('#abiCallData(_,_)_EVM-ABI_Bytes_String_TypedArgs', [stringToken(name), KEVM.typed_args(args)])

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
        return KApply('_+Bytes__BYTES-HOOKED_Bytes_Bytes_Bytes', [b1, b2])

    @staticmethod
    def account_cell(
        id: KInner, balance: KInner, code: KInner, storage: KInner, orig_storage: KInner, nonce: KInner
    ) -> KApply:
        return KApply(
            '<account>',
            [
                KApply('<acctID>', [id]),
                KApply('<balance>', [balance]),
                KApply('<code>', [code]),
                KApply('<storage>', [storage]),
                KApply('<origStorage>', [orig_storage]),
                KApply('<nonce>', [nonce]),
            ],
        )

    @staticmethod
    def wordstack_len(constrained_term: KInner) -> int:
        return len(flatten_label('_:__EVM-TYPES_WordStack_Int_WordStack', get_cell(constrained_term, 'WORDSTACK_CELL')))

    @staticmethod
    def parse_bytestack(s: KInner) -> KApply:
        return KApply('#parseByteStack(_)_SERIALIZATION_Bytes_String', [s])

    @staticmethod
    def bytes_empty() -> KApply:
        return KApply('.Bytes_BYTES-HOOKED_Bytes')

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

    @staticmethod
    def accounts(accts: List[KInner]) -> KInner:
        wrapped_accounts: List[KInner] = []
        for acct in accts:
            if type(acct) is KApply and acct.label.name == '<account>':
                acct_id = acct.args[0]
                wrapped_accounts.append(KApply('AccountCellMapItem', [acct_id, acct]))
            else:
                wrapped_accounts.append(acct)
        return build_assoc(KApply('.AccountCellMap'), KLabel('_AccountCellMap_'), wrapped_accounts)
