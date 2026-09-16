# Contributing

Contributions are welcome when they improve the current repository while preserving its evidence, provenance, recovery, and historical boundaries.

## Before proposing a change

- Start from the current `main` revision and read the relevant current repository documents before relying on historical snapshots or archived material.
- Keep current state, historical observation, external claims, and proposals distinct.
- Prefer a small, reviewable change with a clear owner and rollback.
- Do not bundle unrelated architecture, maintenance, metadata, or historical cleanup into one pull request.

## Issues

Use the repository Issue templates:

- **Bug report** for a reproducible defect in the current repository state.
- **Proposal** for a bounded improvement with explicit non-goals and acceptance criteria.
- **Evidence or governance correction** for a claim, metadata, governance, recovery, or provenance mismatch.

Security-sensitive reports belong in the private route described by `SECURITY.md`, not in a public issue.

## Pull requests

Use a feature branch and the pull-request template. A useful PR identifies:

- the base revision and exact scope
- repository observations versus inference or proposal
- affected implementation, contract, documentation, metadata, or governance surfaces
- checks actually performed and their results
- relevant checks intentionally left unrun
- historical/provenance impact
- security/privacy impact where applicable
- a practical rollback

Never report an unrun check as passed. Do not silently rewrite historical evidence merely to make the archive match later knowledge; use a forward correction or reconciliation when the original record must remain auditable.

## Style and scope

Follow the existing repository style and naming conventions. Prefer clear, searchable, maintainable changes over clever or decorative complexity. New dependencies or new authority surfaces require an explicit reason and boundary.

Purely cosmetic changes, unrelated feature accumulation, and changes that weaken protocol/evidence boundaries may be declined.

## Conduct

Keep discussion professional, specific, evidence-aware, and focused on the repository. Do not publish credentials, private information, or sensitive exploit details.

## License and attribution

Contributions to repository-owned work are submitted under the repository's current `LICENSE`. Third-party, archived, referenced, or vendored material retains its own attribution and licensing where applicable.

Contributor credit should reflect actual contribution history. `AUTHORS` identifies the primary author/maintainer and does not erase Git commit or pull-request attribution.

The repository owner retains final review and merge authority.
