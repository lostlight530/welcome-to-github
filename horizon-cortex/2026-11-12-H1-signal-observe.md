# H1 Daily Signal Observe — 2026-11-12

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-12
Logical Timezone: Asia/Shanghai
Execution Time UTC: 2026-11-12T01:00:00Z / approximate authoring window, not a runner timestamp
Execution Time Asia/Shanghai: 2026-11-12 / exact task-start timestamp not independently captured
Agent: GPT-6 / GPT_NATIVE / NOT_JULES_REPLAY
Producer Identity: HUMAN_REQUESTED_GPT_NATIVE
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: c8354b6ea8cb2a80b3da0448ae90cb83a52f5a41
Run Identity: welcome-to-github/horizon/H1/2026-11-12/GPT_NATIVE/c8354b6ea8cb2a80b3da0448ae90cb83a52f5a41/mcp-servers-240-observe-01
Network Status: OFFICIAL_GITHUB_RELEASE_AND_SECURITY_ADVISORIES_OPENED
Source Status: FIRST_PARTY_RELEASE_AND_ADVISORY_TEXT / PATCH_AND_FIX_TESTS_NOT_EXECUTED
Task Status: SUCCESS / BOUNDED_EXTERNAL_SOURCE_OBSERVATION
Source Identity: modelcontextprotocol/servers@v2.4.0 / released 2026-11-11T07:07:16Z
Source Authority For Claim: FIRST_PARTY_RELEASE_FOR_PUBLISHED_FIX_CLAIMS / FIRST_PARTY_ADVISORIES_FOR_REPORTED_FAILURE_MECHANISMS
Independent Verification: RELEASE_API_AND_TWO_ADVISORY_PAGES_INSPECTED / SAME_PUBLISHER_LINEAGE / REPRODUCTION_NOT_EXECUTED
Evidence Upgrade Basis: DISTINCT_PREVIOUSLY_UNRECORDED_OFFICIAL_RELEASE_SIGNAL / NO_INDEPENDENT_RUNTIME_EVIDENCE
Host Applicability: UNKNOWN / HOST_NOT_INSPECTED_OR_TESTED
Original Execution Status: GPT_NATIVE_NEW_RESEARCH_2026-11-12 / NOT_JULES
Current Path Status: PROPOSED_BRANCH_ARTIFACT / MAIN_VISIBILITY_PENDING_AT_AUTHORING
Write Scope: horizon-cortex/2026-11-12-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Authoritative baseline is the exact merged main above, with no open PRs at preflight. Read current Horizon README and EVIDENCE_POLICY, 2026-11-11 H1/H2, and checked the directory inventory for the previous weekly and monthly files.
- Previous H1 on 2026-11-11 recorded google/adk-python required-argument serialization; the present signal is a different upstream repository, package release and failure family. The official release occurred on 2026-11-11, not on the logical date of this research record.
- Focus: newly verified MCP reference-server fixes relevant to Agent tool isolation, filesystem TOCTOU and untrusted Git execution. Search checked first-party GitHub release details, versioned fixed packages and the exact security advisories below.
- Current ISO week 2026-W46 and calendar month 2026-11 remain open. Existing 2026-W45 H3/H4 and 2026-10 H5/H6 are historical context only; they are not rerun here.
- Unverified topics: actual local package versions, host dependencies, installed or exploited server instances, independent security reproductions, individual patch test results, broader protocol conformance and deployment adoption.

## EXTERNAL_SOURCE_RECORDS

### SRC-20261112-H01 — MCP reference servers release
Source ID: SRC-20261112-H01
Title: modelcontextprotocol/servers v2.4.0
Publisher: modelcontextprotocol/servers maintainers
URL: https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0
Published or Updated Date: 2026-11-11T07:07:16Z (GitHub release published_at)
Date Checked: 2026-11-12 Asia/Shanghai
Source Type: FIRST_PARTY_VERSIONED_RELEASE
Evidence Tier: PRIMARY_FOR_RELEASE_METADATA_AND_MAINTAINER_FIX_CLAIMS
Access Status: RELEASE_BODY_AND_GITHUB_RELEASE_METADATA_READ
Independent Source: ONE_UPSTREAM_RELEASE_LINEAGE
Claim Supported: v2.4.0 declares six security fixes across filesystem, git and fetch servers; affected package families have distinct fixed versions, filesystem 2.3.0 and Python git/fetch 2026.11.11.
Claim Not Supported: patches independently passed tests in this research, any downstream runtime is updated, all platforms have complete mitigation, or Welcome runs any affected package.
Relevance: real tool capability and confinement boundaries, including read-only commands with side effects.
Confidence: HIGH_FOR_RELEASE_CONTENT / UNKNOWN_FOR_DOWNSTREAM_EXECUTION
Limitations: a versioned release statement does not itself constitute an independent exploit replay or local host incident.

### SRC-20261112-H02 — Git read-only operation execution boundary
Source ID: SRC-20261112-H02
Title: GHSA-6hqx-gqrx-c5r2 — arbitrary command execution from repository Git configuration
Publisher: modelcontextprotocol/servers security advisory
URL: https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-6hqx-gqrx-c5r2
Published or Updated Date: 2026-11-11 (advisory publication date displayed)
Date Checked: 2026-11-12 Asia/Shanghai
Source Type: FIRST_PARTY_SECURITY_ADVISORY
Evidence Tier: PRIMARY_FOR_PUBLISHED_VULNERABILITY_DESCRIPTION
Access Status: ORIGINAL_ADVISORY_DESCRIPTION_AND_PATCH_SCOPE_READ
Independent Source: SAME_UPSTREAM_SECURITY_LINEAGE_AS_SRC-20261112-H01
Claim Supported: prior mcp-server-git read-only invocations on untrusted repositories could execute commands configured in repository Git settings, including core.fsmonitor and other executable Git configuration; advisory declares fixed release 2026.11.11 and a Git minimum-version guard.
Claim Not Supported: any specifically named external user suffered an incident, patched behavior was locally reproduced here, or ordinary read-only semantics universally imply arbitrary command execution.
Relevance: tool-read classification cannot replace effect-capability analysis.
Confidence: HIGH_FOR_ADVISORY / LOCAL_RUN_NOT_OBSERVED
Limitations: affected runtime and configuration preconditions matter; no test runner or exploitation attempt in this task.

### SRC-20261112-H03 — Filesystem race boundary
Source ID: SRC-20261112-H03
Title: GHSA-p9cv-8g75-4xcg — symlink swap after allowed-path validation
Publisher: modelcontextprotocol/servers security advisory
URL: https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-p9cv-8g75-4xcg
Published or Updated Date: 2026-11-11 (advisory publication date displayed)
Date Checked: 2026-11-12 Asia/Shanghai
Source Type: FIRST_PARTY_SECURITY_ADVISORY
Evidence Tier: PRIMARY_FOR_PUBLISHED_VULNERABILITY_AND_REPORTED_TEST
Access Status: ORIGINAL_ADVISORY_DESCRIPTION_AND_RELEASE_LIMITS_READ
Independent Source: SAME_UPSTREAM_RELEASE_SECURITY_LINEAGE
Claim Supported: advisory documents a path validation followed by a by-name open and a symlink-swap window; it reports an external-file disclosure in an author's Linux experiment. Release states the mitigation binds checked file to read on Linux/macOS, while the Windows race is narrowed but not fully closed.
Claim Not Supported: any Welcome data was exposed, Windows is fully fixed, the experiment was independently repeated here, or all filesystems share identical behavior.
Relevance: time-of-check/time-of-use and object identity in tool execution.
Confidence: HIGH_FOR_PUBLISHED_ADVISORY / REPLICATION_NOT_EXECUTED
Limitations: the source-reported experiment is not an independent second execution performed by this producer.

## RAW_SIGNAL_LOG

### SIG-20261112-H01 — READ_ONLY_GIT_TOOL_EFFECT_BOUNDARY
Signal ID: SIG-20261112-H01
Signal: Versioned security release documents repository-controlled Git configuration as an executable effect path during nominally read-only MCP tool operations.
Source IDs: SRC-20261112-H01, SRC-20261112-H02
What Changed: a public fix now explicitly overrides executable repository Git configuration and rejects Git versions too old to honor the override.
Why It May Matter: authorization of a tool call by name or read-only label is weaker than evaluating its true subprocess and repository configuration effect surface.
Evidence Tier: FIRST_PARTY_RELEASE_PLUS_ADVISORY_ONE_LINEAGE
Confidence: HIGH_FOR_PUBLISHED_MECHANISM / UNKNOWN_FOR_DOWNSTREAM_INTEGRATIONS
Uncertainty: independent patched/unpatched replay; exact affected integrations; installed version and target OS.
Freshness: upstream publication 2026-11-11, newly admitted in this 2026-11-12 research record; NOT a claim of a Nov 12 release.
Possible Noise: overlapping release and advisory are NOT independent corroboration; no generalized exploit frequency is inferred.
Needs H2 Verification: YES, with bounded negative and positive controls, pinned Git versions, and effect receipts.
Host Repository Change: NO

### SIG-20261112-H02 — FILESYSTEM_PATH_CHECK_OPEN_RACE
Signal ID: SIG-20261112-H02
Signal: a path authorized by a directory check is not necessarily the same object later opened if directory components are replaceable.
Source IDs: SRC-20261112-H01, SRC-20261112-H03
What Changed: filesystem server release describes mitigation for Linux/macOS and an explicitly residual Windows race boundary.
Why It May Matter: path allowlists, object identity and atomic access deserve separate verification at the tool runtime boundary.
Evidence Tier: FIRST_PARTY_RELEASE_PLUS_ADVISORY_ONE_LINEAGE
Confidence: HIGH_FOR_PUBLISHED_MECHANISM / EFFECTIVENESS_NOT_REPRODUCED
Uncertainty: deployment version; OS and filesystem prerequisites; Windows residual exploitation conditions; host applicability.
Freshness: upstream publication 2026-11-11; checked 2026-11-12.
Possible Noise: one server's issue is not a universal MCP protocol flaw.
Needs H2 Verification: YES; compare validation/open object identity and the patched code behavior under explicit environment constraints.
Host Repository Change: NO

## EVIDENCE_DELTA
- NEW_EVIDENCE: a versioned first-party security release and two concrete advisories expose distinct read-tool execution and filesystem object-identity failure mechanisms not present in the previous Horizon H1.
- CORRECTED_INTERPRETATION: a tool labeled read-only can still invoke lower-level executable configuration; a prechecked path string is not proof of a subsequently opened object's identity.
- UNCHANGED_BOUNDARY: MCP reference-server advisory != MCP specification guarantee != every client implementation != Welcome host adoption.
- NEW_COUNTEREVIDENCE: upstream report of a successful Linux disclosure and documented residual Windows race contradict a universal assertion that allowlist precheck alone suffices.
- UNKNOWN_RETAINED: independent reproduction, patched coverage beyond exact sources, local installed versions, real usage, exploit frequency and host relevance.
- NEXT_RETEST_CONDITION: pin upstream pre/post package and Git versions, run isolated effect-instrumented negative/positive tests, include symlink race controls by OS, record commands, exit codes, logs and exact opened object identities.

## NEXT_HANDOFF
- H2 must not start until this same-date H1 is reviewed/merged and visible on refreshed main; its provenance must not be replaced with an old Jules claim.
- Verify advisory-to-patch scope and OS limitations, distinguish publisher-controlled tests from independent execution, and explicitly classify findings without host migration decisions.
- Weekly W46 and November H5/H6 are NOT_DUE. No Host, NEXUS, Parallax, Actions or governance change is authorized from this H1.

## BOUNDARY_CHECK
- Only the canonical current-date Horizon H1 path is proposed. No historical output, checker, policy, host code, Actions, NEXUS, Parallax or archive changed.
- Repository check.py, vulnerable or patched MCP server tests, and Welcome host checks: NOT_EXECUTED at authoring; original release and advisories: READ.
- External sources shared with other research repositories retain one publisher lineage, never independent evidence count inflation.
- Original Jules history and all prior task-time negative states preserved.
- Boundary Violation: NO
