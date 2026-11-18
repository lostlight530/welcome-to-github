# H2 Daily Horizon Orient — 2026-11-18 / MCP prompt argument authority and compatibility counterchecks

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-18
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: b8e5e4216b57101d375b9241e955b51034338f6a
Run Identity: welcome-to-github/horizon/H2/2026-11-18/GPT_NATIVE/b8e5e4216b57101d375b9241e955b51034338f6a/mcp-delegation-counterchecks-01
Source Identity: google/adk-python@889ddd3134df1dd1a626205ee78811950dec2a5c
Source Authority For Claim: FIRST_PARTY_PINNED_ADK_IMPLEMENTATION_DIFF / SAME_ISSUER_AS_H1
Independent Verification: MERGED_H1_SHA_AND_BLOB_READBACK / PINNED_IMPLEMENTATION_AND_AUTHORED_TEST_REVIEW / NO_LOCAL_SDK_RUN
Host Applicability: UNKNOWN / WELCOME_DEPLOYMENT_AND_INSTALLED_ADK_VERSION_NOT_VERIFIED
Evidence Upgrade Basis: NEW_CONDITIONAL_AUTHORITY_AND_COMPATIBILITY_CONTROL_MATRIX / NOT_SECOND_INDEPENDENT_ISSUER
Original Execution Status: GPT_NATIVE_SOURCE_AND_DEPENDENCY_REVIEW_PERFORMED / UPSTREAM_TESTS_AND_HOST_RUNTIME_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_ORIENTATION / NO_HOST_ADOPTION_DECISION / NO_EXPLOIT_ASSERTION
Write Scope: horizon-cortex/2026-11-18-H2-horizon-orient.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Original same-date `horizon-cortex/2026-11-18-H1-signal-observe.md` is actually merged in PR [#1010](https://github.com/lostlight530/welcome-to-github/pull/1010).
- Fresh main H1 merge commit: `b8e5e4216b57101d375b9241e955b51034338f6a`; exact main-retained H1 blob: `c0844ea5375f78f4be264a48f9f3c68ae6f0fbba`.
- H2 began only after the main ref and H1 blob were reread; H1 Draft alone was not accepted as dependency proof.
- Current Horizon `README.md`, `EVIDENCE_POLICY.md`, `check.py` required sections and 2026-11-17 H2 were inspected in context of same-day H1.
- Reopened pinned first-party [ADK commit 889ddd31](https://github.com/google/adk-python/commit/889ddd3134df1dd1a626205ee78811950dec2a5c) source and authored tests. No independent publisher, release package, host process or real MCP server was run.
- Upstream source event 2026-11-17T21:56:09Z is the 2026-11-18 Shanghai logical day. PR merge is a delivery event, not a second external source.
- H1 and H2 therefore share one original ADK source lineage; H2 adds counterfactual analysis, not an independent observation of exploitation or remediation.

## SIGNAL_CLASSIFICATION
Signal ID: SIG-20261118-H01
Layer: SDK-level MCP prompt integration and host session-state export boundary
Source-supported mechanism: before this pinned patch, remote prompt definition argument names could select identically named `context.state` values. The patch replaces the selection with developer-supplied `arguments` defaulting to `None`.
Potential confidentiality failure class: MCP_PROMPT_DEFINITION_CAN_EXPAND_SESSION_STATE_READ_SURFACE_IN_AFFECTED_CLIENT
Required exploit preconditions: affected prepatch `McpInstructionProvider` code path, untrusted/compromised prompt issuer, matching sensitive session key, call execution, and observing peer response or transport. None were demonstrated in Welcome.
Updated authority model: remote MCP server declares its prompt needs; that declaration no longer automatically grants access to local state. The developer instead explicitly chooses a map or callback.
Residual limitation: developer-authored callable `arguments=lambda ctx: ...` can still export sensitive values. Control relocation is not a proof of complete sanitization, authenticated MCP server identity, or network-level isolation.
Status: `WATCH / NO_DECISION / NO_HOST_CHANGE`
Evidence class: `FIRST_PARTY_CODE_PATH_SUPPORTED / ACTUAL_EXPLOIT_OR_HOST_EFFECT_UNKNOWN`
Independent issuer added: `NONE`.

## ORIENTATION_NOTES
- Positive test case P1 (proposed, NOT_EXECUTED): run prepatch provider with an in-memory state containing a canary key, mock a prompt definition declaring the same key, capture serialized `get_prompt` request arguments.
- Positive test case P2 (proposed, NOT_EXECUTED): run patch revision with default arguments and same state. The externally observed request must have `arguments=None`; ensure there is no ancillary request to `list_prompts` selecting private keys.
- Negative N1 (proposed, NOT_EXECUTED): explicit `arguments={"locale":"en-US"}` must carry only locale, even if session includes many names matching prompt definition.
- Negative N2 (proposed, NOT_EXECUTED): developer callable deliberately returns sensitive state; patched provider cannot guarantee confidentiality against developer-authorized disclosure. Treat this as a separate authority decision.
- Negative N3 (proposed, NOT_EXECUTED): remote prompt requires a field that callers previously sent implicitly. Default-none behavior can break compatibility; note potential regression instead of asserting universally safe transparent migration.
- Negative N4 (proposed, NOT_EXECUTED): server lies about argument semantics or response content; fixing outbound argument selection alone cannot authenticate remote returned instructions.
- Negative N5 (proposed, NOT_EXECUTED): an unaffected SDK revision or application using no MCP prompt provider should not be counted as a local vulnerability or remediation.
- Trust plane: untrusted protocol metadata `INSPECT`; outbound argument mapping `ALLOW/DENY/MODIFY` at the developer-controlled boundary; actual network request and downstream effects need `TRACE/INSTRUMENT` receipts.
- Source-level `get_prompt(arguments=None)` in a mocked test is not a packet capture; a commit with tests does not show this producer executing them.
- No observation was made of repository host session keys, active MCP server allowlists, real network calls, installed ADK dependency or any hosted NEXUS deployment.
- The correct source hierarchy: pinned implementation primary for that ADK code path; protocol-wide normative claims would require an independently checked MCP specification and conformance evidence.

## NO_DECISION_SECTION
Decision: NO_DECISION
Decision Basis: a first-party code and authored-test change supports a specific authority-boundary improvement but does not show affected Welcome execution, exploited state leakage, completed mitigation or runtime compatibility.
Decision ID: NO_DECISION
Host Change: NONE / NO_MIGRATION / NO_NEXUS_CHANGE
Claim Promotion: NO / COUNTEREVIDENCE_GATE_NOT_MET
Watchlist: SDK prompt argument trust, explicit callback audit, compatibility with required prompt fields, session-state read instrumentation and protocol/source identity.
Retest: before/after patch controlled fake MCP server with serialised request capture and canary argument, paired developer-null/fixed/callback controls, stdout/stderr/exit, exact SDK version, host installed dependency and immutable store/run IDs.

## EVIDENCE_DELTA
- NEW_EVIDENCE: merged H1 canonical provenance, exact source branch classification and bounded five-control falsification matrix.
- CORRECTED_INTERPRETATION: remote argument declarations != local read grants; explicit developer callbacks can still leak despite a protective default.
- UNCHANGED_BOUNDARY: SOURCE_FIX != SDK_RELEASE != HOST_ADOPTION != REAL_EXPLOIT; H1/H2 same upstream lineage remains one source.
- NEW_COUNTEREVIDENCE: default-none compatibility regressions, developer-defined secret export and untrusted returned prompt instructions limit remediation claims.
- UNKNOWN_RETAINED: published SDK distribution, installed Welcome package, actual server/session identities, network receipt, test execution and residual leaks.
- NEXT_RETEST_CONDITION: capture paired pinned code behavior and explicit preconditions at a real or trusted test client; name authority decision, actual outgoing argument bytes and independent reviewer.

## NEXT_HANDOFF
- 2026-W46 was previously closed and has own H3/H4; this 2026-11-18 H2 is in open 2026-W47 and may inform H3 only after that ISO week closes.
- November H5/H6 NOT_DUE; H2 adds no evidence to Horizon Memory until natural month closure and claim promotion.
- Independent A1/A2 maintenance and periodic audits remain separate; this H2 is NOT Independent A2.

## BOUNDARY_CHECK
- Actually verified: current main after H1 merge, same-day H1 exact blob, pinned first-party source and repository checker/contract shape.
- NOT_EXECUTED: full Horizon check.py, upstream pytest, MCP server, sdk client, NEXUS host, packet capture and effect sink.
- One new H2 canonical file only. No Jules history, H1 original blob, Parallax, workflow, governance, Host Kernel or audit modifications.
- Subject to separate maintainer-authorized merge; GitHub merge must not convert any of the above unexecuted items into PASS.
