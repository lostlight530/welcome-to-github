# H1 Daily Signal Observe — 2026-10-28

CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-10-28
Logical Timezone: Asia/Shanghai
Execution Date UTC: 2026-10-28
Exact Start Timestamp: NOT_CAPTURED
Agent: GPT-6
Producer Identity: GPT_NATIVE_PROSPECTIVE / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_NATIVE_PRODUCTION
Base Main SHA: df87bdd542aa2a95ad773c19c5d2e2e3f714c13f
Run Identity: welcome-to-github/horizon/H1/2026-10-28/GPT_NATIVE/df87bdd542aa2a95ad773c19c5d2e2e3f714c13f/gpt-native-20261028-h1-01
Knowledge Source: GOOGLE_ADK_VERSIONED_FIRST_PARTY_RELEASE
Network Status: PRIMARY_SOURCE_OPENED
Source Status: ONE_CANONICAL_VERSIONED_RELEASE / ZERO_INDEPENDENT_REPRODUCTIONS
Task Status: SUCCESS
Evidence Scope: BOUNDED_DOCUMENTARY_OBSERVATION
Repository Inspection: CURRENT_HORIZON_POLICY_READ / OCT26_H1_H2_AND_W43_H4_READ / OCT27_DAILY_PATHS_ABSENT_ON_MAIN
GitHub Actions Inspection: RECENT_RUN_METADATA_ONLY / NOT_H1_SDK_VALIDATION
Write Scope: horizon-cortex/2026-10-28-H1-signal-observe.md
Boundary Violation: NO
Original Execution Status: NEW_GPT_NATIVE_PROSPECTIVE_OBSERVATION / NOT_JULES_REPLAY
Current Path Status: PROPOSED_ON_DRAFT_BRANCH / NOT_MERGED
Host Applicability: UNKNOWN

INPUT_RECORD
- Current merged main, Horizon EVIDENCE_POLICY, 2026-10-26 H1/H2, 2026-W43 H4, and the latest naturally closed 2026-09 H6 were read.
- The repository tree inspected at this run did not contain a 2026-10-27 H1/H2 or a 2026-10-28 H1/H2 on main. No claim about whether an unobserved external producer attempted the task is made.
- W43 H4 watchlist prioritized source/version-scoped transport, authorization receipts and memory/context-continuity boundaries. This Daily chooses the ADK session/memory and telemetry boundary, not a host architecture change.
- Search themes: Google ADK Python versioned release, agent session persistence and memory, event/telemetry contract migration. Other ecosystem topics were not exhaustively surveyed.
- The release notes carry release-version date 2026-10-22; the GitHub release interface displays its posting on October 23. Checked 2026-10-28. This is first documented here, not a claim that the release was published today.
- October is still open; a 2026-10 H6 path, if present, does not constitute a closed-month memory baseline.

EXTERNAL_SOURCE_RECORDS

### SRC-20261028-H01
Source ID: SRC-20261028-H01
Title: google/adk-python v2.13.0 release
Publisher: google/adk-python maintainers
URL: https://github.com/google/adk-python/releases/tag/v2.13.0
Version: v2.13.0
Published or Updated Date: 2026-10-22 IN_RELEASE_NOTES / 2026-10-23 GITHUB_RELEASE_UI
Date Checked: 2026-10-28
Source Type: FIRST_PARTY_VERSIONED_RELEASE_NOTES
Evidence Tier: PRIMARY_FOR_MAINTAINER_DECLARED_SDK_CHANGES
Access Status: RELEASE_BODY_OPENED
Independent Source: ONE_PUBLISHER_AND_ONE_RELEASE_LINEAGE / ZERO_INDEPENDENT_RUNTIME_REPLAYS
Claim Supported: the release lists experimental MongoDbSessionService and experimental MongoDbMemoryService, a delete_memory API addition, and default OpenTelemetry GenAI v2 telemetry with an opt-in legacy schema switch
Claim Not Supported: measured durability under replica failures, semantic equivalence to vector memory, successful migration for every user, Zero/Welcome adoption, or external integration test success
Relevance: separating session persistence, keyword-based memory recall, and telemetry schema contract from application-level guarantees
Confidence: HIGH_FOR_VERSIONED_RELEASE_DESCRIPTION / UNKNOWN_FOR_DEPLOYED_EFFECT
Limitations: original SDK code/diff, migration rehearsal, exact dependency graph and comparable benchmark were NOT_EXECUTED; one changelog is not independent feature verification

RAW_SIGNAL_LOG

### SIG-20261028-01
Signal ID: SIG-20261028-01
Signal: SESSION_PERSISTENCE_AND_MEMORY_RECALL_ARE_DISTINCT_ADK_SERVICE_CONTRACTS
Source IDs: SRC-20261028-H01
What Changed: v2.13.0 advertises experimental MongoDB-backed session storage for runner replicas and an experimental keyword-search MongoDB memory service without an embedding index
Why It May Matter: a shared session store's continuity and a long-term memory recall service have different identity, retrieval, consistency and effect-evidence obligations
Evidence Tier: FIRST_PARTY_VERSIONED_RELEASE_NOTE
Confidence: HIGH_FOR_MAINTAINER_DESCRIPTION
Uncertainty: replication failover, write acknowledgement, retention, search recall quality and permissions were not exercised
Freshness: VERSION_NOTE_2026-10-22 / OBSERVED_2026-10-28
Possible Noise: calling both services durable memory proof, or treating an experimental service as a generally mature solution
Needs H2 Verification: YES / pin package source, implementation tests and separately verify experimental label

### SIG-20261028-02
Signal ID: SIG-20261028-02
Signal: TELEMETRY_SEMCONV_DEFAULT_IS_AN_INSTRUMENTATION_COMPATIBILITY_BOUNDARY
Source IDs: SRC-20261028-H01
What Changed: v2.13.0 release notes identify OpenTelemetry GenAI v2 default and a legacy schema opt-in setting, with removal of call_llm under the new default
Why It May Matter: span naming and instrumentation can change independent of actual agent action semantics, so historical traces require schema-version attribution before comparison
Evidence Tier: SAME_FIRST_PARTY_RELEASE_NOT_INDEPENDENT_SUPPORT
Confidence: HIGH_FOR_RELEASE_NOTE
Uncertainty: exact span fields, migration correctness, downstream dashboards and real agent trace continuity were not verified
Freshness: VERSION_NOTE_2026-10-22 / OBSERVED_2026-10-28
Possible Noise: mistaking telemetry field migration for better runtime correctness or a measured reliability gain
Needs H2 Verification: YES / inspect source patch, migration guide and replay version-pinned sample traces

EVIDENCE_DELTA
- NEW_EVIDENCE: a first-party ADK 2.13.0 release documents distinct session, experimental memory and telemetry contract changes not in the inspected Oct26 Horizon H1 subject.
- CORRECTED_INTERPRETATION: a session store and a keyword memory service are not the same authority or state-continuity mechanism; release metadata does not prove deployment.
- UNCHANGED_BOUNDARY: SDK release != host adoption; telemetry schema != effect success; repeated features within one release != independent sources.
- NEW_COUNTEREVIDENCE: both MongoDbSessionService and MongoDbMemoryService are explicitly experimental in the original release notes; the opt-in legacy telemetry schema shows that the new default is not an unconditional compatibility guarantee.
- UNKNOWN_RETAINED: run-scoped tool effects, end-to-end persistence, host dependencies, independent implementation reproductions and real performance changes.
- NEXT_RETEST_CONDITION: H2 inspects exact source/tag and tests, reproduces a version-pinned session write/reopen and schema-labeled trace comparison if an execution environment becomes available.

NEXT_HANDOFF
- H2 requires this exact 2026-10-28 H1 to be reviewed and merged into main before downstream execution; the Draft branch does not satisfy main-visible input.
- H2 must preserve this single-source lineage and independent test count of zero; no H3/H4 decision, host runtime action, NEXUS change or H6 memory promotion follows from this H1.

BOUNDARY_CHECK
- One prospective H1 artifact within horizon-cortex only; no history, host runtime, Parallax, NEXUS, Actions or governance modified.
- GitHub main/open PR metadata was inspected for delivery coordination only, not as external technology evidence.
- ADK source test replay, Horizon offline checker, and host tests: NOT_EXECUTED; no PASS claimed.
- Neither prior Jules provenance nor original historical missing/degraded state was rewritten.
