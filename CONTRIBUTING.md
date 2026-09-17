# Contributing

Contributions are welcome when they improve the current repository while preserving Horizon/Parallax producer identity, evidence, provenance, recovery, and historical boundaries.

## Before proposing a change

- Start from the current merged `main` revision and read the most specific current repository authority before relying on historical snapshots, handoffs, or model memory.
- For repository maintenance, also read `governance/README.md` and `governance/independent-gpt/README.md`.
- Keep current state, historical observation, external claims, execution evidence, inference, and proposals distinct.
- Prefer a bounded, reviewable change with a clear owner and rollback.
- Inspect open pull requests and active maintenance branches before writing; use `COORDINATE` instead of creating a parallel repair for the same surface or logical period.
- Never create or mutate a branch merely to test write permission.

## Producer and plane boundaries

Keep these planes distinct:

```text
Horizon native production != Parallax research
Parallax Daily research production != maintenance/no-change task
Independent GPT != native producer
GitHub Actions != research truth
current path presence != earlier execution
later success != earlier success
correction != history rewrite
```

Private Jules task prompts, repository memory, credentials, hidden reasoning, and unrelated operator context are not reconstructed into public repository files by default. This repository currently has no public `AGENTS.md`; do not infer one from private controls or prior conversations.

Parallax Daily/Special/CASE/NOTES artifacts are research evidence, not routine repository-maintenance edit targets. A separate authorized research correction may own one of those artifacts; ordinary maintenance does not silently rewrite it.

## Issues

Use the repository Issue templates:

- **Bug report** for a reproducible defect in the current repository state.
- **Proposal** for a bounded improvement with explicit non-goals and acceptance criteria.
- **Evidence or governance correction** for a claim, metadata, governance, recovery, maintenance, producer-identity, or provenance mismatch.

Security-sensitive reports belong in the private route described by `SECURITY.md`, not in a public issue.

## Maintenance outcome

For maintenance work:

- no confirmed maintenance defect → `NO_CHANGE_REQUIRED`; no activity-only edit, branch, or PR;
- bounded defect with safe ownership → `REPAIR`;
- overlapping live ownership → `COORDINATE`;
- missing authority/current state or unsafe delivery → `BLOCKED`.

## Pull requests

Use a feature/maintenance branch and the pull-request template. A useful PR identifies:

- exact base `main` revision and delivery head;
- owning surface and logical period where relevant;
- overlapping PR/branch state;
- repository observations versus inference or proposal;
- changed files and deliberately unchanged boundaries;
- checks actually performed and their observed results;
- relevant checks intentionally left unrun as `NOT_EXECUTED`;
- historical/provenance and producer-identity impact;
- security/privacy impact where applicable;
- a practical rollback.

Before delivery, refresh current `main`, recheck overlap, inspect the aggregate `main...branch` diff, open one Draft PR, and stop for maintainer review unless a different repository-native workflow explicitly applies.

Never report an unrun checker, Parallax check, workflow, or local command as passed. Do not silently rewrite historical evidence merely to make the archive match later knowledge; use the current owning maintenance/control source or an explicit forward correction when the historical artifact itself needs calibration.

Do not push directly to `main`, force-push history, or auto-merge maintenance work.

## Style and scope

Follow existing repository style and naming conventions. Prefer clear, searchable, maintainable changes over decorative complexity. New dependencies or new authority surfaces require an explicit reason and boundary.

Purely cosmetic changes, unrelated feature accumulation, and changes that weaken protocol/evidence boundaries may be declined.

## Conduct, license, and attribution

Keep discussion professional, specific, evidence-aware, and focused on the repository. Do not publish credentials, private information, private prompts, or sensitive exploit details.

Contributions to repository-owned work are submitted under the current `LICENSE`. Third-party, archived, referenced, or vendored material retains its own attribution and licensing where applicable.

Contributor credit should reflect actual contribution history. `AUTHORS` identifies the primary author/maintainer and does not erase Git commit or pull-request attribution.

The repository owner retains final doctrine, review, and merge authority.
