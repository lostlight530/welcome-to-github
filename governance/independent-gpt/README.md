# Independent GPT Governance — Horizon Relay

Status: current public recovery kernel
Scope: repository-local recovery, independent audit, reconciliation, and bounded repair

This directory is the public handoff point for a memoryless independent reviewer. It is intentionally small: it tells a new reviewer how to recover repository truth from repository-visible evidence without duplicating native task instructions or exposing non-repository operator context.

## Recovery order

For the subject under review, recover current truth from current merged `main` first. Prefer current implementation and the current subject-specific contract or policy over dated maintenance prose. Use dated audits and reconciliations as point-in-time evidence for their own windows.

At audit start record the current date, default branch, `main` SHA, relevant open pull requests, recent merged changes, and checks actually executed.

## Repository map

Use only the surfaces needed for the question:

1. `README.md`, current source, and current frontend files for the present public surface.
2. `horizon-cortex/EVIDENCE_POLICY.md` for Horizon evidence semantics.
3. Current dated `horizon-cortex/` artifacts for repository-visible Horizon output.
4. `parallax/` only as Parallax evidence; do not collapse it into Horizon evidence.
5. `.github/workflows/` plus revision-matched workflow runs for GitHub Actions evidence.
6. `historical-audits/INDEX.md` for corrections, period audits, closure ledgers, maintenance, and reconciliation history.
7. Git history and merged PR chronology when original path, producer identity, timing, or historical state is disputed.

## Evidence boundaries

Keep identity explicit:

- native Horizon output remains native Horizon output;
- GPT Web or other substitute output retains its actual producer identity;
- Parallax is not Horizon;
- GitHub Actions proves only the workflow execution actually observed for the referenced revision;
- independent governance is an audit layer, not native task execution.

Do not infer `SUCCESS`, network access, source independence, deployment health, or current truth from file presence alone.

## History discipline

Historical records are immutable point-in-time evidence. Later evidence may change the current interpretation, but it does not rewrite what an earlier run observed.

Use a dated correction or reconciliation when interpretation changes. Preserve degraded, blocked, rejected, missing, negative, and unknown states. Archive relocation is not semantic replacement. If a historical runtime fact is not recoverable from repository-visible evidence, keep it `UNKNOWN`.

## Independent audit outcome

Separate current facts, historical facts, corrections, external claims, execution evidence, inference, and unknown state. Use one of these governance outcomes when a concise status is needed:

- `HEALTHY`
- `REPAIR`
- `COORDINATE`
- `BLOCKED`

`HEALTHY` means no repair is required for the audited surface; it does not certify unrelated repository claims.

If repair is justified, change only the owning current file(s) and the contracts or projections that must remain synchronized. Do not create activity-only edits or fabricated backfill.

## Public boundary

This recovery kernel is intentionally repository-bounded. It neither requires nor attempts to reconstruct unavailable operator context, credentials, hidden memory, or unrelated orchestration. Repository-visible evidence is sufficient for an independent repository audit; unavailable context remains unavailable rather than guessed.

## Handoff minimum

A durable audit should leave the next reviewer able to identify the base `main` SHA, scope and evidence window, authority used, checks run, checks not run, current findings, historical findings, corrections, unresolved items, and whether history and negative evidence were preserved.

Independent governance may recommend or prepare bounded changes. Final merge and doctrine authority remains with the maintainer.
