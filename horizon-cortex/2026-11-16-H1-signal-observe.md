# H1 Daily Signal Observe — 2026-11-16

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-16
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Source Identity: google/adk-python@c6586f19ab8a2bb8b53e70041633b10858d9902e (2026-11-16 commit)
Source Authority For Claim: FIRST_PARTY_COMMIT_DIFF_AND_PINNED_IMPLEMENTATION
Independent Verification: ORIGINAL_COMMIT_AND_EXACT_SOURCE_READ / SDK_RUNTIME_NOT_EXECUTED
Host Applicability: UNKNOWN / NO_WELCOME_ADK_OR_TOOL_RUNTIME_ADOPTION_PROVEN
Evidence Upgrade Basis: NEW_DISTINCT_2026_11_16_DEFAULT_ON_FEATURE_CHANGE / NOT_RELEASE_VERIFIED
Original Execution Status: GPT_NATIVE_BOUNDED_PRIMARY_SOURCE_OBSERVATION / NO_ADK_RUNTIME_EXECUTION
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED
Base Main SHA: bd36f00a6145ecd7774d0409adc12f13afd2fb43
Run Identity: welcome-to-github/horizon/H1/2026-11-16/GPT_NATIVE/bd36f00a6145ecd7774d0409adc12f13afd2fb43/adk-dynamic-instruction-role-routing-default-01
Observation Window: 2026-11-16 Asia/Shanghai / upstream commit created on 2026-11-16 UTC
Task Status: SUCCESS_BOUNDED_SOURCE_OBSERVATION / RUNTIME_UNVERIFIED
Network Status: GITHUB_API_COMMIT_AND_PINNED_SOURCE_READ
Source Status: CURRENT_MAIN_COMMIT / RELEASE_PACKAGE_BEHAVIOR_NOT_VERIFIED
Write Scope: horizon-cortex/2026-11-16-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Recovered current merged Welcome `main@bd36f00a6145ecd7774d0409adc12f13afd2fb43`, `horizon-cortex/README.md` and `EVIDENCE_POLICY.md`; 2026-11-15 H1/H2 read. No pre-existing 2026-11-16 H1 on main at preflight.
- Separate W46 H3 is in Draft PR #998; it concerns 2026-11-09–15 and does not make today's H1 a W46 input. Same-day H2 is not yet eligible until the original H1 Draft merges and fresh main is read.
- Directly fetched upstream [exact ADK commit](https://github.com/google/adk-python/commit/c6586f19ab8a2bb8b53e70041633b10858d9902e). Commit changes exactly one code line: `FeatureConfig(FeatureStage.EXPERIMENTAL, default_on=False)` to `default_on=True` for `DYNAMIC_INSTRUCTION_ROUTING` in `src/google/adk/features/_feature_registry.py`.
- Also directly opened pinned `src/google/adk/flows/llm_flows/prompt/_dynamic_instructions.py`: when flag is enabled, `finalize_dynamic_instructions` creates a `types.Content(role='user', parts=[..._label_dynamic_instruction(...)])` and delegates insertion to `_add_instructions_to_user_content`; on disabled branch it calls `llm_request.append_instructions([combined_text])`.
- This is a **default-configuration delta** on an existing implementation path, not a fresh security theorem, major version release, universal tool-provenance solution, or production measurement.

## EXTERNAL_SOURCE_RECORDS
Source ID: SRC-20261116-H01
Title: Enable dynamic instruction routing by default while retaining EXPERIMENTAL stage
Publisher: google/adk-python upstream maintainers
Canonical Source Identity: google/adk-python@c6586f19ab8a2bb8b53e70041633b10858d9902e
URL: https://github.com/google/adk-python/commit/c6586f19ab8a2bb8b53e70041633b10858d9902e
Feature Registry URL: https://github.com/google/adk-python/blob/c6586f19ab8a2bb8b53e70041633b10858d9902e/src/google/adk/features/_feature_registry.py
Implementation URL: https://github.com/google/adk-python/blob/c6586f19ab8a2bb8b53e70041633b10858d9902e/src/google/adk/flows/llm_flows/prompt/_dynamic_instructions.py
Feature Change Date: 2026-11-16 UTC (upstream Git commit)
Date Checked: 2026-11-16 Asia/Shanghai
Evidence Tier: PRIMARY_SOURCE_PINNED_COMMIT_AND_IMPLEMENTATION / NO_RUN
Access Status: EXACT_COMMIT_AND_SOURCE_BLOBS_READ
Independent Source Count: ONE_UPSTREAM_REPOSITORY_LINEAGE
Claim Supported: The default for `DYNAMIC_INSTRUCTION_ROUTING` is now enabled on the inspected upstream main commit while its stage remains `EXPERIMENTAL`; current gated implementation routes tool-contributed instructions as labelled user-role content rather than appending them to system instructions.
Claim Not Supported: a named released google-adk package shipping this default, deployment on Welcome/NEXUS, improved prompt-injection immunity, lower latency or higher cache-hit rate, universal agreement among model providers.
Confidence: HIGH_FOR_SOURCE_CODE_AND_CONFIGURATION_CHANGE / UNKNOWN_FOR_RUNTIME_OUTCOMES
Limitations: The conditional feature flag can be overridden (`ADK_DISABLE_DYNAMIC_INSTRUCTION_ROUTING=1` per commit description); rollout behavior depends on package revision, flow, tool contribution and request construction. No test suite or rendered model request was executed by this producer.

## RAW_SIGNAL_LOG
Signal ID: SIG-20261116-H01
Signal: EXPERIMENTAL_TOOL_CONTRIBUTED_INSTRUCTION_ROLE_ROUTING_ENABLED_BY_DEFAULT
Mechanism: The original gated implementation already moved dynamic tool/skill-supplied instruction text from a concatenated system instruction path to a labelled user-role carrier. The new committed change activates this path by default on this exact main revision.
Evidence: one-line pinned feature-registry patch plus opened exact implementation of `finalize_dynamic_instructions`.
Technical Separation: Feature policy default != algorithm change; user-role carrier != authenticated trusted instruction; stable system prefix != measured caching outcome.
Why It May Matter: harness context contracts, role/capability priority, cache-key stability, and origin tracing should treat tool-supplied text, static developer/system instructions and real current-user turn as distinct logical sources even if some share transport role.
Counterevidence: user-role content remains model-visible text and could still be instruction-like; a label alone does not attest source authority or prevent prompt injection. Tool contributed dynamic text may still affect generation. The disabled flag path remains available; release/rollout may differ from pinned main.
Noise Filter: Exact version-specific upstream source, not a launch announcement or inference of broad adoption.
Independent Upgrade Eligibility: WATCHLIST_ONLY_PENDING_PINNED_REQUEST_DIFF_AND_RUNTIME_CONTROL
Host Applicability: UNKNOWN / NO_LOCAL_WELCOME_ADK_INTEGRATION_RUN
Status: SOURCE_BOUNDED_OBSERVATION

## EVIDENCE_DELTA
- NEW_EVIDENCE: exact 2026-11-16 change enabling experimental dynamic instruction routing by default, with code-branch identity.
- CORRECTED_INTERPRETATION: a role-routing default is not a new authority policy, security proof or measured caching optimization.
- UNCHANGED_BOUNDARY: EXTERNAL_SOURCE_PATCH != WELCOME_HOST_DEPLOYMENT, TOOL_SOURCE_LABEL != TRUSTED_AUTHORITY.
- NEW_COUNTEREVIDENCE: explicit fallback/disable branch and model-visible untrusted dynamic text invalidate categorical security claims.
- UNKNOWN_RETAINED: released binary/version ancestry, provider request/response, cache-hit results, host dependency chain and injection safety.
- NEXT_RETEST_CONDITION: pin same ADK revision under an executable workflow, compare enabled vs disabled generated `LlmRequest` role/content ordering for `load_artifacts` or `load_mcp_resource`, record encoded request, token/cache telemetry, stdout/stderr/exit and unaffected-control path.

## NEXT_HANDOFF
- Same-day `welcome/horizon/H2`: BLOCKED_UNTIL_THIS_H1_ORIGINAL_PR_MERGED_AND_VISIBLE_ON_FRESH_MAIN. H2 can independently read request-construction implementations, counterexamples, conditional overrides and downstream model role behavior, but cannot credit new independent publisher without another source.
- W46 H3/H4 is an independent closed-week chain; November H5/H6 NOT_DUE. No NEXUS, Parallax, Actions or host migration change.

## BOUNDARY_CHECK
- One canonical H1 Daily research record only. Jules history, previous H1/H2, Horizon Memory, host NEXUS, Parallax, maintenance, workflows and private prompts untouched.
- Exact GitHub upstream code read: PERFORMED. `horizon-cortex/check.py`, ADK runtime and Welcome host integration: NOT_EXECUTED; local git worktree unavailable from HTTPS DNS failure. No checker PASS claimed.
- Human Maintainer approval/merge pending; no downstream H2 execution credit.
