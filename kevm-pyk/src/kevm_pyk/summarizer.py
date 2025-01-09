from __future__ import annotations


import json
import logging
import time
from typing import TYPE_CHECKING

from pyk.cterm import CSubst, CTerm, CTermSymbolic, cterm_build_claim
from pyk.kast.inner import KApply, KInner, KSequence, KToken, KVariable, Subst
from pyk.kast.outer import KSort
from pyk.kcfg import KCFGExplore, KCFG
from pyk.kdist import kdist
from pyk.kore.rpc import KoreClient
from pyk.proof import APRProof
from pyk.proof.show import APRProofShow
from pyk.utils import ensure_dir_path

from kevm_pyk.kevm import KEVM, KEVMSemantics, kevm_node_printer
from kevm_pyk.utils import initialize_apr_proof, legacy_explore, run_prover

if TYPE_CHECKING:
    from pathlib import Path

_LOGGER = logging.getLogger(__name__)

OPCODES = {
    'STOP': KApply('STOP_EVM_NullStackOp'),
    'ADD': KApply('ADD_EVM_BinStackOp'),
    'MUL': KApply('MUL_EVM_BinStackOp'),
    'SUB': KApply('SUB_EVM_BinStackOp'),
    'DIV': KApply('DIV_EVM_BinStackOp'),
    'SDIV': KApply('SDIV_EVM_BinStackOp'),
    'MOD': KApply('MOD_EVM_BinStackOp'),
    'SMOD': KApply('SMOD_EVM_BinStackOp'),
    'ADDMOD': KApply('ADDMOD_EVM_BinStackOp'),
    'MULMOD': KApply('MULMOD_EVM_BinStackOp'),
    'EXP': KApply('EXP_EVM_BinStackOp'),
    'SIGNEXTEND': KApply('SIGNEXTEND_EVM_BinStackOp'),
    'LT': KApply('LT_EVM_BinStackOp'),
    'GT': KApply('GT_EVM_BinStackOp'),
    'SLT': KApply('SLT_EVM_BinStackOp'),
    'SGT': KApply('SGT_EVM_BinStackOp'),
    'EQ': KApply('EQ_EVM_BinStackOp'),
    'ISZERO': KApply('ISZERO_EVM_BinStackOp'),
    'AND': KApply('AND_EVM_BinStackOp'),
    'EVMOR': KApply('EVMOR_EVM_BinStackOp'),
    'XOR': KApply('XOR_EVM_BinStackOp'),
    'NOT': KApply('NOT_EVM_BinStackOp'),
    'BYTE': KApply('BYTE_EVM_BinStackOp'),
    'SHL': KApply('SHL_EVM_BinStackOp'),
    'SHR': KApply('SHR_EVM_BinStackOp'),
    'SAR': KApply('SAR_EVM_BinStackOp'),
    'SHA3': KApply('SHA3_EVM_BinStackOp'),
    'ADDRESS': KApply('ADDRESS_EVM_BinStackOp'),
    'BALANCE': KApply('BALANCE_EVM_BinStackOp'),
    'ORIGIN': KApply('ORIGIN_EVM_BinStackOp'),
    'CALLER': KApply('CALLER_EVM_BinStackOp'),
    'CALLVALUE': KApply('CALLVALUE_EVM_BinStackOp'),
    'CALLDATALOAD': KApply('CALLDATALOAD_EVM_BinStackOp'),
    'CALLDATASIZE': KApply('CALLDATASIZE_EVM_BinStackOp'),
    'CALLDATACOPY': KApply('CALLDATACOPY_EVM_BinStackOp'),
    'CODESIZE': KApply('CODESIZE_EVM_BinStackOp'),
    'CODECOPY': KApply('CODECOPY_EVM_BinStackOp'),
    'GASPRICE': KApply('GASPRICE_EVM_BinStackOp'),
    'EXTCODESIZE': KApply('EXTCODESIZE_EVM_BinStackOp'),
    'EXTCODECOPY': KApply('EXTCODECOPY_EVM_BinStackOp'),
    'RETURNDATASIZE': KApply('RETURNDATASIZE_EVM_BinStackOp'),
    'RETURNDATACOPY': KApply('RETURNDATACOPY_EVM_BinStackOp'),
    'EXTCODEHASH': KApply('EXTCODEHASH_EVM_BinStackOp'),
    'BLOCKHASH': KApply('BLOCKHASH_EVM_BinStackOp'),
    'COINBASE': KApply('COINBASE_EVM_BinStackOp'),
    'TIMESTAMP': KApply('TIMESTAMP_EVM_BinStackOp'),
    'NUMBER': KApply('NUMBER_EVM_BinStackOp'),
    'PREVRANDAO': KApply('PREVRANDAO_EVM_BinStackOp'),
    'DIFFICULTY': KApply('DIFFICULTY_EVM_BinStackOp'),
    'GASLIMIT': KApply('GASLIMIT_EVM_BinStackOp'),
    'CHAINID': KApply('CHAINID_EVM_BinStackOp'),
    'SELFBALANCE': KApply('SELFBALANCE_EVM_BinStackOp'),
    'BASEFEE': KApply('BASEFEE_EVM_BinStackOp'),
    'POP': KApply('POP_EVM_BinStackOp'),
    'MLOAD': KApply('MLOAD_EVM_BinStackOp'),
    'MSTORE': KApply('MSTORE_EVM_BinStackOp'),
    'MSTORE8': KApply('MSTORE8_EVM_BinStackOp'),
    'SLOAD': KApply('SLOAD_EVM_BinStackOp'),
    'SSTORE': KApply('SSTORE_EVM_BinStackOp'),
    'JUMP': KApply('JUMP_EVM_BinStackOp'),
    'JUMPI': KApply('JUMPI_EVM_BinStackOp'),
    'PC': KApply('PC_EVM_BinStackOp'),
    'MSIZE': KApply('MSIZE_EVM_BinStackOp'),
    'GAS': KApply('GAS_EVM_BinStackOp'),
    'JUMPDEST': KApply('JUMPDEST_EVM_BinStackOp'),
    'TLOAD': KApply('TLOAD_EVM_BinStackOp'),
    'TSTORE': KApply('TSTORE_EVM_BinStackOp'),
    'MCOPY': KApply('MCOPY_EVM_BinStackOp'),
    'PUSHZERO': KApply('PUSHZERO_EVM_BinStackOp'),
    'PUSH': KApply('PUSH_EVM_BinStackOp'),
    'DUP': KApply('DUP_EVM_BinStackOp'),
    'SWAP': KApply('SWAP_EVM_BinStackOp'),
    'LOG': KApply('LOG_EVM_BinStackOp'),
    'CREATE': KApply('CREATE_EVM_BinStackOp'),
    'CALL': KApply('CALL_EVM_BinStackOp'),
    'CALLCODE': KApply('CALLCODE_EVM_BinStackOp'),
    'RETURN': KApply('RETURN_EVM_BinStackOp'),
    'DELEGATECALL': KApply('DELEGATECALL_EVM_BinStackOp'),
    'CREATE2': KApply('CREATE2_EVM_BinStackOp'),
    'STATICCALL': KApply('STATICCALL_EVM_BinStackOp'),
    'REVERT': KApply('REVERT_EVM_BinStackOp'),
    'INVALID': KApply('INVALID_EVM_BinStackOp'),
    'SELFDESTRUCT': KApply('SELFDESTRUCT_EVM_BinStackOp'),
    'UNDEFINED': KApply('UNDEFINED_EVM_BinStackOp'),
}

OPCODES_SUMMARY_STATUS = {
    'STOP': 'TODICUSS, all the leaves are terminal or stuck, find NDBranch',
}

def get_summary_status(opcode: str) -> str:
    return OPCODES_SUMMARY_STATUS[opcode].split(',')[0]

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
        opcode_symbol: str,
    ) -> APRProof:
        """
        Build the specification to symbolically execute one abitrary instruction.
        """
        cterm = CTerm(self.kevm.definition.empty_config(KSort('GeneratedTopCell')))

        # construct the initial substitution
        # opcode = KVariable('OP_CODE', KSort('OpCode'))
        # opcode = KVariable('OP_CODE', KSort('BinStackOp'))
        opcode = OPCODES[opcode_symbol]
        next_opcode = KApply('#next[_]_EVM_InternalOp_MaybeOpCode', opcode)
        _init_subst: dict[str, KInner] = {'K_CELL': KSequence([next_opcode, KVariable('K_CELL')])}
        init_subst = CSubst(Subst(_init_subst), ())

        # construct the final substitution
        _final_subst: dict[str, KInner] = {vname: KVariable('FINAL_' + vname) for vname in cterm.free_vars}
        _final_subst['K_CELL'] = KVariable('K_CELL')
        final_subst = CSubst(Subst(_final_subst), ())

        kclaim, _ = cterm_build_claim(f'{opcode_symbol}_SPEC', init_subst(cterm), final_subst(cterm))
        return APRProof.from_claim(self.kevm.definition, kclaim, {}, self.proof_dir)

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
    
    def analyze_proof(self, proof_id: str) -> None:
        proof = APRProof.read_proof_data(self.proof_dir, proof_id)
        for successor in proof.kcfg.successors(11):
            print('Type: ', type(successor))
            print('Source: ', successor.source.id)
            print('Target: ', [target.id for target in successor.targets])
