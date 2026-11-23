# Independent GPT Governance — Horizon Relay

Status: current public recovery kernel  
Calibration: 2026-09-17  
Scope: repository-local maintenance recovery, independent review handoff, reconciliation, and bounded repair

This directory is the public handoff point for a memoryless Independent GPT reviewer. It routes the reviewer to repository-native authority without duplicating native producer instructions or exposing private operator context.

## Recovery order

For the maintenance subject under review, recover current truth from current merged `main` first. Prefer current implementation and the current subject-specific contract or policy over dated maintenance prose. Use dated audits/reconciliations, handoffs, and prior model recollection only as point-in-time or secondary recovery evidence.

At start record current date, default branch, exact `main` SHA, relevant open pull requests, active maintenance branches, recent merged changes, and checks actually executed.

## Repository map

Use only the surfaces needed for the question:

1. `README.md`, current source, and current frontend files for the present public surface when relevant.
2. `horizon-cortex/EVIDENCE_POLICY.md` for Horizon evidence semantics.
3. Current dated `horizon-cortex/` artifacts for repository-visible Horizon output.
4. `parallax/README.md` and `parallax/METHOD.md` for Parallax research-production semantics; Parallax records/CASES/NOTES remain Parallax evidence, not Horizon evidence.
5. `governance/README.md` for repository-level maintenance/control routing.
6. `.github/workflows/` plus revision-matched observed workflow runs for GitHub Actions evidence.
7. `historical-audits/INDEX.md` for corrections, period audits, closure ledgers, maintenance, and reconciliation history.
8. Git history and open/merged PR chronology when producer identity, original path, timing, overlap, or historical/current state is disputed.

## Task identity and idempotency

Treat a maintenance run as a tuple of repository, maintenance surface/task, logical period when applicable, producer, exact base revision, and run identity when available.

Before writing:

- confirm fresh `main`;
- inspect overlapping open PRs and active maintenance branches;
- determine the owning maintenance/control file;
- check whether the same logical repair already exists or has merged;
- refresh assumptions if `main` advances materially.

If another live change owns the same maintenance surface or period, use `COORDINATE` rather than creating a parallel repair. Never write merely to test whether writes are possible.

## Evidence boundaries

Keep identity explicit:

- native Horizon output remains native Horizon output;
- GPT Web or other substitute output retains its actual producer identity;
- Parallax is not Horizon;
- Parallax Daily research production is not a maintenance/no-change task;
- GitHub Actions proves only the execution actually observed for the referenced revision;
- a workflow definition, file path, or later success does not prove an earlier run;
- independent governance is a maintenance/review layer, not native task execution.

Do not infer `SUCCESS`, network access, source independence, deployment health, current truth, or historical execution from file presence alone.

An unrun checker, Parallax checker, workflow, or local command is `NOT_EXECUTED`. Contract inspection is not checker execution.

## History discipline

Historical records are point-in-time evidence. Later evidence may change current interpretation, but it does not rewrite what an earlier run observed.

Preserve degraded, blocked, rejected, missing, negative, partial, unverified, no-conclusion, and unknown states. Archive relocation is not semantic replacement. If a historical runtime/producer fact is not recoverable from repository-visible evidence, keep it `UNKNOWN`.

Use the current owning maintenance/control file for a current maintenance correction when safe. Use a dated historical correction/reconciliation only when the historical artifact itself requires a forward correction or provenance pointer.

## Maintenance outcome

Use one of these states when useful:

- `HEALTHY` — reviewed maintenance surface has no confirmed defect;
- `REPAIR` — a confirmed maintenance defect has a safe bounded repair;
- `COORDINATE` — another live change owns the same surface or period;
- `BLOCKED` — authority, current state, or safe delivery cannot be established.

When no confirmed maintenance defect exists, the action is `NO_CHANGE_REQUIRED`: no activity-only edit, branch, or PR.

If repair is justified, change only the owning current maintenance/control file(s) and direct synchronized projections. Horizon/Parallax research artifacts and unrelated implementation are not default edit targets unless the current owning contract or maintainer explicitly makes them part of the repair.

## Delivery discipline

For a justified repair:

1. branch from exact fresh `main`;
2. make the bounded maintenance/control-plane change;
3. run only available targeted validation and retain its real result;
4. refresh `main` and overlap state before delivery;
5. inspect the aggregate `main...branch` diff;
6. open one Draft PR;
7. stop for maintainer review.

Do not push directly to `main`, force-push history, auto-merge, or claim a checker/CI PASS that was not actually observed.

## Public boundary

This recovery kernel is intentionally repository-bounded. It neither requires nor attempts to reconstruct private Jules task prompts, repository memory, credentials, hidden reasoning, or unrelated orchestration. Repository-visible evidence is sufficient for an independent repository maintenance decision; unavailable context remains unavailable rather than guessed.

The repository currently has no public `AGENTS.md`; do not infer one from private task controls or prior conversations.

## Public-release privacy preflight — 2026-10-26

Apply this check to the complete proposed publication, not only the changed Markdown file

1. **Public allowlist:** disclose repository-visible task identity, exact Git refs, authorized scope, evidence status, non-sensitive validation results, risks and rollback; do not reconstruct off-repository private controls
2. **Pre-publish review:** inspect the final `main...branch` diff, PR title and description, intended comments, report attachments, copied command output and log excerpts for material that is not authorized for public distribution
3. **Withhold restricted material:** never reproduce passwords, API credentials, access tokens, confidential instructions, private workspace memory, hidden reasoning, private personal information or nonpublic addresses in repository files, PRs, screenshots or logs
4. **Fail closed:** when a suspect disclosure cannot be ruled out, stop publication and request a confidential maintainer decision; report only the issue category and affected surface, without quoting the underlying material
5. **After confirmed exposure:** coordinate private incident response and relevant credential revocation/rotation; a follow-up edit alone does not remove old commits, caches or copies

The check is a maintenance publication rule, not evidence of a historical secret scan, native scientific run, CI gate, or verified cancellation of a private scheduler. Retain original producer identity and historical research outcomes.

## Handoff minimum

A durable handoff should make it possible to recover:

- base `main` SHA and delivery head;
- maintenance scope and owning files;
- relevant logical period if any;
- overlapping PR/branch state;
- checks actually run and checks not run;
- confirmed defect or `NO_CHANGE_REQUIRED` basis;
- unresolved items and negative evidence;
- whether Horizon/Parallax producer identity and history were preserved;
- whether the Draft PR is clean against current `main`.

No separate audit artifact is required merely to prove that review happened. Prefer the owning maintenance source plus Draft PR description as the delivery summary.

Final merge and doctrine authority remains with the maintainer.

## 2026-11-11 scoped independent A1/A2 acceptance clarification

This public recovery note records an evidence-based interpretation correction for the Nov01–11, 2026 window. See [dated original-PR reconciliation](../../historical-audits/2026-11/2026-11-11-a1a2-effective-pr-acceptance-reconciliation.md). It does not amend native production authority, retroactively modify PRs, or replace the independent periodic audit.

- Independent A1 = complete applicable MonthStart..N−1 source/artifact coverage, evidence inspection and per-file disposition, not merely a yesterday note.
- Independent A2 = complete MonthStart..N relationship/current-state version, starting only after its original A1 is merged and freshly reread from main.
- Real, non-duplicated custody rows, source identity, exact SHA/path references, per-file decisions, NO_FOLLOW_UP with examined basis, provenance deltas, relationship revisions, negative evidence and correction records are valid maintenance content.
- An effective 100-line PR does **not** require 100 distinct novel scientific claims, 100 independent external issuers or invented daily changes.
- GitHub original PR additions >=100 remains a separate hard numeric check; count at its own final merged head, never across successors, cleanup, other PRs or repositories.
- Do not count boilerplate, filler, repeated text inserted only to inflate additions, fake checks or unsupported scientific assertions as effective content.
- Review task coverage, semantic quality, Git merge, native production state, actual execution checks and current main retention as distinct evidence dimensions.
- Early Draft NOT_MET may describe an earlier head; after same-original-PR supplementation inspect final diff and record final-head assessment without erasing the Draft event.
- A numerically short original can still be a real merged maintenance delivery; preserve NUMERIC_NOT_MET while stating the actual completed scope accurately.
- Actual BLOCKED/PARTIAL/UNKNOWN native gaps remain unresolved unless direct native/runner evidence shows otherwise; maintenance never invents host execution.
- D7/D10/D14/D30 are separate periodic audits; source-level A1/A2 cannot falsely claim these checks or Human Review.
- November is OPEN at the 2026-11-11 evidence cut; W45 closed, W46 open; do not make period-final claims before due.
- This repository's original Nov02–11 ledger contains 20 merged original PRs, 12 with >=100 additions and 8 numeric NOT_MET; substantive acceptance is not inferred solely from these numbers.

## Prospective ten-repository SOP vNext — repository-local execution bridge (2026-11-23)

This **prospective operating bridge** generalizes the dated November 11 acceptance clarification above to any legitimately due logical period. It is not a new Native task, periodic audit, independent review, scheduler, or retroactive PR verdict. Current merged `main` and current subject-specific Native/machine contracts remain authoritative.

### Cold-start, cadence, and evidence gates

1. Establish `repository / role / canonical task ID / logical period / timezone / cutoff / producer / run ID`. Distinguish Native, independent A1, independent A2, D7/D10/D14/D30, Governance, Correction, and Reconciliation.
2. Read exact latest `main`, owning contracts, canonical paths/blob SHAs, relevant open/Draft PRs and active overlaps, recent merged changes, dependencies, and revision-matched runner/Actions results. Historical summaries are dated evidence, not live state.
3. Determine Native Daily/Weekly/Monthly/Special/Stage eligibility under each repository's actual contract. Exclude not-yet-due periods from the missing-input denominator; keep `NOT_DUE`, `BLOCKED`, `UNKNOWN`, `NOT_EXECUTED`, `NOT_COMPUTED`, and legitimate negative results visible.
4. Do not equate a file, external source, PR merge, configured workflow, passing test, independent AI review, and human approval. Each is a separate evidence claim with its own version, producer, run and time boundary.

### Native → Independent A1 → Independent A2

5. Native output follows repository-owned IDs, dependencies and actual execution evidence. A governance note never substitutes for producer research, formal scanner, runtime, effect receipt, or source verification.
6. **Independent A1 = MonthStart → N−1**, not yesterday alone. Enumerate all applicable month-to-date Daily, Weekly, Monthly, Special and Stage inputs. For each file record canonical path/blob SHA, producer, upstream dependency, source/evidence/counterevidence, and a justified disposition (`NO_FOLLOW_UP`, `CORRECT_IN_PLACE`, `APPEND_RELATION`, `CONFLICT`, `UNKNOWN`, `NOT_DUE`).
7. Prior A1 source reviews may be inherited only when exact path/blob SHA and governing contract still match. Mark inherited and newly inspected coverage; correct only real defects and leave valid sources unchanged.
8. Each legitimate A1 run uses its own original PR. **A2 starts only after that original A1 PR is merged and reread from a fresh `main`**; pending Drafts, future successors and cleanup do not satisfy this dependency.
9. **Independent A2 = MonthStart → N**. Maintain the full month's unified source/evidence/relationship state, not only Day N. Identify supported `STRENGTHENED`, `WEAKENED`, `CHANGED`, `CONFLICT`, `INVALIDATED`, `INHERITED`, `UNKNOWN` transitions and their provenance/counterevidence.
10. Month-to-date A2 coverage is not Native Monthly `FINAL`; D7/D10/D14/D30 have separate legal windows, cutoffs, actual audit runs and original records. A partial-day audit remains partial even after PR merge.

### Original A1/A2 acceptance: seven independent axes

| Axis | Verification |
| --- | --- |
| `TASK_COMPLETENESS` | Applicable source denominator and per-file disposition |
| `NUMERIC_GATE` | Each **original A1/A2** PR's final merged GitHub additions ≥100 |
| `SEMANTIC_QUALITY` | True, necessary custody, source/decision/relation content; no filler |
| `DEPENDENCY` | Exact original A1 merge and fresh-main read for A2 |
| `DELIVERY` | Original PR number, final head SHA, merged status and merge SHA |
| `MAIN_RETENTION` | Current canonical path/blob/content checked independently |
| `EXECUTION_VALIDATION` | Only actually executed Native/checker/CI/reviewer evidence |

11. Numeric `≥100` is distinct from semantic quality and is **not** a requirement for 100 original scientific discoveries. Genuine source rows, SHA custody, justified no-change judgments, matrices and relationship updates can count; padding, invented science and fake runs cannot.
12. Evaluate the **same original PR at its final merged head**, not an earlier unfinished Draft. A numerically short but real delivery is `NUMERIC_NOT_MET`; reaching 100 lines with false content is not semantic PASS. Successor, cleanup, correction and reconciliation never backfill original additions.
13. Historical producer, failed run, PR and observation facts remain intact. Move interpretations forward through linked correction/reconciliation without altering the historical event or claiming unavailable evidence.
14. For real work: fresh isolated branch → minimal owning-file changes → actual validation and declared `NOT_EXECUTED` checks → whole `main...head` diff and public-safety review → one scoped Draft PR → concrete maintainer review/authorization → merge under repo rules → latest-main retention readback. Do not test permission with empty commits or copy private controls into public artifacts.
15. Every handoff records identity/period/cutoff, initial main SHA, owning contracts and source blob SHAs, producer/run evidence, counterevidence, checked/not-checked validation, original PR/final additions and semantic decision, approval/merge receipt, current-main retention and next legal trigger.
16. **Scope note:** an SOP governance PR implementing this bridge is **not** an original independent A1/A2 PR and is not required to meet their ≥100-additions numeric acceptance gate.

### Repository-specific Native ownership and non-transferable boundaries

- Horizon H1→H2 Daily, H3→H4 Weekly, and H5→H6 Monthly follow `horizon-cortex/EVIDENCE_POLICY.md`; Parallax Daily follows its own `parallax/METHOD.md`. Parallax findings, Horizon source analysis, and NEXUS host implementation are distinct producer/evidence identities; an upstream source patch is not host adoption.
