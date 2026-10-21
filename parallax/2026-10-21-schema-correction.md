# Parallax schema-only correction ledger — 2026-10-21

## Scope and authority

- Correction date: 2026-10-21 Asia/Shanghai
- Observed main baseline: `f9b2c2de6be63a852aae90fb79b8cabbd444bea1`
- Rationale: current `parallax/tools/check.py` requires one integer-only `独立来源数量` metadata value when Record Provenance is present, and rejects the ideographic full-stop U+3002 anywhere under `parallax/**`
- Correction class: parser contract alignment and typography only, not later source evidence, new original run, historical re-attribution, new publisher, or a changed research finding
- Historical original Git blobs remain available by immutable SHA; the original assigned date, actual execution date, independent window, case, evidence and judgment must not be reinterpreted from correction commit time

## Exact correction relation

| Original Daily | Original blob SHA | Corrected blob SHA | Minimal change |
| --- | --- | --- | --- |
| [2026-09-07](records/2026-09/2026-09-07.md) | `2c5ad4aef0b05a43a929fa5b75ba2d40d22527b3` | `ca7ff1d8d26a798af7bced583a48f514d8298306` | Remove second machine-key occurrence in metric section while retaining value 1 |
| [2026-09-08](records/2026-09/2026-09-08.md) | `ee3e028d9540c9a901b7d12a8dec52cbc76f9eac` | `3b666d146ff3706122a77f6e72ae3606511ad780` | Remove second machine-key occurrence in metric section while retaining value 1 |
| [2026-09-20](records/2026-09/2026-09-20.md) | `c0c6a62e92acd1d77128bf036e2bdd7066f02686` | `5d3231d8ed2356e7741938c00b82da161ae6710a` | Keep numeric metadata 1 and move same-publisher rationale to separate prose field |
| [2026-09-21](records/2026-09/2026-09-21.md) | `20b23c01e4436a64c9faabe27161363bed1438d0` | `de502e91a87df42a6d816030ad26781de9a99a8c` | Only punctuation contract, 43 replacements |
| [2026-09-22](records/2026-09/2026-09-22.md) | `52414f5d5b476a6bdb9c9f816077eca0d727bb0c` | `81f861e4a0cd69b2bbed4b24fe4100349b7afc34` | Only punctuation contract, 11 replacements |
| [2026-09-30](records/2026-09/2026-09-30.md) | `ebd7d79f6a7b7fa209c561af1c3cc0bf49ab4b91` | `f7e4447e4a2639284cdf1c916820d900ab7088bb` | Only punctuation contract, 1 replacement |
| [2026-10-01](records/2026-10/2026-10-01.md) | `d54222843ecffc562b71e0f073d5aaf9cabdf86d` | `57b7c48b443b0c910351a90edca3a1c691a48861` | Only punctuation contract, 9 replacements |
| [2026-10-02](records/2026-10/2026-10-02.md) | `e4b78b17335a41ff5c782dfd7a2cad41782d2e37` | `ca648db1ad3fce74c234092700504be4292323d5` | Only punctuation contract, 9 replacements |

## Research and validation boundary

- Daily research units added: 0
- Research batches added: 0
- Independent execution windows added: 0
- Trials or CASE support added: 0
- NOTES, Specials, Audits added: 0
- Original evidence claims updated: 0
- Checker source inspected at blob `a405b69408ce6e2cde1f4d6bea84e340314b7ac3`, the active parser enforces a single metadata occurrence, digits-only independent count, and no U+3002
- Static source scan identified the eight changed Daily files, while 93 Daily date files, 17 Special files, 7 Audit files and support artifacts were reviewed for the scoped patterns
- Exact native `python parallax/tools/check.py` on a complete local checkout: NOT_EXECUTED because the current local environment cannot resolve GitHub archive hosts
- This ledger documents a forward correction relation and must not be counted as an Audit or new research batch
