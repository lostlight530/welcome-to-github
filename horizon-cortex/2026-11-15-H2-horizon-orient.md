# H2 Daily Horizon Orient — 2026-11-15

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-15
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Source Identity: google/adk-python issue #8058, main d05e482038bdbb226c3a1179550cf83bd8fcbefb, draft PR #8119 head 167a13730a5bcdda2be96af589e9691550fa99af
Source Authority For Claim: FIRST_PARTY_CURRENT_SOURCE_AND_UNMERGED_PROPOSED_PATCH / AUTHOR_REPORTED_TESTS
Independent Verification: CONDITIONAL_PATCH_DIFF_INDEPENDENTLY_REOPENED / NO_LOCAL_ADK_EXECUTION / ONE_UPSTREAM_LINEAGE
Host Applicability: UNKNOWN / NO_WELCOME_DEPLOYMENT_CHECKED
Evidence Upgrade Basis: EXACT_H1_MERGE_AND_SOURCE_BLOB_FRESH_READ_PLUS_NONTRIVIAL_PROPOSED_FIX_BRANCH_COMPARISON / NO_INDEPENDENT_RUNTIME
Original Execution Status: GPT_NATIVE_BOUNDED_SOURCE_ORIENTATION_COMPLETED
Current Path Status: DRAFT_PR_PENDING_HUMAN_REVIEW
Base Main SHA: 01600cc7dc59b879b29f2754f8716059715ad19d
Run Identity: welcome-to-github/horizon/H2/2026-11-15/GPT_NATIVE/01600cc7dc59b879b29f2754f8716059715ad19d/adk-durable-replay-candidate-fix-compare-01
Upstream H1: horizon-cortex/2026-11-15-H1-signal-observe.md
Upstream H1 Blob SHA: e561022cb1afa4faac0fb2d43c0bb4f46c1ca5f7
Upstream H1 Original PR: https://github.com/lostlight530/welcome-to-github/pull/993
Upstream H1 Merge SHA: 01600cc7dc59b879b29f2754f8716059715ad19d
Input Status: EXACT_SAME_DATE_H1_MAIN_MERGED_READ
Task Status: COMPLETED_BOUNDED_SOURCE_ORIENTATION / NO_SYSTEM_ADOPTION
Source Status: CURRENT_MAIN_BRANCH_AND_DRAFT_FIX_PATCH_INSPECTED / UPSTREAM_TESTS_NOT_RUN
Write Scope: horizon-cortex/2026-11-15-H2-horizon-orient.md
Boundary Violation: NO

## INPUT_RECORD
- Actual H1 merge #993 confirmed, new main 01600cc7dc59b879b29f2754f8716059715ad19d read, and exact H1 blob e561022cb1afa4faac0fb2d43c0bb4f46c1ca5f7 reopened before this H2.
- Contract and historical context: Horizon evidence policy plus 2026-11-14 H1/H2 and W45 records. These older statements cannot be retroactively revised by a November 15 investigation.
- Original issue #8058 creation 2026-11-09; upstream maintainer comment Nov 11 reports reproducing issue script on earlier main and proposes identity-sensitive condition.
- Reopened upstream source at exact main d05e482038bdbb226c3a1179550cf83bd8fcbefb: replayed branch still invokes _maybe_reemit_replayed_output unconditionally relative to recovered_state; helper enqueues Event(output=...) when resumable and output exists.
- Separately retrieved current #8119 Draft PR metadata and patch. PR head 167a13730a5bcdda2be96af589e9691550fa99af was unmerged, dated Nov 13. Do not claim it is current-release code.
- No actual google-adk install, runner, local durable session, source test suite, NEXUS use or production event was run. W46 H3/H4 and November H5/H6 remain NOT_DUE at this Shanghai-day observation.

## SIGNAL_CLASSIFICATION
Signal ID: SIG-20261115-H01
H1 Source: horizon-cortex/2026-11-15-H1-signal-observe.md
Classification: WATCHLIST / EFFECT_REPLAY_IDENTITY_PRECISION
Verification Status: EXACT_CODE_BRANCH_COMPARISON / UPSTREAM_REPORTED_REPRO / LOCAL_RUNTIME_NOT_EXECUTED
Verification Sources:
- https://github.com/google/adk-python/issues/8058
- https://github.com/google/adk-python/pull/8119
- https://github.com/google/adk-python/blob/d05e482038bdbb226c3a1179550cf83bd8fcbefb/src/google/adk/workflow/_workflow.py
- https://github.com/google/adk-python/pull/8119/files
Source Lineage Count: ONE_GOOGLE_ADK_REPOSITORY
New Bounded Observation: #8119 replaces the replayed-node else branch with elif run.recovered_state is None or run.recovered_state.output is None; its authored test asserts exactly one stored answer per resumed RequestInput path, and modifies older tests expecting re-emitted prior outputs.
Difference From H1: H1 identified a candidate duplication condition from main and issue text; H2 directly compared the proposed condition and source tests, confirming the negative control is a previously unresolved RequestInput answer requiring first emission, versus an earlier completed run whose output was already session-persisted.
Counterevidence: suppressing every replayed output would lose the newly answered RequestInput event, and changing consumer-visible event emission during resume may change downstream stream expectations; patch tests were not executed by this producer.
Counterevidence: an output that is re-emitted is not proof that its upstream node re-ran or that an external effect happened again. Persistent append count, logical execution count and effect count must be independently observed.
Uncertainty: whether #8119 will be approved, backported, released or fully applicable to alternate session backends; actual event counts outside the upstream reporter fixture; Welcome dependency adoption.
Evidence Strength: HIGH_FOR_PATCH_INTENT_AND_BRANCH_CONDITION / UNKNOWN_FOR_RUNTIME_REPRO_AND_RELEASE
Promotion Eligibility: WATCHLIST_ONLY, no host or protocol mandate.

## ORIENTATION_NOTES
- Contract triple for later test: logical node output key (invocation ID + node path + content identity), append-event ID, durable store revision. These are analysis candidate fields, not proven ADK API invariants.
- A duplicate append can inflate event-count-based observability and replay cost without evidence of repeated action/effect. Conversely a legitimate resumed answer cannot be dropped merely because the runner is in replay mode.
- Pin both the unmodified ADK 2.14.0 and #8119 head. Compare original/patch 1, 10, 100 RequestInput rounds under the same backend and fixture; record session store ID, n physical events, n unique logical output IDs, content bytes, actually executed node counts and negative controls.
- The source-reported 6055 versus 1105 100-round event counts are upstream-reported one study; the independently executed Axiom standalone triangular arithmetic is a separate mathematical model, not a second real ADK experiment.
- Independent evidence does not increase by linking this PR to Welcome H1 or Axiom's November 15 report.
- No host NEXUS, Parallax, frontend, workflow, GitHub Actions or production adoption recommendation follows.

## NO_DECISION_SECTION
- No H3 strategic Decision ID, H4 Action ID, runtime migration, MCP/A2A standard statement or guaranteed exactly-once conclusion.
- NO_DECISION for host architecture, adoption, benchmark validity, general event semantics and bug remediation.
- W46 weekly conclusion cannot be FINAL before full natural-week cutoff, and November H5/H6 remain OPEN / NOT_DUE.

## NEXT_HANDOFF
- W46 H3 after ISO week closure can inherit this one source lineage and any later merged H2 evidence, with explicit Daily coverage and current state. If no independent test or host relevance emerges, preserve NO_DECISION.
- Retest source under stable revisions, with both recovered-state-known and newly resolved RequestInput cases, stream consumers and different session backends; record command/stdout/stderr/exit, persistent store identity and effect observation separately.
- Source freshness to be checked again at next observation; do not infer fix release from this historical Draft PR.

## BOUNDARY_CHECK
- Only one new canonical Horizon H2, not a rewrite of H1 or old Jules provenance.
- H1 was actually merged, new main and exact source blob re-read before H2.
- Source patch read is not test execution; local checker and ADK runtime NOT_EXECUTED.
- No Host Repository Change: NO; no other repo files, governance, scheduler, NEXUS, Parallax, memory or CI altered.
- Human Maintainer authorizes review/merge separately; do not mislabel chat authorization as independent GitHub review.
