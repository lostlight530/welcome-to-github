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
Agent: GPT-6
Producer Identity: GPT_NATIVE / NOT_JULES_REPLAY
Base Main SHA: 29bcfe87d650d94d8163b5c33f3a4053fc490be3
Run Identity: welcome/horizon/H1/2026-11-07/GPT_NATIVE/29bcfe87d650d94d8163b5c33f3a4053fc490be3/01
Task Status: SUCCESS_BOUNDED_PRIMARY_CODE_OBSERVATION
Network Status: FIRST_PARTY_COMMIT_AND_PATCH_READ
Runtime Verification: NOT_EXECUTED
Write Scope: horizon-cortex/2026-11-07-H1-signal-observe.md

## INPUT_RECORD
- Cold-started from current main, reviewed canonical Horizon README, evidence policy, prior 2026-11-06 H1/H2, W44 and October output existence, and open Draft PR #920 (separate maintenance correction).
- This is a new GPT-native observation, not an edit to Jules history, an A1/A2 maintenance record, or evidence of host adoption.
- Source cutoff: original upstream commit timestamp 2026-11-07T08:58:18Z (2026-11-07T16:58:18+08:00); checked on 2026-11-07 Asia/Shanghai.

## EXTERNAL_SOURCE_RECORD
Source ID: SRC-20261107-H01
Title: fix(eval): stop judge and Vertex metrics from scoring model thoughts
Issuer: google/adk-python
Canonical URL: https://github.com/google/adk-python/commit/dd7161f7a2b88cd7ae482cc2acd8423675ac027c
Source identity: original commit dd7161f7a2b88cd7ae482cc2acd8423675ac027c; issuer code and authored regression-test patch, not a release tag
Source date: 2026-11-07T08:58:18Z
Independent source families: 1
Evidence: issuer code replaces naive Part.text extraction with extract_text_from_content for judge inputs; excludes Part.thought from intermediate natural-language hallucination steps. Authored tests explicitly inject thought=true parts and check that text-only judge inputs exclude them.
Nuance: multi-turn Vertex ConversationTurn mapping retains thought-bearing structured parts with the thought flag; this patch does NOT establish that every downstream Vertex evaluator ignores them.
Evidence tier: PRIMARY_STATIC_IMPLEMENTATION_AND_TEST_DESIGN
Test execution: NOT_EXECUTED
Release adoption: UNKNOWN

## RAW_SIGNAL_LOG
Signal ID: SIG-20261107-H01
Claim: evaluation input projection and model output identity are different surfaces; a thought-bearing structured Part must not be silently counted as a user-visible response in text-only scoring.
Technical layer: EVALUATION_HARNESS / DATA_PROJECTION / OBSERVABILITY
Why new: a dated upstream source-level change and explicit regression cases, distinct from the Nov6 pass@k/pass^k cross-run scoring feature.
Counterexample: if a downstream evaluator receives structured content and itself chooses whether to consume thought parts, the plain-text filtering behavior cannot be generalized to that evaluator.
Noise/duplication: one ADK lineage; repeated tests and multiple modified files are not independent external sources.
Confidence: HIGH_FOR_PATCH_INTENT_AND_EXACT_DIFF / UNKNOWN_FOR_RUNTIME_RESULT
Host relevance: RESEARCH_LEAD_ONLY; no Welcome runtime integration or production effect inferred.

## EVIDENCE_DELTA
- NEW_EVIDENCE: upstream commit and test additions define a concrete exclusion boundary for thought parts in text-only evaluation.
- CORRECTED_INTERPRETATION: a judge's visible text input and a full structured trajectory are not interchangeable; evaluation denominators must name which surface was scored.
- UNCHANGED_BOUNDARY: original patch != executed test != released artifact != local deployment.
- NEW_COUNTEREVIDENCE: structured Vertex trajectory retains thought flags, so global "all evaluators exclude thoughts" is unsupported.
- UNKNOWN_RETAINED: actual CI outcome, deployed version, metric effect size, host adoption.
- NEXT_RETEST_CONDITION: pin ADK commit and evaluator type; feed one visible answer and one thought=true distractor; capture exact judge input and compare structured Vertex path separately.

## NEXT_HANDOFF
H2 is BLOCKED until this exact H1 is merged and visible on main. H2 must independently re-read source, test the structured-vs-text counterexample, and retain release/host UNKNOWN.
No H3–H6, host files, governance, A1/A2 maintenance or historical records modified.
