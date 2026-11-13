# H1 Daily Signal Observe — 2026-11-13

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-13
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / NOT_JULES_REPLAY
Producer Identity: HUMAN_REQUESTED_GPT_NATIVE
Base Main SHA: df54f5c0de3a505405a661ec9c50c8a233939c12
Run Identity: welcome-to-github/horizon/H1/2026-11-13/GPT_NATIVE/df54f5c0de3a505405a661ec9c50c8a233939c12/adk-nested-session-live-response-01
Execution Time UTC: 2026-11-13 / exact task start not independently captured
Execution Time Asia/Shanghai: 2026-11-13 / exact task start not independently captured
Network Status: OFFICIAL_GITHUB_COMMIT_PATCH_READ
Source Status: FIRST_PARTY_CODE_AND_AUTHORED_TESTS / NOT_EXECUTED
Task Status: SUCCESS / BOUNDED_PRIMARY_SOURCE_OBSERVATION
Repository Inspection: HORIZON_POLICY_AND_PERIOD_IDENTITY_READ
GitHub Actions Inspection: RECENT_METADATA_ONLY / H1_VALIDATOR_NOT_EXECUTED
Write Scope: horizon-cortex/2026-11-13-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Read current merged main and current Horizon evidence policy; five-core preflight found no open PRs. Prior H1/H2, W45 H4 and October H6 were checked for continuity and duplicates only, not inherited as novel evidence.
- First-party discovery checked recent google/adk-python, langgraph, MCP and A2A commits. A2A partner-list updates were not admitted as material runtime changes. Selected two dated implementation diffs, not marketing announcements.
- ISO W46 and November month remain open: H3/H4 and H5/H6 NOT_DUE. Same-date H2 is not input for H1. Host/SDK runtime and code tests NOT_EXECUTED.

## EXTERNAL_SOURCE_RECORDS

### SRC-20261113-H01 — nested AgentTool parent and child identities
Source ID: SRC-20261113-H01
Title: feat(plugins): isolate nested AgentTool state and add response_text_key
Publisher: google/adk-python
Source Identity: google/adk-python@5ce1d0c15af9edef87692f43230bc5bc01103202
URL: https://github.com/google/adk-python/commit/5ce1d0c15af9edef87692f43230bc5bc01103202
Committed At: 2026-11-13T00:55:13Z
Date Checked: 2026-11-13 Asia/Shanghai
Source Type: FIRST_PARTY_COMMIT_IMPLEMENTATION_AND_DOCUMENTATION
Evidence Tier: PRIMARY_FOR_PATCH_MECHANISM / RUNTIME_NOT_VERIFIED
Access Status: ORIGINAL_DIFF_READ
Independent Source: ONE_GOOGLE_ADK_UPSTREAM_LINEAGE
Claim Supported: InvocationContext stores private parent invocation identity for nested AgentTool runs when plugins are included. BigQuery analytics SQL excludes child-session rows carrying attributes.adk.parent_session_id from parent session/turn evaluation, where their tool call/response already appears in parent traces.
Claim Not Supported: custom AgentTool overrides always propagate this metadata; denied attributes columns permit the same filtering; production analytics are complete or deployed by Welcome.
Confidence: HIGH_FOR_COMMITTED_SOURCE / UNKNOWN_FOR_EXECUTION
Limitations: upstream documentation says custom Runner overrides may lack parent attribution and when attributes is denied, child sessions can appear as independent rows. No SQL or integration test was executed here.

### SRC-20261113-H02 — finished tool responses on live connection failure
Source ID: SRC-20261113-H02
Title: fix(live): yield finished tool responses when the live connection fails
Publisher: google/adk-python
Source Identity: google/adk-python@1a0ddabf1b65d49bb814ac1c2b0c06af4a3a57a4
URL: https://github.com/google/adk-python/commit/1a0ddabf1b65d49bb814ac1c2b0c06af4a3a57a4
Committed At: 2026-11-12T22:34:40Z (November 13 Shanghai)
Date Checked: 2026-11-13 Asia/Shanghai
Source Type: FIRST_PARTY_CODE_AND_AUTHORED_REGRESSION_TEST
Evidence Tier: PRIMARY_FOR_CODE_INTENT / EXECUTION_UNKNOWN
Access Status: ORIGINAL_PATCH_AND_TEST_DIFF_READ
Independent Source: DISTINCT_COMMIT / SAME_GOOGLE_ADK_PUBLISHER_FAMILY
Claim Supported: exception path drains already-finished function responses from live queue before rethrowing; newly authored test models a ConnectionClosed after a tool call completes.
Claim Not Supported: authored test was actually run, all in-flight tools finish, connections resume, or already-created tool effects roll back.
Confidence: HIGH_FOR_COMMITTED_CODE / UNKNOWN_FOR_RUNTIME
Limitations: completed queued responses and external tool effects are different objects.

## RAW_SIGNAL_LOG
Signal ID: SIG-20261113-H01
Signal: NESTED_AGENT_TOOL_TELEMETRY_ATTRIBUTION_BOUNDARY
Source IDs: SRC-20261113-H01
What Changed: first-party source now explicitly tracks parent invocation and excludes qualifying child rows from analytics aggregation.
Why It May Matter: nested session counting and evaluation denominators can diverge when parent trace or child metadata is missing.
Evidence Tier: FIRST_PARTY_CODE
Confidence: SOURCE_SUPPORTED / RUNTIME_UNKNOWN
Uncertainty: custom subclasses, attributes denial, query execution, real deployment.
Freshness: 2026-11-13 UTC
Possible Noise: applies to this telemetry integration, not every agent runner.
Needs H2 Verification: YES

Signal ID: SIG-20261113-H02
Signal: FINISHED_RESPONSE_VISIBILITY_AFTER_STREAM_FAILURE
Source IDs: SRC-20261113-H02
What Changed: queue draining on an exception preserves visibility of already finished responses, with authored regression fixture.
Why It May Matter: socket failure is not evidence that the already-executed tool had no effect.
Evidence Tier: FIRST_PARTY_CODE
Confidence: SOURCE_SUPPORTED / RUNTIME_UNKNOWN
Uncertainty: unfinished calls, durable persistence and retry semantics untested.
Freshness: 2026-11-13 Asia/Shanghai
Possible Noise: only one observed live exception path.
Needs H2 Verification: YES

## EVIDENCE_DELTA
- NEW_EVIDENCE: two new dated source-code commits and their exact narrow mechanisms.
- CORRECTED_INTERPRETATION: parent/child session counting is not a count of independent runs; response visibility is not effect identity.
- UNCHANGED_BOUNDARY: SOURCE_DIFF != RUNNER_PASS != HOST_ADOPTION; two commits from one publisher are not independent ecosystem corroboration.
- NEW_COUNTEREVIDENCE: custom nested Runners and denied attributes constrain first mechanism; non-completed tasks and lost external side effects are not repaired by draining a response queue.
- UNKNOWN_RETAINED: independently run tests, version rollout, deployed telemetry, full persistence, host applicability.
- NEXT_RETEST_CONDITION: pin exact code revisions; run nested/custom AgentTool and missing-attributes SQL controls plus deliberate connection-drop tests, capturing invocation IDs, queue receipt identities, side effects and command exits.

## NEXT_HANDOFF
- H2 requires this same-day H1 artifact to be visible on merged main, not merely in an open Draft PR. Reopen source and challenge both mechanisms independently. H3/H4 and H5/H6 NOT_DUE.
- No host, Parallax, NEXUS, Actions or governance decision is authorized by H1.

## BOUNDARY_CHECK
- Read/wrote only Horizon research surface plus original external sources; no host code, workflows or NEXUS state was modified.
- No test execution, independent reproduction, universal adoption, or host incident claimed; no private task or memory exposed.
- No final weekly decision, monthly memory promotion, or Host recommendation.
