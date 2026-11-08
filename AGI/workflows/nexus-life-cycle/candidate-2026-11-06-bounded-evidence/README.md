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
- The authorized native apply was required to archive replaced current files first, update active state, verify provenance and content hashes, rebuild the active graph and pass the final write boundary

## Post-acceptance outcome

- Implementation PR [#921](https://github.com/lostlight530/welcome-to-github/pull/921) merged at `2026-11-06T16:21:34Z` as `ac7d65a8b2889e44988e5607933331c303add0a7`
- Production gate fix PR [#922](https://github.com/lostlight530/welcome-to-github/pull/922) merged as `347344e0c60559e66d41c3317bb78edf18112d73`
- Authorized native apply [run 42252528859](https://github.com/lostlight530/welcome-to-github/actions/runs/42252528859) completed successfully and produced commit `960f2a277bd433be0198b5730f2aa9c9cc76c23e`
- Migration status after apply: `EXECUTED_AND_VERIFIED`
- WorkflowHub #2332 was not updated by this repository apply and remains outside the verified acceptance result

## Verification boundary

The candidate workflow copy is inert under `AGI/**`

Pull-request validation established the read-only candidate contract; the later authorized native apply is recorded separately above as production migration evidence

WorkflowHub #2332 and all frozen historical generations remain unchanged
