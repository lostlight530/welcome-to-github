# H1 Daily Signal Observe — 2026-11-17 / A2A streaming artifact closure

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-17
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 25e1140336ced355a87bc6655d45876cc3454539
Run Identity: welcome-to-github/horizon/H1/2026-11-17/GPT_NATIVE/25e1140336ced355a87bc6655d45876cc3454539/a2a-stream-artifact-boundary-01
Observation Window: 2026-11-17 Asia/Shanghai / upstream commit 2026-11-16T22:24:34Z
Source Identity: google/adk-python@dbae28d3ccd0958d202a85e2c39cdf249ae2c7f2
Source Authority For Claim: FIRST_PARTY_PINNED_IMPLEMENTATION_DIFF_AND_AUTHORED_TEST_SOURCE
Independent Verification: EXACT_GITHUB_COMMIT_DIFF_READ / NO_SEPARATE_A2A_RUNTIME_REPRODUCTION
Host Applicability: UNKNOWN / NO_WELCOME_A2A_RUNTIME_DEPLOYMENT_VERIFIED
Evidence Upgrade Basis: NEW_PINNED_A2A_STREAM_ARTIFACT_FINALIZATION_CHANGE / NOT_RELEASE_VERIFIED
Original Execution Status: GPT_NATIVE_SOURCE_REVIEW_EXECUTED / UPSTREAM_TESTS_AND_HOST_RUNTIME_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: SOURCE_BOUNDED_OBSERVATION / RUNTIME_UNKNOWN
Source Status: COMMIT_PATCH_INSPECTED / RELEASE_VERSION_NOT_VERIFIED
Write Scope: horizon-cortex/2026-11-17-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Cold started from merged Welcome main `25e1140336ced355a87bc6655d45876cc3454539` and inspected current `horizon-cortex/README.md`, `EVIDENCE_POLICY.md`, `check.py`, 2026-11-16 H1/H2 and W46 canonical paths; no 2026-11-17 H1/H2 appeared in that main tree at preflight
- Existing 2026-11-16 H1 focused on Google ADK default dynamic instruction routing and does not provide independent evidence for this new A2A artifact-stream closure claim
- Directly fetched first-party upstream [commit dbae28d3](https://github.com/google/adk-python/commit/dbae28d3ccd0958d202a85e2c39cdf249ae2c7f2), inspected its patch touching `src/google/adk/a2a/agent/_remote_a2a_agent.py` and authored `tests/unittests/a2a/agent/test_remote_a2a_agent.py`
- This is an implementation patch under a specific upstream revision, not a verified release, deploy, protocol-wide requirement or host migration. No ADK, A2A server, pytest or real Welcome runtime was launched for this H1
- Clock distinction: upstream commit timestamp 2026-11-16T22:24:34Z is 2026-11-17T06:24:34+08:00; H1 logical research date is 2026-11-17; GitHub PR creation/merge are separate delivery times

## EXTERNAL_SOURCE_RECORDS
Source ID: SRC-20261117-H01
Title: Persist streamed RemoteA2aAgent output even when no final artifact last_chunk marker is delivered
Publisher: google/adk-python maintainers
Canonical Source Identity: google/adk-python@dbae28d3ccd0958d202a85e2c39cdf249ae2c7f2
URL: https://github.com/google/adk-python/commit/dbae28d3ccd0958d202a85e2c39cdf249ae2c7f2
Implementation URL: https://github.com/google/adk-python/blob/dbae28d3ccd0958d202a85e2c39cdf249ae2c7f2/src/google/adk/a2a/agent/_remote_a2a_agent.py
Authored Test URL: https://github.com/google/adk-python/blob/dbae28d3ccd0958d202a85e2c39cdf249ae2c7f2/tests/unittests/a2a/agent/test_remote_a2a_agent.py
Source Version: EXACT_COMMIT_SHA / RELEASE_TAG_UNVERIFIED
Upstream Change Time: 2026-11-16T22:24:34Z UTC
Date Checked: 2026-11-17 Asia/Shanghai
Evidence Tier: PRIMARY_SOURCE_IMPLEMENTATION_DIFF / AUTHOR_TEST_SOURCE_ONLY
Access Status: COMMIT_AND_DIFF_READ / TEST_BODY_PARTIALLY_INSPECTED
Independent Source Count: ONE_UPSTREAM_REPOSITORY_LINEAGE
Claim Supported: This pinned ADK change adds an artifact-id keyed streaming buffer and boundary finalization so partial artifact updates may be emitted as finalized events even if a streaming A2A server ends with a task/status boundary rather than `last_chunk=True`
Claim Not Supported: all A2A implementations have identical failure, all upstream tests pass in our environment, a specific release includes the fix, end-to-end durable-effect recovery, authenticated remote artifact provenance, Welcome/NEXUS adopting this path, or measured latency/completeness
Confidence: HIGH_FOR_PATCH_MECHANISM / UNKNOWN_FOR_DEPLOYED_RUNTIME
Limitations: Only inspected a first-party patch and authored test source; dynamic behavior, store persistence and cross-version compatibility remain untested by this producer. An SDK-internal `Event` emitted to a runner is not proof of external effect settlement.

## RAW_SIGNAL_LOG
Signal ID: SIG-20261117-H01
Signal: REMOTE_A2A_ARTIFACT_STREAM_PARTIAL_CHUNK_BOUNDARY_FINALIZATION
Observation: The patch adds `_OpenArtifactBuffer` and `_StreamingArtifactAggregator`; comments explicitly identify proto3 1.x streams where `last_chunk` defaults False and a `TaskStatusUpdateEvent` closes a turn. The implementation checks explicit `True` for flags, tracks chunks per artifact ID, handles empty closing markers, append-only closing delta, replacement artifact and status/message boundaries.
Mechanism: A stream chunk is not necessarily a completed durable record. New code tries to convert buffered partial payloads to final non-partial `Event` output at the appropriate boundary, including handling pending events in finish-task argument recovery.
Potential False Negative Pre-Patch: An application that treats `last_chunk=True` as the only artifact completion signal can lose output if the final boundary arrives through task status, despite the remote stream containing the material.
Control Case: A full task snapshot that already contains an artifact can supersede the partial stream, so unconditional flush could duplicate material; the patch includes logic to discard already materialized artifacts.
Counterexample A: No partial artifact, or a genuine complete replacement with correct `last_chunk`, need not exhibit the original loss path.
Counterexample B: Network failure, interceptor rejection, duplicated artifact identities, or missing status boundary can still prevent fully persisted results; this change is not a universal exactly-once or durable delivery theorem.
Counterexample C: A finalized runner event can remain local in-process; downstream DB durability, provenance authentication and application-level completion require separate receipts.
Evidence Class: REVISION_SCOPED_UPSTREAM_IMPLEMENTATION_CHANGE
Independent Verification Needed: before/after pinned ADK revisions, fake streaming A2A transport with `last_chunk=False` followed by terminal status; independent check of finalized event content, artifact ID, deduplication and persisted session readback
Host Applicability: UNKNOWN / NO_WELCOME_REMOTE_A2A_EXECUTION_OBSERVED
Noise Filter: An exact source/test delta, not an announcement or a claim that the A2A standard changed on the same date
Disposition: WATCHLIST / SOURCE_BOUNDED_OBSERVATION

## EVIDENCE_DELTA
- NEW_EVIDENCE: pinned upstream RemoteA2aAgent artifact-id buffering and task/status boundary finalization implementation
- CORRECTED_INTERPRETATION: `last_chunk=False` or absence of explicit final-chunk marker is not itself authoritative proof the remote artifact lacks content; runner materialization must be traced separately
- UNCHANGED_BOUNDARY: streamed transport content != committed session event != external durable effect != host production adoption
- NEW_COUNTEREVIDENCE: full snapshot/replacement may already contain artifact; forced flush can duplicate content, and network/interceptor failures remain separate
- UNKNOWN_RETAINED: named SDK package release, test outcomes, any production impact, persistence coverage, A2A protocol conformance and Welcome integration
- NEXT_RETEST_CONDITION: pin both ADK revisions and a controlled A2A stream without last_chunk; capture per-event partial/final identity, emitted event count, saved session revision, stdout/stderr/exit and same-revision rollback control

## NEXT_HANDOFF
- H2 canonical `welcome/horizon/H2` for 2026-11-17 is BLOCKED_DEPENDENCY until the original H1 Draft PR is merged, visible on fresh main and exact same-date H1 blob is reread
- Closed ISO W46 was 2026-11-09 to 2026-11-15; this 2026-11-17 source is not retroactively W46 input
- November H5/H6 are NOT_DUE until natural month closure under current contract
- Human review may accept, reject or request stricter source-level proof, but must not infer H2 or Host adoption from H1 file delivery

## BOUNDARY_CHECK
- Only the new `horizon-cortex/2026-11-17-H1-signal-observe.md` H1 Native record, no changes to NEXUS, Parallax, workflows, other Horizon records, independent maintenance, governance, original Jules history or host runtime
- Actual check: GitHub current main + first-party commit patch read; deterministic required-section/field inspection performed before write
- NOT_EXECUTED: `python horizon-cortex/check.py`, upstream authored tests, A2A server, ADK SDK runtime, host integration, release provenance and end-to-end durable persistence
- Delivery target: one Draft PR for Human Maintainer; no authorization for automatic merge
