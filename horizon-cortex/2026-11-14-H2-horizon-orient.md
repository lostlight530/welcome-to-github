# H2 Daily Horizon Orient — 2026-11-14

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-14
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Source Identity: langchain-ai/langgraph@ccfb0a1bf82ac6d56e909ca782779574362bb8c4
Source Authority For Claim: FIRST_PARTY_CHANGED_SOURCE_AND_AUTHOR_TESTS / NO_RAN_TEST
Independent Verification: SOURCE_DIFF_REOPENED / RUNTIME_NOT_EXECUTED / ONE_UPSTREAM_LINEAGE
Host Applicability: UNKNOWN / NO_WELCOME_ADOPTION_OBSERVED
Evidence Upgrade Basis: EXACT_RECHECK_AND_NARROWER_CONDITIONS / NO_INDEPENDENT_REPRO
Original Execution Status: GPT_NATIVE_SOURCE_SCOPED_H2_COMPLETED
Current Path Status: DRAFT_PR_PENDING_REVIEW
Base Main SHA: ef555b924f28f4c037ed9921457e0db95adc1e44
Run Identity: welcome-to-github/horizon/H2/2026-11-14/GPT_NATIVE/ef555b924f28f4c037ed9921457e0db95adc1e44/independent-subgraphs-callback-scope-01
Execution Time UTC: 2026-11-14 / exact H2 start NOT_CAPTURED
Execution Time Asia/Shanghai: 2026-11-14 / exact H2 start NOT_CAPTURED
Upstream H1: horizon-cortex/2026-11-14-H1-signal-observe.md
Upstream H1 Blob SHA: 855f8bf483da409aea65770d45233be524a0afb6
Upstream H1 Merge PR: https://github.com/lostlight530/welcome-to-github/pull/986
Input Status: SAME_DATE_H1_MERGED_MAIN_VISIBLE_AND_EXACT_BLOB_READ
Input H1 Task Status: SUCCESS_BOUNDED_PRIMARY_CODE_OBSERVATION
Network Status: FIRST_PARTY_GITHUB_EXACT_COMMIT_REOPENED
Source Status: PYTHON_SYNC_ASYNC_IMPLEMENTATION_AND_AUTHOR_TEST_PATCH_READ / NO_TEST_EXECUTION
Task Status: SUCCESS_BOUNDED_STATIC_ORIENTATION / NO_STRATEGIC_PROMOTION
Write Scope: horizon-cortex/2026-11-14-H2-horizon-orient.md
Boundary Violation: NO

## INPUT_RECORD
- Directly read the exact Nov 14 H1 blob 855f8bf483da409aea65770d45233be524a0afb6 from current merged main ef555b924f28f4c037ed9921457e0db95adc1e44 after GitHub PR #986 was confirmed merged. Its source, task identity, Shanghai period, provenance and unexecuted-test boundary were checked.
- Read Nov 13 H2 and closed W45 H4 as dated continuity sources. Neither is independent corroboration of today's LangGraph change. October H6 remains a dated owner with earlier provisional header and later historical updates, not today's newly executed H6.
- Reopened upstream langchain-ai/langgraph exact commit ccfb0a1bf82ac6d56e909ca782779574362bb8c4 and inspected sync + async implementation and changed tests; did not merely restate H1 prose.
- No repository or SDK runtime tests, installed package introspection, production stream observations, host NEXUS or Parallax inputs executed.
- Current ISO W46 ends Nov 15 Shanghai; Monthly November remains OPEN. H3/H4 and H5/H6 are NOT_DUE.

## SIGNAL_CLASSIFICATION

### SIG-20261114-H01 — conditional child-stream callback restoration
Signal ID: SIG-20261114-H01
H1 Claim: a child graph invoked outside its caller task with its own thread or configurables previously lost messages/tools callbacks even when caller requested subgraphs=True; source patch preserves requested subgraph handlers.
Classification: watchlist
Verification Status: ORIGINAL_SYNC_AND_ASYNC_PATCH_REOPENED / AUTHOR_REGRESSION_TESTS_PRESENT / NATIVE_TESTS_NOT_EXECUTED
Verification Sources:
- https://github.com/langchain-ai/langgraph/commit/ccfb0a1bf82ac6d56e909ca782779574362bb8c4
- libs/langgraph/langgraph/pregel/main.py changed stream() and astream() handler filtering: _is_stream_mode_handler replaced by _streams_only_its_graph
- _streams_only_its_graph(handler) returns true only for StreamMessagesHandler / StreamToolCallHandler when handler.subgraphs is false
- libs/langgraph/tests/test_stream_namespaces.py has updated synchronous and added asynchronous own-thread child tests
Repository Record Comparison: prior W45 H4 NO_ACTIONABLE_DECISION and Nov 13 H2 concerned different upstream changes; neither demonstrates deployed LangGraph semantics at Welcome.
Reason: handler filtering is a conditional streaming boundary, not a general execution boundary. Keeping handler when subgraphs=True requests child output; discarding it for a normal parent stream avoids falsely attributing child events to parent nodes.
Evidence Strength: HIGH_FOR_COMMITTED_BRANCH_CONDITIONS / NO_INDEPENDENT_EXECUTION
Counterevidence:
- subgraphs=False still filters the child's inherited messages/tools handlers when the graph runs outside the caller task. This is deliberate; an absence of parent-stream events under this flag is not proof of failed child execution.
- Child event namespaces remain their own, including the empty tuple for top-level child nodes, rather than being nested under the calling node path; consumers assuming such reparenting are wrong.
- Source commit description names regression after LangGraph 1.2.19; exact deployed version and real host behavior were not checked. The upstream author reports four previously failing cases, but this producer did not run those tests or inspect external CI receipts.
- JS has a different implementation path and already filters by subgraphs in isOutsideStream; the Python patch is not proof of a JavaScript regression or a universal MCP/A2A event contract.
Remaining Uncertainty: installed release coverage, callbacks dropped by other layers, stream delivery under interruption, tested node/config variants, and actual Welcome adoption.
Promotion Eligibility: WATCHLIST_ONLY / NOT_AN_ACTIONABLE_ARCHITECTURE_OR_HOST_CHANGE

## ORIENTATION_NOTES
- Narrowly supported mechanism: sync/async Python streaming now retains child messages/tools handlers requested by subgraphs=True for outside-task children. No independent runtime reproduction in this H2.
- Contradiction resolved: a child's own stream namespace being root-like does not mean the event was generated by the parent graph; use explicit graph/thread/namespace identity when interpreting telemetry.
- Counterevidence Gate: compare subgraphs=True against False, sync versus async, child's own thread versus caller thread, and parent stream with/without separate checkpoint configuration. Include a deliberately child-executed-but-parent-silent control.
- Independent evidence count remains one upstream commit lineage, even after H1, H2, upstream authored tests, PR merge and repeated source citation.
- Host applicability UNKNOWN, not missing by assumption and not confirmed. No NEXUS or public portal migration was attempted.

## NO_DECISION_SECTION
- No H3 strategic positioning, H4 narrative action, SDK/Runtime migration, production deployment, Host NEXUS indexing, Parallax import or approval decision.
- No claim of benchmark pass, source rollout, provider dominance, event correctness for all agent systems, exactly-once event delivery or verified host adoption.
- No W46 final or November H5/H6 long-term memory promotion before period closure.

## NEXT_HANDOFF
- To H3 after W46 closes: admit this as one first-party Python streaming boundary observation, with provenance and reproducibility unknown; only promote if independent revision-pinned runtime results and real host relevance are recovered.
- Retest: pin code and test fixture, launch subgraphs True/False sync/async on child thread/config cases, capture child steps, handler IDs, event modes, namespaces, exit status, stdout/stderr and actual downstream consumer receipt.
- Next research candidate: compare event existence, namespace attribution, durable checkpoint identity and effect identity as separate observational planes.
- H4 and H6 are not authorized by H2. Human review/merge remains the sole delivery gate for this note.

## BOUNDARY_CHECK
- Same-date upstream H1 was merged, main-visible and read by blob SHA before H2 execution.
- Only a new dated Horizon H2 path is proposed; original H1 and all earlier Jules/GPT-native records untouched.
- No host code, runtime config, NEXUS, Parallax, workflow, historical audit, memory or external source changed.
- Native tests: NOT_EXECUTED; source-patch inspection and remote file verification only.
- Boundary Violation: NO
