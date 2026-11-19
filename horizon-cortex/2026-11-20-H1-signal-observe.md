# H1 Daily Signal Observe — 2026-11-20 / Windows lock restoration under transient sharing denial

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-20
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: adff8df1877189fae025c7df7a74e4df750fa566
Run Identity: welcome-to-github/horizon/H1/2026-11-20/GPT_NATIVE/adff8df/windows-lock-restore-01
Source Identity: modelcontextprotocol/servers PR #5637, head 7a1511cd2e0e6ce1019e259bdef959621492fe26
Source Authority For Claim: FIRST_PARTY_PINNED_IMPLEMENTATION_AND_TEST_DIFF
Independent Verification: GITHUB_PR_METADATA_AND_FILE_PATCH_READ / AUTHOR_TESTS_NOT_REPRODUCED
Host Applicability: UNKNOWN / NO NEXUS OR WELCOME MEMORY SERVER DEPLOYMENT OBSERVED
Evidence Upgrade Basis: NEW_PLATFORM_SPECIFIC_RESTORE_FAILURE_AND_BOUNDED_GUARD_RETRY
Original Execution Status: REMOTE_SOURCE_PATCH_INSPECTION / LOCAL_UPSTREAM_TESTS_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_EXTERNAL_SOURCE_MECHANISM / NO_HOST_ADOPTION
Write Scope: horizon-cortex/2026-11-20-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Fresh owner main adff8df1877189fae025c7df7a74e4df750fa566; non-truncated Git tree reviewed for existing Daily and W46 H3/H4 records. No overlapping open Horizon PR at preflight.
- Owning evidence policy blob 060eaff65437bda48718a9703477815c574a9846; README blob fb6a2d828764571af66caf94259f67f16b1a8b0d.
- Prior 2026-11-19 H1 source: PR #5623 memory lock hand-off. This record is a *new residual platform-specific counterexample and remediation*, not an independent remeasurement of the same upstream publisher or proof prior H1 was false.
- Upstream PR #5637 was created 2026-11-19T15:24:42Z, which is 2026-11-19 23:24:42 Asia/Shanghai; at this inspection GitHub shows closed/merged, with merge timestamp 2026-11-19T15:41:17Z. These are upstream publication/merge events; 2026-11-20 is our observation identity.
- Upstream issue #5635 describes Windows CI failures after #5623. Issue claims are first-party incident reports about upstream CI, not our own experiments.
- Git bootstrap diagnostic in this environment: `git ls-remote https://github.com/lostlight530/Axiom-0.git refs/heads/main` returned exit 128 and `Could not resolve host: github.com`; the diagnostic concerns local network acquisition and is **not** a memory lock test.

## EXTERNAL_SOURCE_RECORDS
Source ID: SRC-20261120-H01
Title: fix(memory): keep retrying a lock put-back that Windows refuses for a moment
Publisher: modelcontextprotocol/servers upstream maintainers and PR author
Canonical Source Identity: modelcontextprotocol/servers PR #5637, head 7a1511cd2e0e6ce1019e259bdef959621492fe26
URL: https://github.com/modelcontextprotocol/servers/pull/5637
Issue URL: https://github.com/modelcontextprotocol/servers/issues/5635
Pinned implementation: https://github.com/modelcontextprotocol/servers/blob/7a1511cd2e0e6ce1019e259bdef959621492fe26/src/memory/index.ts
Pinned author tests: https://github.com/modelcontextprotocol/servers/blob/7a1511cd2e0e6ce1019e259bdef959621492fe26/src/memory/__tests__/file-lock.test.ts
Source Version: MERGED_UPSTREAM_PR_HEAD / RELEASE_PACKAGE_AND_DEPLOYMENT_UNVERIFIED
Source Publication: 2026-11-19T15:24:42Z PR creation
Source Access: CONNECTED_GITHUB_PR_METADATA_AND_EXACT_FILE_PATCH
Source Authority: FIRST_PARTY_IMPLEMENTATION_FOR_THIS_PATCH / NOT_INDEPENDENT_CROSS_PLATFORM_VALIDATION

## RAW_SIGNAL_LOG
Signal ID: SIG-20261120-H01
- Mechanism: stale-lock breaking can move a successor writer's live lock aside when a lock changes owners during the break. A third writer creates its own lock at the original path and continuously opens it while awaiting guard clearance.
- Before this patch, direct rename of the live aside lock back onto the existing file could be refused by Windows with transient EPERM, EACCES, or EBUSY when an open handle exists. The error could be treated as an acquisition busy state and the guard released, leaving the live lock aside; the upstream author reports a window where competing writers both proceed.
- Patch introduces `isReplaceBusy(error)`, matching those three codes **only on win32**; it adds `restoreLock(asidePath, lockPath, guardTakenAt, staleMs, retryMs)` to retry the put-back while retaining the guard.
- Retry cutoff is `guardTakenAt + staleMs / 2`; persistent failure throws a distinctive `Could not put back the live memory file lock` error rather than returning an ambiguous busy state. Thus retry exhaustion is an explicit failure, not silent successful acquisition.
- Non-Windows errors are propagated immediately rather than blanket retried. This platform branching is consequential to the implementation claim.
- Three new test scenarios in the pinned patch exercise transient Windows failures, non-Windows immediate failure, and a permanently refused Windows restoration. Those are authored fixtures observed in source code; *their runtime results were not reproduced here*.
- External issue text reports 4 failures in first 9 Windows CI runs of the prior fix. Numerator/denominator are upstream's report, not a frequency estimate for production memory servers or a locally measured rate.
- Positive discriminator: a transient two-failure restore test expects the third attempt to succeed, while the waiting third writer never enters its operation.
- Negative discriminator: persistent Windows rename refusal should throw and prevent operation; on Linux the same EPERM should be propagated without retry.
- Residual risk: expiration of a guard's stale window, unexpected filesystems, reentrancy and process termination still require bounded experiments; this patch does not establish distributed lock correctness for all platforms.
- Current source supports a narrow code path amendment, not a formal proof of mutual exclusion, a released server package, or an observed local NEXUS behavior.
- Source lineage: PR #5623 and PR #5637 are one upstream maintenance lineage, so they are not counted as two independent issuers.

## EVIDENCE_DELTA
- NEW_EVIDENCE: exact merged upstream diff adds Windows-specific guarded lock restoration and three explicit test fixtures for transient, permanent, and off-platform rename failures.
- CORRECTED_INTERPRETATION: a prior guard-based fix does not by itself prove lock restoration survives Windows file-sharing semantics; handling the error as busy can be unsafe when a live lock remains aside.
- UNCHANGED_BOUNDARY: UPSTREAM_IMPLEMENTATION != RELEASED_PACKAGE != HOST_DEPLOYMENT != RUNTIME_VERIFICATION; first-party issue and code are not independent production corroboration.
- NEW_COUNTEREVIDENCE: the follow-up bug and platform-specific failure path constrain the completeness of PR #5623's stated protection; permanent refusal intentionally fails closed.
- UNKNOWN_RETAINED: actual Windows result here, deployment adoption, third-party reproduction, package release identity, network filesystem semantics, host applicability, further interleavings.
- NEXT_RETEST_CONDITION: pin released build and OS/FS identity, run deterministic three-writer schedule under Windows and Linux with lock token and guard timestamps, collect invocation/operation IDs, exit and observed overlapping writer critical sections.

## NEXT_HANDOFF
- Same-day `welcome/horizon/H2` remains BLOCKED_DEPENDENCY until this H1 original PR is actually merged and the merged main/blob is freshly read.
- H2 should inspect the residual contention path, guard deadline assumptions, platform error handling and independent evidence; do not just restate the H1 patch.
- 2026-W47 H3/H4 NOT_DUE (week ends 2026-11-22); November H5/H6 NOT_DUE (natural month still open).
- Preserve all past Jules/GPT Native files and the independent Parallax, NEXUS and maintenance scopes.

## BOUNDARY_CHECK
- External source metadata, merged head and patch: INSPECTED via GitHub.
- Independent Windows/Linux execution and author test reproduction: NOT_EXECUTED.
- Horizon `check.py` structural checker: NOT_EXECUTED (no complete executable repository tree).
- No claims of host code changes, merged status, human approval, verified lock correctness or two independent evidence issuers.
- Proposed public diff contains only public source metadata and bounded interpretations, not private scheduling controls or secrets.
