# H2 Daily Horizon Orient — 2026-11-13

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-13
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Base Main SHA: 966991a709296f0c96e29c1b7a63ab0d7250a28a
Run Identity: welcome-to-github/horizon/H2/2026-11-13/GPT_NATIVE/966991a709296f0c96e29c1b7a63ab0d7250a28a/adk-parent-identity-and-live-exception-recheck-01
Execution Time UTC: exact start NOT_CAPTURED; pre-write UTC observation 2026-11-13T14:06:37Z
Execution Time Asia/Shanghai: pre-write observation 2026-11-13T22:06:37+08:00
Upstream H1: horizon-cortex/2026-11-13-H1-signal-observe.md
Upstream H1 Blob SHA: 146942727b2afe35c137b560fce5a8dcfb6d568f
Upstream H1 Merge PR: https://github.com/lostlight530/welcome-to-github/pull/981
Input Status: SAME_DATE_H1_MERGED_MAIN_VISIBLE_AND_BLOB_READ
Input H1 Task Status: SUCCESS / BOUNDED_PRIMARY_SOURCE_OBSERVATION
Input H1 Network Status: OFFICIAL_GITHUB_COMMIT_PATCH_READ
Input H1 Source Status: FIRST_PARTY_CODE_AND_AUTHORED_TESTS / NOT_EXECUTED
Network Status: FIRST_PARTY_EXACT_GITHUB_COMMIT_AND_FILE_PATCH_REOPENED
Source Status: TWO_PINNED_IMPLEMENTATION_DIFFS / ONE_UPSTREAM_ORGANIZATION / AUTHOR_TESTS_NOT_EXECUTED
Task Status: SUCCESS_BOUNDED_STATIC_ORIENTATION / NO_STRATEGIC_PROMOTION / NO_HOST_DECISION
Host Applicability: UNKNOWN
Write Scope: horizon-cortex/2026-11-13-H2-horizon-orient.md
Boundary Violation: NO

## INPUT_RECORD
- The exact Nov 13 H1 was freshly fetched from merged main after PR #981 was confirmed merged; its task ID, logical date, task/source/network status and blob were inspected. No Nov 12 or future H1 substituted.
- Seven preceding canonical H2 documents actually read: horizon-cortex/2026-11-06-H2-horizon-orient.md through horizon-cortex/2026-11-12-H2-horizon-orient.md (each dated file, excluding sample). These are continuity controls, not independent corroboration.
- Closed weekly context actually read: horizon-cortex/2026-W45-H4-narrative-act.md, which retained NO_ACTIONABLE_DECISION and required bounded evidence.
- October relational context actually read: horizon-cortex/2026-10-H6-horizon-memorize.md, explicitly a month-to-date owner with provisional status, NOT a natural-month final or new November decision.
- Independent H2 source inspection: GitHub API exact original google/adk-python commit patches for 5ce1d0c15af9edef87692f43230bc5bc01103202 and 1a0ddabf1b65d49bb814ac1c2b0c06af4a3a57a4. Reopened source implementation, published SQL/docs and authored test code, rather than promoting H1 prose.
- Missing verification: SQL execution with actual BigQuery session tables; include_plugins=False and custom-runner telemetry; live model/socket execution; independent pytest; host SDK version and deployment.

## SIGNAL_CLASSIFICATION

### SIG-20261113-H01 — nested AgentTool evaluation attribution
Signal ID: SIG-20261113-H01
H1 Claim: parent invocation identity can be passed into nested AgentTool context and attributed via session metadata; the BigQuery analytics view excludes qualifying nested child sessions from session/turn rows.
Classification: weak signal
Verification Status: FIRST_PARTY_PATCH_VERIFIED / RUNTIME_NOT_VERIFIED / NO_STRATEGIC_PROMOTION
Verification Sources:
- https://github.com/google/adk-python/commit/5ce1d0c15af9edef87692f43230bc5bc01103202
- Exact changed paths: src/google/adk/agents/invocation_context.py; src/google/adk/tools/agent_tool.py; src/google/adk/plugins/bigquery_agent_analytics_sql/eval_view_ctes_v1.sql; docs/guides/plugins/bigquery_agent_analytics_eval_sql/index.md
Repository Record Comparison: 2026-W45-H4 retained NO_ACTIONABLE_DECISION; seven preceding H2 records are separate source-bound observations. No Horizon record read establishes deployment of this November 13 source patch.
Reason: The source itself documents a precise conditional predicate: parent invocation is stamped by the built-in nested runner only when include_plugins is enabled and a caller context is available; the SQL SessionEvents CTE filters JSON_VALUE(attributes, '$.adk.parent_session_id') IS NULL. This is narrower than universal nested-agent deduplication. The same commit also adjusts response-text parsing, so the entire diff cannot be credited solely to deduplication.
Evidence Strength: HIGH_FOR_COMMITTED_IMPLEMENTATION_AND_DOCUMENTED_SQL_PREDICATE / NONE_FOR_EXECUTION
Counterevidence: custom AgentTool overriding run_async with its own Runner retains no parent attribution; include_plugins=False does not stamp the parent identity. When the attributes column is denied/missing, the SQL sees NULL, retains child-session rows and may count them separately. Missing metadata is not proof there is no nesting.
Remaining Uncertainty: plugin metadata emission across actual deployments, SQL row counts, custom runners, denied columns, session denominator under mixed topologies, any host adoption.
Promotion Eligibility: WATCHLIST_CANDIDATE_ONLY / STRATEGIC_SIGNAL_NO

### SIG-20261113-H02 — completed response visibility on live stream exception
Signal ID: SIG-20261113-H02
H1 Claim: the live flow exception path yields already-finished tool responses from the queue before rethrowing the connection failure.
Classification: watchlist
Verification Status: FIRST_PARTY_EXCEPTION_BRANCH_AND_AUTHOR_TEST_REOPENED / NO_INDEPENDENT_REPLAY
Verification Sources:
- https://github.com/google/adk-python/commit/1a0ddabf1b65d49bb814ac1c2b0c06af4a3a57a4
- Exact changed paths: src/google/adk/live/_live_llm_flow.py; tests/unittests/streaming/test_live_tool_shutdown.py
Repository Record Comparison: the W45 H4 review required real source/effect receipts rather than implementation narratives. Earlier H2 files do not establish an actual stream failure or effect ledger for this Nov 13 case.
Reason: a new except Exception block drains function_response_queue with get_nowait() and re-raises. The authored regression fixture awaits lookup completion, raises ConnectionClosed, and expects names == ['lookup'] while preserving the exception. It is a source-level event visibility repair, not a durable-execution or exactly-once guarantee.
Evidence Strength: HIGH_FOR_PATCH_BRANCH_AND_AUTHORED_FIXTURE / NO_EXECUTED_TEST_RECEIPT
Counterevidence: unfinished calls produce no finished queued response; process death before the Python exception handler, external effects not captured by the queue, network retries, downstream persistence and cancellation in finally remain outside the patch. Re-raising means the overall request can still fail even when a response event was yielded.
Remaining Uncertainty: actual independent failure injection, queue race behavior, persistence, effect-to-response identity binding, test exit and deployed SDK version.
Promotion Eligibility: WATCHLIST_CANDIDATE_ONLY / STRATEGIC_SIGNAL_NO

## ORIENTATION_NOTES
- Verified external changes: source-level nested-session attribution under explicit plugin/metadata conditions and queued response visibility in one live Exception path.
- Marketing narrative: NONE used. A committed first-party source change is stronger than advertising but does not independently establish release uptake or production efficacy.
- Continue observing: session/evaluation denominator contamination under denied attributes; stream failure paths whose completed side effects outlive the visibility of responses.
- Weakened assumptions: child session == independent top-level session; ConnectionClosed == zero successful tool effects; original publisher's written pytest == independently observed pytest PASS.
- Unresolved: runtime compatibility, actual SQL dataset, upstream test execution and any Welcome host integration. Both patches are one google/adk-python publisher lineage, not two independent organizations.

## NO_DECISION_SECTION
- No final W46 H3 positioning, H4 narrative action, SDK selection, production architecture change, model/tool rollout or host repair.
- No host repository, Parallax, NEXUS, scheduler, governance, Actions or ongoing research automation modified.
- No H6 long-term memory promotion; November remains open and weekly W46 is not a completed ISO week.
- No upgrade from H1/H2 repeated source reading to independent verification.

## NEXT_HANDOFF
- H3 input: SIG-20261113-H01 weak signal and SIG-20261113-H02 watchlist, both direct code changes from one upstream organization; neither meets strategic promotion criteria without independent runtime or longitudinal observations.
- Test gate: pin SQL and original SDK SHAs; exercise normal and custom nested Runners with include_plugins True/False and attributes allowed/denied, compare per-invocation IDs and query denominators.
- Tool-effect gate: inject a connection close after a tool effect is committed, then distinguish effect receipt, response_queue event, yielded event, downstream persistence and exception exit. Cover process interruption and in-flight incomplete calls as negative controls.
- No W46 decision before week closure and verified H3 input; no claim that an upstream patch is a Welcome implementation.

## BOUNDARY_CHECK
- Same-date H1 was actually visible on merged main before H2 began; H1 was not rewritten.
- Read only canonical Horizon records and external original sources; no host source, configuration, workflow or other repo surface read as input to H2.
- This artifact adds only today's canonical H2 path. No older record rewritten, no runtime test PASS claimed, no final weekly decision or memory promotion.
- Boundary Violation: NO
