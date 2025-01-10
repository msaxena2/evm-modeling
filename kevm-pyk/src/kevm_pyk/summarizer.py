from __future__ import annotations

import logging
import time
import traceback
from multiprocessing import Pool
from pathlib import Path
from typing import TYPE_CHECKING

from pyk.cterm import CSubst, CTerm, CTermSymbolic, cterm_build_claim
from pyk.kast.inner import KApply, KInner, KSequence, KVariable, Subst
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
    'ADDMOD': KApply('ADDMOD_EVM_TernStackOp'),
    'MULMOD': KApply('ADDMOD_EVM_TernStackOp'),
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
    'STOP': 'TOSUMMARIZE, One rule? Several rules?',
    'ADD': 'TODICUSS, smt out of time, find NDBranch, inconsistent stack overflow check between the optimized rule and the original rule',
    'MUL': '',
    'ALL': 'TODICUSS, failed to summarize, the optimized rule applies one step to obtain the target, the failure process rules are applied to obtain the failure, we need to summarize these ndbranches and exclude these conditions from individual opcode spec',
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

    _LOGGER.info(f'Starting batch summarization of {len(opcodes_to_process)} opcodes with {num_processes} processes')

    with Pool(processes=num_processes) as pool:
        pool.map(_process_opcode, opcodes_to_process)

    _LOGGER.info('Batch summarization completed')


def summarize(opcode: str) -> None:
    proof_dir = Path(__file__).parent / 'proofs'
    save_directory = Path(__file__).parent / 'summaries'
    summarizer = KEVMSummarizer(proof_dir, save_directory)
    proof = summarizer.build_spec(opcode)
    summarizer.explore(proof)
    summarizer.summarize(proof)
    # summarizer.analyze_proof(proof_dir / 'STOP_SPEC')
    

def analyze_proof(opcode: str, node_id: int) -> None:
    proof_dir = Path(__file__).parent / 'proofs'
    save_directory = Path(__file__).parent / 'summaries'
    summarizer = KEVMSummarizer(proof_dir, save_directory)
    summarizer.analyze_proof(proof_dir / f'{opcode}_SPEC', node_id)
