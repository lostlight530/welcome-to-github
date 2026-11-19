# H2 Daily Horizon Orient — 2026-11-19 / residual stale-guard race and version boundary

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-19
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 8925f29a47645bbb0ecc188009623f8a48451efc
Run Identity: welcome-to-github/horizon/H2/2026-11-19/GPT_NATIVE/8925f29/memory-lock-guard-counterchecks-01
Source Identity: modelcontextprotocol/servers PR #5623 ec42f5bbb6a72ad212b827cf27354e25066c1086
Source Authority For Claim: FIRST_PARTY_PINNED_IMPLEMENTATION_AND_AUTHORED_TEST_TEXT / SAME_ISSUER_AS_H1
Independent Verification: MERGED_H1_PR_1015_SHA_BLOB_READBACK / FIRST_PARTY_ISSUE_5624_AND_PATCH_REVIEW / NOT_REPRODUCED
Host Applicability: UNKNOWN / WELCOME_NEXUS_MCP_MEMORY_SERVER_DEPLOYMENT_NOT_VERIFIED
Evidence Upgrade Basis: NEW_EXPLICIT_COUNTEREXAMPLE_AND_RELEASE_DEPLOYMENT_GATE / NOT_SECOND_INDEPENDENT_SOURCE
Original Execution Status: SOURCE_AND_DEPENDENCY_REVIEW_PERFORMED / LOCAL_MCP_SERVER_AND_AUTHOR_TESTS_NOT_EXECUTED
Current Path Status: DRAFT_PROPOSED_AT_AUTHORING / MERGE_NOT_YET_OBSERVED
Task Status: BOUNDED_SOURCE_ORIENTATION / NO_HOST_MIGRATION_DECISION
Write Scope: horizon-cortex/2026-11-19-H2-horizon-orient.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- The same-date native H1 is **actually merged** via [PR #1015](https://github.com/lostlight530/welcome-to-github/pull/1015), merge SHA `8925f29a47645bbb0ecc188009623f8a48451efc`; exact H1 blob in main `0924a4ee5d1f375136083b96d62b15b2dfa42db5`. Fresh main and this exact file were reread; no draft dependency substitution.
- H1 source [PR #5623](https://github.com/modelcontextprotocol/servers/pull/5623), public issue [#5565](https://github.com/modelcontextprotocol/servers/issues/5565), residual [#5624](https://github.com/modelcontextprotocol/servers/issues/5624) and implementation patch are one first-party provenance lineage, not three independent experiments.
- External observation date for merged upstream PR does not prove an installed downstream npm release; the source fix and residual report address Node memory server interprocess file locks, not the MCP protocol's normative state or this host's NEXUS persistence.
- H1 includes a bounded negative result. H2 tests whether its scope survives counterexamples, not whether a production server was successfully reproduced.

## SIGNAL_CLASSIFICATION
Signal ID: SIG-20261119-H01
Layer: Memory server implementation / per-file cross-process serialization / guard lifecycle
First-party observed patch mechanism: `<file>.lock.break` now protects release compare-then-delete and post-create token confirmation. It reduces three named historical interleavings.
Preconditions: multiple same-host same-user writers share one memory file, affected source builds and stale lock or guard scheduling conditions. Not universally applicable to all tools or storage systems.
Residual case: #5624 documents two stale-guard clearers deleting a live new guard by path. The implementation itself acknowledges that an actor stalled beyond stale timeout while guarded can lose protection. These do not establish a *current* real production incident on Welcome.
Mixed-version case: older server instance can still execute its old unguarded acquire/release; newer-version protection of its own handoff does not imply an automatically safe mixed deployment against all races.
Evidence: PINNED_FIRST_PARTY_CODE / AUTHOR_REPORTED_DETERMINISTIC_TESTS / PUBLIC_OPEN_COUNTEREXAMPLE.
Disposition: WATCH / NO_DECISION / NO_HOST_CHANGE.
Independent issuer added: NONE.

## ORIENTATION_NOTES
- Hypothesis P1 (NOT_EXECUTED): pin exact new/old versions, inject stale-lock break between comparison and unlink, and inspect whether final file token remains owned by the current writer.
- Hypothesis P2 (NOT_EXECUTED): new writer creates lock while a live successor's lock is temporarily renamed aside; require the new writer not to enter critical section on the overwritten token.
- Negative N1 (NOT_EXECUTED): dual stale-guard clearers, A removes judged guard, C creates fresh guard, B attempts path deletion; require C guard survival to eliminate the *remaining* known race.
- Negative N2 (NOT_EXECUTED): a process pauses inside guard beyond stale timeout; assume recovery mechanism might judge a live guard stale, so stale detection is not a universally correct failure detector.
- Negative N3 (NOT_EXECUTED): mixed old/new versions on one path with writer identity on each acquisition/release; a limited successful interleaving does not prove all cross-version concurrency.
- Negative N4 (NOT_EXECUTED): single-process memory test never exercises cross-process lock ownership and is not corroboration of hard race-free concurrency.
- Negative N5 (NOT_EXECUTED): process crash after returning success but before durable fsync still needs disk recovery and exact record readback; lock mutual exclusion does not prove durability.
- Require exact `source revision`, `installed runtime package`, `process IDs`, `lock token+inode`, `stale timeout`, `file-store identity`, `critical-section events`, `effect receipt` and `post-recovery replay` for promotion.
- Source evidence is one lineage; a closed upstream issue and passing author tests do not make the future #5624 resolution completed, nor do they show Welcome has deployed the package.
- INSPECT: code and test lineage; TRACE: acquisition and release receipt; INSTRUMENT: injected interleavings; ALLOW/DENY/MODIFY: host-specific approval remains separate from file-lock synchronization.

## NO_DECISION_SECTION
Decision: NO_DECISION
Decision ID: NO_DECISION
Decision Basis: bounded source-level improvement exists; #5624 open counterexample, old-version participants, timeout/liveness assumptions and absent host installation receipts block generalization.
Claim Promotion: NO
Host Change: NONE / NO_NEXUS_MODIFICATION
Watchlist: lock-file version identity, stale-guard cleanup, crash/replay proof, durable write receipt and source-to-host dependency.
Future retest: fixed 3-process schedules on exact upstream revisions, include guard cleanup/release windows and independent persisted store oracle.

## EVIDENCE_DELTA
- NEW_EVIDENCE: actual same-day H1 merged-main dependency readback and explicit upstream residual #5624 condition.
- CORRECTED_INTERPRETATION: resolved issue #5565 and merged PR #5623 do not establish lock protocol universally free of all races.
- UNCHANGED_BOUNDARY: FIRST_PARTY_PATCH != INSTALLED_PACKAGE != LOCAL_RUNTIME != DURABLE_EFFECT; H1/H2 one source lineage.
- NEW_COUNTEREVIDENCE: live-guard deletion, mixed-version old acquire/release and stale timeout liveness limitations.
- UNKNOWN_RETAINED: independent test reproduction, release installation, Welcome host relevance, actual crashes, durable effects, all remaining race conditions.
- NEXT_RETEST_CONDITION: exact pinned old/new+mixed runner schedule and authoritative final memory-file readback with all process/lock identities.

## NEXT_HANDOFF
- Independent A1/A2 maintenance is a separate role; H2 itself grants no original A1/A2 numeric credit.
- W47 H3/H4 NOT_DUE before 2026-11-22 closes; November H5/H6 NOT_DUE until natural month closure.
- No Horizon Memory promotion or host migration without independent evidence and maintainer authorization.

## BOUNDARY_CHECK
- Actually inspected: new main after H1 merge, exact H1 blob, author-published PR patch, unresolved upstream counterexample and current Horizon checker-required fields.
- NOT_EXECUTED: full Horizon checker, upstream tests, MCP server, NEXUS runtime, actual process crash experiment and external effect sink.
- No original H1 revision, Jules history, Parallax, workflows, maintenance, governance or protected host file changed.
- Proposed one original Native H2 file; merger only upon the separately granted user merge authorization and GitHub final status.
