# Bounded Active Source Evidence — 2026-11-06

## Candidate identity

- Repository: `lostlight530/welcome-to-github`
- Source commit: [`187586e71cd8d50c91c1971ac94c0d9be885c45b`](https://github.com/lostlight530/welcome-to-github/commit/187586e71cd8d50c91c1971ac94c0d9be885c45b)
- Canonical source: `.github/workflows/nexus-life-cycle.yml`
- Git blob: `f17fbcd349e5aad3deea9ca170abd1f7d784d5e8`
- Content SHA-256: `6d092350a740df6a2352d16ac1648d5f6f6247df26f0c07ae9252d5a40255164`
- Byte-identical inert AGI backup: [workflow YAML](../../backups/nexus-life-cycle/candidate-2026-11-06-bounded-evidence/nexus-life-cycle.yml)

## Architecture transition

This candidate adds a fail-closed active-source evidence boundary after harvesting and before projection

The harvester accepts approved text source types only, rejects invalid UTF-8 and NUL bytes, converts oversized active snapshots to bounded pinned references and archives the replaced full snapshot before writing the bounded current representation

The native `validate` and conditional `apply` jobs remain separate, and only the native workflow under `.github/workflows` can receive repository permissions

## 2026-08-31 through 2026-11-06 migration boundary

- Main-state documents observed before this candidate: `23`
- Oversized current snapshots observed above 65,536 bytes: `3`
- Binary source paths observed in active state: `0`
- Migration status at capture: `NOT_EXECUTED_REQUIRES_MERGED_AUTHORIZED_APPLY`
- Existing archive content is never edited or re-ingested
- The next authorized native apply must archive replaced current files first, update active state, verify provenance and content hashes, rebuild the active graph and pass the final write boundary

## Verification boundary

The candidate workflow copy is inert under `AGI/**`

Successful pull-request validation proves repository tests and read-only contracts for the candidate commit, not a production migration, external WorkflowHub publication or successful native apply

WorkflowHub #2332 and all frozen historical generations remain unchanged
