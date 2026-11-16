# H2 Daily Horizon Orient — 2026-11-16

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-16
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Source Identity: google/adk-python@c6586f19ab8a2bb8b53e70041633b10858d9902e
Source Authority For Claim: PINNED_FIRST_PARTY_IMPLEMENTATION / SAME_PUBLISHER_LINEAGE
Independent Verification: FRESH_SOURCE_REOPEN_AND_ARGUMENT_SCOPE_REVIEW / NO_INDEPENDENT_SDK_RUN
Host Applicability: UNKNOWN / NO_WELCOME_HOST_INTEGRATION_TEST
Evidence Upgrade Basis: SOURCE_RECHECK_OF_INSERTION_POSITION_AND_LABEL_SANITIZATION / NO_SECOND_INDEPENDENT_ISSUER
Original Execution Status: NEW_GPT_NATIVE_2026_11_16_H2_SOURCE_ORIENTATION / SDK_RUNTIME_NOT_EXECUTED
Current Path Status: DRAFT_PR_PROPOSED / NOT_MERGED
Base Main SHA: c979306c439e8951117036afe7530869a0ebdf8f
Run Identity: welcome-to-github/horizon/H2/2026-11-16/GPT_NATIVE/c979306c439e8951117036afe7530869a0ebdf8f/dynamic-instruction-carrier-counterevidence-01
Task Status: BOUNDED_SOURCE_ORIENTATION_COMPLETED / NO_HOST_DECISION
Network Status: MAIN_H1_AND_UPSTREAM_EXACT_SOURCE_READ / TESTS_NOT_EXECUTED
Host Repository Change: NO
Boundary Violation: NO
Write Scope: horizon-cortex/2026-11-16-H2-horizon-orient.md

## INPUT_RECORD
- Recovered current merged main `c979306c439e8951117036afe7530869a0ebdf8f` after original H1 [PR #999](https://github.com/lostlight530/welcome-to-github/pull/999) merged. The same-day original `horizon-cortex/2026-11-16-H1-signal-observe.md` exists on main as Git blob `ff6226722564889018d383dc2e8e03426c30c2bc`; it was not read from an unmerged side branch.
- Governing `horizon-cortex/EVIDENCE_POLICY.md`, latest merged H1, and the separate closed-week W46 H3 read. Same-day H1 is about the 2026-11-16 main default-on experimental flag; W46 ends Nov15 and does not inherit today's signal.
- Reopened original pinned upstream `google/adk-python@c6586f19ab8a2bb8b53e70041633b10858d9902e` source under the same issuer. The relevant feature change is `default_on: false→true` while stage remains `EXPERIMENTAL`, not a new tool broker or protocol version.
- Independently inspected source paths not fully described by H1: `src/google/adk/flows/llm_flows/context/_contents.py` blob `38b6983f2b5ab5f78b330412d61e964c8905de73` and `prompt/_instructions.py` blob `10d47ef72a97454934a4b3fe4887840f2e96369b`.
- No published wheel, provider request, cache telemetry, explicit A/B model output, security test or host runtime integration was executed. Fresh source reading is new *interpretation*, not a new independent runtime receipt.

## SIGNAL_CLASSIFICATION
Signal ID: SIG-20261116-H01
Input H1: horizon-cortex/2026-11-16-H1-signal-observe.md @ ff6226722564889018d383dc2e8e03426c30c2bc
Class: HARNESS_MODEL_REQUEST_ROLE_AND_ORIGIN_ATTRIBUTION / CODE_SOURCE_SCOPED
Original Code Fact: in enabled feature path, `finalize_dynamic_instructions` creates a labelled `types.Content(role='user', ...)` and inserts it via `_add_instructions_to_user_content`; disabled path instead appends dynamic text via `append_instructions`.
New Source-Specific Narrowing: `_add_instructions_to_user_content` calls `llm_request._insert_transient_user_content` and documents insertion before the last continuous batch of user contents. This is transport placement, not provenance authentication; not the same as appending to the literal current end-user turn.
Origin Labelling: `_label_dynamic_instruction` replaces occurrences of internal BEGIN/END marker strings with `QUOTED_CONTENT_ELIDED` before wrapping the dynamic text. This is marker-spoofing narrowing inside that labeling function, not a proof that arbitrary untrusted tool text cannot issue misleading commands.
Authority Classification: SOURCE_CODE_SUPPORTS_WIRE_CARRIER_AND_MARKER_BOUNDARY / SECURITY_GUARANTEE_NOT_PROVED.
Independent Source Count: ONE_GOOGLE_ADK_LINEAGE. H2 re-opening and citing new modules does not add another publisher or cross-version behavioral reproduction.
Host Applicability: UNKNOWN; no Welcome NEXUS SDK version, feature toggle or tool behavior established.
Promotion: NO_HOST_DECISION / WATCHLIST_ONLY.

## ORIENTATION_NOTES
- Model instruction precedence and attribution are not identical. A `role='user'` carrier injected by the harness may have different provenance from a real person's user turn, despite sharing a wire role. Provenance must be tracked at the harness contract and tool-source identity, not reconstructed from a transport role.
- The upstream commit describes a stable static system prefix as its caching motivation, but provides no observed local Welcome cache hit/miss or token cost distribution. `MODEL_REQUEST_SHAPE_CHANGE != MEASURED_CACHE_BENEFIT`.
- The label routine protects its own text-boundary markers from direct literal marker injection. It does not enforce user/tool permissions, guarantee source truth, or prove all cross-model prompt-injection cases impossible.
- Counterexample 1: tool-contributed misleading instruction text remains model-visible in user-role carrier; a label tells the model how to interpret it but cannot certify an instruction was authorized by the actual end user.
- Counterexample 2: `ADK_DISABLE_DYNAMIC_INSTRUCTION_ROUTING=1` or a feature override enables fallback, so a main-code default is not proof all deployments use the path.
- Counterexample 3: request-specific insertion ordering and model interpretation could vary by provider and run; reading one implementation helper does not prove exact final serialized request or the model's actual adherence.
- Counterexample 4: when no `_dynamic_instructions` are queued, `finalize_dynamic_instructions` returns early; not every inference request changes.
- H2 negative control: compare identical static instruction, tool text and actual user message across enabled/disabled flag, then inspect request order and visible tool-source label, plus a separate intentionally hostile tool-content fixture. No such execution occurred.

## NO_DECISION_SECTION
Decision: NO_DECISION
Rationale: source-proven default and insertion branch are sufficiently clear for research, but no installed Welcome dependency, security test, model/provider receipt or measurable cache effect can justify a host migration or safety declaration.
Host Action: NONE.
Next Research Condition: exact SDK artifact and version plus reproducible `LlmRequest` serialization for feature on/off, host dependency check, output/effect receipt, stdout/stderr/exit and separate counterfactual tool payload.

## EVIDENCE_DELTA
- NEW_EVIDENCE: exact helper insertion and marker-elision behavior with pinned file blob identities.
- CORRECTED_INTERPRETATION: source/authority identity cannot be deduced from a user-role wrapper; safe source labeling is narrower than authorization.
- UNCHANGED_BOUNDARY: UPSTREAM_FEATURE_DEFAULT != WELCOME_DEPLOYMENT, SOURCE_REVIEW != RUNTIME_EFFECT.
- NEW_COUNTEREVIDENCE: zero-dynamic-instruction early return; feature-off fallback; attacker-controlled tool text still model visible.
- UNKNOWN_RETAINED: runtime request shape in installed package, cache improvement, prompt-injection risk reduction and host compatibility.
- NEXT_RETEST_CONDITION: execute paired exact-source tests of request content order, source label, flag disable path and hostile text with logs/output.

## NEXT_HANDOFF
- W46 H3 already merged as [PR #998](https://github.com/lostlight530/welcome-to-github/pull/998); its H4 is a separate closed-week handoff and must cite its own `DEC-2026W46-01`. Today's H2 does not alter W46 or require an H3 rewrite.
- 2026-11 H5/H6 are NOT_DUE until natural month closure.
- No adopted NEXUS architecture, Parallax research result or Horizon long-memory promotion follows from this H2.

## BOUNDARY_CHECK
- One canonical same-day H2 file only; no H1 edits, Jules history, NEXUS/Parallax, Actions, private task controls or maintenance writes.
- GitHub upstream source read: PERFORMED. Full SDK execution and repository structural checker: NOT_EXECUTED; local Git HTTPS DNS acquisition failed in a later independent probe. Structural section/field check performed within this delivery, not a native checker PASS.
- Delivery: reviewable PR, no secret, no force push, no external version inference.
