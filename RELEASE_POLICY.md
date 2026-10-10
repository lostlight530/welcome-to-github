# Release and Archival Policy

This repository treats `main` as the current repository state and release tags as immutable point-in-time snapshots.

## Policy

- Create a release or tag only from a reviewed and merged `main` revision.
- A release records a historical snapshot; it does not override later repository state, governance, contracts, or evidence.
- Release identifiers may be repository-specific. Do not invent a semantic version where the repository has not established one.
- Add `version`, `date-released`, DOI, SWHID, or other archival identifiers to citation metadata only after those identifiers actually exist.
- Do not rewrite historical tags or releases to reflect later corrections; publish a new release or correction record instead.
- Archive externally only after the release snapshot and its metadata have been validated.

For current repository truth, follow the repository's native implementation, evidence, governance, and recovery surfaces rather than citation or archival metadata.

## Current archived software publication

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
| Initial open-research baseline | 2026-09-16 | See the canonical [Zenodo concept versions](https://zenodo.org/api/records/23137203/versions) for the exact initial version DOI |
| `v2026.09-natural-month-close` | 2026-09-30 | [`10.5281/zenodo.23068145`](https://doi.org/10.5281/zenodo.23068145) |
| `v2026.10-open-research-production-framework` | 2026-10-04 | [`10.5281/zenodo.23137203`](https://doi.org/10.5281/zenodo.23137203) |

The October GitHub release [`v2026.10-open-research-production-framework`](https://github.com/lostlight530/welcome-to-github/releases/tag/v2026.10-open-research-production-framework) reports `published_at=2026-10-04T13:00:12Z`. These identifiers are confirmed public release/DOI records, **not a claim that present `main` was frozen in that snapshot**. The existing `CITATION.cff` September 16 date remains a recorded archival baseline; do not silently rewrite it into a present-day retrieval or publication date. This documentation note creates **no new software release, DOI, prospective observation, or evidence of external research adoption**. The [independent identity audit](https://github.com/lostlight530/research-software-identity-audit) observes ten fixed software objects and remains an external control repository, not an eleventh research sample.
