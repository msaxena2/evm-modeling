import pytest
from pyk.kast.outer import KRuleLike
from pyk.kcfg import KCFG

from kevm_pyk.summarizer import OPCODES, OPCODES_SUMMARY_STATUS, get_summary_status, summarize


@pytest.mark.parametrize('opcode', OPCODES.keys())
def test_summarize(opcode: str) -> None:
    if get_summary_status(opcode) != 'PASSED':
        pytest.skip(f'{opcode} status: {OPCODES_SUMMARY_STATUS[opcode]}')
    if opcode == 'ADD':
        print(f'[{opcode}] selected')
        summarizer, proofs = summarize(opcode)
        print(f'[{opcode}] summarize finished')
        print(f'[{opcode}] {len(proofs)} proofs generated')

        #
        # proof_dir = Path(__file__).parent / 'proofs'
        # save_directory = Path(__file__).parent / 'summaries'
        # proofs = [APRProof.read_proof_data(Path(__file__).parent.parent.parent / 'kevm_pyk' / 'proofs', 'ADD_2_SPEC')]
        # print(f'{len(proofs)} proofs')

        for proof in proofs:
            claims: list[KRuleLike] = []

            # no pending, failing, bounded nodes in the proof
            for leaf in proof.kcfg.leaves:
                assert not proof.is_pending(leaf.id)
                assert not proof.kcfg.is_stuck(leaf.id)
                assert not proof.kcfg.is_vacuous(leaf.id)
                assert not proof.is_bounded(leaf.id)
                print(f'[{opcode}] Node {leaf.id} is not pending, stuck, vacuous, or bounded')

            # only one successor from the initial node in the proof
            successors = proof.kcfg.successors(proof.init)
            assert len(successors) == 1
            successor = successors[0]
            print(f'[{opcode}] Node {proof.init} has only one successor')

            # only one edge to the terminal node
            if isinstance(successor, KCFG.Split):
                targets = successor.targets
                assert len(proof.kcfg.edges()) == len(targets)
                print(f'[{opcode}] Split has {len(targets)} targets')
                for target in targets:
                    successors = proof.kcfg.successors(target.id)
                    assert len(successors) == 1
                    edge = successors[0]
                    assert isinstance(edge, KCFG.Edge)
                    assert proof.is_terminal(edge.target.id) or proof.kcfg.is_covered(edge.target.id)
                    claims.append(edge.to_rule(f'{opcode}-SUMMARY', claim=True))
                    print(f'[{opcode}] Edge {edge.source.id} -> {edge.target.id} is terminal or covered')
            else:
                assert len(proof.kcfg.edges()) == 1
                assert isinstance(successor, KCFG.Edge)
                assert proof.is_terminal(successor.target.id) or proof.kcfg.is_covered(successor.target.id)
                claims.append(successor.to_rule(f'{opcode}-SUMMARY', claim=True))
                print(f'[{opcode}] Edge {successor.source.id} -> {successor.target.id} is terminal or covered')

            # # prove the correctness of the summary
            # for claim in claims:
            #     print(f'[{opcode}] Proving claim {claim.att.get(Atts.LABEL)}')
            #     assert summarizer.explore(
            #         APRProof.from_claim(summarizer.kevm.definition, claim, {}, summarizer.proof_dir)
            #     )
            #     print(f'[{opcode}] Claim {claim.att.get(Atts.LABEL)} proved')
    else:
        pytest.skip(f'{opcode} ignored')
