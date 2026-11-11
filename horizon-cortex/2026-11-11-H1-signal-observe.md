# H1 Daily Signal Observe — 2026-11-11

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-11
Logical Timezone: Asia/Shanghai
Execution Time UTC: 2026-11-11 / EXACT_TIME_NOT_CAPTURED
Execution Time Asia/Shanghai: 2026-11-11 / EXACT_TIME_NOT_CAPTURED
Agent: GPT-6 / GPT_NATIVE / NOT_JULES_REPLAY
Producer Identity: HUMAN_REQUESTED_GPT_NATIVE
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE / NEW_PROSPECTIVE_RESEARCH
Base Main SHA: 97fa31008fe6443d66cc4fc12fbfc3508856efaa
Run Identity: welcome-to-github/horizon/H1/2026-11-11/GPT_NATIVE/97fa31008fe6443d66cc4fc12fbfc3508856efaa/adk-openapi-required-source-01
Network Status: GITHUB_ORIGINAL_COMMIT_AND_PATCH_READ
Source Status: FIRST_PARTY_CODE_AND_AUTHORED_TEST_DIFF / RUNTIME_NOT_EXECUTED
Task Status: SUCCESS / SOURCE_BOUNDED_OBSERVATION
Source Identity: google/adk-python@e5ffe9c9daed15b952e83d5d778fe89c251f1d48
Source Authority For Claim: FIRST_PARTY_COMMITTED_SOURCE_AND_AUTHORED_REGRESSION_TEST
Independent Verification: SOURCE_DIFF_INSPECTED / REGRESSION_TESTS_NOT_EXECUTED
Evidence Upgrade Basis: NEW_DISTINCT_UPSTREAM_PATCH / NO_INDEPENDENT_RUNTIME_CORROBORATION
Host Applicability: UNKNOWN / HOST_NOT_ASSESSED
Original Execution Status: GPT_NATIVE_2026-11-11 / NOT_JULES
Current Path Status: PROPOSED_BRANCH_ARTIFACT / MAIN_VISIBILITY_PENDING
Write Scope: horizon-cortex/2026-11-11-H1-signal-observe.md
Boundary Violation: NO

## INPUT_RECORD
- The source-base for this new H1 record is merged main 97fa31008fe6443d66cc4fc12fbfc3508856efaa. The current Horizon evidence policy, prior 2026-11-10 H1, closed 2026-W45 H4 and 2026-10 H6 records were read for bounded continuity. No same-day H2 was read.
- Search/verification focus: exact first-party Google ADK OpenAPI tool schema serialization change, its committed regression fixtures, and distinctions among source patch, tests authored, tests executed, package release and deployed behavior.
- The 2026-11-10 H1 concerns evaluator session-details retrieval identity. Today's patch concerns the required-parameter flag when serializing and reconstructing an API tool, a different code path and failure predicate.
- W46 is still open. October H6 retains its own dated closure interpretation; November H5/H6 final are NOT_DUE.
- Unverified themes: other SDK releases, independently executed integration fixtures, tool-call effects and host adoption. These are not presented as verified negatives.

## EXTERNAL_SOURCE_RECORDS
### SRC-20261111-H01 — ADK RestApiTool parameter required preservation
Source ID: SRC-20261111-H01
Title: fix: preserve required flag in RestApiTool serialization
Publisher: google/adk-python
URL: https://github.com/google/adk-python/commit/e5ffe9c9daed15b952e83d5d778fe89c251f1d48
Related upstream PR: https://github.com/google/adk-python/pull/8067
Published or Updated Date: 2026-11-11T08:18:48Z (commit timestamp; NOT tagged SDK release date)
Date Checked: 2026-11-11 Asia/Shanghai
Source Type: ORIGINAL_GITHUB_COMMIT_AND_CHANGED_TEST_SOURCE
Evidence Tier: PRIMARY_FOR_SOURCE_IMPLEMENTATION_CHANGE / NOT_RUNTIME_RESULT
Access Status: COMMIT_MESSAGE_AND_ALL_THREE_CHANGED_FILE_PATCHES_READ
Independent Source: ONE_GOOGLE_ADK_COMMIT_LINEAGE / TEST_SOURCE_NOT_INDEPENDENT
Claim Supported: ApiParameter custom serializer now includes the stored required field. Authored tests check all stored serialization fields except recomputed derived fields, and verify that a RestApiTool reloaded from parsed operation JSON retains id and tenant as required parameters while limit is optional.
Claim Not Supported: the authored tests passed, every OpenAPI schema is handled, existing generated tools are migrated, a tagged release contains the patch, production tools enforce all required parameters, or Welcome uses this ADK code.
Confidence: HIGH_FOR_COMMITTED_SOURCE_DIFF / UNKNOWN_FOR_EXECUTED_EFFECT
Relevance: tool schema contract preservation across serialization/deserialization and action input validation.
Limitations: a code patch and new tests provide an intended behavior and a falsifiable implementation claim, not an independently observed runtime receipt.

## RAW_SIGNAL_LOG
### SIG-20261111-H01 — TOOL_PARAMETER_REQUIRED_FLAG_ROUNDTRIP
Signal ID: SIG-20261111-H01
Signal: ADK changed the ApiParameter serialization surface to preserve required metadata through RestApiTool parsed-operation reconstruction.
Source IDs: SRC-20261111-H01
What Changed: The custom serialization dictionary gained required: self.required in src/google/adk/tools/openapi_tool/common/common.py. Authored test cases cover mandatory path/query parameters and optional query parameters after from_parsed_operation_str.
Why It May Matter: Loss of required metadata at an intermediate representation boundary can alter which arguments an agent-facing tool schema declares mandatory. Schema generation, caller input validation and the actual downstream API result remain distinct predicates.
Evidence Tier: FIRST_PARTY_IMPLEMENTATION_PATCH_AND_TEST_DESIGN
Confidence: HIGH_FOR_DIFF / ACTUAL_REPLAY_NOT_VERIFIED
Uncertainty: behavior before/after in a pinned runner, tagged release identity, path coverage outside the authored fixtures, external API enforcement and host dependency state.
Freshness: 2026-11-11T08:18:48Z upstream commit is new relative to 2026-11-10 H1, not a repackaged earlier observation.
Possible Noise: One SDK serialization correction does not imply protocol-wide failure prevalence, general adoption or a newly validated framework-wide reliability score.
Needs H2 Verification: YES. Reconstruct a three-parameter operation before and after the exact commit, check serialized required set and both valid/invalid tool-call behavior, and retain code revision plus actual command/exit/output receipts.
Host Repository Change: NO

## EVIDENCE_DELTA
- NEW_EVIDENCE: the exact upstream commit added required to a custom ApiParameter serializer and authored negative/positive roundtrip fixture cases.
- CORRECTED_INTERPRETATION: tool schema availability alone is not proof that the required/optional argument contract survived a serialization boundary.
- UNCHANGED_BOUNDARY: COMMITTED_PATCH != TEST_EXECUTION != RELEASED_PACKAGE != DEPLOYED_TOOL_EFFECT != WELCOME_HOST_ADOPTION.
- NEW_COUNTEREVIDENCE: the pre-patch custom serializer omitted required even while the model stored that field; metadata presence in memory did not guarantee reconstructed tool schema preservation.
- UNKNOWN_RETAINED: measured runtime behavior, release tag, real external service responses, any host integration and other serialization paths.
- NEXT_RETEST_CONDITION: pin parent and patched source revisions, run serialized JSON roundtrip with required path/query and optional query controls, compare emitted schema and instrumented call-validation result, and record command, environment, stdout/stderr and exit code.

## NEXT_HANDOFF
- H2 for logical 2026-11-11 must first observe this exact H1 artifact merged into a refreshed authoritative main; an unmerged PR is not upstream availability.
- H2 should preserve one-source lineage, seek independent runnable evidence and test version/deployment counterconditions rather than treating the same authored fixtures as a second independent source.
- W46 Weekly and November natural-month final remain NOT_DUE. No host, NEXUS, Parallax or governance action follows from this H1 observation.

## BOUNDARY_CHECK
- This native H1 delivery proposes only the canonical 2026-11-11 Horizon file. No prior H1–H6 body, host, NEXUS, Parallax, source code, Actions, archives or monthly memory is modified.
- Horizon structural checker: NOT_EXECUTED at authoring. Upstream authored tests: NOT_EXECUTED. Live SDK/host integration: NOT_EXECUTED. Claim-specific source patch: READ.
- This is prospective GPT Native research, not a Jules replay or a recovery/maintenance audit, and it does not disclose private producer control text.
- Boundary Violation: NO
