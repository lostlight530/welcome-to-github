# H1 Daily Signal Observe — 2026-11-15

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-15
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Source Identity: google/adk-python issue #8058; source main d05e482038bdbb226c3a1179550cf83bd8fcbefb; fix draft PR #8119
Source Authority For Claim: UPSTREAM_ISSUE_REPORT / SOURCE_LEVEL_MAIN_INSPECTION / MAINTAINER_REPRODUCTION_COMMENT
Independent Verification: UPSTREAM_MAINTAINER_REPORTED_REPRODUCTION / NO_LOCAL_EXECUTION / NO_RELEASE_FIX_VERIFICATION
Host Applicability: UNKNOWN / NO_WELCOME_ADK_INTEGRATION_OBSERVED
Evidence Upgrade Basis: EXACT_ISSUE_PLUS_PINNED_SOURCE_AND_NEGATIVE_CONTROL_REVIEW / NO_HOST_PROMOTION
Original Execution Status: GPT_NATIVE_BOUNDED_SOURCE_OBSERVATION_COMPLETED / UPSTREAM_RUNTIME_NOT_EXECUTED
Current Path Status: DRAFT_PR_PENDING_HUMAN_REVIEW
Base Main SHA: 748b563b1645819cb10e8ac0c00dcfdd99af0f9e
Run Identity: welcome-to-github/horizon/H1/2026-11-15/GPT_NATIVE/748b563b1645819cb10e8ac0c00dcfdd99af0f9e/adk-workflow-output-replay-observe-01
Observation Window: 2026-11-15 Asia/Shanghai; upstream issue created 2026-11-09T16:03:32Z
Task Status: SUCCESS_BOUNDED_SOURCE_OBSERVATION / RUNTIME_UNVERIFIED
Network Status: GITHUB_API_EXACT_SOURCE_READ
Source Status: ISSUE_AND_WORKFLOW_MAIN_READ / NO_ADK_EXECUTION
Write Scope: horizon-cortex/2026-11-15-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Checked fresh merged Welcome main 748b563b1645819cb10e8ac0c00dcfdd99af0f9e, current Horizon policy, Nov 14 H1/H2, W45 H3/H4; new logical-date H1/H2 absent, and no open PR at preflight.
- Source discovery was new to this repository's Nov 15 H1, not a claim that the upstream source was published today. W46 ends at 2026-11-15 23:59:59 Asia/Shanghai and remains OPEN at this observation; H3/H4 and November H5/H6 are NOT_DUE.
- Opened upstream issue #8058 through GitHub API; checked issue creation/update and maintainer response with claimed reproduction on a pinned earlier upstream main, plus current upstream main source at d05e482038bdbb226c3a1179550cf83bd8fcbefb.
- Opened upstream Draft PR #8119 metadata: it was open, draft, unmerged at inspection; its title is not proof of a merged patch or passing tests. The maintainer's reported local results remain external-reported evidence.
- No ADK 2.14 package, author script, workflow runner, NEXUS host, Parallax, production event sink or CI suite was executed here.

## EXTERNAL_SOURCE_RECORDS
Source ID: SRC-20261115-H01
Title: Resumable Workflow re-persists every fast-forwarded output on each resume
Publisher: google/adk-python, issue contributor and subsequent maintainer response
Canonical Source Identity: google/adk-python/issues/8058 (issue), google/adk-python@d05e482038bdbb226c3a1179550cf83bd8fcbefb (current source snapshot), PR #8119 (unmerged proposed fix)
URL: https://github.com/google/adk-python/issues/8058
Source Code URL: https://github.com/google/adk-python/blob/d05e482038bdbb226c3a1179550cf83bd8fcbefb/src/google/adk/workflow/_workflow.py
Candidate Fix URL: https://github.com/google/adk-python/pull/8119
Issue Created: 2026-11-09T16:03:32Z
Issue Updated: 2026-11-13T04:09:06Z
Date Checked: 2026-11-15 Asia/Shanghai
Evidence Tier: PRIMARY_FOR_ISSUE_AND_SOURCE_BRANCH / REPORTER_AND_MAINTAINER_REPRODUCTION_NOT_OURS
Access Status: GITHUB_API_OPEN / EXACT_MAIN_SOURCE_OPEN / UPSTREAM_PR_METADATA_OPEN
Independent Source Count: ONE_UPSTREAM_REPOSITORY_LINEAGE; the maintainer's separate reproduction report is not a cross-platform deployment validation
Claim Supported: Upstream main's _handle_completion invokes _maybe_reemit_replayed_output for replayed nodes; helper enqueues Event(output=...) when is_resumable and output is present. The issue describes a repeated-resume case where already-persisted outputs are emitted again.
Maintainer Report: On source revision 59b0dd63, a commenter reports repeating the issue script, observing a descending [10,9,...,1] output-copy pattern and 6,055 events at 100 rounds; their proposed conditional re-emission reports 1,105 events instead. Neither number was measured by this producer.
Claim Not Supported: a general exactly-once guarantee, the fix being merged or released, every resumable workflow affected, incident in Welcome, or a completed local reproduction.
Confidence: HIGH_FOR_READ_CODE_BRANCH_AND_REPORTED_ISSUE / INDEPENDENT_RERUN_UNKNOWN
Limitations: replayed nodes with no previously recovered output may legitimately need a first emission; blindly suppressing all replay emissions can break RequestInput resume semantics.

## RAW_SIGNAL_LOG
Signal ID: SIG-20261115-H01
Signal: WORKFLOW_RESUME_EVENT_DELIVERY_NOT_IDENTICAL_TO_UNIQUE_PERSISTED_OUTPUT
Mechanism: completion of an already-replayed node can re-emit an output to the session, so the same logical node-output identity may be stored more than once across resumptions.
Why It May Matter: state-continuity, durable session growth, replay provenance and monitoring denominators require separating logical output, emitted event and appended persistent event.
Source IDs: SRC-20261115-H01
Evidence Tier: PINNED_UPSTREAM_CODE_PLUS_ISSUE_REPORT / NO_LOCAL_REPRO
Noise Filter: Nov 9 issue newly inspected on Nov 15, not claimed as Nov 15 release or confirmed platform-wide regression.
Independent Upgrade Eligibility: WATCHLIST_ONLY, until revision-pinned direct replay checks and a target host dependency are established.
Needs H2 Verification: YES

## EVIDENCE_DELTA
- NEW_EVIDENCE: source-pinned replay branch and upstream maintainer-reported duplicated outputs under a bounded repeating RequestInput test, with distinct fix PR status.
- CORRECTED_INTERPRETATION: a durable event stream can have multiple persisted emission records for one logical recovered output; event counts do not imply distinct tool or workflow executions.
- UNCHANGED_BOUNDARY: SOURCE_OBSERVED != ADK_REPRODUCED != WELCOME_ADOPTED; REPORTER_REPRO != OUR_EXECUTION; SOURCE_FIX_PR != RELEASED_FIX.
- NEW_COUNTEREVIDENCE: newly answered RequestInput output may have no persisted counterpart and require emission on its first resume; blanket suppression would lose legitimate information.
- UNKNOWN_RETAINED: affected released versions beyond reporter's 2.14.0, patch reachability in release, actual persistence under multiple backends, branch-specific semantics, local target relevance.
- NEXT_RETEST_CONDITION: pin ADK 2.14.0 and the #8119 head; run 1/10/100 resumed RequestInput rounds with a stable logical output ID, capture append counts per ID, session bytes, stdout/stderr/exit, and verify both prior-completed output suppression and new-answer retention.

## NEXT_HANDOFF
- H2 requires the exact same-day H1 original PR to merge and become visible on fresh main; then independently reopen both unchanged and proposed code branches and challenge the issue's reproduction denominator.
- No H2, H3, H4, H5, H6 or host migration task is substituted or credited by this H1 observation.

## BOUNDARY_CHECK
- One dated H1 record only, with an older source publication clearly dated; no historical records, host NEXUS, Parallax, workflow, config, runtime, database, or memory changed.
- Structural checker and native runtime tests: NOT_EXECUTED in this connector-only repository execution environment; GitHub API source inspection was performed.
- Human Maintainer approval and merge remain pending; no authorization to treat this record as adopted host functionality.
