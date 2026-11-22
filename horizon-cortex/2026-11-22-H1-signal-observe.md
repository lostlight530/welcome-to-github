# H1 Daily Signal Observe — 2026-11-22 / nullable tool input crosses GenAI-to-MCP schema dialects

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-22
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 5125ac2fa0ade5072a12d53c66ce77f8402ebe16
Run Identity: welcome-to-github/horizon/H1/2026-11-22/GPT_NATIVE/5125ac2/mcp-nullable-schema-01
Source Identity: google/adk-python PR #8283 head eb2c975e9e495e641a1063749fc68dc09e4241b9
Source Authority For Claim: FIRST_PARTY_OPEN_PR_IMPLEMENTATION_AND_TEST_DIFF
Independent Verification: UPSTREAM_PR_PATCH_INSPECTED_PLUS_STANDALONE_JSONSCHEMA_DIALECT_CONTROL / UPSTREAM_ADK_TESTS_NOT_REPRODUCED
Host Applicability: UNKNOWN / NO_NEXUS_MCP_EXPORT_DEPLOYMENT_OBSERVED
Evidence Upgrade Basis: SOURCE_PATCH_AND_INDEPENDENT_DIALECT_SEMANTICS_ONLY / NO_UPSTREAM_RUN
Original Execution Status: SOURCE_REVIEW_AND_BOUNDED_STANDALONE_SCHEMA_CONTROL_EXECUTED / UPSTREAM_TESTS_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_EXTERNAL_IMPLEMENTATION_PROPOSAL / RELEASE_UNVERIFIED
Write Scope: horizon-cortex/2026-11-22-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Fresh `main` SHA `5125ac2fa0ade5072a12d53c66ce77f8402ebe16`, current `horizon-cortex/EVIDENCE_POLICY.md` blob `060eaff65437bda48718a9703477815c574a9846`, Horizon README blob `fb6a2d828764571af66caf94259f67f16b1a8b0d`.
- 2026-11-21 H1/H2, 2026-W46 H3/H4 and October H5/H6 were found retained on main. 2026-W47 has not closed; November Monthly remains `NOT_DUE`. No open Welcome PR or matching active 2026-11-22 branch found at preflight.
- Yesterday examined proposed Redis session approval checkpoint recovery; today's distinct signal concerns **tool argument JSON Schema wire compatibility**, not durable external effects.
- A local `git ls-remote https://github.com/lostlight530/welcome-to-github.git refs/heads/main` failed exit `128`, stdout empty, stderr `Could not resolve host: github.com`. Full host checkout and upstream ADK test suite were not available.

## EXTERNAL_SOURCE_RECORDS
Source ID: SRC-20261122-H01
URL: https://github.com/google/adk-python/pull/8283
Title: fix(mcp): preserve nullable arguments in exported JSON schemas
Publisher: google/adk-python contributor PR, not a formal release or independent auditor
Source Version: OPEN_UNMERGED_PR_HEAD `eb2c975e9e495e641a1063749fc68dc09e4241b9`
Source Publication: created 2026-11-21T09:56:53Z, observed 2026-11-22 Asia/Shanghai
Pinned implementation: https://github.com/google/adk-python/blob/eb2c975e9e495e641a1063749fc68dc09e4241b9/src/google/adk/tools/mcp_tool/conversion_utils.py
Pinned tests: https://github.com/google/adk-python/blob/eb2c975e9e495e641a1063749fc68dc09e4241b9/tests/unittests/tools/mcp_tool/test_conversion_utils.py
Source Access: connected GitHub PR metadata, two exact code/test patches; primary for proposed conversion behavior, not a released SDK
Source Authority: FIRST_PARTY_PATCH_FOR_ADK_MCP_EXPORT / NOT_GENERAL_MCP_CONFORMANCE_PROOF
Evidence Tier: CODE_PATCH_INSPECTED / STANDALONE_DIALECT_CONTROL_ONLY
Confidence: HIGH_FOR_PROPOSED_TRANSFORM_SHAPE / INDEPENDENT_ADK_E2E_UNKNOWN
Uncertainty: upstream merge/release, complete SDK compatibility, host use and independently reproduced converter effects unknown.

## RAW_SIGNAL_LOG
Signal ID: SIG-20261122-H01
- The upstream patch reports that exporting `FunctionTool` with a nullable input may produce `{"type":"string","nullable":true}` on the MCP tool `inputSchema` wire. Draft 2020-12 JSON Schema does not confer nullable type semantics on that proprietary key; a `null` argument remains invalid if the type is `string`.
- Proposed transformation wraps a nullable schema as `{"anyOf":[original_nonnullable_schema,{"type":"null"}]}`, recursively over properties, array items, definitions and compound schema keywords. This preserves non-null enum/type restrictions, defaults and input declaration identity (as the authored test asserts).
- Implementation patch touches `adk_to_mcp_tool_type`, adds `_convert_nullable_schema`, and adjusts `gemini_to_json_schema`; two code/test files changed. `anyOf` is a union at the wire schema layer, not tool authorization or guaranteed execution.
- The contributor reports `641` passing tests using MCP SDK 2.3.0 and `641` using SDK 1.30.0, plus four local JSON wire round trips. These are **AUTHOR_REPORTED_TESTS**, not executed by this H1.
- Author regression examples use `query: null`, nullable array elements, a non-null string control, and invalid numeric values. The declared schema and wire serialization are distinct proof surfaces.
- Direct bounded local control (independent **JSON Schema dialect**, not ADK): Python 3.13.5 with `jsonschema 4.26.0`, `Draft202012Validator`; validated three values `[None,"rice",7]` against (a) `{"type":"string","nullable":true}` and (b) `{"anyOf":[{"type":"string"},{"type":"null"}]}`. Actual command: `python3 - <<'PY' ... Draft202012Validator(schema).is_valid(v) ... PY`; exit `0`; stderr only a `jsonschema.__version__` deprecation warning. Stdout records original acceptance `[false,true,false]`, proposed `[true,true,false]`. This demonstrates the isolated dialect discrepancy, **not** that the ADK converter or MCP client was executed.
- A permissive transformation that incorrectly drops the original non-null constraints could create false positives (e.g. accepting numeric `7` where only `str|null` is legal). Conversely, preserving `nullable:true` as a no-op on the wire creates false rejection of a valid declared optional argument.
- This is a specific source-verified proposed bridge between Google GenAI schema and MCP JSON Schema; it is not a new MCP spec release, proof of production compatibility, security hardening, or adoption by NEXUS.
- Source lineage: PR patch, authored tests, author-reported test counts and issue references are one upstream publisher, not four independent confirmations.

## Controls, counterevidence and applicability
- Positive wire control (PARTIAL_EXECUTED_STANDALONE_SCHEMA): `null` accepted by `anyOf` and a string remains accepted, as predicted by JSON Schema semantics.
- Negative wire control (PARTIAL_EXECUTED_STANDALONE_SCHEMA): numeric `7` remains rejected; guards against overbroad loss of type constraints in the minimal schema case.
- Negative ADK control (NOT_EXECUTED): nested `properties/items/anyOf/$defs` containing nullable types with `default` payloads that incidentally contain a key named `nullable`; wrapper must not rewrite data blobs.
- Negative tool-run control (NOT_EXECUTED): client accepts nullable wire schema but runtime `FunctionTool` argument preprocessing mishandles `None` or nested model values; `SCHEMA_ACCEPTED != FUNCTION_CALLED_CORRECTLY`.
- Negative host control (NOT_EXECUTED): use a tool named in a document without NEXUS using that converter; `UPSTREAM_PATCH != HOST_ADOPTED`.
- Applicability: `UNKNOWN`. No implementation search or deployment evidence showed Welcome NEXUS exposing Google ADK FunctionTool through this MCP conversion path.

## EVIDENCE_DELTA
- NEW_EVIDENCE: exact first-party converter patch and tests plus locally executed Draft202012 minimal acceptance matrix distinguish nullable declaration from JSON wire behavior.
- CORRECTED_INTERPRETATION: `nullable: true` in a provider dialect is not itself a standard JSON Schema `null` alternative; convert without relaxing existing non-null constraints.
- UNCHANGED_BOUNDARY: SOURCE_FOUND != SOURCE_RELEASED != INDEPENDENT_ADK_TESTED != HOST_DEPLOYED; local dialect test is not upstream E2E or a full formal conformance test.
- NEW_COUNTEREVIDENCE: data-preserving recursive transformation and nested union/enum types need distinct negative fixtures; otherwise the patch may introduce a new compatibility defect.
- UNKNOWN_RETAINED: upstream release, full schema dialect coverage, MCP transport runtime, host adoption, external reliability effects and longitudinal ecosystem uptake.
- NEXT_RETEST_CONDITION: on immutable ADK PR revision, run both converter modes and validate actual exported MCP schema via pinned client versions, exercise nested null/enum/array/default fixtures, invoke the real FunctionTool, and inspect NEXUS adoption independently.
- Counterevidence Gate: LIMITED_DIALECT_SEMANTICS_CONFIRMED / CONVERTER_E2E_NOT_REPRODUCED / HOST_CLAIM_NOT_PROMOTED.

## NEXT_HANDOFF
- H2 must wait for H1 original PR actual merge and current `main` reread with this file's blob SHA. Then recheck upstream PR head/status and independently evaluate whether the patch's recursive conversion can preserve schema meaning under unions, refs and defaults.
- Until the exact merge gate: `welcome/horizon/H2/2026-11-22 = BLOCKED_UPSTREAM_NOT_MERGED`; no same-day H2 artifact or execution credit created.
- `2026-W47` H3/H4 and November H5/H6: `NOT_DUE` until their owning period closes.

## BOUNDARY_CHECK
- Only the Horizon H1 canonical research path is proposed. NEXUS implementation, Parallax, Independent A1/A2, governance, Jules artifacts and scheduler remain unchanged.
- `python3 horizon-cortex/check.py horizon-cortex/2026-11-22-H1-signal-observe.md` was `NOT_EXECUTED` without complete checkout; structural success and independent claim validation are not asserted.
- Draft PR delivery requires Human Maintainer review before merge; H2 will be a separate post-merge dependency step.
