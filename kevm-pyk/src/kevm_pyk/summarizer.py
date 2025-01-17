from __future__ import annotations

from itertools import count
import logging
from platform import node
import time
import traceback
from multiprocessing import Pool
from pathlib import Path
from typing import TYPE_CHECKING

from pyk.cterm import CSubst, CTerm, CTermSymbolic, cterm_build_claim
from pyk.kast.inner import KApply, KInner, KSequence, KToken, KVariable, Subst
from pyk.kast.outer import KSort, KClaim
from pyk.kcfg import KCFGExplore, KCFG
from pyk.kdist import kdist
from pyk.kore.rpc import KoreClient
from pyk.proof import APRProof
from pyk.proof.show import APRProofShow
from pyk.utils import ensure_dir_path
from pyk.prelude.ml import mlEqualsFalse, mlEqualsTrue, mlEquals, mlOr, mlNot

from kevm_pyk.kevm import KEVM, KEVMSemantics, kevm_node_printer
from kevm_pyk.utils import initialize_apr_proof, legacy_explore, run_prover

if TYPE_CHECKING:
    from pathlib import Path

_LOGGER = logging.getLogger(__name__)

OPCODES: dict[str, KApply] = {
    'STOP': KApply('STOP_EVM_NullStackOp'),
    'ADD': KApply('ADD_EVM_BinStackOp'),
    'MUL': KApply('MUL_EVM_BinStackOp'),
    'SUB': KApply('SUB_EVM_BinStackOp'),
    'DIV': KApply('DIV_EVM_BinStackOp'),
    'SDIV': KApply('SDIV_EVM_BinStackOp'),
    'MOD': KApply('MOD_EVM_BinStackOp'),
    'SMOD': KApply('SMOD_EVM_BinStackOp'),
    'ADDMOD': KApply('ADDMOD_EVM_TernStackOp'),
    'MULMOD': KApply('MULMOD_EVM_TernStackOp'),
    'EXP': KApply('EXP_EVM_BinStackOp'),
    'SIGNEXTEND': KApply('SIGNEXTEND_EVM_BinStackOp'),
    'LT': KApply('LT_EVM_BinStackOp'),
    'GT': KApply('GT_EVM_BinStackOp'),
    'SLT': KApply('SLT_EVM_BinStackOp'),
    'SGT': KApply('SGT_EVM_BinStackOp'),
    'EQ': KApply('EQ_EVM_BinStackOp'),
    'ISZERO': KApply('ISZERO_EVM_UnStackOp'),
    'AND': KApply('AND_EVM_BinStackOp'),
    'EVMOR': KApply('EVMOR_EVM_BinStackOp'),
    'XOR': KApply('XOR_EVM_BinStackOp'),
    'NOT': KApply('NOT_EVM_UnStackOp'),
    'BYTE': KApply('BYTE_EVM_BinStackOp'),
    'SHL': KApply('SHL_EVM_BinStackOp'),
    'SHR': KApply('SHR_EVM_BinStackOp'),
    'SAR': KApply('SAR_EVM_BinStackOp'),
    'SHA3': KApply('SHA3_EVM_BinStackOp'),
    'ADDRESS': KApply('ADDRESS_EVM_NullStackOp'),
    'BALANCE': KApply('BALANCE_EVM_UnStackOp'),
    'ORIGIN': KApply('ORIGIN_EVM_NullStackOp'),
    'CALLER': KApply('CALLER_EVM_NullStackOp'),
    'CALLVALUE': KApply('CALLVALUE_EVM_NullStackOp'),
    'CALLDATALOAD': KApply('CALLDATALOAD_EVM_UnStackOp'),
    'CALLDATASIZE': KApply('CALLDATASIZE_EVM_NullStackOp'),
    'CALLDATACOPY': KApply('CALLDATACOPY_EVM_TernStackOp'),
    'CODESIZE': KApply('CODESIZE_EVM_NullStackOp'),
    'CODECOPY': KApply('CODECOPY_EVM_TernStackOp'),
    'GASPRICE': KApply('GASPRICE_EVM_NullStackOp'),
    'EXTCODESIZE': KApply('EXTCODESIZE_EVM_UnStackOp'),
    'EXTCODECOPY': KApply('EXTCODECOPY_EVM_QuadStackOp'),
    'RETURNDATASIZE': KApply('RETURNDATASIZE_EVM_NullStackOp'),
    'RETURNDATACOPY': KApply('RETURNDATACOPY_EVM_TernStackOp'),
    'EXTCODEHASH': KApply('EXTCODEHASH_EVM_UnStackOp'),
    'BLOCKHASH': KApply('BLOCKHASH_EVM_UnStackOp'),
    'COINBASE': KApply('COINBASE_EVM_NullStackOp'),
    'TIMESTAMP': KApply('TIMESTAMP_EVM_NullStackOp'),
    'NUMBER': KApply('NUMBER_EVM_NullStackOp'),
    'PREVRANDAO': KApply('PREVRANDAO_EVM_NullStackOp'),
    'DIFFICULTY': KApply('DIFFICULTY_EVM_NullStackOp'),
    'GASLIMIT': KApply('GASLIMIT_EVM_NullStackOp'),
    'CHAINID': KApply('CHAINID_EVM_NullStackOp'),
    'SELFBALANCE': KApply('SELFBALANCE_EVM_NullStackOp'),
    'BASEFEE': KApply('BASEFEE_EVM_NullStackOp'),
    'POP': KApply('POP_EVM_UnStackOp'),
    'MLOAD': KApply('MLOAD_EVM_UnStackOp'),
    'MSTORE': KApply('MSTORE_EVM_BinStackOp'),
    'MSTORE8': KApply('MSTORE8_EVM_BinStackOp'),
    'SLOAD': KApply('SLOAD_EVM_UnStackOp'),
    'SSTORE': KApply('SSTORE_EVM_BinStackOp'),
    'JUMP': KApply('JUMP_EVM_UnStackOp'),
    'JUMPI': KApply('JUMPI_EVM_BinStackOp'),
    'PC': KApply('PC_EVM_NullStackOp'),
    'MSIZE': KApply('MSIZE_EVM_NullStackOp'),
    'GAS': KApply('GAS_EVM_NullStackOp'),
    'JUMPDEST': KApply('JUMPDEST_EVM_NullStackOp'),
    'TLOAD': KApply('TLOAD_EVM_UnStackOp'),
    'TSTORE': KApply('TSTORE_EVM_BinStackOp'),
    'MCOPY': KApply('MCOPY_EVM_TernStackOp'),
    'PUSHZERO': KApply('PUSHZERO_EVM_PushOp'),
    'PUSH': KApply('PUSH', KVariable('N', KSort('Int'))),
    'DUP': KApply('DUP', KVariable('N', KSort('Int'))),
    'SWAP': KApply('SWAP', KVariable('N', KSort('Int'))),
    'LOG': KApply('LOG', KVariable('N', KSort('Int'))),
    'CREATE': KApply('CREATE_EVM_TernStackOp'),
    'CALL': KApply('CALL_EVM_CallOp'),
    'CALLCODE': KApply('CALLCODE_EVM_CallOp'),
    'RETURN': KApply('RETURN_EVM_BinStackOp'),
    'DELEGATECALL': KApply('DELEGATECALL_EVM_CallSixOp'),
    'CREATE2': KApply('CREATE2_EVM_QuadStackOp'),
    'STATICCALL': KApply('STATICCALL_EVM_CallSixOp'),
    'REVERT': KApply('REVERT_EVM_BinStackOp'),
    'INVALID': KApply('INVALID_EVM_InvalidOp'),
    'SELFDESTRUCT': KApply('SELFDESTRUCT_EVM_UnStackOp'),
    'UNDEFINED': KApply('UNDEFINED(_)_EVM_InvalidOp_Int', KVariable('W', KSort('Int'))),
    # OpCode Variable
    # 'ALL': KVariable('OP_CODE', KSort('OpCode'))
}

OPCODES_PRECONDITIONS = {
    # 'STOP': 'TODICUSS, all the leaves are terminal or stuck, find NDBranch',
    'STACK_UNDERFLOW': ''
}

OPCODES_SUMMARY_STATUS = {
    'STOP': 'PASSED, One rule? Several rules?',
    'ADD': 'PASSED, No underflow check in KCFG',
    'MUL': 'PASSED, No underflow check in KCFG',
    'SUB': 'PASSED, No underflow check in KCFG',
    'DIV': 'PASSED, No underflow check in KCFG',
    'SDIV': 'PASSED, No underflow check in KCFG',
    'MOD': 'PASSED, No underflow check in KCFG',
    'SMOD': 'PASSED, No underflow check in KCFG',
    'ADDMOD': 'PASSED, No underflow check in KCFG',
    'MULMOD': 'PASSED, No underflow check in KCFG',
    'EXP': 'PASSED, No underflow check in KCFG',
    'SIGNEXTEND': 'PASSED, No underflow check in KCFG',
    'LT': 'PASSED, No underflow check in KCFG',
    'GT': 'PASSED, No underflow check in KCFG',
    'SLT': 'PASSED, No underflow check in KCFG',
    'SGT': 'PASSED, No underflow check in KCFG',
    'EQ' : 'PASSED, No underflow check in KCFG',
    'ISZERO': 'PASSED, No underflow check in KCFG',
    'AND': 'PASSED, No underflow check in KCFG',
    'EVMOR': 'PASSED, No underflow check in KCFG',
    'XOR': 'PASSED, No underflow check in KCFG',
    'NOT': 'PASSED, No underflow check in KCFG',
    'BYTE': 'PASSED, No underflow check in KCFG',
    'SHL': 'PASSED, No underflow check in KCFG',
    'SHR': 'PASSED, No underflow check in KCFG',
    'SAR': 'PASSED, No underflow check in KCFG',
    'SHA3': 'PASSED, No underflow check in KCFG',
    'ADDRESS': 'PASSED, No underflow check, no .Account',
    'BALANCE': 'PASSED, no underflow check, no gas usage',
    'ORIGIN': 'PASSED, no underflow check, no .Account in origin cell',
    'CALLER': 'PASSED, no underflow check, no gas usage',
    'CALLVALUE': 'PASSED, No underflow check in KCFG',
    'CALLDATALOAD': 'PASSED, No underflow check in KCFG',
    'CALLDATASIZE': 'PASSED, No underflow check in KCFG',
    'CALLDATACOPY': 'PASSED, No underflow check in KCFG',
    'CODESIZE': 'PASSED, No underflow check in KCFG',
    'CODECOPY': 'PASSED, No underflow check in KCFG',
    'GASPRICE': 'PASSED, No underflow check in KCFG',
    'EXTCODESIZE': 'PASSED, No underflow check, No gas usage',
    'EXTCODECOPY': 'PASSED, No underflow check, No gas usage',
    'RETURNDATASIZE': 'PASSED, No underflow check, No gas usage',
    'RETURNDATACOPY': 'PASSED, No underflow check in KCFG',
    'EXTCODEHASH': 'PASSED, No underflow check, No gas usage',
    'BLOCKHASH': 'PASSED, No underflow check in KCFG',
    'COINBASE': 'PASSED, No underflow check, No gas usage',
    'TIMESTAMP': 'PASSED, No underflow check in KCFG',
    'NUMBER': 'PASSED, No underflow check in KCFG',
    'PREVRANDAO': 'PASSED, No underflow check in KCFG',
    'DIFFICULTY': 'PASSED, No underflow check in KCFG',
    'GASLIMIT': 'PASSED, No underflow check in KCFG',
    'CHAINID': 'PASSED, No underflow check in KCFG',
    'SELFBALANCE': 'PASSED, No underflow check in KCFG',
    'BASEFEE': 'PASSED, No underflow check in KCFG',
    'POP': 'PASSED, No underflow check, no gas usage',
    'MLOAD': 'PASSED, No underflow check, no gas usage',
    'MSTORE': 'PASSED, No underflow check in KCFG',
    'MSTORE8': 'PASSED, No underflow check, no gas usage',
    'SLOAD': 'PASSED, No underflow check in KCFG',
    'SSTORE': 'PASSED, No underflow check in KCFG',
    'JUMP': 'PASSED, No underflow check, wierd ndbranch that looks like a split',
    'JUMPI': 'PASSED, no underflow check, no gas usage, weird ndbranch that looks like a split',
    'PC': 'PASSED, No underflow check in KCFG',
    'MSIZE': 'PASSED, No underflow check in KCFG, no gas usage',
    'GAS': 'PASSED, No underflow check in KCFG',
    'JUMPDEST': 'PASSED, No underflow check in KCFG',
    'TLOAD': 'PASSED, No underflow check, no gas usage',
    'TSTORE': 'PASSED, No underflow check, no gas usage, strange info about smt reason timeout',
    'MCOPY': 'PASSED, No underflow check in KCFG',
    'PUSHZERO': 'PASSED, No underflow check in KCFG',
    'PUSH': 'PASSED, No underflow check, no gas usage',
    'DUP': 'PASSED, No underflow check in KCFG',
    'SWAP': 'PASSED, No underflow check in KCFG',
    'LOG': 'TODO, Proof crashed',
    'CREATE': 'TODO, Proof crashed',
    'CALL': 'UNCHECKED',
    'CALLCODE': 'UNCHECKED',
    'RETURN': 'UNCHECKED',
    'DELEGATECALL': 'UNCHECKED',
    'CREATE2': 'UNCHECKED',
    'STATICCALL': 'UNCHECKED',
    'REVERT': 'UNCHECKED',
    'INVALID': 'UNCHECKED',
    'SELFDESTRUCT': 'UNCHECKED',
    'UNDEFINED': 'PASSED',
    'ALL': 'TODICUSS, failed to summarize, the optimized rule applies one step to obtain the target, the failure process rules are applied to obtain the failure, we need to summarize these ndbranches and exclude these conditions from individual opcode spec',
}

def get_passed_opcodes() -> list[str]:
    passed_opcodes = []
    for opcode in OPCODES_SUMMARY_STATUS:
        if get_summary_status(opcode) == 'PASSED':
            passed_opcodes.append(opcode)
    return passed_opcodes


def get_summary_status(opcode: str) -> str:
    assert opcode in OPCODES_SUMMARY_STATUS
    return OPCODES_SUMMARY_STATUS[opcode].split(',')[0]

def word_stack(size_over: int) -> KInner:
    def _word_stack_var(n: int) -> KInner:
        return KVariable(f'W{n}', KSort('Int'))
    
    def _word_stack(w0: KInner, w1: KInner) -> KInner:
        return KApply('_:__EVM-TYPES_WordStack_Int_WordStack', [w0, w1])
    
    ws = KVariable('WS', KSort('WordStack'))
    for i in reversed(range(size_over)):
        ws = _word_stack(_word_stack_var(i), ws)
    return ws

def get_todo_list() -> list[str]:
    todo_list = []
    _LOGGER.info(f'Number of opcodes: {len(OPCODES)}')
    for opcode in OPCODES:
        if get_summary_status(opcode) != 'PASSED':
            todo_list.append(opcode)
    _LOGGER.info(f'Number of passed opcodes: {len(OPCODES)-len(todo_list)}')
    _LOGGER.info(f'Number of todo opcodes: {len(todo_list)}')
    _LOGGER.info(f'Todo opcodes: {todo_list}')
    return todo_list

def stack_needed(opcode_id: str) -> list[int]:
    """
    Return the stack size needed for the opcode, corresponding `#stackNeeded` in the semantics.
    """
    opcode = OPCODES[opcode_id].label.name
    if 'CallOp' in opcode:
        return [7]
    elif 'CallSixOp' in opcode:
        return [6]
    elif 'LOG' in opcode:
        return range(5)
    elif 'SWAP' in opcode:
        return range(1, 17)
    elif 'DUP' in opcode:
        return range(1, 17)
    elif 'QuadStackOp' in opcode:
        return [4]
    elif 'TernStackOp' in opcode:
        return [3]
    elif 'BinStackOp' in opcode:
        return [2]
    elif 'UnStackOp' in opcode:
        return [1]
    return [0]
    
    
    
class KEVMSummarizer:
    """
    A class for summarizing the instructions of the KEVM.

    TODO:
    1. Build the proof to symbolically execute one abitrary instruction.
    2. Run the proof to get the KCFG.
    3. Summarize the KCFG to get the summarized rules for the instructions.
    """

    _cterm_symbolic: CTermSymbolic
    kevm: KEVM
    proof_dir: Path
    save_directory: Path

    def __init__(self, proof_dir: Path, save_directory: Path) -> None:
        self.kevm = KEVM(kdist.get('evm-semantics.haskell'))
        self.proof_dir = proof_dir
        self.save_directory = save_directory

    def build_spec(
        self,
        opcode: KApply,
        stack_needed: int,
        id_str: str = ''
    ) -> APRProof:
        """
        Build the specification to symbolically execute one abitrary instruction.
        """
        cterm = CTerm(self.kevm.definition.empty_config(KSort('GeneratedTopCell')))

        # construct the initial substitution
        # opcode = OPCODES[opcode_symbol]
        next_opcode = KApply('#next[_]_EVM_InternalOp_MaybeOpCode', opcode)
        _init_subst: dict[str, KInner] = {'K_CELL': KSequence([next_opcode, KVariable('K_CELL')])}
        _init_subst['WORDSTACK_CELL'] = word_stack(stack_needed)
        init_subst = CSubst(Subst(_init_subst), ())

        # construct the final substitution
        _final_subst: dict[str, KInner] = {vname: KVariable('FINAL_' + vname) for vname in cterm.free_vars}
        _final_subst['K_CELL'] = KVariable('K_CELL')
        final_subst = CSubst(Subst(_final_subst), ())

        opcode_symbol = opcode.label.name.split('_')[0]
    
        kclaim, subst = cterm_build_claim(f'{opcode_symbol}{id_str}_{stack_needed}_SPEC', init_subst(cterm), final_subst(cterm))
        # >> TODO: The cterm_build_claim will remove all the type I've set.
        kclaim = KClaim(subst(kclaim.body), subst(kclaim.requires), subst(kclaim.ensures), kclaim.att)
        proof = APRProof.from_claim(self.kevm.definition, kclaim, {}, self.proof_dir)
        if opcode_symbol == 'ADDRESS':
            # >> CHECK THIS: Because #push doesn't handle `.Account`, we need to set the type of `ID_CELL` to `Int`
            _LOGGER.info(f'Setting the type of `ID_CELL` to `Int` for {opcode_symbol}')
            _type_subst: dict[str, KInner] = {'ID_CELL': KVariable('ID_CELL', KSort('Int'))}
            type_subst = CSubst(Subst(_type_subst), ())
            node = proof.kcfg.get_node(1)
            proof.kcfg.let_node(1, cterm=type_subst(node.cterm), attrs=node.attrs)
        if opcode_symbol == 'CALLER':
            _LOGGER.info(f'Setting the type of `CALLER_CELL` to `Int` for {opcode_symbol}')
            _type_subst: dict[str, KInner] = {'CALLER_CELL': KVariable('CALLER_CELL', KSort('Int'))}
            type_subst = CSubst(Subst(_type_subst), ())
            node = proof.kcfg.get_node(1)
            proof.kcfg.let_node(1, cterm=type_subst(node.cterm), attrs=node.attrs)
        if opcode_symbol == 'ORIGIN':
            _LOGGER.info(f'Setting the type of `ORIGIN_CELL` to `Int` for {opcode_symbol}')
            _type_subst: dict[str, KInner] = {'ORIGIN_CELL': KVariable('ORIGIN_CELL', KSort('Int'))}
            type_subst = CSubst(Subst(_type_subst), ())
            node = proof.kcfg.get_node(1)
            proof.kcfg.let_node(1, cterm=type_subst(node.cterm), attrs=node.attrs)
        if opcode_symbol in ['BALANCE', 'EXTCODESIZE', 'EXTCODECOPY', 'CALLER', 'RETURNDATASIZE', 'EXTCODEHASH', 'COINBASE', 'SELFBALANCE', 'POP', 'MLOAD', 'MSTORE8', 'SLOAD', 'SSTORE', 'JUMP', 'JUMPI', 'MSIZE', 'TLOAD', 'TSTORE', 'PUSH']:
            # >> CHECK THIS: don't calculate Gas
            _LOGGER.info(f'Setting the type of `USEGAS_CELL` to `false` for {opcode_symbol}')
            _gas_subst: dict[str, KInner] = {'USEGAS_CELL': KToken('false', KSort('Bool'))}
            gas_subst = CSubst(Subst(_gas_subst), ())
            node = proof.kcfg.get_node(1)
            proof.kcfg.let_node(1, cterm=gas_subst(node.cterm), attrs=node.attrs)
        if opcode_symbol in ['SELFBALANCE', 'SLOAD', 'SSTORE', 'TLOAD', 'TSTORE']:
            _LOGGER.info(f'Setting the type of `ID_CELL` to `Int` for {opcode_symbol}')
            _subst: dict[str, KInner] = {'ID_CELL': KVariable('ID_CELL', KSort('Int'))}
            
            _LOGGER.info(f'Setting more concrete `ACCOUNTS_CELL` for {opcode_symbol}')
            acct_id_cell = KApply('<acctID>', KVariable('ID_CELL', KSort('Int')))
            balance_cell = KApply('<balance>', KVariable('BALANCE_CELL', KSort('Int')))
            code_cell = KApply('<code>', KVariable('CODE_CELL', KSort('AccountCode')))
            storage_cell = KApply('<storage>', KVariable('STORAGE_CELL', KSort('Map')))
            orig_storage_cell = KApply('<origStorage>', KVariable('ORIG_STORAGE_CELL', KSort('Map')))
            transient_storage_cell = KApply('<transientStorage>', KVariable('TRANSIENT_STORAGE_CELL', KSort('Map')))
            nonce_cell = KApply('<nonce>', KVariable('NONCE_CELL', KSort('Int')))
            account_cell = KApply('<account>', [acct_id_cell, balance_cell, code_cell, storage_cell, orig_storage_cell, transient_storage_cell, nonce_cell])
            dot_account_var = KVariable('DotAccountVar', KSort('AccountCellMap'))
            _subst['ACCOUNTS_CELL'] = KApply('_AccountCellMap_', [account_cell, dot_account_var])
            
            _LOGGER.info(f'Setting constraints on `ACCOUNTS_CELL` for {opcode_symbol}')
            constraint = mlEqualsFalse(KApply('AccountCellMap:in_keys', [KApply('<acctID>', KVariable('ID_CELL', KSort('Int'))), KVariable('DotAccountVar', KSort('AccountCellMap'))]))
            
            subst = CSubst(Subst(_subst), ())
            node = proof.kcfg.get_node(1)
            new_cterm = subst(node.cterm)
            new_cterm = new_cterm.add_constraint(constraint)
            proof.kcfg.let_node(1, cterm=new_cterm, attrs=node.attrs)
        
        if opcode_symbol in ['JUMP']:
            _LOGGER.info(f'Setting the final state of `K_CELL` to `#endBasicBlock ~> K_CELL` for {opcode_symbol}')
            _subst = {'K_CELL': KSequence([KApply('#endBasicBlock_EVM_InternalOp'), KVariable('K_CELL')])}
            subst = CSubst(Subst(_subst), ())
            node = proof.kcfg.get_node(2)
            proof.kcfg.let_node(2, cterm=subst(node.cterm), attrs=node.attrs)
            
        # if opcode_symbol in ['JUMPI']:
        #     _LOGGER.info(f'Setting the final state of `K_CELL` to `#endBasicBlock ~> K_CELL` for {opcode_symbol}')
        #     _subst = {'K_CELL': KVariable('FINAL_K_CELL')}
        #     subst = CSubst(Subst(_subst), ())
        #     node = proof.kcfg.get_node(2)
        #     constraint0 = mlEquals(KVariable('FINAL_K_CELL'), KVariable('K_CELL'))
        #     constraint1 = mlEquals(KVariable('FINAL_K_CELL'), KSequence([KApply('#endBasicBlock_EVM_InternalOp'), KVariable('K_CELL')]))
        #     constraint = mlOr([constraint0, constraint1])
        #     proof.kcfg.let_node(2, cterm=subst(node.cterm).add_constraint(constraint), attrs=node.attrs)
            
        _LOGGER.debug(proof.kcfg.nodes[0].cterm.to_dict())
        return proof

    def explore(self, proof: APRProof) -> None:
        """
        Execute the specification to explore the KCFG for all possible instructions.
        """

        # Construct the KCFGExplore
        # Copy from kevm-pyk/src/kevm_pyk/__main__.py/exec_prove
        # TODO: Make this process as an independent function to reuse； best to be in pyk.

        def _init_and_run_proof(proof: APRProof) -> tuple[bool, list[str]]:
            with legacy_explore(
                self.kevm,
                kcfg_semantics=KEVMSemantics(allow_symbolic_program=True),
                id=proof.id,
                llvm_definition_dir=self.kevm.definition_dir / 'llvm-library',
                bug_report=None,
                kore_rpc_command=('kore-rpc-booster',),
                smt_timeout=None,
                smt_retry_limit=None,
                log_succ_rewrites=True,
                log_fail_rewrites=True,
                fallback_on=None,
                interim_simplification=25,
                no_post_exec_simplify=False,
                port=None,
                haskell_threads=8,
            ) as kcfg_explore:

                def create_kcfg_explore() -> KCFGExplore:
                    client = KoreClient(
                        'localhost',
                        kcfg_explore.cterm_symbolic._kore_client.port,
                        bug_report=None,
                        bug_report_id=None,
                        dispatch=None,
                    )
                    cterm_symbolic = CTermSymbolic(
                        client,
                        self.kevm.definition,
                        log_succ_rewrites=True,
                        log_fail_rewrites=True,
                    )
                    return KCFGExplore(
                        cterm_symbolic,
                        kcfg_semantics=KEVMSemantics(allow_symbolic_program=True),
                        id=proof.id,
                    )

                initialize_apr_proof(kcfg_explore.cterm_symbolic, proof)
                proof.write_proof_data()

                start_time = time.time()
                passed = run_prover(
                    proof,
                    create_kcfg_explore=create_kcfg_explore,
                    max_depth=1000,
                    max_iterations=None,
                    cut_point_rules=KEVMSemantics.cut_point_rules(
                        break_on_jumpi=False,
                        break_on_jump=False,
                        break_on_calls=False,
                        break_on_storage=False,
                        break_on_basic_blocks=False,
                        break_on_load_program=False,
                    ),
                    terminal_rules=KEVMSemantics.terminal_rules(False),
                    fail_fast=False,
                    fast_check_subsumption=False,
                    direct_subproof_rules=False,
                    max_frontier_parallel=8,
                    force_sequential=False,
                    assume_defined=False,
                    optimize_kcfg=False,
                )
            end_time = time.time()
            print(f'Proof timing {proof.id}: {end_time - start_time}s')
            # failure_log = None

            node_printer = kevm_node_printer(self.kevm, proof)
            proof_show = APRProofShow(self.kevm, node_printer=node_printer)

            res_lines = proof_show.show(
                proof,
                nodes=[node.id for node in proof.kcfg.nodes],
            )

            return passed, res_lines

        passed, res_lines = _init_and_run_proof(proof)

        ensure_dir_path(self.save_directory / proof.id)
        with open(self.save_directory / proof.id / 'proof-result.txt', 'w') as f:
            f.write(f'Proof {proof.id} Passed' if passed else f'Proof {proof.id} Failed')
            f.write('\n')
            for line in res_lines:
                f.write(line)
                f.write('\n')

    def summarize(self, proof: APRProof, merge: bool = False) -> None:
        # TODO: need customized minimization rules, maybe
        proof.minimize_kcfg(KEVMSemantics(allow_symbolic_program=True), merge)
        node_printer = kevm_node_printer(self.kevm, proof)
        proof_show = APRProofShow(self.kevm, node_printer=node_printer)
        ensure_dir_path(self.save_directory / proof.id)
        with open(self.save_directory / proof.id / 'summary.md', 'w') as f:
            for res_line in proof_show.show(proof, to_module=True):
                f.write(res_line)
                f.write('\n')

    def analyze_proof(self, proof_id: str, node_id: int) -> None:
        proof = APRProof.read_proof_data(self.proof_dir, proof_id)
        for successor in proof.kcfg.successors(node_id):
            print('Type: ', type(successor))
            print('Source: ', successor.source.id)
            if isinstance(successor, KCFG.Edge) or isinstance(successor, KCFG.NDBranch):
                print('Rules: ', successor.rules)
            print('Target: ', [target.id for target in successor.targets])


def _process_opcode(opcode: str) -> None:
    try:
        summarize(opcode)
        _LOGGER.info(f'Successfully processed opcode: {opcode}')
    except Exception as e:
        _LOGGER.error(f'Failed to process opcode {opcode}: {str(e)}')
        _LOGGER.debug(traceback.format_exc())


def batch_summarize(num_processes: int = 4) -> None:
    """
    Parallelize the summarization of opcodes using multiple processes.

    Args:
        num_processes: Number of parallel processes to use. Defaults to 4.
    """

    opcodes_to_process = [op for op in OPCODES.keys()]
    passed_opcodes = get_passed_opcodes()
    unpassed_opcodes = [opcode for opcode in opcodes_to_process if opcode not in passed_opcodes]
    # 分成两组，一组是有CALL的，一组是没有的
    has_call_opcodes = [opcode for opcode in unpassed_opcodes if 'Call' in OPCODES[opcode].label.name]
    no_call_opcodes = [opcode for opcode in unpassed_opcodes if 'Call' not in OPCODES[opcode].label.name]
    
    _LOGGER.info(f'Starting batch summarization of {len(unpassed_opcodes)} opcodes with {num_processes} processes')

    with Pool(processes=num_processes) as pool:
        _LOGGER.info(f'Summarizing {len(no_call_opcodes)} opcodes without CALL')
        pool.map(_process_opcode, no_call_opcodes)
        _LOGGER.info(f'Summarizing {len(has_call_opcodes)} opcodes with CALL')
        pool.map(_process_opcode, has_call_opcodes)

    _LOGGER.info('Batch summarization completed')


def summarize(opcode_symbol: str) -> None:
    proof_dir = Path(__file__).parent / 'proofs'
    save_directory = Path(__file__).parent / 'summaries'
    summarizer = KEVMSummarizer(proof_dir, save_directory)
    needs = stack_needed(opcode_symbol)
    opcode = OPCODES[opcode_symbol]
    for need in needs:
        if len(needs) > 1:
            opcode = KApply(opcode.label.name, KToken(str(need), KSort('Int')))
        if opcode_symbol == 'JUMPI':
            proof = summarizer.build_spec(opcode, need, id_str='_FALSE')
            constraint = mlEquals(KVariable('W1', KSort('Int')), KToken('0', KSort('Int')), 'Int')
            proof.kcfg.let_node(1, cterm=proof.kcfg.get_node(1).cterm.add_constraint(constraint), attrs=proof.kcfg.get_node(1).attrs)
            summarizer.explore(proof)
            summarizer.summarize(proof)
            
            proof = summarizer.build_spec(opcode, need, id_str='_TRUE')
            _subst = {'K_CELL': KSequence([KApply('#endBasicBlock_EVM_InternalOp'), KVariable('K_CELL')])}
            subst = CSubst(Subst(_subst), ())
            constraint = mlNot(mlEquals(KVariable('W1', KSort('Int')), KToken('0', KSort('Int')), 'Int'))
            proof.kcfg.let_node(1, cterm=proof.kcfg.get_node(1).cterm.add_constraint(constraint), attrs=proof.kcfg.get_node(1).attrs)
            proof.kcfg.let_node(2, cterm=subst(proof.kcfg.get_node(2).cterm), attrs=proof.kcfg.get_node(2).attrs)
            summarizer.explore(proof)
            summarizer.summarize(proof)
        else:
            proof = summarizer.build_spec(opcode, need)
            summarizer.explore(proof)
            summarizer.summarize(proof)
    # summarizer.analyze_proof(proof_dir / 'STOP_SPEC')
    

def analyze_proof(opcode: str, node_id: int) -> None:
    proof_dir = Path(__file__).parent / 'proofs'
    save_directory = Path(__file__).parent / 'summaries'
    summarizer = KEVMSummarizer(proof_dir, save_directory)
    summarizer.analyze_proof(proof_dir / f'{opcode}_SPEC', node_id)
