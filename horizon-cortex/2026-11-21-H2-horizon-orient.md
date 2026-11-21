# H2 Daily Horizon Orient — 2026-11-21 / checkpoint compare-and-replace is not external-effect reconciliation

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-21
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 9047b170ea1f6bea91425ca442e7c2439a2b9ba0
Run Identity: welcome-to-github/horizon/H2/2026-11-21/GPT_NATIVE/9047b17/approval-cas-retest-01
Source Identity: openai/openai-agents-python PR #6103; pinned head 2dcb27954e47ded5f2670c662e74383002fd1bb7
Source Authority For Claim: FIRST_PARTY_OPEN_IMPLEMENTATION_AND_TESTS / SAME_ISSUER_AS_H1
Independent Verification: MERGED_H1_PR_1029_AND_EXACT_MAIN_BLOB_READBACK / NO_INDEPENDENT_REDIS_RUN
Host Applicability: UNKNOWN / NO_NEXUS_SDK_ADOPTION_OBSERVED
Evidence Upgrade Basis: DEPENDENCY_SATISFIED_PLUS_COUNTEREXAMPLE_AND_OBSERVABILITY_GATE / NO_NEW_ISSUER
Original Execution Status: DIRECT_DEPENDENCY_AND_SOURCE_REVIEW / UPSTREAM_TESTS_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_HORIZON_ORIENTATION / NO_DECISION / NO_HOST_ADOPTION
Write Scope: horizon-cortex/2026-11-21-H2-horizon-orient.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Same-day H1 original PR #1029 merged with GitHub merge SHA `9047b170ea1f6bea91425ca442e7c2439a2b9ba0` by authorized merge, then exact `main` file `horizon-cortex/2026-11-21-H1-signal-observe.md` reopened.
- Exact H1 blob retained: `255c23810a659e0a2e1eb0291beb824a50123eb8`. This is the authoritative dependency; the H1 text's historical `PROPOSED_DRAFT_PR` field is an at-authoring observation, not its final delivery state.
- Owning policy `horizon-cortex/EVIDENCE_POLICY.md` blob `060eaff65437bda48718a9703477815c574a9846`; source-custody and host-applicability boundary remains in force.
- Source PR https://github.com/openai/openai-agents-python/pull/6103 was independently rechecked for current disposition: OPEN / NOT_MERGED; head still `2dcb27954e47ded5f2670c662e74383002fd1bb7`. Its 2026-11-20 UTC publication is not a new 2026-11-21 upstream release.
- Original H1 inspected the proposed Redis checkpoint and its authored tests. This H2 is a *second-stage interpretation of the same source lineage*, not independent corroboration or upstream runtime execution.

## SIGNAL_CLASSIFICATION
Signal ID: SIG-20261121-H01
Layer: Agent SDK pending approval / Redis checkpoint concurrency / process crash / external effect
Supported source mechanism: proposed `ResumableSession`, Redis store conditional replacement, serialized pending approval, saved run state and unknown-outcome error classification in the pinned diff
Source status: OPEN_PROPOSAL, not yet a released version or production deployment
Applicability to Horizon host: UNKNOWN; no evidence Welcome's NEXUS uses this SDK Redis path
Scientific confidence: FIRST_PARTY_IMPLEMENTATION_PROPOSAL_INSPECTED; AUTHOR_TESTS_ONLY; INDEPENDENT_REPRODUCTION_NOT_EXECUTED

## ORIENTATION_NOTES_AND_REBUTTAL
- Dependency correction: H1 being merged confirms this record is eligible for H2, but **does not** convert H1's upstream proposal into a released feature, independently validated approval mechanism, or host capability.
- Control P1 (NOT_EXECUTED): worker A persists exact `(tenant, approval_id, tool_call_id, normalized_arguments, policy_revision)`; worker B loads the same checkpoint under a new process and an authoritative sink confirms exactly one matching effect.
- Control P2 (NOT_EXECUTED): user rejects approval; a restarted worker must not invoke tool and must retain a rejection receipt keyed to the approval identity.
- Counterexample N1 (NOT_EXECUTED): two workers both read revision `r`, only one commits `r+1`; CAS can reject the stale checkpoint while an already-started external effect may still have happened. Redis CAS != distributed effect transaction.
- Counterexample N2 (NOT_EXECUTED): worker commits effect, crashes before checkpoint CAS; restored state may mark `UNKNOWN_OUTCOME`. Blindly treating error as `NOT_OCCURRED` risks duplicate effect.
- Counterexample N3 (NOT_EXECUTED): approved tool name matches but resolved target/arguments mutate after an input hook; loading generic approval without exact argument identity would permit an unauthorized different effect.
- Counterexample N4 (NOT_EXECUTED): checkpoint expires or tenant is wrong; Redis key existence/lookup is not evidence a continuation is authorized for an external resource.
- Counterexample N5 (NOT_EXECUTED): a read-only retry and a side-effectful retry are not equivalent under a missing acknowledgement, even if both calls share the session ID.
- Source authored tests describe duplicate approval, rejection, worker restart and post-write pod kill. They are evidence of intended test coverage, not an independently reproduced sink oracle, nor a proof of all crash interleavings.
- Proposed candidate trace for a future bounded test: `session_id, tenant, checkpoint_revision, approval_revision, approved_argument_digest, worker_id, operation_id, sink_id, sink_commit_revision, response_or_missing, recovery_decision`.
- `approval_retained`, `checkpoint_saved`, `runner_resumed`, `effect_committed`, `effect_confirmed` and `task_completed` are six distinct predicates; no current source validates them end-to-end for Welcome.

## NO_DECISION_SECTION
Decision: NO_DECISION
Decision ID: NO_DECISION
Decision Basis: bounded open implementation patch, source-level authored tests, no independently reproduced Redis/sink crash path or host adoption
Horizon Memory Promotion: NO
Host Change: NONE
Independent Corroborating Publishers: NONE
Next Watchlist: final release identity; tenant/approval/argument binding; CAS race; effect-after-checkpoint gap; crash/replay; sink readback

## EVIDENCE_DELTA
- NEW_EVIDENCE: original same-date H1 merge SHA and retained canonical blob plus a current recheck showing upstream PR #6103 remains open at the pinned head.
- CORRECTED_INTERPRETATION: an atomic checkpoint write only controls one record's revision; it is not a globally atomic transaction with the external tool effect or proof that a resumed request is authorized.
- UNCHANGED_BOUNDARY: H1/H2 one publisher and one source lineage; SOURCE_PATCH != RELEASE != DEPLOYMENT != HOST_ADOPTION != END_TO_END_EFFECT_RECOVERY.
- NEW_COUNTEREVIDENCE: effect committed before checkpoint receipt, concurrent stale worker, substituted tool arguments and tenant-expired approval defeat naive `persisted checkpoint == safe retry` reasoning.
- UNKNOWN_RETAINED: independently verified crash resilience, provider sink receipt, actual host dependency, deployment version and third-party reproduction.
- NEXT_RETEST_CONDITION: pin released SDK revision, one Redis tenant-scoped checkpoint store and a real instrumented effect sink; crash at each durable state transition, verify allowed/denied/unknown outcomes under both duplicate and benign requests.

## NEXT_HANDOFF_AND_BOUNDARY
- W47 H3/H4 NOT_DUE until 2026-11-22 closes Asia/Shanghai; November H5/H6 NOT_DUE until natural month end. Existing W46 artifacts not duplicated.
- Native H2 distinct from Independent A1/A2 and Parallax, NEXUS, audit, Governance or correction roles.
- Source/PR/main/blobs INSPECTED. Horizon `check.py`, upstream Redis integration, provider sink, release package, local host validation: NOT_EXECUTED.
- Only canonical same-date H2 file added; no private scheduler controls, secrets or historical Jules outputs included. Draft PR awaits Human Maintainer review/merge.
