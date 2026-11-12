# H2 Daily Horizon Orient — 2026-11-12

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-12
Logical Timezone: Asia/Shanghai
Execution Time UTC: 2026-11-12T01:31:16Z / date-command observed before this orientation write
Agent: GPT-6 / GPT_NATIVE / NOT_JULES_REPLAY
Producer Identity: HUMAN_REQUESTED_GPT_NATIVE
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 2387e751d4b454012d82ef024b0771eb63584838
Run Identity: welcome-to-github/horizon/H2/2026-11-12/GPT_NATIVE/2387e751d4b454012d82ef024b0771eb63584838/mcp-servers-read-boundary-orient-01
Upstream H1: horizon-cortex/2026-11-12-H1-signal-observe.md
Upstream H1 Blob SHA: fd635676b30b7b26cd80b696c2876c70297bb1a7
Upstream H1 Merge PR: https://github.com/lostlight530/welcome-to-github/pull/965
Input Status: SAME_DATE_H1_MERGED_MAIN_VISIBLE_AND_IDENTITY_PINNED
Source Identity: modelcontextprotocol/servers@v2.4.0 / GHSA-6hqx-gqrx-c5r2 / GHSA-p9cv-8g75-4xcg
Source Authority For Claim: FIRST_PARTY_PUBLISHED_RELEASE_AND_ADVISORY_FOR_PRECISE_PACKAGE_FAILURE_MECHANISMS
Independent Verification: H1_BLOB_AND_OFFICIAL_RELEASE_ADVISORIES_REOPENED / SAME_PUBLISHER_LINEAGE / CODE_REPLAY_NOT_EXECUTED
Evidence Upgrade Basis: NARROWED_EXECUTION_PRECONDITIONS_AND_OS_COUNTERCONDITIONS / ZERO_NEW_INDEPENDENT_PUBLISHERS
Original Execution Status: GPT_NATIVE_2026-11-12_NEW_ORIENTATION / NOT_JULES_REPLAY
Current Path Status: NEW_CANONICAL_H2_PROPOSED_ON_REVIEW_BRANCH / MAIN_MERGE_PENDING_AT_AUTHORING
Task Status: BOUNDED_SOURCE_ORIENTATION / NO_HOST_DECISION
Network Status: GITHUB_FIRST_PARTY_RELEASE_AND_ADVISORY_SOURCE_READ
Host Applicability: UNKNOWN / NO_WELCOME_DEPENDENCY_OR_RUNTIME_EFFECT_REPLAY
Host Repository Change: NO
Write Scope: horizon-cortex/2026-11-12-H2-horizon-orient.md
Boundary Violation: NO

## INPUT_RECORD
- Current authoritative merged main is `2387e751d4b454012d82ef024b0771eb63584838`, not the earlier H1 draft branch. Same-day H1 at `horizon-cortex/2026-11-12-H1-signal-observe.md` was reread from this main with blob `fd635676b30b7b26cd80b696c2876c70297bb1a7`. H1 merged via PR #965 before this H2 was prepared.
- The current Horizon README, EVIDENCE_POLICY, previous 2026-11-11 H2 and closed W45/October file inventory govern continuity. W46 and November final remain OPEN/NOT_DUE.
- H1's official MCP reference-server security release is **published 2026-11-11**, checked as a 2026-11-12 research input. GitHub release `v2.4.0` and two advisory texts were reopened and reconciled against exact package versions, preconditions and residual limitations.
- No Welcome NEXUS Host Code, tool integration, installed versions, Git server, filesystem exploit fixture, affected package usage or Windows test was executed. This H2 is source interpretation, not local applicability proof.

## SOURCE_VERIFICATION_RECORDS
### SRC-20261112-H2-01 — read-only Git API versus executable config
- First-party release: https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0 ; published `2026-11-11T07:07:16Z`.
- Original advisory: https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-6hqx-gqrx-c5r2 ; GHSA dated 2026-11-11; fixed `mcp-server-git 2026.11.11`, affected older versions.
- Advisory describes untrusted repository Git configuration including `core.fsmonitor` and other executable settings triggering programs from nominally read-only calls like `git_status`. The fix uses explicit Git command overrides and refuses Git below 2.31 to preserve override semantics.
- Countercondition 1: a Git tool never accepting untrusted repository configuration, or a correctly updated affected server with supported Git, does not automatically share this precise reported failure path.
- Countercondition 2: a read-only API label, a zero exit code or a successful response is **not** a subprocess-effect receipt or a proof of no helper execution; conversely, this advisory does not prove that all read-only API calls on all implementations execute commands.
- Countercondition 3: one official release and its publisher's security advisory are the same evidence lineage, not independent reproduction. The mechanism is publisher reported, not author-tested by H2.

### SRC-20261112-H2-02 — filesystem checked path versus opened object
- Original advisory: https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-p9cv-8g75-4xcg ; published 2026-11-11.
- Reported vulnerable `@modelcontextprotocol/server-filesystem` behavior: allowed-path validation and later by-name file open occur at separate times; an attacker able to rename an in-scope directory may swap a symlink between operations.
- Author's advisory describes a two-user Linux disclosure experiment, not an independent H2 experiment. v2.4.0 release claims Linux/macOS mitigation in `@modelcontextprotocol/server-filesystem 2.3.0`, while Windows reduces but does not fully close the race.
- Countercondition 1: an attacker needs write/rename opportunity in an allowed path and a suitable race; a path disallow or nonmutatable filesystem context need not expose that same race.
- Countercondition 2: treating Linux/macOS mitigation as a Windows universal property would be a false evidence promotion; a repo or package supporting MCP protocol does not imply it runs the vulnerable server.
- Countercondition 3: the advisory is a mechanism description and bounded experiment report, not evidence of Welcome host file leakage, installed package identity or successful local exploit replay.

## SIGNAL_CLASSIFICATION
Signal ID: SIG-20261112-H01
Upstream H1 Signal: READ_ONLY_GIT_TOOL_EFFECT_BOUNDARY
Classification: FIRST_PARTY_PATCHED_SERVER_RISK / EFFECT_TIME_TRUST_BOUNDARY / WATCHLIST
Evidence Status: PUBLISHED_UPSTREAM_ADVISORY_AND_RELEASE / NO_INDEPENDENT_RUNTIME_REPLAY
Independent Sources Added: ZERO; publisher release + advisory + source explanations stay one lineage
Claim Upgrade: NO_GENERALIZED_MCP_PROTOCOL_SECURITY_CLAIM / NO_HOST_ADOPTION
Host Applicability: UNKNOWN / NOT_EXECUTED_FOR_WELCOME
Confidence: HIGH_FOR_OFFICIAL_REPORTED_PRECONDITIONS / PATCH_EFFECT_NOT_INDEPENDENTLY_MEASURED

Signal ID: SIG-20261112-H02
Upstream H1 Signal: FILESYSTEM_PATH_CHECK_OPEN_RACE
Classification: FIRST_PARTY_OS_BOUNDED_TOCTOU_RISK / OBJECT_IDENTITY_CANDIDATE
Evidence Status: UPSTREAM_REPORTED_LINUX_EXPERIMENT / WINDOWS_RESIDUAL_GAP_DECLARED
Independent Sources Added: ZERO
Claim Upgrade: NO_UNIVERSAL_FIX_ASSERTION
Host Applicability: UNKNOWN / NO_LOCAL_FILESYSTEM_TEST

## ORIENTATION_NOTES
- A tool contract must distinguish declared API intent, lower-level executable authority, actual subprocess launch, path allowlisting and the identity of the object actually opened or affected.
- Focused candidate evidence tuple: `source_server_version + Git_or_OS_version + repository_config_identity + input_path_identity + resolved_object_identity + command/effect_receipt + stdout/stderr/exit + run_environment`.
- This is a **research test design**, not a policy requirement already adopted by Welcome. A2A/MCP publication, reference-server code, installed dependency, host deployment and exploit impact are distinct propositions.
- A controlled positive/negative test would use benign instrumented fixtures pinned before and after the package version boundary; record actual process/file effects and negative controls rather than infer runtime correctness from authored fix descriptions.
- Cross-repo research reuse by Aegis/Axiom/Reflective is the same original release/advisory lineage, not independent adoption or reproduction evidence.

## NO_DECISION_SECTION
Decision: NO_DECISION / NO_HOST_CHANGE / NO_MIGRATION_OR_DEPLOYMENT_INSTRUCTION
Reason: source claims support a bounded technical hypothesis; no Welcome installed package provenance, applicable runtime checkout, independent before/after execution or maintainer-authorized Host change was observed.
Retain: exact package/advisory/version/OS boundaries, distinct preconditions, residual Windows caveat, publisher lineage and current H1 merged blob identity.
Not inferred: Welcome NEXUS incident, Parallax credit, broad MCP vulnerability prevalence, protocol-wide insecurity or application adoption.

## EVIDENCE_DELTA
- NEW_EVIDENCE: publisher-specific preconditions and fix-version constraints were independently re-read by H2; source detail added, independent empirical sources ZERO
- CORRECTED_INTERPRETATION: read-only labels are API claims, whereas lower-level Git config and filesystem opened-object identity determine separate observed effects
- UNCHANGED_BOUNDARY: SOURCE_SUPPORTED_MECHANISM != PATCH_RUNTIME_PASS != INSTALLED_PACKAGE != WELCOME_HOST_INCIDENT
- NEW_COUNTEREVIDENCE: patched supported Git versions, absence of attacker-writable path, and Windows residual limits contradict overbroad universal failure/fix claims
- UNKNOWN_RETAINED: independent pre/post replay, host dependency use, actual side effects, exploit frequency, other OS cases and broader transport behavior
- NEXT_RETEST_CONDITION: authorized pinned benign Git and filesystem fixtures, exact package/OS/version controls, effect receipts, negative controls, stdout/stderr/exit and object identity

## NEXT_HANDOFF
- H2 is bounded source verification of the **merged** H1, not independent evidence credit; subsequent 2026-W46 H3/H4 should include it only after full week closure and main visibility.
- Do not invoke Host migrations, NEXUS changes, CI policy rewrites, source registry promotions or monthly H5/H6 because of this H2.
- No valid source-family decision beyond a constrained watchlist, with November monthly not yet due.

## BOUNDARY_CHECK
- Write only `horizon-cortex/2026-11-12-H2-horizon-orient.md`; no H1 rewrite, Parallax, NEXUS, host, scheduler, indexes, historical audits, weekly/monthly or governance changes.
- Source texts were read. Repository `horizon-cortex/check.py`, upstream security unit tests, exploit reproductions and any Welcome host integration: `NOT_EXECUTED`.
- Producer is GPT Native with separately attributable main revision; prior Jules history remains unchanged.
- Boundary Violation: NO
