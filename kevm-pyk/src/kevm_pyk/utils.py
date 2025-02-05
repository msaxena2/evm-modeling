from __future__ import annotations

import logging
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING

from pyk.cterm import CTermSymbolic
from pyk.kast import Atts
from pyk.kast.inner import KApply, KInner, KRewrite, KVariable, Subst
from pyk.kast.manip import (
    abstract_term_safely,
    bottom_up,
    free_vars,
    is_anon_var,
    split_config_and_constraints,
    split_config_from,
)
from pyk.kcfg import KCFGExplore
from pyk.kore.rpc import KoreClient, KoreExecLogFormat, TransportType, kore_server
from pyk.ktool import TypeInferenceMode
from pyk.ktool.claim_loader import ClaimLoader
from pyk.prelude.ml import is_bottom, is_top
from pyk.proof import APRProof, APRProver
from pyk.proof.implies import EqualityProof, ImpliesProver
from pyk.proof.proof import parallel_advance_proof
from pyk.utils import single

if TYPE_CHECKING:
    from collections.abc import Callable, Collection, Iterable, Iterator
    from typing import Final, TypeVar

    from pyk.kast.outer import KClaim, KDefinition, KFlatModule
    from pyk.kcfg import KCFG
    from pyk.kcfg.semantics import KCFGSemantics
    from pyk.kore.rpc import FallbackReason
    from pyk.ktool.kprint import KPrint
    from pyk.ktool.kprove import KProve
    from pyk.proof.proof import Proof
    from pyk.utils import BugReport
    from rich.progress import Progress, TaskID

    T1 = TypeVar('T1')
    T2 = TypeVar('T2')

_LOGGER: Final = logging.getLogger(__name__)


def claim_dependency_dict(claims: Iterable[KClaim], spec_module_name: str | None = None) -> dict[str, list[str]]:
    claims_by_label = {claim.label: claim for claim in claims}
    graph: dict[str, list[str]] = {}
    for claim in claims:
        graph[claim.label] = []  # noqa: B909
        for dependency in claim.dependencies:
            if dependency not in claims_by_label:
                if spec_module_name is None:
                    raise ValueError(f'Could not find dependency and no spec_module provided: {dependency}')
                else:
                    spec_dependency = f'{spec_module_name}.{dependency}'
                    if spec_dependency not in claims_by_label:
                        raise ValueError(f'Could not find dependency: {dependency} or {spec_dependency}')
                    dependency = spec_dependency
            graph[claim.label].append(dependency)
    return graph


def get_apr_proof_for_spec(
    kprove: KProve,
    spec_file: Path,
    save_directory: Path | None,
    spec_module_name: str | None = None,
    include_dirs: Iterable[Path] = (),
    md_selector: str | None = None,
    claim_labels: Iterable[str] | None = None,
    exclude_claim_labels: Iterable[str] | None = None,
    include_dependencies: bool = True,
) -> APRProof:
    if save_directory is None:
        save_directory = Path('.')
        _LOGGER.info(f'Using default save_directory: {save_directory}')

    _LOGGER.info(f'Extracting claim from file: {spec_file}')
    claim = single(
        ClaimLoader(kprove).load_claims(
            spec_file,
            spec_module_name=spec_module_name,
            include_dirs=include_dirs,
            md_selector=md_selector,
            claim_labels=claim_labels,
            exclude_claim_labels=exclude_claim_labels,
            type_inference_mode=TypeInferenceMode.SIMPLESUB,
            include_dependencies=include_dependencies,
        )
    )

    apr_proof = APRProof.read_proof_data(save_directory, claim.label)
    return apr_proof


def run_prover(
    proof: Proof,
    create_kcfg_explore: Callable[[], KCFGExplore],
    max_depth: int = 1000,
    max_iterations: int | None = None,
    cut_point_rules: Iterable[str] = (),
    terminal_rules: Iterable[str] = (),
    fail_fast: bool = False,
    counterexample_info: bool = False,
    fast_check_subsumption: bool = False,
    direct_subproof_rules: bool = False,
    max_frontier_parallel: int = 1,
    force_sequential: bool = False,
    progress: Progress | None = None,
    task_id: TaskID | None = None,
    maintenance_rate: int = 1,
    assume_defined: bool = False,
    extra_module: KFlatModule | None = None,
    optimize_kcfg: bool = False,
) -> bool:
    prover: APRProver | ImpliesProver
    try:
        if type(proof) is APRProof:

            def create_prover() -> APRProver:
                return APRProver(
                    create_kcfg_explore(),
                    execute_depth=max_depth,
                    terminal_rules=terminal_rules,
                    cut_point_rules=cut_point_rules,
                    counterexample_info=counterexample_info,
                    fast_check_subsumption=fast_check_subsumption,
                    direct_subproof_rules=direct_subproof_rules,
                    assume_defined=assume_defined,
                    extra_module=extra_module,
                    optimize_kcfg=optimize_kcfg,
                )

            def update_status_bar(_proof: Proof) -> None:
                if progress is not None and task_id is not None:
                    progress.update(task_id, summary=_proof.one_line_summary)

            if force_sequential:
                prover = create_prover()
                prover.advance_proof(
                    proof=proof,
                    max_iterations=max_iterations,
                    fail_fast=fail_fast,
                    callback=update_status_bar,
                    maintenance_rate=maintenance_rate,
                )
            else:
                parallel_advance_proof(
                    proof=proof,
                    create_prover=create_prover,
                    max_iterations=max_iterations,
                    fail_fast=fail_fast,
                    max_workers=max_frontier_parallel,
                    callback=update_status_bar,
                    maintenance_rate=maintenance_rate,
                )

        elif type(proof) is EqualityProof:
            prover = ImpliesProver(proof, kcfg_explore=create_kcfg_explore(), assume_defined=assume_defined)
            prover.advance_proof(proof)
        else:
            raise ValueError(f'Do not know how to build prover for proof: {proof}')

    except Exception as e:
        if type(proof) is APRProof:
            proof.error_info = e
        _LOGGER.error(f'Proof crashed: {proof.id}\n{e}', exc_info=True)
        return False

    _LOGGER.info(f'Proof status {proof.id}: {proof.status}')
    return proof.passed


def print_failure_info(proof: Proof, kcfg_explore: KCFGExplore, counterexample_info: bool = False) -> list[str]:
    if type(proof) is APRProof:
        target = proof.kcfg.node(proof.target)

        res_lines: list[str] = []

        num_pending = len(proof.pending)
        num_failing = len(proof.failing)
        res_lines.append(
            f'{num_pending + num_failing} Failure nodes. ({num_pending} pending and {num_failing} failing)'
        )
        if num_pending > 0:
            res_lines.append('')
            res_lines.append('Pending nodes:')
            for node in proof.pending:
                res_lines.append('')
                res_lines.append(f'ID: {node.id}:')
        if num_failing > 0:
            res_lines.append('')
            res_lines.append('Failing nodes:')
            for node in proof.failing:
                res_lines.append('')
                res_lines.append(f'  Node id: {str(node.id)}')

                node_cterm, _ = kcfg_explore.cterm_symbolic.simplify(node.cterm)
                target_cterm, _ = kcfg_explore.cterm_symbolic.simplify(target.cterm)

                res_lines.append('  Failure reason:')
                _, reason = kcfg_explore.implication_failure_reason(node_cterm, target_cterm)
                res_lines += [f'    {line}' for line in reason.split('\n')]

                res_lines.append('  Path condition:')
                res_lines += [f'    {kcfg_explore.pretty_print(proof.path_constraints(node.id))}']
                if counterexample_info:
                    res_lines.extend(print_model(node, kcfg_explore))

        res_lines.append('')
        res_lines.append(
            'Join the Runtime Verification Discord server (https://discord.com/invite/CurfmXNtbN) or Telegram group (https://t.me/rv_kontrol) for support.'
        )

        return res_lines
    elif type(proof) is EqualityProof:
        return ['EqualityProof failed.']
    else:
        raise ValueError('Unknown proof type.')


def print_model(node: KCFG.Node, kcfg_explore: KCFGExplore) -> list[str]:
    res_lines: list[str] = []
    result_subst = kcfg_explore.cterm_symbolic.get_model(node.cterm)
    if type(result_subst) is Subst:
        res_lines.append('  Model:')
        for var, term in result_subst.to_dict().items():
            term_kast = KInner.from_dict(term)
            res_lines.append(f'    {var} = {kcfg_explore.pretty_print(term_kast)}')
    else:
        res_lines.append('  Failed to generate a model.')

    return res_lines


def arg_pair_of(
    fst_type: Callable[[str], T1], snd_type: Callable[[str], T2], delim: str = ','
) -> Callable[[str], tuple[T1, T2]]:
    def parse(s: str) -> tuple[T1, T2]:
        elems = s.split(delim)
        length = len(elems)
        if length != 2:
            raise ValueError(f'Expected 2 elements, found {length}')
        return fst_type(elems[0]), snd_type(elems[1])

    return parse


def byte_offset_to_lines(lines: Iterable[str], byte_start: int, byte_width: int) -> tuple[list[str], int, int]:
    text_lines = []
    line_start = 0
    for line in lines:
        if len(line) < byte_start:
            byte_start -= len(line) + 1
            line_start += 1
        else:
            break
    line_end = line_start
    for line in list(lines)[line_start:]:
        if byte_start + byte_width < 0:
            break
        else:
            text_lines.append(line)
            byte_width -= len(line) + 1
            line_end += 1
    return (text_lines, line_start, line_end)


def KDefinition__expand_macros(defn: KDefinition, term: KInner) -> KInner:  # noqa: N802
    def _expand_macros(_term: KInner) -> KInner:
        if type(_term) is KApply:
            prod = defn.symbols[_term.label.name]
            if any(key in prod.att for key in [Atts.MACRO, Atts.ALIAS, Atts.MACRO_REC, Atts.ALIAS_REC]):
                for r in defn.macro_rules:
                    assert type(r.body) is KRewrite
                    _new_term = r.body.apply_top(_term)
                    if _new_term != _term:
                        _term = _new_term
                        break
        return _term

    old_term = None
    while term != old_term:
        old_term = term
        term = bottom_up(_expand_macros, term)

    return term


def abstract_cell_vars(cterm: KInner, keep_vars: Collection[KVariable] = ()) -> KInner:
    state, _ = split_config_and_constraints(cterm)
    config, subst = split_config_from(state)
    for s in subst:
        if type(subst[s]) is KVariable and not is_anon_var(subst[s]) and subst[s] not in keep_vars:
            subst[s] = abstract_term_safely(KVariable('_'), base_name=s)  # noqa: B909
    return Subst(subst)(config)


def constraints_for(vars: list[str], constraints: Iterable[KInner]) -> Iterable[KInner]:
    accounts_constraints = []
    constraints_changed = True
    while constraints_changed:
        constraints_changed = False
        for constraint in constraints:
            if constraint not in accounts_constraints and any(v in vars for v in free_vars(constraint)):
                accounts_constraints.append(constraint)
                vars.extend(free_vars(constraint))
                constraints_changed = True
    return accounts_constraints


def initialize_apr_proof(cterm_symbolic: CTermSymbolic, proof: APRProof) -> None:
    init_cterm = proof.kcfg.node(proof.init).cterm
    target_cterm = proof.kcfg.node(proof.target).cterm

    _LOGGER.info(f'Computing definedness constraint for initial node: {proof.id}')
    init_cterm = cterm_symbolic.assume_defined(init_cterm)

    _LOGGER.info(f'Simplifying initial and target node: {proof.id}')
    init_cterm, _ = cterm_symbolic.simplify(init_cterm)
    target_cterm, _ = cterm_symbolic.simplify(target_cterm)

    if is_bottom(init_cterm.kast, weak=True):
        raise ValueError('Simplifying initial node led to #Bottom, are you sure your LHS is defined?')
    if is_top(target_cterm.kast, weak=True):
        raise ValueError('Simplifying target node led to #Bottom, are you sure your RHS is defined?')

    proof.kcfg.let_node(proof.init, cterm=init_cterm)
    proof.kcfg.let_node(proof.target, cterm=target_cterm)


@contextmanager
def legacy_explore(
    kprint: KPrint,
    *,
    kcfg_semantics: KCFGSemantics | None = None,
    id: str | None = None,
    port: int | None = None,
    kore_rpc_command: str | Iterable[str] | None = None,
    llvm_definition_dir: Path | None = None,
    smt_timeout: int | None = None,
    smt_retry_limit: int | None = None,
    smt_tactic: str | None = None,
    bug_report: BugReport | None = None,
    haskell_log_format: KoreExecLogFormat = KoreExecLogFormat.ONELINE,
    haskell_log_entries: Iterable[str] = (),
    haskell_threads: int | None = None,
    log_axioms_file: Path | None = None,
    log_succ_rewrites: bool = True,
    log_fail_rewrites: bool = True,
    start_server: bool = True,
    maude_port: int | None = None,
    fallback_on: Iterable[FallbackReason] | None = None,
    interim_simplification: int | None = None,
    no_post_exec_simplify: bool = True,
) -> Iterator[KCFGExplore]:
    bug_report_id = None if bug_report is None else id
    if start_server:
        # Old way of handling KCFGExplore, to be removed
        with kore_server(
            definition_dir=kprint.definition_dir,
            llvm_definition_dir=llvm_definition_dir,
            module_name=kprint.main_module,
            port=port,
            command=kore_rpc_command,
            bug_report=bug_report,
            smt_timeout=smt_timeout,
            smt_retry_limit=smt_retry_limit,
            smt_tactic=smt_tactic,
            haskell_log_format=haskell_log_format,
            haskell_log_entries=haskell_log_entries,
            haskell_threads=haskell_threads,
            log_axioms_file=log_axioms_file,
            fallback_on=fallback_on,
            interim_simplification=interim_simplification,
            no_post_exec_simplify=no_post_exec_simplify,
        ) as server:
            with KoreClient('localhost', server.port, bug_report=bug_report, bug_report_id=bug_report_id) as client:
                cterm_symbolic = CTermSymbolic(
                    client, kprint.definition, log_succ_rewrites=log_succ_rewrites, log_fail_rewrites=log_fail_rewrites
                )
                yield KCFGExplore(cterm_symbolic, kcfg_semantics=kcfg_semantics, id=id)
    else:
        if port is None:
            raise ValueError('Missing port with start_server=False')
        if maude_port is None:
            dispatch = None
        else:
            dispatch = {
                'execute': [('localhost', maude_port, TransportType.HTTP)],
                'simplify': [('localhost', maude_port, TransportType.HTTP)],
                'add-module': [
                    ('localhost', maude_port, TransportType.HTTP),
                    ('localhost', port, TransportType.SINGLE_SOCKET),
                ],
            }
        with KoreClient(
            'localhost', port, bug_report=bug_report, bug_report_id=bug_report_id, dispatch=dispatch
        ) as client:
            cterm_symbolic = CTermSymbolic(
                client, kprint.definition, log_succ_rewrites=log_succ_rewrites, log_fail_rewrites=log_fail_rewrites
            )
            yield KCFGExplore(cterm_symbolic, kcfg_semantics=kcfg_semantics, id=id)
