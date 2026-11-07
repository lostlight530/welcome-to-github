# H1 Daily Signal Observe — 2026-11-07

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-07
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / NOT_JULES_REPLAY
Producer Identity: HUMAN_REQUESTED_GPT_NATIVE
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 174fb95f787c604f0fd40a8cdabea4da2c3f3aa2
Run Identity: welcome-to-github/horizon/H1/2026-11-07/GPT_NATIVE/174fb95f787c604f0fd40a8cdabea4da2c3f3aa2/h1-primary-commit-01
Source Identity: google/adk-python@dd7161f7a2b88cd7ae482cc2acd8423675ac027c
Source Authority For Claim: FIRST_PARTY_COMMITTED_CODE_AND_AUTHORED_TESTS
Independent Verification: COMMIT_AND_FILE_PATCHES_READ / NO_INDEPENDENT_RUNTIME_REPLAY
Host Applicability: UNKNOWN
Evidence Upgrade Basis: NEW_SOURCE_COMMIT_VERIFIED_NOT_RELEASED_OR_EXECUTED
Original Execution Status: GPT_NATIVE_BOUNDED_STATIC_SOURCE_OBSERVATION
Current Path Status: NEW_DRAFT_PR_NOT_MERGED
Task Status: SUCCESS_BOUNDED_STATIC_SOURCE_OBSERVATION
Write Scope: horizon-cortex/2026-11-07-H1-signal-observe.md
Boundary Violation: NO

## INPUT_RECORD
- Cold-start source of truth: current `main` 174fb95f787c604f0fd40a8cdabea4da2c3f3aa2; previous canonical H1/H2 dated 2026-11-06 exist and were read. Yesterday's ADK topic was pass@k/pass^k aggregation; this record covers a different evaluation-input contract.
- Previous W44 H3/H4 and October H5/H6 exist on main. W45 is not closed as of 2026-11-07 Shanghai, so no H3/H4. November is open, so no H5/H6.
- No same-date H1 artifact or competing open H1 PR existed at preflight. Later branch/PR creation is delivery evidence, not the original source's execution evidence.
- Original public upstream GitHub commit + changed-file code/test patches inspected by the GitHub connector. Neither ADK package installation nor the Welcome host runtime was executed.
- This observation is separate from A1/A2 repository maintenance and independent of the current host's NEXUS / Parallax implementation.

## EXTERNAL_SOURCE_RECORDS
### SRC-20261107-H01 — evaluation thought-part exclusion
Source ID: SRC-20261107-H01
Title: fix(eval): stop judge and Vertex metrics from scoring model thoughts
Publisher: google/adk-python, first-party repository
URL: https://github.com/google/adk-python/commit/dd7161f7a2b88cd7ae482cc2acd8423675ac027c
Published or Updated Date: 2026-11-07T08:58:18Z (commit clock; 2026-11-07 16:58:18 Asia/Shanghai)
Date Checked: 2026-11-07
Source Type: PRIMARY_GITHUB_COMMIT_AND_CODE_TEST_DIFF
Evidence Tier: HIGH_FOR_COMMIT_CONTENT / UNKNOWN_FOR_EXECUTION_AND_RELEASE
Access Status: ORIGINAL_COMMIT_AND_CHANGED_FILE_PATCH_READ
Independent Source: ONE_GOOGLE_ADK_SOURCE_LINEAGE
External Claim: several evaluator text extraction paths were changed to skip `Part.thought` when constructing text for an LLM judge, hallucination evaluator, rubric dialogue or single-turn Vertex metric.
Confidence: HIGH_FOR_AUTHORED_DIFF / NO_ADK_TEST_RUN
Limitations: new authored tests and patch do not establish CI outcome, release inclusion, every Vertex route, or downstream judge behavior.
Host Applicability: UNKNOWN / WELCOME_NEXUS_NOT_INSPECTED_FOR_ADOPTION

## RAW_SIGNAL_LOG
### SIG-20261107-H01 — EVALUATOR_OBSERVATION_SURFACE_IDENTITY
Signal ID: SIG-20261107-H01
Source IDs: SRC-20261107-H01
Observed Change: `evaluation/llm_as_judge_utils.py` now calls `extract_text_from_content`; `evaluation/hallucinations_v1.py` excludes `p.thought` from intermediate natural-language response scoring; rubric dialogue assembly and single-turn Vertex text extraction similarly use thought-aware text extraction.
Observed Test Design: authored unit cases exercise response text with `Part.thought=True`, including a judge's draft thought that conflicts with final JSON. These are source tests, not observed successful executions.
Critical Counterexample: the same upstream change explicitly retains thought-bearing structured parts when mapping multi-turn `ConversationTurn` to Vertex; a single-turn plain-text filtering fix MUST NOT be generalized into a promise that every evaluator or vendor receives zero thought-bearing data.
Research Question: which exact observable response projection is fed to each evaluator, and can acceptance scores be changed by content that was not user-visible?
Why It Matters: evaluation input domain and redaction boundary are part of a metric's contract; an answer score should not silently depend on hidden model thought fields.
Noise Filter: source-level regression patch is NOT equivalent to an SDK release, runtime rollout, privacy guarantee, model improvement, or measured benchmark quality gain.
Host Change: NO
Independent Replay: NOT_EXECUTED

## EVIDENCE_DELTA
- NEW_EVIDENCE: original ADK commit and authored evaluator/test patches show a concrete thought-vs-visible-text projection change.
- CORRECTED_INTERPRETATION: benchmark evaluator input is a typed observation surface, not necessarily the full model content object.
- UNCHANGED_BOUNDARY: issuer authored tests, GitHub commit and host runtime are three different evidence classes; one source family is counted once.
- NEW_COUNTEREVIDENCE: multi-turn structured Vertex `ConversationTurn` deliberately retains thought flags and delegates visibility to Vertex metrics; zero-exposure claim is disproved by source design.
- UNKNOWN_RETAINED: actual test outcomes, SDK tag, third-party Vertex behavior, independent validation, host integration, privacy behavior and benchmark effect.
- NEXT_RETEST_CONDITION: pin released ADK commit and evaluator path; construct mixed thought+answer parts with conflicting judge JSON; capture exact outgoing evaluation payload and numeric decision under one fixed environment.

## NEXT_HANDOFF
- H2 is eligible ONLY after this canonical 2026-11-07 H1 file is on merged main. H2 must bind to the exact H1 blob and independently inspect the plain-text versus structured Vertex behavior.
- In the interim, H2 input state is `WAITING_FOR_MERGED_H1`, not a completed same-date research task.
- No W45 Weekly decision, November Monthly compression, policy promotion, host runtime mutation, Parallax/NEXUS modification or CI success is asserted.

## BOUNDARY_CHECK
- One prospective canonical H1 date artifact only, no old file edits, Jules history change or private producer prompt.
- GitHub source observation is not proof of live ADK execution. Native checker: NOT_EXECUTED by this research production; GitHub PR Checks remain separately inspectable.
- Boundary Violation: NO
