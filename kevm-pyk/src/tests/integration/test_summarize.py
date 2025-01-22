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
            # KRequire('edsl.md'),
            # module = KFlatModule(f'{opcode}-SUMMARY', claims)
            # with open(summarizer.save_directory / proof.id / f'{opcode.lower()}-summary.k', 'w') as f:
            #     res_lines = 'requires "edsl.md"\n'
            #     res_lines += summarizer.kevm.pretty_print(module)
            #     splited_lines = res_lines.split('\n')
            #     splited_lines.insert(2, '    imports public EDSL')
            #     res_lines = '\n'.join(splited_lines)
            #     f.write(res_lines)
                
            # int = 0
            # print(len(claims))
            # proof_result = summarizer.explore(APRProof.from_claim(summarizer.kevm.definition, claims[2], {}, summarizer.proof_dir))
            # print(proof_result)
            for claim in claims:
                assert summarizer.explore(APRProof.from_claim(summarizer.kevm.definition, claim, {}, summarizer.proof_dir))
            #     # TODO: fix the sort issue caused by `APRProof.from_claim`
            #     # print(f'validating {claim.att[Atts.LABEL]}')
            #     # _subst = {'_USEGAS_CELL': KVariable('_USEGAS_CELL', sort = 'Bool')}
            #     # subst = CSubst(Subst(_subst), ())
            #     summary_proof = APRProof.from_claim(summarizer.kevm.definition, claim, {}, summarizer.proof_dir)
            #     # summary_proof.kcfg.let_node(1, cterm = subst(summary_proof.kcfg.get_node(1).cterm), attrs = summary_proof.kcfg.get_node(1).attrs)
            #     proof_result = summarizer.explore(summary_proof)
            #     # print(f'{claim.att[Atts.LABEL]} proof result: {proof_result}')
            #     assert proof_result
    else:
        pytest.skip(f'{opcode} ignored')
