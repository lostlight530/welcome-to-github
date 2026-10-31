# H2 Daily Horizon Orient — 2026-10-31

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-10-31
Logical Timezone: Asia/Shanghai
Execution Date UTC: 2026-10-31
Exact Execution Timestamp: NOT_CAPTURED
Agent: GPT-6
Producer Identity: GPT_NATIVE_PROSPECTIVE / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_NATIVE_PRODUCTION
Base Main SHA: fb7fb4060fbcedb21da92a0ec4cff3ee0056c052
Run Identity: welcome-to-github/horizon/H2/2026-10-31/GPT_NATIVE/fb7fb4060fbcedb21da92a0ec4cff3ee0056c052/gpt-native-20261031-h2-01
Upstream H1 Path: horizon-cortex/2026-10-31-H1-signal-observe.md
Upstream H1 Blob SHA: 37d4477e6c513d8f95ce010afb4932d0c57281c8
Upstream H1 PR: #872 / MERGED
Upstream H1 Merge SHA: fb7fb4060fbcedb21da92a0ec4cff3ee0056c052
Input Status: SAME_DATE_H1_MERGED_MAIN_VISIBLE
Task Status: SUCCESS_BOUNDED_SOURCE_AND_PATCH_ORIENTATION
Network Status: FIRST_PARTY_RELEASE_AND_SOURCE_DIFFS_OPENED
Source Status: VERSIONED_UPSTREAM_IMPLEMENTATION_TRACE / ONE_MAINTAINER_LINEAGE
Repository Inspection: MERGED_H1_BLOB_AND_HORIZON_POLICY_AND_PRIOR_H1_H2_READ
GitHub Actions Inspection: CODEQL_FOR_PRIOR_H1_DRAFT_OBSERVED / NO_H2_RUNTIME_VALIDATION
Host Applicability: UNKNOWN
Independent Verification: SOURCE_DIFF_REVIEW / NO_CLUSTER_EXECUTION
Evidence Upgrade Basis: MAINTAINER_RELEASE_TO_PATCH_LEVEL_READ / ZERO_INDEPENDENT_REPRODUCTIONS
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Write Scope: horizon-cortex/2026-10-31-H2-horizon-orient.md
Boundary Violation: NO

## INPUT_RECORD
- Cold-start exact main fb7fb4060fbcedb21da92a0ec4cff3ee0056c052 after H1 PR #872 merged. Confirmed H1 Git blob 37d4477e6c513d8f95ce010afb4932d0c57281c8 with same logical date and task H1. Its author-time Draft state remains true at original writing; H2 observes the later merge.
- H1 signal family: upstream agent-sandbox v1.0.9, published 2026-10-29T21:48:41Z (2026-10-30 Shanghai); rechecked 2026-10-31, not new publication today. Horizon 2026-10-30 H1/H2 and 2026-W43 H4 are historical comparison, not independent support.
- Primary release: https://github.com/kubernetes-sigs/agent-sandbox/releases/tag/v1.0.9
- Original merged upstream diffs read: https://github.com/kubernetes-sigs/agent-sandbox/pull/1880 (gRPC/proxy/NetworkPolicy); /pull/1944 (409 status retry); /pull/2010 (stale-cache cold-create); /pull/2079 (Suspended/Finished); /pull/2065 (WebSocket upgrade and metrics).
- These original PRs are same maintainer/project lineage. GitHub-reported PR merge metadata and source patches demonstrate implemented source changes, not a downstream cluster test or independent production replication.
- H2 did not inspect, deploy or mutate Welcome/NEXUS, Parallax, host knowledge database, Kubernetes clusters, or application runtime. W44 remains open and October final H5/H6 is NOT_DUE.

## SIGNAL_CLASSIFICATION
### SIG-20261031-01 — Router target reachability, per-RPC authority and TCP 9090 policy
Signal ID: SIG-20261031-01
H1 Claim: v1.0.9 adds native gRPC and warns about default Kustomize NetworkPolicy permitting TCP 9090 to all namespaces under permissive router authorization.
Classification: strategic signal
Verification Status: SOURCE_PATCH_AND_DEPLOYMENT_VARIANT_INSPECTED / NOT_CLUSTER_REPRODUCED
Verification Sources: v1.0.9 release; upstream PR #1880 description, NetworkPolicy and test diffs.
Repository Record Comparison: H1 is same-day first-party observation; H2 adds exact PR diff without a second independent source. Prior Horizon did not establish Welcome deployment.
Reason: PR #1880 adds gRPC/h2c route and changes policy files to permit port 9090. Authorization must still be checked for exact routing header/target and deployment variant. The release warns about Kustomize deploy/ policy's namespaceSelector {} with default allow-all; PR #1880 also modifies an OLM networkpolicy.yaml, so the release's 'OLM installs do not include this NetworkPolicy' must NOT be broadened to 'OLM deployments have no 9090 policy'. The repository-specific effective manifests must be inspected before judging OLM exposure.
Evidence Strength: PRIMARY_IMPLEMENTATION_DIFF / CONFIGURATION-CONDITIONAL
Counterevidence: Helm chart instead restricts egress by sandbox Pod selector; Kustomize and Helm are not interchangeable. Router authentication, Pod identity, network reachability and egress policy are separate gates. No actual deployed policy was observed.
Remaining Uncertainty: live image/configuration/authz settings, CNI policy enforcement, target Pod membership and per-RPC authorization effect.
Promotion Eligibility: BOUNDED_EXTERNAL_STRATEGIC_WATCHLIST / NO_WELCOME_HOST_PROMOTION

### SIG-20261031-02 — Warm-pool adoption and claim status are distinct
Signal ID: SIG-20261031-02
H1 Claim: optimistic-lock 409 drops status updates and stale cache may duplicate Sandbox allocation.
Classification: strategic signal
Verification Status: TWO_DISTINCT_CONTROLLER_SOURCE_PATCHES_INSPECTED
Verification Sources: upstream PR #1944 and #2010.
Repository Record Comparison: H1 supplied release assertion; H2 observes updateStatus retryStatusPatchOnFreshBase on conflict and an authoritativeReader pre-cold-create guard in separate PRs.
Reason: PR #1944 adds an in-pass authoritative status re-read/retry after 409. PR #2010 adds a fresh claim read before cold-create when not force-cold and skips when assigned/UID differs; a failed fresh read can fall back to creation. Do not claim transactional exactly-once allocation for all errors or broad readiness correctness.
Evidence Strength: SOURCE_LEVEL_CODE_AND_TEST_DIFF / NO_TEST_EXECUTION_BY_H2
Counterevidence: the guard explicitly skips forced cold-start paths and continues on authoritative-read error; no independent exhaustive race test observed. A Ready Sandbox is not automatically a Ready claim.
Remaining Uncertainty: real cache lag, retries under API failure, full Pod/create timeline, workload correctness and local applicability.
Promotion Eligibility: BOUNDED_EXTERNAL_MECHANISM / NOT_LOCAL_PROBLEM

### SIG-20261031-03 — Suspend is not workload completion
Signal ID: SIG-20261031-03
H1 Claim: deleted Pod's terminal phase during Suspend could wrongly trigger Finished/TTL cleanup.
Classification: strategic signal
Verification Status: SOURCE_GUARD_AND_TEST_FIXTURE_INSPECTED
Verification Sources: upstream PR #2079, source method computeFinishedCondition and controller test additions.
Repository Record Comparison: same source lineage; no NEXUS/Welcome lifecycle inference.
Reason: new branch returns preexisting Finished condition or nil while Sandbox operatingMode is Suspended. This prevents deriving new Finished from Pod phase during normal suspend; it does NOT erase a previously valid Finished, nor prove all TTL cleanup is safe.
Evidence Strength: PRIMARY_SOURCE_PATCH / CONDITIONAL
Counterevidence: original PR says a Finished recorded before suspend persists; failure while draining can still be distinct from own suspension. Runtime effect depends on claim policy and TTL.
Remaining Uncertainty: real Pod termination ordering, cluster versions, status propagation, destructive effects and actual rollout.
Promotion Eligibility: BOUNDED_EXTERNAL_LIFECYCLE_BOUNDARY

### SIG-20261031-04 — Metrics wrapper and WebSocket Upgrade protocol
Signal ID: SIG-20261031-04
H1 Claim: byte metrics wrapper caused router WebSocket Upgrade regressions, fixed in v1.0.9.
Classification: watchlist
Verification Status: SOURCE_PATCH_AND_TEST_SOURCE_INSPECTED
Verification Sources: upstream PR #2065 proxy.go, metrics transport and WebSocket integration test diffs.
Repository Record Comparison: release claim narrowed to the Go router and upstream unit/integration test source.
Reason: wrapper preserved io.Reader but masked io.Writer after an HTTP 101 handshake; new ReadWriteCloser restoration is explicit. Presence of tests is not executed-test evidence in this run.
Evidence Strength: IMPLEMENTATION_DIFF / NO_LOCAL_HANDSHAKE
Counterevidence: repair depends on upstream writable response body and transport/metrics path; not proof for every bidirectional protocol.
Remaining Uncertainty: deployed router versions and end-to-end stream replay.
Promotion Eligibility: TECHNICAL_WATCHLIST / NO_STRATEGIC_ADOPTION_CLAIM

## ORIENTATION_NOTES
- Release and its five change PRs form one maintainers' ecosystem; they add source-level detail but no independent publisher corroboration or independent execution window.
- Evidence layers: (1) release text, (2) source patch/test code, (3) author-reported tests, (4) independently executed tests, (5) deployed effect. This run verifies only levels 1–2; any upstream test statement remains author report.
- Source/authority correction: OLM policy mention in PR #1880 and release note wording require variant-specific reconciliation; do not collapse a Kubernetes path or deployment mechanism into a universal coverage claim.
- Counterevidence gate failed for any claim of unconditional router exposure, guaranteed exactly-once Sandbox allocation, all Suspend safety, or universally correct WebSockets.
- Welcome current main contains Horizon record H1; it does NOT establish installed Agent Sandbox components or local action authorization.

## NO_DECISION_SECTION
- No Weekly H3 direction chosen, no H4 action, no October H5/H6 memory promotion.
- No Host, NEXUS, Parallax, Kubernetes deployment, source package or Authorization Policy change.
- Host Repository Change: NO.
- Claim promotion: NO universal or local implementation assertion.

## EVIDENCE_DELTA
- NEW_EVIDENCE: five original merged patch surfaces, actual 409 recovery and cold-create guards, Suspended condition rule, writable metrics body restoration, and deployment-policy variant discrepancy.
- CORRECTED_INTERPRETATION: router transport support, network reachability, Pod/claim identity, controller readiness and lifecycle completion represent different authority/effect predicates.
- UNCHANGED_BOUNDARY: external source diff != live execution; same upstream PR cluster != independent verification; Horizon != Welcome host adoption.
- NEW_COUNTEREVIDENCE: weak/failed fresh-read fallback, preexisting Finished preservation, Kustomize/Helm/OLM differences, and source-vs-runtime absence narrow any simplistic 'patch proves safety' claim.
- UNKNOWN_RETAINED: deployment, source-independent replay, CNI/NetworkPolicy effects, per-RPC auth, exactly-once allocation, multi-run status correctness.
- NEXT_RETEST_CONDITION: authorized pinned v1.0.9 disposable Kubernetes test of policy variant, per-RPC unauthorized/authorized target, stale claim adoption with failed authoritative read, Pod suspend with TTL, and WebSocket 101 roundtrip. Capture exact manifests, image, revision, effect receipts, stdout/stderr and exit.

## NEXT_HANDOFF
- W44 H3/H4 may only synthesize this H1/H2 after ISO week 2026-W44 has naturally closed; a duplicate citation adds no independent observation.
- October H5/H6 are NOT_DUE during Oct 31 Shanghai day; later month-close requires naturally ended October and actual 31-day evidence check.
- No NEXUS/host mutation recommended or inferred.

## BOUNDARY_CHECK
- Only new same-day H2 path proposed. Source inspection did not write/execute upstream source, run cluster tests, or alter main directly.
- Prior H1, historical Jules, Horizon policy, Parallax, Host/NEXUS, GitHub Actions unchanged.
- Native Horizon checker and Kubernetes Go/e2e tests: NOT_EXECUTED by this H2 producer; no PASS claim.
