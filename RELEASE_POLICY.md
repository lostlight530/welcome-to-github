# Release and Archival Policy

> **Current bilingual reading guide / 当前双语阅读指引（2026-11-13）**  
> **中文**：Git 当前分支、冻结归档和 DOI 不能混用作现时能力认证；这是一项根目录说明校准，不代表执行新任务或更改私有生产者 SOP  
> **English**: Current Git state, frozen archives and DOI identifiers cannot substitute for runtime capability validation. This root-document calibration does not execute a new task or publish private producer SOPs


This repository treats `main` as the current repository state and release tags as immutable point-in-time snapshots.

## Policy

- Create a release or tag only from a reviewed and merged `main` revision.
- A release records a historical snapshot; it does not override later repository state, governance, contracts, or evidence.
- Release identifiers may be repository-specific. Do not invent a semantic version where the repository has not established one.
- Add `version`, `date-released`, DOI, SWHID, or other archival identifiers to citation metadata only after those identifiers actually exist.
- Do not rewrite historical tags or releases to reflect later corrections; publish a new release or correction record instead.
- Archive externally only after the release snapshot and its metadata have been validated.

For current repository truth, follow the repository's native implementation, evidence, governance, and recovery surfaces rather than citation or archival metadata.

## Initial archived software publication — 2026-09-16

The repository has a public Zenodo software publication dated **2026-09-16**.

- DOI: `10.5281/zenodo.22790907`
- DOI resolver: `https://doi.org/10.5281/zenodo.22790907`
- Code repository: `https://github.com/lostlight530/welcome-to-github`

This DOI is an archival publication identifier, not a moving identifier for every later `main` revision. Later repository changes must not be represented as part of the archived publication unless a new archival release explicitly includes them.

A future archived release should preserve this record as point-in-time publication history and use its own confirmed release metadata. DOI presence, citation metadata, or archival availability does not by itself establish runtime execution, scientific validity, or reproduction.

## Verified archived version lineage (2026-10-10)

The September 16 publication described above is the **initial archival snapshot**; it is not the only release now registered under this software concept. The citation/CodeMeta DOI `10.5281/zenodo.22790907` is the **concept DOI**, not the DOI for the latest specific release.

| Archived release | Published/release date | Immutable version DOI |
| --- | --- | --- |
| `v2026.09-open-research-baseline` | 2026-09-16 | [`10.5281/zenodo.22790908`](https://doi.org/10.5281/zenodo.22790908) |
| `v2026.09-natural-month-close` | 2026-09-30 | [`10.5281/zenodo.23068145`](https://doi.org/10.5281/zenodo.23068145) |
| `v2026.10-open-research-production-framework` | 2026-10-04 | [`10.5281/zenodo.23137203`](https://doi.org/10.5281/zenodo.23137203) |

The October GitHub release [`v2026.10-open-research-production-framework`](https://github.com/lostlight530/welcome-to-github/releases/tag/v2026.10-open-research-production-framework) reports `published_at=2026-10-04T13:00:12Z`. These identifiers are confirmed public release/DOI records, **not a claim that present `main` was frozen in that snapshot**. The existing `CITATION.cff` September 16 date remains a recorded archival baseline; do not silently rewrite it into a present-day retrieval or publication date. This documentation note creates **no new software release, DOI, prospective observation, or evidence of external research adoption**. The [independent identity audit](https://github.com/lostlight530/research-software-identity-audit) observes ten fixed software objects and remains an external control repository, not an eleventh research sample.

## Archived checkpoint — 2026-10-14

The fourth archived version is [v2026.10-fourteen-day-evidence-checkpoint](https://github.com/lostlight530/welcome-to-github/releases/tag/v2026.10-fourteen-day-evidence-checkpoint).

- Version DOI: [10.5281/zenodo.23365504](https://doi.org/10.5281/zenodo.23365504)
- GitHub `published_at`: `2026-10-14T11:14:44Z`
- Tagged source commit: [`d1e732f81a03497af1c5afe43c1a00a77e87a828`](https://github.com/lostlight530/welcome-to-github/tree/d1e732f81a03497af1c5afe43c1a00a77e87a828)
- Software-family concept DOI: [10.5281/zenodo.22790907](https://doi.org/10.5281/zenodo.22790907)

Use the version DOI for this exact checkpoint and the concept DOI for the software family. `CITATION.cff` and CodeMeta retain the family identifier and recorded September 16 baseline date. Later changes to `main` belong to subsequent repository state; the checkpoint tag remains unchanged.

### Publication identity versus longitudinal display / 出版身份与长期展示数据

**中文**：本仓公开门户、Yearbook、Horizon／Parallax 的阶段记录以及十仓软件出版物分别有自己的来源和时间窗；阶段展示引用的是来源文件、Git 修订、观察截止时间、原始与派生口径、未执行或失败状态，不因出现新 release 就重新解释历史事实；Git tag 和 Zenodo version DOI 固定所归档的版本字节，concept DOI 仅表示软件家族，当前 `main` 不随之冻结

**English**: The portal, Yearbook, Horizon/Parallax stages and ten-repository software releases have distinct provenance and cutoffs. A stage display cites source path, Git revision, observation time, raw/derived denominator, and unexecuted or failed state; later releases do not rewrite historical observations. Tags and Zenodo version DOIs identify fixed archived objects; concept DOI identifies the family, while `main` continues evolving

## Open-science reuse and research records

- Cite the software family through [CITATION.cff](CITATION.cff) or [CodeMeta](codemeta.json); cite the version DOI above when a result depends on this checkpoint.
- Use the linked tagged source commit for code inspection and retrieval, and record the revision, environment, procedure and observed result when performing a rerun.
- Follow [OPEN_RESEARCH.md](OPEN_RESEARCH.md) and the repository-native research contracts; use [RESEARCH_TEMPLATE.md](RESEARCH_TEMPLATE.md) for a new bounded research record where a more specific native template does not apply.
- Reuse repository-owned material under [LICENSE](LICENSE), preserve [authorship attribution](AUTHORS), and submit changes through [CONTRIBUTING.md](CONTRIBUTING.md).
- Keep later findings and corrections in new dated records so the archived checkpoint remains recoverable.


## Latest archived checkpoint — 2026-11-10

The latest archived repository snapshot is `v2026.11-ten-day-evidence-checkpoint`.

- GitHub Release: [v2026.11-ten-day-evidence-checkpoint](https://github.com/lostlight530/welcome-to-github/releases/tag/v2026.11-ten-day-evidence-checkpoint)
- GitHub release published: `2026-11-10T14:40:19Z`
- Tagged source commit: [`197a236b684bf6c1afc39df2d55c3c8976c5bfab`](https://github.com/lostlight530/welcome-to-github/commit/197a236b684bf6c1afc39df2d55c3c8976c5bfab)
- Zenodo exact-version record: [10.5281/zenodo.24112453](https://doi.org/10.5281/zenodo.24112453)
- Software-family concept DOI: [10.5281/zenodo.22790907](https://doi.org/10.5281/zenodo.22790907)

The Zenodo version record identifies the exact GitHub tag as its source reference. This is an immutable 2026-11-10 snapshot; subsequent changes on `main` are not part of this archive. The concept DOI remains the software-family identifier and is intentionally distinct from the version DOI.
