# H2 Daily Horizon Orient — 2026-11-28 / termination evidence propagation

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-28
Logical Timezone: Asia/Shanghai
Agent: GPT-6.2 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: a4152339b1f62d033585fbea6e7f85178c8f8667
Run Identity: welcome-to-github/horizon/H2/2026-11-28/GPT_NATIVE/a4152339b1f6/termination-propagation-01
Source Identity: google/adk-python PR #8416 / ab8a94dcdff7eb316c34d8042aff2f51528fbe85; linked issue #8378
Source Authority For Claim: PRIMARY_PROPOSED_SOURCE_PATCH / AUTHOR_REPORTED_REPRO
Independent Verification: MERGED_H1_READBACK / PATCH_AND_LINKED_ISSUE_RECHECK / STANDALONE_CONTROL_EXECUTED / SDK_NOT_EXECUTED
Host Applicability: UNKNOWN
Evidence Upgrade Basis: BOUNDED_SIGNATURE_AND_PREDICATE_CONTROL / NO_UPSTREAM_ACCEPTANCE_PROMOTION
Original Execution Status: SOURCE_REVIEW_AND_STANDALONE_CONTROL_EXECUTED / FULL_CHECKER_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_SOURCE_ORIENTATION / NO_HOST_DECISION
Write Scope: horizon-cortex/2026-11-28-H2-horizon-orient.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Original same-day horizon-cortex/2026-11-28-H1-signal-observe.md merged via #1074; merge a4152339b1f62d033585fbea6e7f85178c8f8667; exact H1 blob a69813a287c1bfc564ec6ff76ff85d1b758b5783 reread from fresh main. Original H1 authoring state preserved.
- Policy blob 060eaff65437bda48718a9703477815c574a9846; checker 5736c90f56a59728db380180557256a151b1ea83; prior H2 blob d76c582f2f73364b730145adf5aab82543ccbd56. W48 and November closure NOT_DUE.
- Upstream https://github.com/google/adk-python/pull/8416 remains OPEN / UNMERGED, unchanged head; created 2026-11-27T19:09:47Z. https://github.com/google/adk-python/issues/8378 (created 2026-11-26T16:31:57Z) is the linked report with author-supplied offline reproduction; issue remains open. One linked evidence lineage, not independently reproduced SDK behavior.

## SIGNAL_CLASSIFICATION
- New source-surface review: local_eval_service.py explicitly forwards termination_reason only when inspect.signature exposes that named parameter; generic **kwargs acceptance alone does not pass that predicate. The proposed per-turn metric skips the synthetic stop turn only for TURN_LIMIT, not all reasons other than STOP_SIGNAL.
- Issue #8378 reports identical SUCCESS status for a capped and a finished run, and judging a synthetic finished turn in the capped case. Reported observations, not independent reproduction. The patch carries a reason separately from inference status; the optional completion metric is not part of this change.
- Reason attribution is a candidate evaluation evidence coordinate, not a task completion oracle, a released ADK feature, or NEXUS adoption.

## ORIENTATION_NOTES
- Standalone H2-20261128-TERMINATION-PROPAGATION-01; actual UTC command group 2026-11-28T02:14:50Z–02:14:52Z; Linux, Python 3.13.5; command python h2.py in isolated scratch; exit 0, stderr empty; script SHA256 20ddf635bbb97d389a94cfb27e1dfb47a35aaa88ff9386d6979277b9fc7b8482.
- Exact UTF-8 LF script:
```python
import inspect

def explicit(*, termination_reason=None):
    return termination_reason

def generic(**kwargs):
    return kwargs.get('termination_reason')

def forward(evaluator, reason):
    params = inspect.signature(evaluator).parameters
    return evaluator(**({'termination_reason': reason} if 'termination_reason' in params else {}))

for reason in ('stop_signal', 'turn_limit', 'no_message', None):
    print(repr(reason), 'synthetic_stop=', reason != 'turn_limit')
assert [r != 'turn_limit' for r in ('stop_signal', 'turn_limit', 'no_message', None)] == [True, False, True, True]
print('explicit:', forward(explicit, 'turn_limit'), 'generic:', forward(generic, 'turn_limit'))
assert forward(explicit, 'turn_limit') == 'turn_limit'
assert forward(generic, 'turn_limit') is None
```
- Actual stdout:
```text
'stop_signal' synthetic_stop= True
'turn_limit' synthetic_stop= False
'no_message' synthetic_stop= True
None synthetic_stop= True
explicit: turn_limit generic: None
```
- This is a stdlib control mirroring two selected predicates, not ADK execution or a defect finding for every evaluator. A generic evaluator might intentionally ignore reason; None can represent static, missing, or other unrecorded conditions. A synthetic stop assessment need not assert an actual observed stop, but a consumer must distinguish counterfactual judgment from an observed event. Explicit named parameter receipt is not proof of correct downstream use.
- Counterevidence: a user stop can precede intended effect; a cap can follow a valid effect. Even correctly propagated reason and successful inference do not establish authorization, external effect, or task postcondition.

## NO_DECISION_SECTION
NO_DECISION / NO_HOST_PROMOTION. No independent external source added; linked issue and patch are related. One independent bounded local control, no SDK reproduction or deployment.

## EVIDENCE_DELTA
- NEW_EVIDENCE: linked issue review, exact metric/forwarding hunks, actual signature and predicate control.
- CORRECTED_INTERPRETATION: recorded reason != propagated reason != observed simulator stop != task completion.
- UNCHANGED_BOUNDARY: SOURCE_PATCH != RELEASE != HOST_ADOPTED.
- NEW_COUNTEREVIDENCE: generic kwargs consumer receives no reason under the named-parameter rule; no_message and None still enter the proposed synthetic-stop branch.
- UNKNOWN_RETAINED: real evaluator coverage, upstream acceptance, runtime behavior, effect verification, local applicability.
- NEXT_RETEST_CONDITION: accepted pinned SDK; explicit/generic/decorated evaluators, stop/cap/no-message/static/live cases; compare persisted reason, metric inputs, actual user messages, and independent postcondition.

## NEXT_HANDOFF
Retain H1/H2 for the next eligible closed week. No host mutation, premature H3/H4 or monthly memory.

## BOUNDARY_CHECK
Original H1 merge/readback, upstream linked issue and patch review and standalone control executed. Actual git ls-remote https://github.com/lostlight530/welcome-to-github.git refs/heads/main exited 128: Could not resolve host: github.com; stdout empty. Full horizon-cortex/check.py, SDK, eval suite and host runtime NOT_EXECUTED. One canonical H2 artifact; no historical rewrite. Human Maintainer review/merge authorization separate from checker status.
