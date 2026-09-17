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
