from ast import Import
from kevm_pyk.summarizer import OPCODES, get_summary_status, OPCODES_SUMMARY_STATUS, summarize
import pytest
from pyk.kcfg import KCFG
from pyk.kast.inner import KVariable, Subst
from pyk.kast.outer import KFlatModule, KRequire, KImport
from pyk.kast.att import Atts
from pyk.cterm import CSubst
from pyk.proof.reachability import APRProof

@pytest.mark.parametrize('opcode', OPCODES.keys())
def test_summarize(opcode: str) -> None:
    if get_summary_status(opcode) != 'PASSED':
        pytest.skip(f'{opcode} status: {OPCODES_SUMMARY_STATUS[opcode]}')
    if opcode == 'STOP':
        summarizer, proofs = summarize(opcode)
        for proof in proofs:
            claims = []
            
            # no pending, failing, bounded nodes in the proof
            for leaf in proof.kcfg.leaves:
                assert not proof.is_pending(leaf.id)
                assert not proof.kcfg.is_stuck(leaf.id)
                assert not proof.kcfg.is_vacuous(leaf.id)
                assert not proof.is_bounded(leaf.id)
            
            # only one successor from the initial node in the proof
            successors = proof.kcfg.successors(proof.init)
            assert len(successors) == 1
            successor = successors[0]
            
            # only one edge to the terminal node
            if isinstance(successor, KCFG.Split):
                targets = successor.targets
                assert len(proof.kcfg.edges()) == len(targets)
                for target in targets:
                    successors = proof.kcfg.successors(target.id)
                    assert len(successors) == 1
                    edge = successors[0]
                    assert isinstance(edge, KCFG.Edge)
                    assert proof.is_terminal(edge.target.id)
                    claims.append(edge.to_rule(f'{opcode}-SUMMARY', claim = True))
            else:
                assert len(proof.kcfg.edges()) == 1
                assert isinstance(successor, KCFG.Edge)
                assert proof.is_terminal(successor.target.id)
                claims.append(successor.to_rule(f'{opcode}-SUMMARY', claim = True))
                
            # prove the correctness of the summary
            for claim in claims:
                assert summarizer.explore(APRProof.from_claim(summarizer.kevm.definition, claim, {}, summarizer.proof_dir))
    else:
        pytest.skip(f'{opcode} ignored')
