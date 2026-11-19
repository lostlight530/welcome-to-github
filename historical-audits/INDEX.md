# Historical Independent Audit Archive

This directory archives historical External Independent GPT audit, correction, reconciliation, evidence-accounting, and maintenance records. Relocation preserves each archived record's original Git blob and does not reinterpret or modernize its historical contents.

## Scope boundaries

Not archived here:
- Horizon H1-H6 Jules scheduled-task artifacts
- `parallax/**` periodic GPT/Codex Agent artifacts
- active repository contracts, policies, architecture, schemas, checkers, or workflows
- current external-maintenance procedure/templates
- Jules-authored archaeology records under `docs/archaeology/**`

## Archive classes

1. `01-corrections-and-errata/` — dated corrections to prior interpretations or evidence identity
2. `02-document-audits/` — independent audits of canonical document corpora
3. `03-stage-and-period-audits/` — provisional/as-of period-state audits
4. `04-evidence-and-closure-ledgers/` — evidence accounting and natural-period closure records
5. `05-maintenance-and-reconciliation/` — maintenance passes, provenance/cadence reconciliation, and post-hoc weekly reconciliation

## Relocation map

| Historical purpose | Archived path | Previous path |
| --- | --- | --- |
| Jules August history correction | `01-corrections-and-errata/2026-09-07--jules-august-history--correction.md` | `horizon-cortex/2026-09-07-jules-august-history-correction.md` |
| August through-23 stage audit | `03-stage-and-period-audits/2026-08-23--august-through-23--stage-audit.md` | `horizon-cortex/2026-08-through-23-stage-audit.md` |
| August through-27 stage audit | `03-stage-and-period-audits/2026-08-27--august-through-27--stage-audit.md` | `horizon-cortex/2026-08-through-27-stage-audit.md` |
| August 1-28 daily/weekly reconciliation | `03-stage-and-period-audits/2026-08-28--august-01-28--daily-weekly-reconciliation.md` | `horizon-cortex/2026-08-01-through-28-daily-weekly-reconciliation.md` |
| September 1-13 reconciliation ledger | `03-stage-and-period-audits/2026-09-13--sep-01-13--reconciliation-ledger.md` | `horizon-cortex/2026-09-13-thirteen-day-reconciliation.md` |
| September 1-13 month-to-date reconciliation | `03-stage-and-period-audits/2026-09-13--sep-01-13--month-to-date-reconciliation.md` | `horizon-cortex/2026-09-13-september-month-to-date-reconciliation.md` |
| August month-end reconciliation | `04-evidence-and-closure-ledgers/2026-08-31--august--month-end-reconciliation.md` | `horizon-cortex/2026-08-month-end-reconciliation.md` |
| W33 post-hoc reconciliation | `05-maintenance-and-reconciliation/2026-W33--weekly-reconciliation.md` | `horizon-cortex/2026-W33-reconciliation.md` |
| W34 post-hoc reconciliation | `05-maintenance-and-reconciliation/2026-W34--weekly-reconciliation.md` | `horizon-cortex/2026-W34-reconciliation.md` |
| W35 partial reconciliation | `05-maintenance-and-reconciliation/2026-W35--partial-weekly-reconciliation.md` | `horizon-cortex/2026-W35-partial-reconciliation.md` |
| 2026-09-02 maintenance record | `05-maintenance-and-reconciliation/2026-09-02--maintenance-record.md` | `horizon-cortex/2026-09-02-maintenance-log.md` |
| Cross-period Jules cadence reconciliation | `05-maintenance-and-reconciliation/2026-09-06--jules-cadence--reconciliation.md` | `horizon-cortex/2026-09-06-jules-cadence-reconciliation.md` |
| Jules content-contract reconciliation | `05-maintenance-and-reconciliation/2026-09-06--jules-content-contract--reconciliation.md` | `horizon-cortex/2026-09-06-jules-content-contract-reconciliation.md` |
| September ten-day successor reconciliation | `05-maintenance-and-reconciliation/2026-09-10--sep-01-10--cadence-reconciliation.md` | `horizon-cortex/2026-09-10-ten-day-cadence-reconciliation.md` |
| September 1-13 maintenance predecessor | `05-maintenance-and-reconciliation/2026-09-13--sep-01-13--maintenance-reconciliation.md` | `horizon-cortex/2026-09-13-full-sop-reconciliation.md` |
| September 14-15 incremental maintenance reconciliation | `05-maintenance-and-reconciliation/2026-09-15--sep-14-15--maintenance-reconciliation.md` | `horizon-cortex/2026-09-15-daily-maintenance-reconciliation.md` |
| September 19 live execution and optimistic-lock reconciliation | `05-maintenance-and-reconciliation/2026-09-19--sep-19--maintenance-reconciliation.md` | created directly in archive |

## Current recovery note

As of 2026-09-19, `05-maintenance-and-reconciliation/2026-09-19--sep-19--maintenance-reconciliation.md` is the latest completed independent maintenance record preserved in this archive. The `Previous path` column above records pre-relocation provenance only; it is not a live Horizon entry point and must not be used to infer a current file at that location.

Current Horizon production authority remains with the active Horizon contracts and policies, including `horizon-cortex/EVIDENCE_POLICY.md`, together with the current Horizon production artifacts. Status labels inside archived maintenance records describe their write-time role and do not turn the archive into current production authority.

The old paths remain recoverable through Git history. The archive directory is historical storage, not a replacement for current task contracts or the current external-maintenance procedure.

## 2026-11-19 bounded classification and filename normalization

This classification edit does **not** create Native, independent A1/A2, or D7/D10/D14/D30 task execution. The original historical record bodies and blob IDs remain unchanged. Only archival paths with no indexed inbound code references found in the repository search were renamed; search coverage is not equivalent to a full external link audit.

| Previous path | Current archival path | Unchanged Git blob SHA |
| --- | --- | --- |
| `historical-audits/2026-10/2026-10-28-sop-minimal-acceptance-audit.md` | `historical-audits/03-stage-and-period-audits/2026-10-28--sop-minimal-acceptance--audit.md` | `daabadb617c9e74e540db310247cd9441cf4919c` |
| `historical-audits/01-corrections-and-errata/2026-10-28-a1-a2-tree-oid-erratum.md` | `historical-audits/01-corrections-and-errata/2026-10-28--a1-a2-tree-oid--erratum.md` | `5210335d8ea164ea29bd74c0114943f30f125e38` |
| `historical-audits/01-corrections-and-errata/2026-10-28-horizon-oct27-dependency-gap-followon.md` | `historical-audits/01-corrections-and-errata/2026-10-28--horizon-oct27-dependency-gap--correction.md` | `241a831c78257f87810b09d5030e6b7f8a6e2a4b` |
| `historical-audits/2026-11/2026-11-09-nov08-nov09-ten-repo-strict-acceptance-reconciliation.md` | `historical-audits/05-maintenance-and-reconciliation/2026-11-09--nov08-nov09-ten-repo-strict-acceptance--reconciliation.md` | `c309a1b71d99a6ca2eda42ab31e35a02af45adaf` |

### Retained referenced path

- `historical-audits/2026-10/2026-10-28-october-native-weekly-gap-recovery-register.md` (blob `d5d7f20b47168c96bac2b087c42b8754f04d5ea0`) remains in its dated directory. A Horizon Native file refers to its original filename; moving it without touching an out-of-scope source would risk broken navigation. Semantic class: `05-maintenance-and-reconciliation/`.
- Original independent A1/A2 and periodic D-task records retain their dates, paths, original producers and historical assertions. All former paths remain recoverable through Git history; a historical pinned path is not automatically a current-main path.
