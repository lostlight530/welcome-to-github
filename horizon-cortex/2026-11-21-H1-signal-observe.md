# H1 Daily Signal Observe — 2026-11-21 / persistent approval checkpoint across worker replacement

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-21
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 355d4db36d1870138a649ab4ac1ee90441ea956e
Run Identity: welcome-to-github/horizon/H1/2026-11-21/GPT_NATIVE/355d4db/redis-approval-checkpoint-01
Source Identity: openai/openai-agents-python PR #6103, head 2dcb27954e47ded5f2670c662e74383002fd1bb7
Source Authority For Claim: FIRST_PARTY_OPEN_PR_IMPLEMENTATION_AND_TEST_DIFF
Independent Verification: GITHUB_PR_METADATA_AND_PATCH_INSPECTED / UPSTREAM_TESTS_NOT_REPRODUCED
Host Applicability: UNKNOWN / NO NEXUS RESUMABLE_SESSION DEPLOYMENT OBSERVED
Evidence Upgrade Basis: BOUNDED_CHECKPOINT_APPROVAL_AND_UNKNOWN_EFFECT_RECOVERY_PATH
Original Execution Status: REMOTE_SOURCE_INSPECTION / LOCAL_UPSTREAM_RUNTIME_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_EXTERNAL_IMPLEMENTATION_PROPOSAL / RELEASE_UNVERIFIED
Write Scope: horizon-cortex/2026-11-21-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Cold-start current main: `355d4db36d1870138a649ab4ac1ee90441ea956e`; complete non-truncated git tree queried, 2026-11-20 H1/H2 and closed 2026-W46 H3/H4 already retained; no open PR visible in five-core preflight.
- Owning `horizon-cortex/EVIDENCE_POLICY.md` blob `060eaff65437bda48718a9703477815c574a9846`; `horizon-cortex/README.md` blob `fb6a2d828764571af66caf94259f67f16b1a8b0d`.
- Prior 2026-11-20 H1 examined modelcontextprotocol/servers lock restoration on Windows. This Daily instead examines *approval and conversational checkpoint continuity across workers*. It is not independent reproduction of a memory-lock fix.
- Source PR #6103 created 2026-11-20T07:02:51Z (= 2026-11-20 15:02:51 Asia/Shanghai), OPEN and unmerged at inspection. The checked head is immutable for this record; eventual merge, tag and release remain separate.
- Local `git ls-remote https://github.com/lostlight530/Axiom-0.git refs/heads/main` attempted in isolated container, exit 128, stdout empty, stderr `Could not resolve host: github.com`. This is acquisition-environment evidence, not a ResumableSession test.

## EXTERNAL_SOURCE_RECORDS
Source ID: SRC-20261121-H01
Title: Resume conversations and pending SDK tool approvals from Redis
Publisher: openai/openai-agents-python upstream PR author and maintainers
Canonical Source Identity: https://github.com/openai/openai-agents-python/pull/6103 ; head 2dcb27954e47ded5f2670c662e74383002fd1bb7
Pinned implementation: https://github.com/openai/openai-agents-python/blob/2dcb27954e47ded5f2670c662e74383002fd1bb7/src/agents/memory/resumable_session.py
Pinned Redis store: https://github.com/openai/openai-agents-python/blob/2dcb27954e47ded5f2670c662e74383002fd1bb7/src/agents/extensions/memory/redis_session_store.py
Pinned tests: https://github.com/openai/openai-agents-python/blob/2dcb27954e47ded5f2670c662e74383002fd1bb7/tests/memory/test_resumable_session.py
Source Version: OPEN_UNMERGED_PR_HEAD / RELEASE_NOT_VERIFIED
Source Publication: 2026-11-20T07:02:51Z (PR creation); observed on logical 2026-11-21
Source Access: CONNECTED_GITHUB_PR_METADATA_AND_PER_FILE_PATCH
Source Authority: PRIMARY_FOR_PROPOSED_UPSTREAM_PATCH / NOT_INDEPENDENT_RUNTIME_REPRODUCTION

## RAW_SIGNAL_LOG
Signal ID: SIG-20261121-H01
- Upstream proposed `ResumableSession` binds conversation history and pending SDK tool approvals to a durable checkpoint keyed by session ID; RedisSessionStore uses application-owned Redis and compares revisions before replacement.
- Proposal exposes `create(store)`, `resume(store, session_id)`, and `load_state(agent)` to move a paused approval from worker A to worker B. The saved state carries approval context; a raw session ID alone is not proof the new worker has loaded the same authorized call.
- Code diff adds a distinct `unknown outcome` error class when an unfinished attempt's effect cannot be resolved from its checkpoint. That is a fail-closed *proposed behavior*, not proof that the external mutation was reversed or never happened.
- The PR author's test plan reports same approval submitted twice executed a tool once, rejected approval skipped execution, and pod interruption after write resulted in unknown outcome rather than a blind repeat. Those are author-reported local tests, not this research run's reproductions.
- Code includes a Redis compare-and-replace pathway and tests for concurrent checkpoint claims; it does not establish universal exactly-once external effects, correct tenant isolation for arbitrary deployments, or reliable behavior when Redis and the external effect sink fail between transactions.
- Material identity distinction: approved argument digest, tool call ID, checkpoint revision, session/tenant, Redis acknowledgement, process instance and provider-side effect receipt should remain separately attributable.
- The source adds a proposed implementation, not a final stable SDK release or a required migration for NEXUS.
- Unlike yesterday's OS-specific lock-restore patch, today's failure surface is durable human approval and effect-uncertainty across agent restarts. Cross-source architectural analogy is not independent evidence for one concrete deployment.

## CONTROLS_AND_COUNTEREXAMPLES
- Positive control: worker A persists an approval for exact tool call/arguments, exits, worker B reloads the checkpoint and executes a single approved effect; verify independent sink-side identity.
- Negative control A: simultaneous workers resume the same revision; stale compare-and-replace must be rejected without a second effect.
- Negative control B: edit tool arguments or target between approval and resume; enforce approved-argument identity rather than accepting a generic prior approval.
- Negative control C: persist the intent, execute an external mutation, lose the provider response or crash before the checkpoint confirms outcome. `UNKNOWN_OUTCOME` must survive; checkpoint CAS alone cannot prove the external sink outcome.
- Negative control D: expired or cross-tenant session ID must not gain access to another tenant's approval or conversation, even when IDs are known.
- Distinguish authored fixtures from a pinned released wheel, cross-worker Redis server experiment and an actual external effect sink.

## EVIDENCE_DELTA
- NEW_EVIDENCE: inspected a specific open first-party patch introducing approval-coupled Redis checkpoint state, revision-constrained updates and unknown-outcome semantics.
- CORRECTED_INTERPRETATION: persistently saving conversation text is not sufficient to restore approval identity or prove a tool effect; a successful resume is still not a sink receipt.
- UNCHANGED_BOUNDARY: FIRST_PARTY_OPEN_PR != RELEASED_SDK != HOST_ADOPTION != VERIFIED_DURABLE_EFFECT; author tests are not independent replications.
- NEW_COUNTEREVIDENCE: duplicate approval, stale checkpoint, substituted arguments, cross-tenant reuse and commit-before-checkpoint-loss scenarios constrain the proposal's guarantees.
- UNKNOWN_RETAINED: PR merge/release, independently reproduced Redis crash window, NEXUS use of this mechanism, sink idempotency and authorization enforcement at effect time.
- NEXT_RETEST_CONDITION: pin released revision and tenant-scoped Redis store; run two workers with crash points around checkpoint save, tool invoke, sink commit and response; compare actual effect receipts and state revisions.

## NEXT_HANDOFF
- Same-date `welcome/horizon/H2` is BLOCKED_DEPENDENCY until this original H1 PR is merged and the new main SHA plus H1 blob are actually re-read. H2 may add independent verification, not duplicate this record.
- 2026-W47 H3/H4 NOT_DUE (week ends Sunday 2026-11-22 Asia/Shanghai); November H5/H6 NOT_DUE (month OPEN).
- Do not change NEXUS host, Parallax, independent A1/A2, other maintenance, historical Jules artifacts, policies or schedulers.

## BOUNDARY_CHECK
- Upstream PR metadata, original diff and test text inspected via GitHub; author's runtime outcomes NOT_REPRODUCED.
- Horizon checker `python3 horizon-cortex/check.py`: NOT_EXECUTED (full worktree cannot be acquired in isolated container).
- No human approval, merged upstream release, local hosted adoption, independently measured production reliability, or shared-source multiplication asserted.
- Public content contains only inspected public source/version metadata and constrained research claims, not private control-plane prompts or secrets.
