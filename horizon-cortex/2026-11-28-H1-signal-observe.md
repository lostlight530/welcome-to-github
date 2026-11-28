# H1 Daily Signal Observe — 2026-11-28 / termination attribution
## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-28
Logical Timezone: Asia/Shanghai
Agent: GPT-6.2 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: e47889df4eef1480375b66d2c8197f23f06313b4
Run Identity: welcome-to-github/horizon/H1/2026-11-28/GPT_NATIVE/e47889df4eef/termination-01
Source Identity: google/adk-python PR #8416 / ab8a94dcdff7eb316c34d8042aff2f51528fbe85
Source Authority For Claim: PRIMARY_PROPOSED_SOURCE_PATCH / AUTHOR_REPORTED_TESTS
Independent Verification: PR_METADATA_AND_SELECTED_PATCHES_INSPECTED / SDK_NOT_EXECUTED
Host Applicability: UNKNOWN
Evidence Upgrade Basis: BOUNDED_SOURCE_REVIEW / OPEN_UNMERGED / NO_RELEASE_PROMOTION
Original Execution Status: SOURCE_REVIEW_EXECUTED / FULL_CHECKER_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_PROPOSAL_SIGNAL / NO_ACCEPTED_RELEASE_SIGNAL
Write Scope: horizon-cortex/2026-11-28-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Owning policy blob 060eaff65437bda48718a9703477815c574a9846, checker blob 5736c90f56a59728db380180557256a151b1ea83, prior H1 blob 803f471c2addd28d01020910a90b70c0ce56c708. Fresh nontruncated tree, no same-day H1 or open PR at initial preflight; W47 retained, W48 and November closure NOT_DUE.
- Observation 2026-11-28 Asia/Shanghai. GitHub API source review. Prior Nov27 signal concerns deferred log formatting; today's signal concerns recording why a simulated conversation ends. Full worktree and checker not acquired/executed.

## EXTERNAL_SOURCE_RECORDS
Source ID: SRC-20261128-H01
URL: https://github.com/google/adk-python/pull/8416
Title: feat(evaluation): record conversation termination reason in eval results
Publisher: ADK repository contributor
Source Publication Time: 2026-11-27T19:09:47Z (Nov28 Shanghai)
Source Revision: head ab8a94dcdff7eb316c34d8042aff2f51528fbe85; base 03725e8c67ca27b2c07569797a0c18e867e0b217; OPEN / UNMERGED
Evidence Tier: PRIMARY_PROPOSED_PATCH / AUTHOR_REPORTED_TESTS
Confidence: selected exact source hunks establish proposed data-flow distinctions; release, efficacy and coverage unverified
Inspected Surface: conversation_termination.py; base_eval_service.py; evaluation_generator.py; eval_result.py; CLI and dev_server hunks; test_evaluation_generator and test_local_eval_service hunks.
Independent Evidence: one PR lineage; author tests not independently executed; corpus-wide deduplication not established.

## RAW_SIGNAL_LOG
- Proposed enum distinguishes stop_signal, turn_limit, no_message; None remains possible for static or unrecorded termination. Generation result carries invocations and reason rather than a bare invocation list; reason is exposed on inference/eval case results and CLI/web response.
- The visible local-eval test fixture uses InferenceStatus.SUCCESS with TURN_LIMIT; that is direct evidence of a proposed separate predicate, not proof the overall task succeeded. The author describes skipping a synthetic finished-turn judge when capped; optional fail-on-turn-limit/completion metric remains follow-up.
- In the visible live generator hunk, a live finished-signal branch can break before assigning a simulator reason. Missing reason cannot automatically mean completion or failure. The legacy generate_responses path shown appends invocations alone; downstream retention is not universal.
- Author reports green suite and offline repro; neither reproduced. No accepted release or host migration established.

## Counterevidence Gate
- Explicit stop can occur before user-intended effect; a turn cap can occur after a valid effect. Reason is attribution, not an effect oracle.
- Null reason may be intentional for static cases or missing telemetry. It is not a negative proof. Consumers dropping the field cannot inherit provenance.
- The proposal is open. Same source may be reused as a research lead elsewhere without additional independent-source credit.

## EVIDENCE_DELTA
- NEW_EVIDENCE: pinned proposed termination enum and selected propagation/test hunks.
- CORRECTED_INTERPRETATION: successful inference, conversation termination reason and verified task completion are separate predicates.
- UNCHANGED_BOUNDARY: SOURCE_PATCH != RELEASE != HOST_ADOPTED.
- NEW_COUNTEREVIDENCE: SUCCESS plus TURN_LIMIT; null on an unrecorded live/static path.
- UNKNOWN_RETAINED: merge, release, complete metric coverage, user-intended effect, host applicability.
- NEXT_RETEST_CONDITION: accepted revision, controlled stop/cap/no-message/static/live fixtures; verify field retention at each API/consumer and independently inspect intended postcondition.

## NEXT_HANDOFF
H2 only after same-day original H1 merges and exact artifact is reread from fresh main. Recheck PR state, reason propagation and counterexamples; no source-identity duplication.

## BOUNDARY_CHECK
Selected remote metadata and patch inspection executed. Full horizon-cortex/check.py, ADK tests, evaluator and host runtime NOT_EXECUTED. No historical or host modification; Human Maintainer review required.
