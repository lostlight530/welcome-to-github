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

## Current navigation for retained duplicate paths

The preferred links below are for navigation. The retained paths point to the same Git blobs and are not separate audits or additional evidence. This section supersedes conflicting path labels in earlier entries of this index without changing their historical provenance.

| Record | Preferred archive path | Retained same-blob path |
| --- | --- | --- |
| October 28 SOP minimal acceptance audit | [Preferred](03-stage-and-period-audits/2026-10-28--sop-minimal-acceptance--audit.md) | [Retained](03-stage-and-period-audits/2026-10-28-sop-minimal-acceptance-audit.md) |
| November 8–9 PR acceptance reconciliation | [Preferred](05-maintenance-and-reconciliation/2026-11-09--nov08-nov09-ten-repo-strict-acceptance--reconciliation.md) | [Retained](04-evidence-and-closure-ledgers/2026-11-09-nov08-nov09-ten-repo-strict-acceptance-reconciliation.md) |

## 2026-11-20 source/provenance document-audit correction

- [Horizon/Parallax A1/A2 source-role review](02-document-audits/2026-11-20--a1-a2-source-and-provenance--document-audit.md) — separate independent review; source-row role fixes are in current canonical A1/A2, original history retained

## 2026-11-24 retained archive navigation additions

These existing records were not explicitly linked by path in the preceding index. This is a navigation supplement, not a new audit, a new producer run, or a reclassification. The directory column reports the retained physical location; original record content and provenance govern interpretation. Path-sensitive references and legacy locations remain intact. Existing same-blob aliases are not additional evidence.

| Retained record | Existing directory | Blob at inspected main |
| --- | --- | --- |
| [2026-10-01--external-review-source-scope--correction.md](01-corrections-and-errata/2026-10-01--external-review-source-scope--correction.md) | `01-corrections-and-errata/` | `95c877eec41e9b6550af7a57331ae629c1038d4a` |
| [2026-10-31--horizon-h2-upstream-state--post-merge-erratum.md](01-corrections-and-errata/2026-10-31--horizon-h2-upstream-state--post-merge-erratum.md) | `01-corrections-and-errata/` | `a8bf035589b2a7aa4bc4146f07b81e19e7aa4f6a` |
| [2026-11-01--a2-successor-retention-and-acceptance--reconciliation.md](01-corrections-and-errata/2026-11-01--a2-successor-retention-and-acceptance--reconciliation.md) | `01-corrections-and-errata/` | `fefd90dc12c7f165019c50a0b159288b018b4b81` |

## 2026-11-25 cloud acceptance navigation

Dated documentary review at [inspected main](https://github.com/lostlight530/welcome-to-github/commit/46cce7368b11ac6b5aa58ae459fdbc64d1f7d4ef); navigation only, not a new original A1/A2, Native, or D-task submission. The historical archive classes above remain unchanged. Original task owners are linked, not relocated or reclassified.

| Identity | Original GitHub delivery | Cloud evidence / disposition |
| --- | --- | --- |
| Independent A1 (Nov 1–24) | [#1058](https://github.com/lostlight530/welcome-to-github/pull/1058), 192 additions, merged | [canonical file](https://github.com/lostlight530/welcome-to-github/blob/46cce7368b11ac6b5aa58ae459fdbc64d1f7d4ef/historical-audits/2026-11/2026-11-25-a1-source-content-review.md) retained; numeric gate met; 170/171 listed source SHA rows match the later inspected main (cutoff/shared-owner changes are not automatically errors) |
| Independent A2 (Nov 1–25) | [#1059](https://github.com/lostlight530/welcome-to-github/pull/1059), 228 additions, merged | [canonical file](https://github.com/lostlight530/welcome-to-github/blob/46cce7368b11ac6b5aa58ae459fdbc64d1f7d4ef/historical-audits/2026-11/2026-11-25-a2-month-relations.md) retained; numeric gate met; 176/176 listed first source SHA rows match inspected main; PR base is the original A1 merge and creation follows that merge |
| Oct 31 original A2 | [#876](https://github.com/lostlight530/welcome-to-github/pull/876), 85 additions, merged | Original numeric gate NOT_MET; delivery and numeric acceptance remain separate |
| Oct 31 successor | [#878](https://github.com/lostlight530/welcome-to-github/pull/878), 261 additions, merged | Successor numeric gate MET; no retroactive credit to original A2 |
| Oct 31 cleanup | [#879](https://github.com/lostlight530/welcome-to-github/pull/879), merged | Separate cleanup, not original task or successor credit |
| Nov 1 forward reconciliation | [#883](https://github.com/lostlight530/welcome-to-github/pull/883), merged | [Retained correction](01-corrections-and-errata/2026-11-01--a2-successor-retention-and-acceptance--reconciliation.md); correction class, not a new original A2 |

Native evidence: Horizon H1/H2 [#1056](https://github.com/lostlight530/welcome-to-github/pull/1056)/[#1057](https://github.com/lostlight530/welcome-to-github/pull/1057); Parallax [#1054](https://github.com/lostlight530/welcome-to-github/pull/1054). Bounded producer evidence is not SDK/checker or remote-effect execution.

D7/D10/D14 retain their separate original identities; D14 is an as-of partial observation, not a full-day closure. D30 is not due at this observation. November remains open. Cloud delivery, numeric acceptance, dependency and retention are confirmed at the inspected revision; source-row custody does not by itself establish full semantic validity or a new runtime execution. Existing archive aliases are navigation only, not additional evidence or task credit.
