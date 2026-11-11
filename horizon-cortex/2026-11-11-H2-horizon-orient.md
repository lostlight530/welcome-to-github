# H2 Daily Horizon Orient — 2026-11-11

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-11
Logical Timezone: Asia/Shanghai
Execution Time UTC: 2026-11-11 / EXACT_TIME_NOT_CAPTURED
Agent: GPT-6 / GPT_NATIVE / NOT_JULES_REPLAY
Producer Identity: HUMAN_REQUESTED_GPT_NATIVE
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 042deef8213b42c9dd8c3f244e3f3f98e29cfb88
Run Identity: welcome-to-github/horizon/H2/2026-11-11/GPT_NATIVE/042deef8213b42c9dd8c3f244e3f3f98e29cfb88/adk-required-schema-orient-01
Upstream H1: horizon-cortex/2026-11-11-H1-signal-observe.md
Upstream H1 Blob SHA: 0d30fd3e395a306aa96daf2b03adebd6390cdcee
Upstream H1 Original PR: https://github.com/lostlight530/welcome-to-github/pull/958
Upstream H1 Forward Correction PR: https://github.com/lostlight530/welcome-to-github/pull/959
Input Status: SAME_DATE_H1_MERGED_MAIN_VISIBLE_AND_PROVENANCE_CORRECTED
Source Identity: google/adk-python@e5ffe9c9daed15b952e83d5d778fe89c251f1d48
Source Authority For Claim: FIRST_PARTY_SOURCE_AND_IMPLEMENTATION_FOR_ADK_SERIALIZATION
Independent Verification: DISTINCT_SOURCE_CODE_CONTEXT_REINSPECTED / NO_EXTERNAL_EXECUTABLE_REPLAY
Evidence Upgrade Basis: MORE_PRECISE_ROUNDTRIP_AND_CONSUMER_BOUNDARY / NO_NEW_INDEPENDENT_SOURCE
Original Execution Status: GPT_NATIVE_2026-11-11_NEW_ORIENTATION / NOT_JULES_REPLAY
Current Path Status: PROPOSED_REVIEW_BRANCH / MERGE_PENDING_AT_AUTHORING
Task Status: SOURCE_BOUNDED_ORIENTATION / NO_HOST_DECISION
Network Status: UPSTREAM_GITHUB_IMPLEMENTATION_SOURCE_AND_TEST_PATCH_READ
Host Applicability: UNKNOWN / NO_WELCOME_HOST_ADK_DEPENDENCY_OR_EXECUTION_CHECK
Host Repository Change: NO
Write Scope: horizon-cortex/2026-11-11-H2-horizon-orient.md
Boundary Violation: NO

## INPUT_RECORD
- Fresh merged-main read at 042deef8213b42c9dd8c3f244e3f3f98e29cfb88 after H1 #958 and separate scoped provenance correction #959 merged. H1 source blob on this exact main: 0d30fd3e395a306aa96daf2b03adebd6390cdcee.
- H1 recorded Google's committed 2026-11-11 fix for ApiParameter required metadata serialization, not a new SDK release, downstream runtime fixture or Welcome implementation.
- This H2 reread the original upstream commit diff and the patched source implementation of `ApiParameter` and `RestApiTool.from_parsed_operation_str` at the same pinned revision. These belong to the SAME original publisher/code lineage and therefore do not create independent corroboration.
- The required-flag change is distinct from the Nov10 evaluator session-details identity fix. 2026-W45 is already closed, W46 still open; November H5/H6 final NOT_DUE.
- No publisher test, independent Python runner, real API call, host integration, or new schema contract was executed in this H2.

## SOURCE_VERIFICATION_RECORDS
### SRC-20261111-H2-01 — required metadata at the serialization boundary
- Original upstream commit: https://github.com/google/adk-python/commit/e5ffe9c9daed15b952e83d5d778fe89c251f1d48 ; 2026-11-11T08:18:48Z upstream commit timestamp, not package publication date.
- Exact source: `src/google/adk/tools/openapi_tool/common/common.py`. `ApiParameter` declares `required: bool = False` and a custom Pydantic `@model_serializer`, whose mapping now includes `'required': self.required`.
- The serializer also conditionally drops `None` fields for `exclude_none`; `required` is a boolean and therefore this specific omission path does not apply to either True or False.
- Changed authored unit tests cover serializable stored fields (other than derived `type_value` and `type_hint`), and a reconstructed three-parameter operation with required `id` and `tenant`, optional `limit`. Their expected schema has `required=["id","tenant"]`. Tests READ, not executed.
- The code-level H1 claim is corroborated as an implementation change by directly inspecting implementation and authored tests at the same pinned commit; this is **source inspection**, not two independent empirical sources.

### SRC-20261111-H2-02 — reconstruction and downstream capability limits
- The exact pinned `RestApiTool.from_parsed_operation_str` source parses `ParsedOperation.model_validate_json(...)` before calling `from_parsed_operation`; the tool declaration draws its schema from `self._operation_parser.get_json_schema()`, with feature-dependent JSON-schema or Gemini-schema representation.
- This gives a concrete serialization → parsed operation → schema declaration chain for a **bounded test hypothesis**, but there is no H2 execution proving every downstream declaration, client or server enforces the required arguments as intended.
- Countercondition 1: a runtime already holding the original in-memory `ApiParameter` object before serialization may not exhibit the same loss, so “all ADK tools failed required validation” would be unsupported.
- Countercondition 2: a correctly retained tool schema does not prove the model supplies mandatory values or that an HTTP server validates them. Schema declaration, tool-call argument admission and external API effect must be separately checked.
- Countercondition 3: the authored three-parameter regression covers a specific parsed-operation pathway, not arbitrary OpenAPI composition, auth, conditional fields, optional path handling or prior saved serialized objects.
- Countercondition 4: no tagged release, dependency lock, installed SDK revision, schema-feature-flag setting or Welcome host adoption was checked. The upstream source revision is not the deployed version.
- Countercondition 5: including `required=false` in the serialization is not evidence of an authorization decision or effect-time tool permission; requiredness is an input-shape requirement, not an ALLOW/DENY security policy.

## SIGNAL_CLASSIFICATION
Signal ID: SIG-20261111-H01
Upstream H1 Signal: TOOL_PARAMETER_REQUIRED_FLAG_ROUNDTRIP
Classification: FIRST_PARTY_CODE_CORRECTION / TOOL_SCHEMA_METADATA_PRESERVATION / HORIZON_WATCHLIST
Evidence Status: SOURCE_DIFF_SUPPORTED / AUTHOR_TEST_DESIGN_READ / INDEPENDENT_EXECUTION_NOT_OBSERVED
Independent Sources Added: ZERO; same pinned Google ADK commit and authored tests
Claim Upgrade: NO_RUNTIME_UPGRADE; the interpretation is narrowed to the specific serializer and parsed-operation chain
Host Applicability: UNKNOWN; neither local dependency usage nor installed runtime confirmed
Confidence: HIGH_FOR_DIFF_AND_READ_CODE_PATH / UNKNOWN_FOR_DEPLOYED_EFFECT

## ORIENTATION_NOTES
- Research priority: the requiredness contract must survive representation changes, but correctness requires a pinned input/metadata roundtrip test, explicit raw schema comparison and an independently checked invocation outcome.
- Relevant axes: canonical source revision, original API parameter definition, intermediate serialized JSON, reconstructed `ParsedOperation`, emitted tool declaration and effect-time call receipt.
- Avoid conflating metadata completeness with source provenance, action permission, model correctness or end-to-end tool success.
- Even if a generated function declaration contains the two required fields, it does not prove a blocked invalid call, successful authorized effect, or a stable cross-SDK compatibility promise.

## NO_DECISION_SECTION
Decision: NO_DECISION / NO_HOST_MIGRATION_OR_SCHEMA_POLICY_CHANGE
Reason: one first-party patch and authored regression tests provide a scoped implementation observation but no independent runner result, installed version proof, host applicability or maintainer-approved architecture action.
Evidence retained: exact upstream commit, specific changed field, independent source-inspection boundary, negative control conditions, merged same-date H1 identity.
Not inferred: Welcome NEXUS ingestion, Parallax research credit, a host dependency security incident, broad SDK adoption or a normative protocol update.

## EVIDENCE_DELTA
- NEW_EVIDENCE: checked the current `ApiParameter` serializer and the `RestApiTool.from_parsed_operation_str`/declaration consumer path, refining the H1 contract boundary.
- CORRECTED_INTERPRETATION: requiredness survives this specified serialization pathway in committed code; the result still does not certify runtime invocation validation or service-side effects.
- UNCHANGED_BOUNDARY: PATCH_PRESENT != TEST_PASS != RELEASED_PACKAGE != HOST_DEPLOYMENT; H2_SOURCE_REVIEW != SECOND_INDEPENDENT_SOURCE.
- NEW_COUNTEREVIDENCE: in-memory no-roundtrip consumers, feature-flagged schema representation, malformed calls or backend differences can produce different outcomes despite this patch.
- UNKNOWN_RETAINED: exact release, SDK test execution, runtime tool declaration across feature flags, API effect-time enforcement, host installed revision, end-to-end behavior.
- NEXT_RETEST_CONDITION: pin commit parent and patched revision; construct required path/query plus optional query fixtures; serialize and reconstruct; compare both declaration formats and invalid-call handling with command, Python/dependency environment, stdout/stderr, exit and tool side-effect receipts.

## NEXT_HANDOFF
- For W46 after its actual closure, H3 may inherit this H1→H2 source lineage once, with no duplicate independent-evidence count. No W46 decision is made here.
- If new independent execution or installed-version evidence appears, record it under a distinct run/source identity with any contradiction; do not silently edit this point-in-time report.
- October records and November Monthly are not changed.

## BOUNDARY_CHECK
- Only the new same-date native H2 record is delivered. Corrected H1 source is an already merged input, not a sibling unmerged proposal. Historical Jules, Host, NEXUS, Parallax, workflow, maintenance, Periodic Audit and governance records unchanged.
- First-party source and authored fixtures: READ. Native Horizon Python checker: NOT_EXECUTED at writing; publisher tests: NOT_EXECUTED; SDK API scenario: NOT_EXECUTED; local host and effect verification: NOT_EXECUTED.
- Original and current producer/delivery states are distinct; no private producer-control content or fabricated validation result.
- Boundary Violation: NO
