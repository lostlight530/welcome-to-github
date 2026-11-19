# H2 Daily Horizon Orient — 2026-11-20 / bounded Windows lock restoration and unresolved stale-guard risks

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-20
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 84fc35f1ca3bf2ea37868cff122e01242594827a
Run Identity: welcome-to-github/horizon/H2/2026-11-20/GPT_NATIVE/84fc35f/windows-guard-orientation-01
Source Identity: modelcontextprotocol/servers PR #5637 head 7a1511cd2e0e6ce1019e259bdef959621492fe26
Source Authority For Claim: FIRST_PARTY_PINNED_PATCH_AND_TESTS / SAME_ISSUER_AS_H1
Independent Verification: MERGED_H1_PR_1023_AND_EXACT_MAIN_BLOB_READBACK / NO_INDEPENDENT_RUNTIME_TEST
Host Applicability: UNKNOWN / NEXUS_MEMORY_SERVER_DEPLOYMENT_NOT_OBSERVED
Evidence Upgrade Basis: DEPENDENCY_SATISFIED_AND_RESIDUAL_NEGATIVE_CONTROLS / NO_SECOND_INDEPENDENT_ISSUER
Original Execution Status: REMOTE_SOURCE_REVIEW_ONLY / CHECKER_AND_UPSTREAM_TESTS_NOT_EXECUTED
Current Path Status: DRAFT_PROPOSED_AT_AUTHORING / MERGE_NOT_YET_OBSERVED
Task Status: BOUNDED_ORIENTATION / WATCH / NO_HOST_CHANGE
Write Scope: horizon-cortex/2026-11-20-H2-horizon-orient.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Same-day H1 original PR https://github.com/lostlight530/welcome-to-github/pull/1023 actually merged, GitHub merge commit `84fc35f1ca3bf2ea37868cff122e01242594827a`; fresh main at that SHA reopened.
- Exact retained H1 path `horizon-cortex/2026-11-20-H1-signal-observe.md`, blob `53fbf0ea4d0e6892e358c8c6988bd1e8a17f91ef` freshly read from merged main, not a Draft dependency.
- Current Horizon evidence policy blob `060eaff65437bda48718a9703477815c574a9846`; do not generalize protocol specifications to deployment or treat repeated first-party source references as independent issuers.
- Upstream first-party change https://github.com/modelcontextprotocol/servers/pull/5637 was merged, addressing Windows transient rename refusal during live lock restoration.
- Upstream earlier #5623 and related #5635 are same issuer lineage; the following interpretation adds failure conditions rather than pretending a fresh third-party replication.

## SIGNAL_CLASSIFICATION
Signal ID: SIG-20261120-H01
Layer: MCP memory server implementation / local file lock / Windows rename semantics / recovery
Supported source mechanism: `restoreLock` retries Windows-only `EPERM`, `EACCES`, `EBUSY` under the stale-break guard and throws on timeout; off Windows those errors remain immediately surfaced.
Positive scoped claim: author source now implements a conditional restoration recovery path, with authored tests for transient and persistent refusal.
Not supported: proved lock mutual exclusion for arbitrary schedules, formal correctness of stale detector, all-filesystem support, published package adoption or deployed Welcome host defense.
The upstream issue reports CI failures after earlier #5623; first-party CI statements do not constitute independent reproduction or this host's local failure.
The restoration guard is time bounded: at `guardTakenAt + staleMs/2` no further attempt begins. Success on a fast system cannot establish safety if process scheduling stalls beyond guard validity.
New writer and breaker may use differing package revisions. The restored lock token and the third writer's view must be checked at exact critical-section timestamps.

## ORIENTATION_NOTES
- Positive P1 (NOT_EXECUTED): reproduce transient Windows sharing denial for two rename attempts, then success; assert no third writer enters the live holder's critical section.
- Negative N1 (NOT_EXECUTED): persistent Windows refusal until deadline must fail closed with distinct restoration error; no new writer permitted by an ambiguous `busy` classification.
- Negative N2 (NOT_EXECUTED): Linux `EPERM` must fail immediately, no Windows-only retry transfer.
- Negative N3 (NOT_EXECUTED): a guard judged stale after a paused live owner must not be accepted as evidence of crash; controlled delayed-owner counterexample required.
- Negative N4 (NOT_EXECUTED): a stale-guard path may be removed then reused under a different owner; restoring memory lock under the current guard does not prove guard replacement identity safe.
- Negative N5 (NOT_EXECUTED): mixed-version clients can violate assumptions of a single fixed restoration protocol.
- Negative N6 (NOT_EXECUTED): a successful lock release before durable data sync does not prove persisted memory state or client-level success.
- Need pinned OS, filesystem, server revision, lock token/inode, guard identity, critical-section events, exit and post-recovery memory-file oracle for any claim promotion.
- Claim hierarchy: external code path verified at pinned head, authored fixtures identified, runtime behavior unreplicated, package/release deployment unknown, host applicability unknown.

## NO_DECISION_SECTION
Decision: NO_DECISION
Decision ID: NO_DECISION
Decision Basis: bounded source-level remediation but absent independent runtime reproduction, mixed-version controls and durable sink receipts
Claim Promotion: NO
Host Change: NONE
Watchlist: stale-guard identity, protected restoration deadline, Windows and Linux controls, released package identity, fsync and final effect receipt
Independent corroborating issuers: NONE

## EVIDENCE_DELTA
- NEW_EVIDENCE: exact merged H1 dependency custody (PR #1023, merge SHA and blob), bounded testable failure branches for restoration retry and expiry.
- CORRECTED_INTERPRETATION: source-level repair of one Windows rename scenario cannot eliminate all previous stale-guard counterexamples.
- UNCHANGED_BOUNDARY: SOURCE_PATCH != INSTALLED_VERSION != HOST_ADOPTION != DURABLE_EFFECT; H1/H2 references retain one publisher lineage.
- NEW_COUNTEREVIDENCE: persistent refusal, expiry, guard reuse, mixed old/new processes and crash-before-fsync provide counterexamples to universal claims.
- UNKNOWN_RETAINED: independent execution, final package coverage, host instance, stale timeout safety and crash recovery.
- NEXT_RETEST_CONDITION: execute fixed three-process schedules on Windows/Linux with pinned revisions and sink-backed final ownership/data receipt.

## NEXT_HANDOFF
- W47 H3/H4 NOT_DUE, 2026-11-16 through 2026-11-22 still open.
- November H5/H6 NOT_DUE.
- No Horizon Memory promotion, NEXUS change, Parallax or Independent A1/A2 credit.

## BOUNDARY_CHECK
- Executed merged-main/H1 blob/source evidence review.
- NOT_EXECUTED Horizon structural checker, upstream tests, source server, NEXUS runtime, independent process interleavings.
- Draft publication and review separate from merge and runtime; historical Jules records unchanged.
