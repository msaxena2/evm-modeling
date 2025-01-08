from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING

from pyk.cterm import CSubst, CTerm, CTermSymbolic, cterm_build_claim
from pyk.kast.inner import KApply, KInner, KSequence, KVariable, Subst
from pyk.kast.outer import KSort
from pyk.kcfg import KCFGExplore
from pyk.kdist import kdist
from pyk.kore.rpc import KoreClient
from pyk.proof import APRProof
from pyk.proof.show import APRProofShow

from kevm_pyk.kevm import KEVM, KEVMSemantics, kevm_node_printer
from kevm_pyk.utils import initialize_apr_proof, legacy_explore, run_prover

if TYPE_CHECKING:
    from pathlib import Path

_LOGGER = logging.getLogger(__name__)


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
    ) -> APRProof:
        """
        Build the specification to symbolically execute one abitrary instruction.
        """
        cterm = CTerm(self.kevm.definition.empty_config(KSort('GeneratedTopCell')))

        # construct the initial substitution
        # opcode = KVariable('OP_CODE', KSort('OpCode'))
        opcode = KVariable('OP_CODE', KSort('BinStackOp'))
        next_opcode = KApply('#next[_]_EVM_InternalOp_MaybeOpCode', opcode)
        _init_subst: dict[str, KInner] = {'K_CELL': KSequence([next_opcode, KVariable('K_CELL')])}
        _init_subst['PROGRAM_CELL'] = self.kevm.bytes_empty()
        init_subst = CSubst(Subst(_init_subst), ())
        # TODO: following provides some special cases that cannot be handled automatically
        # Error Message:
        # Runtime error | code: -32002 | data: {'context': 'CallStack (from HasCallStack):\n  error, called at src/Kore/Rewrite/Function/Evaluator.hs:377:6 in kore-0.1.104-CWw3vBaRpxI3Spyxy9LUQ8:Kore.Rewrite.Function.Evaluator', 'error': 'Error: missing hook\nSymbol\n    LblisValidPoint\'LParUndsRParUnds\'KRYPTO\'Unds\'Bool\'Unds\'G1Point{}\ndeclared with attribute\n    hook{}("KRYPTO.bn128valid")\nWe don\'t recognize that hook and it was not given any rules.\nPlease open a feature request at\n    https://github.com/runtimeverification/haskell-backend/issues\nand include the text of this message.\nWorkaround: Give rules for LblisValidPoint\'LParUndsRParUnds\'KRYPTO\'Unds\'Bool\'Unds\'G1Point{}'}
        # Analysis: need hook in Haskell backend for KRYPTO.bn128valid
        # Temp Solution: skip the PrecompiledOp for now

        # construct the final substitution
        _final_subst: dict[str, KInner] = {vname: KVariable('FINAL_' + vname) for vname in cterm.free_vars}
        _final_subst['K_CELL'] = KVariable('K_CELL')
        _final_subst['PROGRAM_CELL'] = self.kevm.bytes_empty()
        final_subst = CSubst(Subst(_final_subst), ())

        kclaim, _ = cterm_build_claim('instruction_spec', init_subst(cterm), final_subst(cterm))
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
                kcfg_semantics=KEVMSemantics(),
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
                        kcfg_semantics=KEVMSemantics(),
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

        _, res_lines = _init_and_run_proof(proof)
        for line in res_lines:
            print(line)

    def summarize(self, proof: APRProof) -> None:
        proof.minimize_kcfg(KEVMSemantics(), False)
        node_printer = kevm_node_printer(self.kevm, proof)
        proof_show = APRProofShow(self.kevm, node_printer=node_printer)
        for res_line in proof_show.show(proof, to_module=True):
            print(res_line)
