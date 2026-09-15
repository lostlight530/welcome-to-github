# Independent GPT Governance

Status: current public recovery kernel
Scope: repository-local independent recovery, audit, reconciliation, and bounded repair

This file exists so a memoryless independent agent can recover this repository from repository-visible evidence without access to private prompts, hidden memory, prior chats, credentials, or operator-only control logic.

It is not a Jules task prompt, not a Parallax task prompt, not a GitHub Actions workflow, not a research artifact, and not a substitute for current repository contracts.

## Recovery rule

Recover current state from the repository before using historical narrative.

For a subject under review, prefer current merged implementation and the current subject-specific contract or policy. Dated maintenance records and historical audits are evidence about their own time windows; they do not outrank a newer current contract merely because they are detailed.

Start by recording:

- current date and timezone used for the audit
- default branch
- current `main` revision
- open pull requests and recent merged changes relevant to the audit
- checks actually executed and checks not executed

## Repository-local recovery map

Read only what is needed for the question, but use these public entry points when applicable:

1. `README.md` and current repository source / frontend files for the present public surface.
2. `horizon-cortex/EVIDENCE_POLICY.md` for Horizon evidence semantics.
3. Current dated `horizon-cortex/` artifacts for repository-visible Horizon task output.
4. `parallax/` only for Parallax material; do not treat it as Horizon or GitHub Actions evidence.
5. `.github/workflows/` and revision-matched workflow runs for repository-exposed runner evidence.
6. `historical-audits/INDEX.md` and its referenced records for corrections, period audits, closure ledgers, maintenance, and reconciliation history.
7. Git history and merged PR chronology when file location, producer identity, timing, or historical state is disputed.

## Identity separation

Keep producer and evidence identity explicit.

- Jules-native Horizon output is Jules-native output.
- GPT Web or human-authorized substitute output must retain its actual producer identity.
- Parallax material is separate from Horizon material.
- GitHub Actions proves only the workflow execution that was actually observed for the referenced revision.
- Independent GPT governance is an audit / maintenance layer and must not be rewritten as native task execution.

Do not infer `Jules`, `SUCCESS`, `NETWORK_VERIFIED`, independent source corroboration, deployment health, or current truth from file presence alone.

## History discipline

Historical artifacts are point-in-time evidence.

- Never silently rewrite a historical observation to match later knowledge.
- Use a dated correction or reconciliation when later evidence changes the current interpretation.
- Preserve negative, degraded, blocked, rejected, missing, and unknown states.
- A moved or archived file keeps its historical meaning unless an explicit correction says otherwise.
- If a historical runtime fact is not recoverable from repository-visible evidence, record it as unknown rather than reconstructing it from later state.

## Independent audit procedure

An independent pass should distinguish at least:

- current facts
- historical facts
- corrections / reconciliations
- external claims
- verified execution evidence
- inference
- unresolved or unknown state

Inspect current implementation and contracts before proposing repair. If no current defect or drift is established, return `NO_CHANGE_REQUIRED` for the audited surface.

If repair is justified, keep it bounded to the owning current file(s) and the contracts or projections that must remain synchronized. Do not create activity-only edits.

## Public / private boundary

Do not publish or attempt to reconstruct:

- private task prompts or operator instructions
- hidden model memory or private conversation history
- credentials, tokens, account data, or security-sensitive configuration
- private scheduling or orchestration details that are not already repository contracts
- unrelated repository topology or private cross-repository control logic

Repository-visible artifacts may be cited and audited. Absence of private context is not a defect in this public recovery interface.

## Handoff record

A durable independent audit should make the next memoryless reviewer able to identify:

- base `main` SHA
- inspected scope and evidence window
- authority documents used
- checks actually run
- checks not run
- current findings
- historical findings
- corrections applied or required
- unresolved / unknown items
- whether history and negative evidence were preserved

Merge or doctrine changes require explicit maintainer authorization. Independent governance does not declare `FINAL_TRUTH`.
