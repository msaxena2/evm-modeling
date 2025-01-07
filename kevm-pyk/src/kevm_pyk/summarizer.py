from curses.ascii import DEL
from pathlib import Path
import sys
import time
from kevm_pyk.__main__ import wrap_process_pool
from kevm_pyk.kevm import KEVM, KEVMSemantics
from kevm_pyk.utils import legacy_explore, initialize_apr_proof, run_prover, print_failure_info
from pyk.cterm import CTerm, CTermSymbolic, cterm_build_claim
from pyk.proof import APRProof
from pyk.kast.outer import KSort
from pyk.kdist import kdist
from pyk.kast.inner import KInner, bottom_up, KVariable, KSequence, KApply
from pyk.kcfg import KCFGExplore
from pyk.kore.rpc import KoreClient

DEFINITION_DIR = Path('/home/zhaoji/.cache/kdist-4056746/evm-semantics/haskell')
# kdist.get('evm-semantics.haskell')

class KEVMSummarizer:
    """
    A class for summarizing the instructions of the KEVM.
    
    TODO:
    1. Build the proof to symbolically execute one abitrary instruction.
    2. Run the proof to get the KCFG.
    3. Summarize the KCFG to get the summarized rules for the instructions.
    rdots(pyk.KRewrite(pyk.KApply('#next[_]_EVM_InternalOp_OpCode', [opcode]), pyk.KConstant('#EmptyK')))
    """
    _cterm_symbolic: CTermSymbolic
    kevm: KEVM
    proof_dir: Path
    save_directory: Path
    
    def __init__(self, proof_dir: Path, save_directory: Path) -> None:
        self.kevm = KEVM(DEFINITION_DIR)
        self.proof_dir = proof_dir
        self.save_directory = save_directory
    
    def build_spec(self, ) -> APRProof:
        """
        Build the specification to symbolically execute one abitrary instruction.
        """
        cterm = CTerm(self.kevm.definition.empty_config(KSort('GeneratedTopCell')))
        
        def _to_init(kast: KInner) -> KInner:
            if type(kast) is KVariable and kast.name == 'K_CELL':
                return KSequence([KApply('#next[_]_EVM_InternalOp_OpCode', KVariable('OP_CODE', KSort('OpCode'))), KVariable('K_CELL')])
            return kast
        
        def _to_final(kast: KInner) -> KInner:
            if type(kast) is KVariable and kast.name != 'K_CELL':
                return KVariable('FINAL_' + kast.name)
            return kast
        
        init_cterm = CTerm(bottom_up(_to_init, cterm.config), cterm.constraints)
        final_cterm = CTerm(bottom_up(_to_final, cterm.config), cterm.constraints)
        kclaim, _  = cterm_build_claim('individual_instruction', init_cterm, final_cterm)
        return APRProof.from_claim(self.kevm.definition, kclaim, {}, self.proof_dir)
    
    def explore(self, proof: APRProof) -> None:
        """
        Execute the specification to explore the KCFG for all possible instructions.
        """
        
        # Construct the KCFGExplore
        # Copy from kevm-pyk/src/kevm_pyk/__main__.py/exec_prove
        # TODO: Make this process as an independent function to reuse； best to be in pyk.

        def _init_and_run_proof(proof: APRProof) -> tuple[bool, list[str] | None]:
            with legacy_explore(
                self.kevm,
                kcfg_semantics=KEVMSemantics(),
                id=proof.id,
                llvm_definition_dir=DEFINITION_DIR / 'llvm-library',
                bug_report=None,
                kore_rpc_command=('kore-rpc-booster',),
                smt_timeout=None,
                smt_retry_limit=None,
                log_succ_rewrites=True,
                log_fail_rewrites=True,
                fallback_on=None,
                interim_simplification=True,
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
                        kcfg_semantics=KEVMSemantics(),
                        id=proof.id,
                    )
                    
                initialize_apr_proof(kcfg_explore.cterm_symbolic, proof)
                proof.write_proof_data()
                
                if proof.admitted:
                    print(f'Skipping execution of proof because it is marked as admitted: {proof.id}')
                    return True, None

                start_time = time.time()
                passed = run_prover(
                    proof,
                    create_kcfg_explore=create_kcfg_explore,
                    max_depth=1000,
                    max_iterations=None,  # Small number to avoid infinite loop and cut rules more often.
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
                    optimize_kcfg=True,
                )
            end_time = time.time()
            print(f'Proof timing {proof.id}: {end_time - start_time}s')
            failure_log = None
            if not passed:
                failure_log = print_failure_info(proof, kcfg_explore)

            return passed, failure_log

        result: list[tuple[bool, list[str] | None]] = [_init_and_run_proof(proof)]

        failed = 0
        for job, r in zip([proof], result, strict=True):
            passed, failure_log = r
            if passed:
                print(f'PROOF PASSED: {job.id}')
            else:
                failed += 1
                print(f'PROOF FAILED: {job.id}')
                if failure_log is not None:
                    for line in failure_log:
                        print(line)

        if failed:
            sys.exit(failed)
    
    def summarize(self, ):
        pass


if __name__ == '__main__':
    proof_dir = Path(__file__).parent / 'proofs'
    save_directory = Path(__file__).parent / 'summaries'
    summarizer = KEVMSummarizer(proof_dir, save_directory)
    proof = summarizer.build_spec()
    summarizer.explore(proof)
