# 2026-10-01 External Review Source-Scope Correction — welcome-to-github

## Correction identity

- Repository: `lostlight530/welcome-to-github`
- Logical date: 2026-10-01 Asia/Shanghai
- Base main SHA: `8cd52cdbb8b9a40c568545a1ca1a29f3f84375f7`
- Predecessor audit PR: #661
- Predecessor audit path: `historical-audits/2026-10/2026-10-01-external-independent-gpt-review.md`
- Predecessor audit blob: `7f3418444265daccf1de3f73f3a5209b93ae1799`
- Record class: FORWARD_CORRECTION / SOURCE_SCOPE_RECONCILIATION
- Historical rewrite: NO
- Native task execution claimed: NO
- Runtime or test execution claimed: NO

## What this corrects

The predecessor audit uses the phrase `global nine-document audit set (A1/A2/A3/A4/A5/G1/G2/H1/H3)`.

In that predecessor record, those nine labels are nine review-control dimensions defined inside the audit itself. They are not inspectable evidence that nine maintainer-private project source documents were individually reviewed source-by-source.

This correction removes that ambiguity prospectively. It records a maintainer-authorized reconciliation against the full private project recovery set without publishing private filenames, prompts, memory, hidden reasoning, or local control-plane text.

The predecessor audit remains sealed historical evidence for the review it actually performed. Its repository observations are not silently invalidated or rewritten by this correction.

## Authority and evidence boundary

Current repository truth remains authoritative in this order:

1. current merged main and current implementation;
2. current machine-readable and canonical repository contracts;
3. current repository governance and maintenance contracts;
4. current verified execution evidence;
5. cross-repository maintenance design used as a bounded reconciliation input;
6. historical audit records and old memory.

A private control-plane source can calibrate an Independent GPT maintenance decision. It does not become repository-native authority merely because it was consulted.

## Two-cycle maintenance reconciliation

The project maintenance model now distinguishes these layers:

```text
NATIVE TASK DELIVERY
!= A1 FULL-COVERAGE MAINTENANCE
!= A2 CURRENT MONTH RELATIONAL VERSION
!= PERIODIC AUDIT
!= DURABLE GOVERNANCE
```

For a natural-month day N:

- A1 covers Month Start through N-1 and makes an explicit per-artifact decision;
- A1 must be merged before A2 starts;
- A2 must fresh-read the new current main and integrate day N into the fixed current-month relational state;
- D7, D10, D14, and D30 are separate cross-window audits;
- natural-month close remains separate from D30;
- no layer may manufacture research batches, source independence, execution windows, audit credit, CI PASS, runtime evidence, or scientific validity.

## 2026-10-01 time boundary

For October 1, the October A1 prior-day interval is empty.

This correction is not an A1 execution and does not manufacture a vacuous A1 delivery merely to create activity.

This correction also does not initialize the October A2 relational version. A2 requires the applicable current-day native artifacts and a merged A1 authority base. This record does not establish that the repository's October 1 native production and delivery are complete.

Therefore:

- October native production completeness: NOT_ESTABLISHED_BY_THIS_RECORD;
- October A1 execution: NOT_EXECUTED_BY_THIS_RECORD;
- October A2 execution: NOT_EXECUTED_BY_THIS_RECORD;
- D7/D10/D14/D30 audit: NOT_DUE / NOT_EXECUTED_BY_THIS_RECORD;
- October future task success: NOT_CLAIMED.

## Repository-specific boundary retained

Horizon Cortex, Parallax, Welcome Host, and bounded NEXUS remain separate evidence and execution planes. Horizon or Parallax evidence does not become Host or NEXUS runtime fact by aggregation.

The September evidence-freeze and close-reconciliation records remain historical point-in-time evidence. The October predecessor audit remains historical point-in-time evidence. Later October production must not be backdated into either record.

## Decision

- Predecessor source-scope wording: AMBIGUOUS, CORRECTED_FORWARD.
- Predecessor historical body: PRESERVED.
- Current repository-native contract rewrite required by this correction: NO.
- Current runtime repair required by this correction: NO.
- October A1/A2 production claimed: NO.
- Research or audit credit added: ZERO.
- Private control-plane content published: NO.

When October 1 native production is actually present on current main, any A1/A2 maintenance run must restart from fresh repository truth, recheck overlap, preserve native task chronology, and follow the then-current repository contract.

## Delivery verification contract

This change is intentionally additive and limited to one correction record.

Required merge gate:

- exact base main remains known;
- no overlapping foreign PR exists;
- aggregate `main...head` diff contains only this correction file;
- branch is not behind main;
- exact reviewed head SHA is used for merge;
- no unexecuted repository test is reported as PASS.

Full repository test execution: NOT_EXECUTED.

## Rollback

Revert only the commit adding this correction record. Do not alter the predecessor audit, September records, Horizon artifacts, Parallax history, Host state, NEXUS state, or unrelated repository authority.

SOURCE_SCOPE_CORRECTION_END
