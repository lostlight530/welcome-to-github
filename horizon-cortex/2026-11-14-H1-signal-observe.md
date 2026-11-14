# H1 Daily Signal Observe — 2026-11-14

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-14
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / NOT_JULES_REPLAY
Producer Identity: HUMAN_REQUESTED_GPT_NATIVE
Base Main SHA: 78bffa1ebca74b90ce744cd0a2f16f545a5e2e9d
Run Identity: welcome-to-github/horizon/H1/2026-11-14/GPT_NATIVE/78bffa1ebca74b90ce744cd0a2f16f545a5e2e9d/langgraph-child-thread-stream-boundary-01
Execution Time UTC: 2026-11-14 / exact research-start second NOT_CAPTURED
Execution Time Asia/Shanghai: 2026-11-14 / exact research-start second NOT_CAPTURED
Network Status: OFFICIAL_GITHUB_EXACT_COMMIT_AND_PATCH_READ
Source Status: FIRST_PARTY_IMPLEMENTATION_AND_AUTHORED_TESTS / NOT_EXECUTED
Task Status: SUCCESS_BOUNDED_PRIMARY_CODE_OBSERVATION
Repository Inspection: CURRENT_MAIN_HORIZON_POLICY_AND_RECENT_PERIODS_READ
GitHub Actions Inspection: H1_CHECKER_NOT_EXECUTED
Write Scope: horizon-cortex/2026-11-14-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Fresh merged main 78bffa1ebca74b90ce744cd0a2f16f545a5e2e9d, current Horizon evidence policy, Nov 13 H1/H2 and closed W45 H4 were read. October H6 was read as a dated relational owner whose earlier provisional header cannot itself prove historical monthly finality.
- GitHub reported no open Welcome PRs at preflight. Target Nov 14 H1 was not present on main. Nov 14 H2 was not used as input.
- Checked first-party langchain-ai/langgraph commit and its changed implementation/test patches. No installed Python package, streaming runtime, browser or host application was executed.
- W46 (2026-11-09 through 2026-11-15) and November calendar month are OPEN; their Weekly H3/H4 and Monthly H5/H6 are NOT_DUE.

## EXTERNAL_SOURCE_RECORDS
Source ID: SRC-20261114-H01
Title: fix(langgraph): stream a child graph on its own thread to a caller streaming subgraphs (#9698)
Publisher: langchain-ai/langgraph
Canonical Source Identity: langchain-ai/langgraph@ccfb0a1bf82ac6d56e909ca782779574362bb8c4
URL: https://github.com/langchain-ai/langgraph/commit/ccfb0a1bf82ac6d56e909ca782779574362bb8c4
Committed At: 2026-11-14T00:58:23Z (2026-11-14 Asia/Shanghai)
Date Checked: 2026-11-14 Asia/Shanghai
Source Type: FIRST_PARTY_SOURCE_COMMIT_WITH_REGRESSION_TEST_DIFF
Evidence Tier: PRIMARY_FOR_EXACT_PATCH_MECHANISM / RUNTIME_NOT_VERIFIED
Access Status: EXACT_COMMIT_AND_CHANGED_PATCHES_READ
Independent Source: ONE_LANGGRAPH_UPSTREAM_LINEAGE
Claim Supported: for a child graph invoked with a distinct thread/configuration outside the caller's task, inherited messages/tools stream handlers are now retained when the caller requested subgraphs=True, and filtered when that option is false. The patch changes libs/langgraph/langgraph/pregel/main.py and adds source-level tests in libs/langgraph/tests/test_stream_namespaces.py.
Claim Not Supported: authored tests actually passed in this inspection, all nested graphs or runtimes preserve events, child namespace changed to the calling node, host deployment, or all telemetry is delivered exactly once.
Confidence: HIGH_FOR_PATCH_SOURCE / UNKNOWN_FOR_INSTALLED_RUNTIME
Limitations: the patch explicitly preserves the child's existing namespace rather than reparenting it. Different thread or checkpoint configuration and caller subgraphs choice are material scope conditions.

## RAW_SIGNAL_LOG
Signal ID: SIG-20261114-H01
Signal: CHILD_GRAPH_STREAM_CALLBACK_SCOPE_DEPENDS_ON_SUBGRAPHS_FLAG
Source IDs: SRC-20261114-H01
What Changed: source now distinguishes an explicitly requested subgraph event stream from accidental child events being mistaken for caller-owned events.
Why It May Matter: runtime event observability and trace attribution depend on callback propagation, thread boundaries and event namespaces, not merely whether the child computation ran.
Evidence Tier: FIRST_PARTY_IMPLEMENTATION_PATCH
Confidence: SOURCE_SUPPORTED / RUNTIME_UNKNOWN
Uncertainty: exact installed release, independent test result, configuration variants, event delivery under failure and production application.
Freshness: COMMITTED_2026-11-14_UTC
Possible Noise: specific LangGraph Python callback/streaming path, not a normative cross-framework API requirement.
Needs H2 Verification: YES

## EVIDENCE_DELTA
- NEW_EVIDENCE: dated first-party diff restores messages/tools handler propagation for the requested subgraphs=True case for child graphs invoked outside the caller task.
- CORRECTED_INTERPRETATION: absence of tokens/tool callbacks in a parent stream is not proof that the child graph did not execute; a returned child event is not automatically a parent-owned event.
- UNCHANGED_BOUNDARY: SOURCE_DIFF != RUNTIME_PASS != HOST_ADOPTION; authored regression tests are not executed checks or independent corroboration.
- NEW_COUNTEREVIDENCE: subgraphs=False intentionally suppresses outside-task child callbacks; preserving the child namespace does not convert it into the caller's node namespace.
- UNKNOWN_RETAINED: runtime version, executed tests, error/retry behavior, target framework applicability and production telemetry.
- NEXT_RETEST_CONDITION: pin the exact source revision and two caller modes; run child with own thread/config, record emitted messages/tools and namespaces alongside child-side effect/step receipts; capture commands, exits and counterexample configurations.

## NEXT_HANDOFF
- H2 may only process this exact 2026-11-14 H1 after its Draft PR has been reviewed, merged and become visible on current main, then independently reopen source, challenge config-specific boundaries and record its own source/check evidence.
- No H3/H4 decision, monthly memory promotion, NEXUS/Parallax/host adoption recommendation, policy, scheduler or workflow change is made.

## BOUNDARY_CHECK
- One new Horizon-only Daily artifact; historical H1-H6 records remain unchanged.
- No host, NEXUS, Parallax, actions, configuration or memory write.
- No unrun test claimed as PASS and no private control-plane prompt exposed.
