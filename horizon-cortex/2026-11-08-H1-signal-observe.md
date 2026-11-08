# H1 Daily Signal Observe — 2026-11-08

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-08
Logical Timezone: Asia/Shanghai
Execution Time UTC: 2026-11-08T07:48:24.943Z
Execution Time Asia/Shanghai: 2026-11-08T15:48:24+08:00
Agent: GPT-6 / GPT_NATIVE / NOT_JULES_REPLAY
Producer Identity: HUMAN_REQUESTED_GPT_NATIVE
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 2104943f0efe029a0c715ef201eee769d571a475
Run Identity: welcome-to-github/horizon/H1/2026-11-08/GPT_NATIVE/2104943f0efe029a0c715ef201eee769d571a475/unary-a2a-finish-task-01
Source Identity: google/adk-python@1cb926d5b8d702261ec82a26d3f1c4296e0db7d7
Source Authority For Claim: FIRST_PARTY_COMMITTED_SOURCE_AND_AUTHORED_TEST
Independent Verification: DIRECT_COMMIT_AND_PINNED_SOURCE_TEST_READ / RUNTIME_NOT_EXECUTED
Host Applicability: UNKNOWN / HOST_NOT_INSPECTED
Evidence Upgrade Basis: NOV08_NEW_COMMIT_AND_NARROW_SOURCE_DIFF / NOT_RUNTIME_OR_RELEASE_PROMOTION
Original Execution Status: GPT_NATIVE_SOURCE_OBSERVATION_ONLY
Current Path Status: PROPOSED_DRAFT_PR_NOT_MERGED
Network Status: GITHUB_PRIMARY_SOURCE_VERIFIED
Source Status: COMMIT_AND_CODE_TEST_DIFF_READ / RUNTIME_UNKNOWN
Task Status: SUCCESS_BOUNDED_STATIC_SOURCE_OBSERVATION
Write Scope: horizon-cortex/2026-11-08-H1-signal-observe.md
Boundary Violation: NO

## INPUT_RECORD
- Cold-start merged Horizon main 2104943f0efe029a0c715ef201eee769d571a475; previous 2026-11-07 H1 and H2, W44 H4, October H6 relational owner, current EVIDENCE_POLICY and active checker contract were inspected.
- Prior November 7 H1/H2 tracked evaluator thought-part text exclusion, not A2A unary task result argument recovery. The W44 H4 NO_DECISION and original October 27 provenance gap remain unchanged.
- Directly inspected Google ADK original commit metadata/patch plus pinned source code and authored unit test. No Google ADK test run, live A2A peer, or Welcome host/NEXUS/Parallax runtime was executed.
- Current ISO W45 and November remain open. No current-date H1 existed and no competing open Horizon PR existed at preflight. H2 is a downstream task and requires this same-date H1 to become visible on merged main.

## EXTERNAL_SOURCE_RECORDS
### SRC-20261108-H01 — unary A2A finish_task recovery
Source ID: SRC-20261108-H01
Title: fix(a2a): resolve finish_task args from unary A2A task history
Publisher: google/adk-python
URL: https://github.com/google/adk-python/commit/1cb926d5b8d702261ec82a26d3f1c4296e0db7d7
Published or Updated Date: 2026-11-08T05:29:34Z (commit time, not package release)
Date Checked: 2026-11-08 (Asia/Shanghai)
Source Type: ORIGINAL_COMMIT_CODE_AND_AUTHORED_TEST
Evidence Tier: HIGH_FOR_CODE_DIFF / NOT_TEST_EXECUTION
Access Status: COMMIT_AND_TWO_PINNED_CHANGED_FILES_READ
Independent Source: SINGLE_GOOGLE_ADK_LINEAGE
Claim Supported: the implementation adds a fallback from an A2A unary terminal function response to the stored original function-call arguments in `custom_metadata["a2a:response"]["history"]`.
Claim Not Supported: a released SDK fix, a passing ADK test suite, universal A2A conformance or Welcome adoption.
Relevance: A2A task completion and event-to-history projection identity.
Confidence: HIGH_FOR_SOURCE_CONTENT / UNKNOWN_FOR_EFFECTIVENESS
Limitations: metadata shape, matching function-call ID and event isolation scope must be preserved; no executable replay was performed.

## RAW_SIGNAL_LOG
### SIG-20261108-H01 — UNARY_TASK_HISTORY_ARGUMENT_PROJECTION
Signal ID: SIG-20261108-H01
Signal: a unary task-mode remote A2A response can carry a terminal `finish_task` function response in `event.content` while its matching function call and `args` remain in `task.history`, exposed through event custom metadata.
Source IDs: SRC-20261108-H01
What Changed: `_find_finish_task_args_from_history` now searches reversed function response/call sequences, then the reversed history metadata for `finish_task` call data; when a terminal response supplies an ID, the matching call ID is required.
Verified Source Path: src/google/adk/a2a/agent/_remote_a2a_agent.py at commit 1cb926d.
Authored Test Path: tests/unittests/a2a/agent/test_remote_a2a_agent.py — the `test_find_finish_task_args_from_a2a_response_history_metadata` fixture expects `{"result":"42"}` from a function call paired with an `fc-1` terminal response. This test was READ, NOT_EXECUTED.
Why It May Matter: protocol event transformation can preserve terminal status but omit arguments from the immediate content projection, so completion status is distinct from reconstructed output semantics.
Evidence Tier: FIRST_PARTY_IMPLEMENTATION_PATCH_AND_TEST_SOURCE
Confidence: HIGH_FOR_PATCH / OPERATIONAL_RESULT_UNKNOWN
Uncertainty: package release, actual peer behavior, malformed metadata, ID mismatch outcomes, deployment incidence, and downstream adoption remain UNKNOWN.
Freshness: SOURCE_COMMIT_NOV08 / NEW_RELATIVE_TO_NOV07_HORIZON_TOPIC.
Possible Noise: a single SDK code change is not a universal A2A protocol alteration or market-wide signal.
Needs H2 Verification: YES — independently recheck isolation scope and ID matching, compare streaming and unary branches, test missing-history counterexample.
Host Repository Change: NO

## EVIDENCE_DELTA
- NEW_EVIDENCE: November 8 first-party Google ADK commit with exact source/tests for unary A2A finish_task argument fallback.
- CORRECTED_INTERPRETATION: NONE — previous H1/H2 source claims retained.
- UNCHANGED_BOUNDARY: CODE_DIFF != RELEASE != RUNTIME_PASS != HOST_ADOPTION.
- NEW_COUNTEREVIDENCE: direct completed-event function calls are checked first; metadata fallback applies conditionally, not to every event or peer.
- UNKNOWN_RETAINED: actual test execution, peer interoperability, release identity, SDK adoption and real observed failure rate.
- NEXT_RETEST_CONDITION: pin an exact ADK environment, replay unary/streaming peers with matched and mismatched call IDs, inspect arguments and completion receipts; preserve command, stdout, stderr and exit code.

## NEXT_HANDOFF
- H2 waits for an exact same-day H1 artifact to be merged and visible on main, then binds its exact blob and performs an independent source/counterexample orientation.
- This one upstream issuer lineage does not create two independent sources when reread in H2.
- W45 is not closed, November natural-month H5/H6 is not due, and no host/NEXUS/Parallax action is authorized.

## BOUNDARY_CHECK
- Only proposed canonical H1 file for November 8; no history, host, config, workflows, memory or protected subsystems changed.
- Source/test text inspection is not test execution. Repo checker: NOT_EXECUTED; GitHub Actions: NOT_EXECUTED; runtime outcome: UNKNOWN.
- No private control-plane prompt disclosed and no automatic merge. Boundary Violation: NO
