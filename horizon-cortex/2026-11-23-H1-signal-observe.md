# H1 Daily Signal Observe — 2026-11-23 / retired Live streaming tool ownership fences and late output

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-23
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 9dd324a20cbac38c103d714d833e4fa513e7f949
Run Identity: welcome-to-github/horizon/H1/2026-11-23/GPT_NATIVE/9dd324a20/retired-streaming-tool-output-01
Source Identity: google/adk-python PR #8303 / head 57ab6e5718c34abfa1945e907042f63f8c4ee2d2
Source Authority For Claim: FIRST_PARTY_OPEN_PR_IMPLEMENTATION_AND_AUTHORED_TESTS
Independent Verification: EXACT_UPSTREAM_PR_HEAD_AND_DIFF_INSPECTED / NO_UPSTREAM_SDK_RUN
Host Applicability: UNKNOWN / NO_NEXUS_LIVE_STREAMING_RUNTIME_DEPENDENCY_VERIFIED
Evidence Upgrade Basis: BOUNDED_SOURCE_CODE_CHANGE_AND_AUTHOR_FIXTURE / NO_HOST_EXECUTION
Original Execution Status: EXTERNAL_SOURCE_PATCH_REVIEW_EXECUTED / ADK_AND_HOST_TESTS_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_UPSTREAM_LIFECYCLE_CHANGE_PROPOSAL / UPSTREAM_RELEASE_UNVERIFIED
Write Scope: horizon-cortex/2026-11-23-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Fresh GitHub `main` at `9dd324a20cbac38c103d714d833e4fa513e7f949`; `horizon-cortex/EVIDENCE_POLICY.md` is the owning source-authority/handoff contract. 2026-11-22 H1/H2 and closed 2026-W46 H3/H4 remain historical inputs.
- One W47 H3 Draft PR #1041 was already open at preflight. It owns `2026-W47-H3-position-decide.md`, not this logical day's H1. W47 H4 is blocked pending that H3's Human Maintainer merger. This H1 does not consume W47's next-stage credit.
- Actual attempted local source acquisition: `git ls-remote https://github.com/lostlight530/welcome-to-github.git refs/heads/main`; exit `128`, stdout empty, stderr `fatal: unable to access ... Could not resolve host: github.com`. The isolated worktree is unavailable; local Horizon checker and SDK runtime have not run.
- Previous Nov22 Horizon focus was nullable MCP input JSON Schema. This Nov23 source concerns **retired asynchronous streaming-call ownership after Live agent transfer**, not schema conversion or a host incident.
- W48 begins 2026-11-23 and has not closed; W48 H3/H4 `NOT_DUE`. November H5/H6 `NOT_DUE` until the calendar month closes.

## EXTERNAL_SOURCE_RECORDS
Source ID: SRC-20261123-H01
URL: https://github.com/google/adk-python/pull/8303
Title: fix(live): fence retired streaming tool output
Publisher: google/adk-python first-party repository contribution, not an adopted SDK release
Source Publication: created `2026-11-22T20:55:57Z` = 2026-11-23 04:55:57 Asia/Shanghai; observed in the same Shanghai logical date
Source Version: `OPEN_UNMERGED_PR_HEAD=57ab6e5718c34abfa1945e907042f63f8c4ee2d2`; compare base `2b90353cd2f1ee0a8a52262a7843333b6f7d2c8d`
Source Implementation: https://github.com/google/adk-python/blob/57ab6e5718c34abfa1945e907042f63f8c4ee2d2/src/google/adk/flows/llm_flows/tools/_live_caller.py
Source Regression A: https://github.com/google/adk-python/blob/57ab6e5718c34abfa1945e907042f63f8c4ee2d2/tests/unittests/streaming/test_live_tool_shutdown.py
Source Regression B: https://github.com/google/adk-python/blob/57ab6e5718c34abfa1945e907042f63f8c4ee2d2/tests/unittests/flows/llm_flows/tools/test_live_caller.py
Related issue identity: https://github.com/google/adk-python/issues/8302 — link and issue context are from the PR, **not independent runtime replication**
Source Access: connected GitHub PR metadata and three exact source/test patches inspected at fixed head SHA
Evidence Tier: FIRST_PARTY_UNMERGED_PATCH_AND_TEST_SOURCE / NO_INDEPENDENT_E2E
Confidence: HIGH_FOR_PATCH_CONTROL_FLOW / AUTHOR_REPORTED_TESTS_NOT_REPRODUCED / UNKNOWN_FOR_RELEASE_OR_HOST
Uncertainty: upstream review/merge/release, edge-case server streaming, websocket timing, deployment and NEXUS applicability not observed.

## RAW_SIGNAL_LOG
Signal ID: SIG-20261123-H01
- **Conditional failure model:** a streaming tool ignores its first cancellation. The owning agent transfers and the shutdown deadline expires; the background registry entry is cleared, yet the old producer can still emit model responses or user Events into shared queues. A late event is capable of surfacing during the next agent's stream if lifetime ownership is not checked at the emission boundary.
- **Proposed precise owner check:** `_is_current_background_tool(invocation_context, active_tool)` looks up `active_tool.function_call_id` in `_active_background_tools` and requires object identity `is active_tool`. The patch passes an `ActiveBackgroundTool` entry into both emission paths.
- **Emission fence:** `_emit_streaming_tool_event` checks that identity immediately before enqueuing user-visible content. Stream-to-model response paths use the corresponding current-entry gate, rather than assuming the earlier cancellation or task-local function-call ID is enough.
- **ABA/cleanup condition:** cleanup discards an entry only if it is still the same registered object. If the function-call ID is reused for another live invocation, an old worker must not delete its replacement by ID alone. Object identity acts as an invocation-local ownership token, not an authenticated user grant.
- **Retained behavior:** one-second best-effort cancellation and behavior of *still registered* streaming calls are not intended to change; a separate nonblocking launcher is outside the changed path.
- **Author test claim:** PR body reports 50 passing targeted tests, 779 passed + 1 xfailed related suite, and an independent author-controlled worktree with similar results. These are **AUTHOR_REPORTED** and tied to the pinned PR, not tests run by this Horizon producer. The mock-runner regression does not use a real Gemini Live endpoint or credentials.
- **Scope correction:** queue ownership can reduce *late output contamination* but does not prove no external side effect occurred, no message was enqueued before retirement, exactly-once delivery, durable stream replay, tool authorization or cross-agent state consistency.

## Controls, counterevidence and applicability
- Positive control: same tool instance yields a response and an Event while its `ActiveBackgroundTool` entry remains registered; delivery must remain possible.
- Negative N1: producer catches cancellation and yields after transfer; registry entry retired. Both model and user output must be suppressed, with timestamps and queue ID/provenance retained.
- Negative N2: a new call reuses the same function-call ID with a distinct object; old producer must not enqueue or evict the new call. ID equality without object identity is insufficient.
- Negative N3: tool response was queued *before* retirement but consumed after it. This patch's enqueue-time check alone does not establish consumer-time isolation; require a separate consumer/readside receipt before making a universal stream-cleanliness claim.
- Negative N4: a tool performs an external irreversible action before being cancelled and its output is fenced. Absence of output is not proof that its effect was undone, authorized, or nonexistent.
- Applicability to Welcome/NEXUS: `UNKNOWN`; no pinned locally installed `google-adk`, `Runner.run_live`, active background tool registry, Gemini transport or host effect sink has been verified.
- Alternative safe boundary: a producer that obeys cancellation immediately might never emit late output, even without the new owner token. This must be a non-failing control, not evidence of the reported race's universal occurrence.

## EVIDENCE_DELTA
- NEW_EVIDENCE: first-party open PR #8303 identifies specific registry-object identity and emission-ownership gates in both model/user streaming paths; publisher provides exact regression fixture and versioned head.
- CORRECTED_INTERPRETATION: cancellation request, registry deletion, output enqueue, downstream queue consumption and external effect settlement are distinct event identities. A producer can survive shutdown and emit after deregistration.
- UNCHANGED_BOUNDARY: UPSTREAM_PATCH != RELEASED_SDK != NEXUS_ADOPTED; AUTHOR_TEST_REPORT != THIS_RUN_EXECUTION; STREAM_OUTPUT_SUPPRESSED != EXTERNAL_EFFECT_REVERSED.
- NEW_COUNTEREVIDENCE: reused call ID, pre-retirement queued output, successful immediate cancellation and effect-before-cancellation constrain universal safety claims.
- UNKNOWN_RETAINED: actual upstream merge/release, real Gemini timing, installed host dependency, server queues and end-to-end effect/approval identity.
- NEXT_RETEST_CONDITION: pin package revision and two concurrently active call IDs, inject cancellation-resistant generator, transfer agent, monitor both queues and consumer times, separately verify effect sink and host installed path with raw stdout/stderr/exit.

## NEXT_HANDOFF
- Proposed H1 requires Human Maintainer review and actual merge before same-date `welcome/horizon/H2/2026-11-23`. Then H2 fresh-reads exact retained H1 path/blob and upstream PR status, independently checks cancellation/owner object semantics and counterexample controls.
- Prior to that merge: `H2=BLOCKED_UPSTREAM_NOT_MERGED` with no separate H2 file or execution credit. An open W47 H3 PR is a different owning logical period; no overlap or implicit merge credit.
- A source patch can motivate Horizon internal watch/retest but does not authorize NEXUS implementation changes.

## BOUNDARY_CHECK
- Only H1 Daily source research; NEXUS, Parallax, W47 H3, Independent A1/A2, Governance, Jules, schedule and Actions unchanged.
- Actual external GitHub PR/source/test patch review and local git DNS failure recorded. `python3 horizon-cortex/check.py horizon-cortex/2026-11-23-H1-signal-observe.md`, upstream tests, Gemini Live, NEXUS code and real effect verification: `NOT_EXECUTED`.
- This document does not assert structural checker PASS, upstream package release, Human Maintainer approval or merged main retention. Draft PR only.
