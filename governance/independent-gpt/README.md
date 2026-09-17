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
