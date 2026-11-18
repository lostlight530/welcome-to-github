# H1 Daily Signal Observe — 2026-11-18 / MCP prompt argument authority

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-18
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: d658c5630e3d8ae7aaca67002d0db1ca93d56687
Run Identity: welcome-to-github/horizon/H1/2026-11-18/GPT_NATIVE/d658c5630e3d8ae7aaca67002d0db1ca93d56687/mcp-prompt-arguments-source-boundary-01
Observation Window: 2026-11-18 Asia/Shanghai, observed 2026-11-18T09:43Z
Source Identity: google/adk-python@889ddd3134df1dd1a626205ee78811950dec2a5c
Source Authority For Claim: FIRST_PARTY_PINNED_IMPLEMENTATION_AND_AUTHORED_TEST_DIFF
Independent Verification: EXACT_COMMIT_PATCH_REREAD / NO_UPSTREAM_TEST_EXECUTION / NO_INDEPENDENT_DEPLOYMENT
Host Applicability: UNKNOWN / WELCOME_HOST_ADK_DEPENDENCY_NOT_VERIFIED
Evidence Upgrade Basis: NEW_SOURCE_DIFF_WITH_CONCRETE_ARGUMENT_TRUST_BOUNDARY / NOT_PROTOCOL_CHANGE
Original Execution Status: GPT_NATIVE_REMOTE_SOURCE_REVIEW_PERFORMED / ADK_AND_HOST_RUNTIME_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_SOURCE_OBSERVATION / SECURITY_EFFECT_UNKNOWN
Write Scope: horizon-cortex/2026-11-18-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Cold start: current Welcome merged main `d658c5630e3d8ae7aaca67002d0db1ca93d56687`, complete Git tree non-truncated, no open PR or branch named for 2026-11-18 at preflight. Read current Horizon README, EVIDENCE_POLICY, checker requirements, Nov17 H1/H2 and closed W46 files; this day's H1/H2 are absent from main.
- Nov17 H1/H2 addressed A2A artifact stream finalization, not MCP prompt argument authority. Shared research areas do not merge external issuer, revision or task evidence.
- Exact first-party ADK commit `889ddd3134df1dd1a626205ee78811950dec2a5c` changes `src/google/adk/agents/mcp_instruction_provider.py` and `tests/unittests/agents/test_mcp_instruction_provider.py`; GitHub commit reports 73 additions and 51 deletions over 2 files.
- Upstream commit timestamp 2026-11-17T21:56:09Z = 2026-11-18T05:56:09+08:00, separate from this H1 observation and any PR merge timestamp.
- No SDK was installed, MCP server instantiated, prompt fetched, secret transported, external test run or Welcome NEXUS host changed by this H1. Prior contract cannot prove runtime applicability.

## EXTERNAL_SOURCE_RECORDS
Source ID: SRC-20261118-H01
Title: fix!: stop MCP servers from reading session state through prompt arguments
Publisher: google/adk-python maintainers
Canonical Source Identity: google/adk-python@889ddd3134df1dd1a626205ee78811950dec2a5c
URL: https://github.com/google/adk-python/commit/889ddd3134df1dd1a626205ee78811950dec2a5c
Implementation: https://github.com/google/adk-python/blob/889ddd3134df1dd1a626205ee78811950dec2a5c/src/google/adk/agents/mcp_instruction_provider.py
Authored Tests: https://github.com/google/adk-python/blob/889ddd3134df1dd1a626205ee78811950dec2a5c/tests/unittests/agents/test_mcp_instruction_provider.py
Source Version: EXACT_COMMIT_SHA / SDK_RELEASE_TAG_NOT_VERIFIED
Source Publication Time: 2026-11-17T21:56:09Z
Observation Date: 2026-11-18 Asia/Shanghai
Evidence Tier: FIRST_PARTY_IMPLEMENTATION_DIFF / AUTHORED_TEST_TEXT
Access Status: COMMIT_AND_PATCH_INSPECTED / PYTEST_NOT_EXECUTED

## RAW_SIGNAL_LOG
Signal ID: SIG-20261118-H01
Source proposition: before the patch, `McpInstructionProvider` examined prompt definitions from the remote MCP server and intersected declared argument names with `context.state`, forwarding matching values into `session.get_prompt`.
Changed branch: new keyword-only `arguments` accepts a developer-provided mapping, a callable receiving `ReadonlyContext`, or `None`; default sends `arguments=None`. The server's `list_prompts` names no longer select context-state keys.
Concrete threat condition: an untrusted or compromised MCP prompt server that can declare a matching name may receive session content if an affected earlier provider is used and corresponding state values exist. This is source-demonstrated *potential disclosure mechanism*, not observed exfiltration in Welcome.
Positive control proposed: on a pinned before/after revision, mock a server-declared `adk_oauth2_credential` argument and state containing that key; capture exact outgoing `get_prompt` arguments without contacting a live server.
Negative control A: default `arguments=None` on patched revision must not expose the credential; an explicitly supplied fixed `{"locale":"en-US"}` should send only locale.
Negative control B: a developer-supplied callable can still intentionally leak a secret. The patch moves authority to the developer's callable; it cannot validate callable intent or eliminate all untrusted input risks.
Negative control C: a prompt requiring an argument might fail or degrade when the default is now None, so confidentiality improvement does not prove non-breaking compatibility.
Negative control D: unit-test mocks are design fixtures, not real server observations, installed package coverage, an SDK release compatibility matrix or proof of no other state-leak path.
Technical layer: Agent SDK MCP prompt invocation / trust boundary and argument construction, NOT universal MCP wire semantics, NOT NEXUS deployment, NOT host permission-broker evaluation.
Deduplication: ONE ADK upstream patch, ONE publisher lineage, no added independent corroborating issuer from tests in the same patch.
Disposition: WATCH / NO_HOST_CHANGE / NO_CLAIM_PROMOTION.

## EVIDENCE_DELTA
- NEW_EVIDENCE: exact developer-argument source patch replaces server-declared state-key selection and carries first-party negative test fixtures.
- CORRECTED_INTERPRETATION: server-declared argument metadata is not a delegated grant to read host session state; explicit callable arguments still require independent scrutiny.
- UNCHANGED_BOUNDARY: SOURCE_PATCH != SDK_RELEASE != DEPLOYED_WELCOME_RUNTIME != EXFILTRATION_INCIDENT.
- NEW_COUNTEREVIDENCE: explicit developer callback may disclose secrets; required-argument compatibility may break; mock test is not network test.
- UNKNOWN_RETAINED: released package coverage, installed host dependency, real MCP server behavior, upstream pytest result, independent replication and actual effect/readback.
- NEXT_RETEST_CONDITION: execute pinned before/after versions with an instrumented fake MCP prompt server, state canary, fixed/callable/no-arg controls; capture emitted arguments, package versions, stdout/stderr/exit and host dependency identity.

## NEXT_HANDOFF
- Same-date H2 `welcome/horizon/H2` is BLOCKED_DEPENDENCY until original H1 Draft is merged by Human Maintainer and newly merged H1 blob/PR are reread from fresh main. H1 Draft does not satisfy H2 dependency.
- Closed 2026-W46 H3/H4 already exist and are not rewritten; open 2026-W47 H3/H4 are NOT_DUE under current completed-week contract. November H5/H6 are NOT_DUE until calendar closure.
- No Horizon Memory, NEXUS, Parallax, governance, Independent A1/A2, periodic audit or original Jules record receives new runtime authority.

## BOUNDARY_CHECK
- GitHub current main/source patch and authored test text: INSPECTED. Current Horizon `check.py` required-section/field contract: INSPECTED, not executed.
- Local `git clone` / Python checker / upstream ADK pytest / real host or MCP effect sink: NOT_EXECUTED; this environment's GitHub hostname DNS prevents remote clone. No fabricated checker PASS.
- Delivery: one scoped H1 Draft PR proposed for human review. No auto-merge, direct main mutation or claim that H2 ran.
