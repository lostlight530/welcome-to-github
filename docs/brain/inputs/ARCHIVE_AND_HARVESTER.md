# Archive and document synchronization

The legacy archive contains every harvested input present through 2026-07-11 13:40 Asia Shanghai

Files are preserved byte for byte and organized by knowledge layer repository namespace year and month

New synchronization is driven only by `docs/brain/source_profiles.json`

Repository links discovered inside documents are recorded as content only and never become collection targets

Document state uses Git blob SHA and a normalized content hash

Unchanged blobs are skipped and formatting badge or timestamp-only changes do not create new knowledge inputs

Each generated document carries repository path SHA retrieval time owner and a namespaced entity identifier

The archive remains historical and is excluded from the active collection loop

## Active synchronization contract

The active profile contains 15 explicitly declared repository sources

The lifecycle checks out the triggering branch then rebuilds harvests validates ingests ponders and evolves in that order

Push validation covers the workflow brain sources implementation and harvester tests

Generated lifecycle changes are committed only to the triggering branch

Run the focused contract locally with `python -m unittest discover -s tests -p test_harvester.py`
