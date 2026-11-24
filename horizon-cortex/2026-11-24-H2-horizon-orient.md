# H2 Daily Horizon Orient — 2026-11-24 / budget admission is not effect authority

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-24
Logical Timezone: Asia/Shanghai
Agent: GPT-6.2 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 20f5616e6940b75410ea82b2241281fbfdbb7d94
Run Identity: welcome-to-github/horizon/H2/2026-11-24/GPT_NATIVE/20f5616e6940/fresh-source-orientation-01
Source Identity: openai/openai-agents-python PR #6211 / head 4eccd80f4ede2e7d967220405d9f41e69a556d17
Source Authority For Claim: FIRST_PARTY_OPEN_UNMERGED_PATCH_AND_AUTHOR_FIXTURES
Independent Verification: MERGED_MAIN_INPUT_BLOB_538dc3ce205f83b4ddb05757ace0421d5d2d1e37 / CURRENT_UPSTREAM_DIFF_RECHECK / SDK_NOT_EXECUTED
Host Applicability: UNKNOWN / INSTALLED_DEPENDENCY_AND_CONFIG_UNVERIFIED
Evidence Upgrade Basis: LEGAL_DEPENDENCY_AND_ADDITIONAL_SOURCE_INSPECTION / SAME_ISSUER_NO_REPLICATION
Original Execution Status: FRESH_MAIN_INPUT_AND_UPSTREAM_SOURCE_REVIEW_EXECUTED / FULL_CHECKER_AND_SDK_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_SOURCE_ORIENTATION / NO_HOST_DECISION
Write Scope: horizon-cortex/2026-11-24-H2-horizon-orient.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Original same-day horizon-cortex/2026-11-24-H1-signal-observe.md merged via #1049, merge SHA 20f5616e6940b75410ea82b2241281fbfdbb7d94; exact blob 538dc3ce205f83b4ddb05757ace0421d5d2d1e37 read from fresh main. This is a new orientation identity, not another independent external source.
- Current owning horizon-cortex/EVIDENCE_POLICY.md; prior Nov23 orientation and W47 handoff remain historical. W48 and November final NOT_DUE.
- Upstream [PR #6211](https://github.com/openai/openai-agents-python/pull/6211) remains OPEN / UNMERGED at 4eccd80f4ede2e7d967220405d9f41e69a556d17; base f5230b521739fc3212fb503675431cefb694beb3. Non-null synthetic PR merge SHA is not a merge receipt when merged=false.
- Prior producer reported checkout failure; this orientation used exact GitHub source reads. No full worktree or native checker executed in this orientation.

## SIGNAL_CLASSIFICATION
- Bounded SDK-managed admission policy; not released capability or host adoption.
- Additional run_budget.py source inspection: reservations after approval/input guardrails, before hooks/invocation; failures/cancellation after reservation do not refund. Paused child resume avoids another wrapper reservation.
- Explicit limits on observable requests/token consumption permit response overshoot; provider-owned tools and native delegation are outside applicable counters. Source documentation and authored tests only.

## ORIENTATION_NOTES
- Distinguish admission, usage observation, tool start, child wrapper, successful effect, and actual billing. The reviewed authored test test_failed_100_then_retry_1_applies_selected_usage_policy uses 50-token budget; opt-in accounting observes 101 tokens but lookup still runs once before the next admission stops. Default accounting records 2 budget tokens while public usage is 102. These are authored assertions, not this run's measured values.
- Counterevidence: after a limit breach a requested tool can still run; a failed/cancelled reserved slot need not imply an effect. Shared budget checkpoints require same policy, unique enabled tool binding and parent scope. Neither wrapper count nor resumed checkpoint proves sink idempotency.
- Opaque prompt tests reject local and inherited restrictions before provider dispatch; scope is selected SDK routes. Hidden provider work and same-name handlers remain outside stronger authorization claims.
- Candidate retest: vary failed-attempt usage opt-in, response overshoot, approval rejection, reservation/cancellation, same-name child binding and resume; capture observed tokens, outer requests, starts, grant identity and authoritative effect readback separately.

## NO_DECISION_SECTION
NO_DECISION / NO_HOST_PROMOTION. Same source lineage rechecked; zero independent SDK replication added. No NEXUS implementation or budget guarantee established.

## EVIDENCE_DELTA
- NEW_EVIDENCE: additional budget documentation and authored failed-usage/opaque-prompt fixture review.
- CORRECTED_INTERPRETATION: token observation and admission limits do not bound already-requested effects.
- UNCHANGED_BOUNDARY: SDK_COUNTER != PROVIDER_BILLING != EFFECT_SETTLEMENT.
- NEW_COUNTEREVIDENCE: overshoot plus tool invocation and reservation without effect.
- UNKNOWN_RETAINED: release, deployed host, actual SDK execution and sink evidence.
- NEXT_RETEST_CONDITION: exact version, executable positive/negative matrix and authoritative effect receipt.

## NEXT_HANDOFF
Retain bounded research in next eligible closed-week synthesis; do not advance W48 or November final early.

## BOUNDARY_CHECK
Current main, original merge and upstream source rechecked. Full repository checker, SDK tests and host runtime NOT_EXECUTED. Only this canonical orientation file; history, host, governance and independent maintenance unchanged. Draft awaiting authorized merge.
