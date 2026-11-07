# H2 Daily Horizon Orient — 2026-11-07

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-07
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / NOT_JULES_REPLAY
Producer Identity: HUMAN_REQUESTED_GPT_NATIVE
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Source Identity: google/adk-python@dd7161f7a2b88cd7ae482cc2acd8423675ac027c
Source Authority For Claim: FIRST_PARTY_COMMIT_PATCH_AND_AUTHORED_TEST_SOURCE
Independent Verification: CODE_BRANCHES_REOPENED / NO_INDEPENDENT_RUNTIME_REPLAY
Evidence Upgrade Basis: SOURCE_BRANCH_COUNTEREXAMPLE_VERIFIED / NO_PROMOTION
Original Execution Status: GPT_NATIVE_BOUNDED_SOURCE_ORIENTATION
Current Path Status: NEW_DRAFT_PROPOSAL_NOT_MERGED
Base Main SHA: 87929b704567c3cc595434538e2a25ab716a563a
Run Identity: welcome-to-github/horizon/H2/2026-11-07/GPT_NATIVE/87929b704567c3cc595434538e2a25ab716a563a/first-party-patch-orientation
Upstream H1: horizon-cortex/2026-11-07-H1-signal-observe.md
Upstream H1 Blob SHA: 2ddb1f398da3986fd35ff76a063420ccb12e2d08
Input Status: SAME_DATE_H1_MERGED_MAIN_VISIBLE / PR_924
Input H1 Task Status: SUCCESS_BOUNDED_STATIC_SOURCE_OBSERVATION
Source Status: FIRST_PARTY_EXACT_COMMIT_AND_CODE_TEST_DIFF_READ / NO_NATIVE_REPLAY
Network Status: PRIMARY_GITHUB_COMMIT_AND_CHANGED_FILE_PATCH_READ
Task Status: SUCCESS_BOUNDED_STATIC_ORIENTATION / NO_HOST_DECISION
Host Applicability: UNKNOWN
Write Scope: horizon-cortex/2026-11-07-H2-horizon-orient.md
Boundary Violation: NO

## INPUT_RECORD
- Fresh merged main 87929b704567c3cc595434538e2a25ab716a563a was read after H1 #924 merged; exact same-date H1 blob 2ddb1f398da3986fd35ff76a063420ccb12e2d08 establishes visible admissible input. Earlier duplicate H1 proposal #925 was closed unmerged, not a second observed signal or independent source.
- Prior canonical 2026-11-06 H2 covers ADK pass@k/pass^k; today H1 instead concerns evaluator-input thought filtering. Closed W44 and October baselines are historical; W45 and November remain OPEN / NOT_DUE.
- Direct recheck of original https://github.com/google/adk-python/commit/dd7161f7a2b88cd7ae482cc2acd8423675ac027c and its changed-file patches at this research execution. Source commit timestamp 2026-11-07T08:58:18Z is publisher Git time, not release or execution date. All paths belong to ONE original issuer lineage.

## SOURCE_VERIFICATION_RECORDS
### SRC-20261107-H2-01 — plain text judge projection
URL: https://github.com/google/adk-python/commit/dd7161f7a2b88cd7ae482cc2acd8423675ac027c
Exact source files: src/google/adk/evaluation/llm_as_judge_utils.py, src/google/adk/evaluation/hallucinations_v1.py, src/google/adk/evaluation/rubric_based_multi_turn_trajectory_evaluator.py
Observed code: get_text_from_content now routes Content text through extract_text_from_content; hallucination intermediate response selection requires p.text and not p.thought; rubric assembled dialogue uses the same extraction helper. These are source-level conditional behaviors, not observed production scores.
Authored test diffs: tests/unittests/evaluation/test_llm_as_judge_utils.py and test_hallucinations_v1.py exercise thought-only and mixed parts. Test source was inspected; test execution: NOT_EXECUTED.

### SRC-20261107-H2-02 — structured Vertex counterexample
URL: https://github.com/google/adk-python/blob/dd7161f7a2b88cd7ae482cc2acd8423675ac027c/src/google/adk/evaluation/vertex_ai_eval_facade.py
Single-turn _get_text calls extract_text_from_content because the metric receives plain text without the thought flag. In contrast, _map_invocation_turn intentionally retains thought-bearing structured parts inside ConversationTurn, leaving handling to Vertex. No Vertex external request was run; downstream metric behavior remains UNKNOWN.
Authority: SAME_PUBLISHER_LINEAGE / FIRST_PARTY_COMMITTED_DIFF / NOT_INDEPENDENT_REPLICATION.

## SIGNAL_CLASSIFICATION
Signal ID: SIG-20261107-H01
H1 Claim: ADK evaluation-input projection now excludes thought parts for selected text judging paths.
Classification: weak signal / watchlist
Verification Status: DIRECT_SOURCE_PATCH_CORROBORATED / BOUNDED
Verification Sources: SRC-20261107-H2-01 and SRC-20261107-H2-02 (one canonical commit, not two independent sources)
Repository Record Comparison: H1 blob 2ddb1f398da3986fd35ff76a063420ccb12e2d08; prior Nov6 H2 concerned multi-run aggregation; prior W44/October do not authorize host or Horizon policy mutation.
Reason: source-level input projection and authored negative tests support a narrow technical change; official release, actual evaluator behavior, Vertex structured transport, external adoption and score effects have not been tested.
Evidence Strength: HIGH_FOR_CODE_DIFF / UNKNOWN_FOR_RELEASED_RUNTIME
Counterevidence: structured multi-turn Vertex path intentionally retains thought flags; universal removal, privacy guarantee or all-evaluators-fixed interpretation would be false.
Remaining Uncertainty: actual test and runtime receipts, version tag, metric output, structured Vertex judge handling, affected integrations and host applicability.
Promotion Eligibility: WATCHLIST_ONLY / NOT_ELIGIBLE_FOR_DURABLE_HORIZON_MEMORY

## ORIENTATION_NOTES
- NEW_EVIDENCE: independently reopened the upstream commit and examined the exact plain-text extraction changes, authored tests and preserved structured Vertex exception.
- CORRECTED_INTERPRETATION: judge input is a path-specific typed projection; a filtered plain-text evaluator does not imply all structured downstream consumers discard thought parts.
- UNCHANGED_BOUNDARY: H1 and H2 repeat the same issuer source and cannot be counted as independent validations, actual execution, product release or Welcome adoption.
- NEW_COUNTEREVIDENCE: _map_invocation_turn deliberately retains thought-bearing structured parts, so universal absence is contradicted at source level.
- UNKNOWN_RETAINED: independent runtime behavior, exact tagged shipping version, Vertex metric internals, benchmark-score delta and any host effect.
- NEXT_RETEST_CONDITION: pin ADK and Vertex versions; run a mixed visible-answer/thought fixture through both single-turn text and structured multi-turn evaluator, capture exact outgoing payload and scores under one harness identity.

## NO_DECISION_SECTION
Decision: NO_DECISION.
No H3 weekly priority change, Horizon memory promotion, host/NEXUS/Parallax implementation change, GitHub Actions change or policy inference from this single source family.

## NEXT_HANDOFF
- H3 may consider this one bounded source observation when ISO W45 closes; do not count H1/H2 as two independent changes or treat Nov7 as a complete week.
- Revisit only upon release/runtime receipt, independent test or falsifier addressing structured Vertex handling. Missing independent receipts remain UNKNOWN.

## BOUNDARY_CHECK
- New same-date H2 file only, after matching H1 became visible on main. No old H1/H2 edits, no original Jules history rewrite, no host code or active state writes.
- Author tests and GitHub diff were inspected; ADK tests, Vertex and Welcome host runtime NOT_EXECUTED. Structural checker execution NOT_EXECUTED until independently run.
- Boundary Violation: NO
