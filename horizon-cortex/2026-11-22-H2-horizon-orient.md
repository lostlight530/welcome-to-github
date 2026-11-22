# H2 Daily Orient — 2026-11-22 / nullable schema transport is not executable tool assurance

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-22
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 36c75046b14392f4cf544fb016dcf61b9e11f8b7
Run Identity: welcome-to-github/H2/2026-11-22/GPT_NATIVE/36c7504/counterevidence-orient-01
Source Identity: google/adk-python PR #8283, head eb2c975e9e495e641a1063749fc68dc09e4241b9
Source Authority For Claim: FIRST_PARTY_OPEN_PATCH_AND_AUTHOR_TESTS / SAME_ISSUER_AS_UPSTREAM
Independent Verification: UPSTREAM_MERGE_SHA_be51d1a113604089900d4fa18f9498ca1ba847a7 / EXACT_MAIN_BLOB_04d33e9385b27d4020e012ec709b23e450dfed4f / NO_INDEPENDENT_ADK_SDK_REPRODUCTION
Host Applicability: UNKNOWN / NO_HOST_DEPLOYMENT_OR_EXTERNAL_EFFECT_RECEIPT
Evidence Upgrade Basis: PREDECESSOR_DEPENDENCY_SATISFIED / COUNTEREXAMPLE_NARROWING / NO_ADOPTION_PROMOTION
Original Execution Status: GITHUB_SOURCE_AND_MERGED_PREDECESSOR_REVIEW / ADK_E2E_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_H2_ORIENTATION / NO_HOST_DECISION
Write Scope: horizon-cortex/2026-11-22-H2-horizon-orient.md
Boundary Violation: NO

## INPUT_RECORD
- Current fresh main after independent A1: `36c75046b14392f4cf544fb016dcf61b9e11f8b7`, original Native upstream PR merge commit `be51d1a113604089900d4fa18f9498ca1ba847a7` was observed before this task
- Actual `horizon-cortex/2026-11-22-H1-signal-observe.md` on current main reopened with Git blob `04d33e9385b27d4020e012ec709b23e450dfed4f` exactly matching the original upstream artifact
- Current evidence policy: `horizon-cortex/EVIDENCE_POLICY.md` blob `060eaff65437bda48718a9703477815c574a9846`
- Upstream first-party source: google/adk-python PR #8283, head eb2c975e9e495e641a1063749fc68dc09e4241b9, OPEN / NOT_MERGED at recheck; an unmerged patch is not a released package
- Source patch and authored tests refer to one upstream issuer; following H1/A1 is not independent corroboration
- Previous day and closed weekly records remain historical; Nov22's novel source is not a separate second daily signal

## SIGNAL_CLASSIFICATION
Signal ID: SIG-20261122-H01
Layer: ADK tool definition -> JSON Schema wire -> MCP client acceptance -> FunctionTool runtime -> host effect
Source classification: OPEN_PROPOSED_CONVERTER_PATCH; upstream patch and tests inspected, SDK converter and real MCP transport NOT_EXECUTED here
Scientific disposition: bounded schema-dialect semantics confirmed with a standalone jsonschema control; no actual ADK converter/host tool call validated
Host applicability: UNKNOWN; NEXUS adopting this Google ADK export path NOT_OBSERVED

## ORIENTATION_NOTES
- The H1 limited control executed `jsonschema.Draft202012Validator` on values (None, 'rice', 7): provider dialect `{type:string,nullable:true}` accepts (false,true,false); standards-compatible `anyOf` accepts (true,true,false). This is one minimal independent dialect control, not a vendor SDK regression
- H2 did not rerun a second distinct validator execution and does not double-count H1 experiment, despite independent readback of its result
- Source patch recurses over schema-bearing positions such as properties/items/allOf/anyOf/$defs while avoiding rewriting default/example user data; that is patch intent, not independently proved converter coverage
- Counterexample C1 (NOT_EXECUTED): nested `nullable` value inside an ordinary data default is rewritten as schema, corrupting user-specified default even though minimal union control passes
- Counterexample C2 (NOT_EXECUTED): `anyOf` transformation with enum/oneOf/$ref changes the non-null acceptance set; a quick happy-path validator pass is insufficient
- Counterexample C3 (NOT_EXECUTED): MCP client accepts `null` from exported tool schema, but downstream FunctionTool argument preprocessing or permission broker rejects/changes it; schema PASS != executable effect
- Counterexample C4 (NOT_EXECUTED): host never uses this bridge; upstream converter fix supplies no NEXUS migration requirement
- Positive P1 (NOT_EXECUTED): actual FunctionTool with nested nullable elements round-trips through pinned MCP SDK versions, with post-call parameter identity and no extra unexpected values
- Scope: One original H1 first-party PR patch, one local dialect experiment; no independent issuer multiplication, production adoption, host-code modification or source release

## NO_DECISION_SECTION
Decision: NO_DECISION / HOST_CHANGE_NOT_AUTHORIZED; only observe upstream patch readiness and preserve source version
Risk of premature promotion: schema acceptance could be mistaken for authorized invocation or durable user-intended external effect

## NEXT_HANDOFF
- Future 2026-W47 H3 input only when the full ISO week is closed and this H2 has actually been merged; no early week FINAL
- Future H5/H6 November Monthly remains NOT_DUE until natural month close and evidence gates pass
- H1 same-day original merger and exact blob are already confirmed; H2's own delivery and main retention remain separate future receipts

## EVIDENCE_DELTA
- NEW_EVIDENCE: exact merged same-day upstream task identity and source blob, followed by independent counterevidence-focused orientation
- CORRECTED_INTERPRETATION: same publisher's source/tests cannot be transformed into independent verification by a second research phase
- UNCHANGED_BOUNDARY: external proposal != released SDK != host adoption != local incident/effect; Native != independent maintenance
- NEW_COUNTEREVIDENCE: intermediate contract, aliasing/concurrency or runtime effect gaps can invalidate broader guarantees inferred from patch/code shape
- UNKNOWN_RETAINED: production use, broad SDK regression, local host behavior, release status, verified impact and independent external effect
- NEXT_RETEST_CONDITION: immutable before/after SDK test, source-version-pinned real invocation, exact arg/tool identity and authoritative effect receipt
Counterevidence Gate: PASS_FOR_BOUNDED_SOURCE_ORIENTATION / DENY_CLAIM_PROMOTION

## BOUNDARY_CHECK
- Scope only this canonical Native H2/A2; historical Jules, Parallax/Ballast, Independent A1/A2, governance, host kernel and private scheduler unchanged
- GitHub source, merged upstream artifact and policy were read; complete local checker/native SDK E2E and host runtime NOT_EXECUTED
- Independent human review and own PR merge/main retention NOT_OBSERVED at authoring; no automatic role-level PASS
Host Repository Change: NO
Local test status: STANDALONE_JSON_SCHEMA_CONTROL_INHERITED_FROM_H1 / NOT_NEW_H2_EXECUTION
