# Workflow Lineage Index

## Scope

This index records selected architecture generations recovered from Git history and points to their later byte-identical AGI backups

The lineage records preserve identity, provenance and recovery evidence; [the backup inventory](backups/README.md) contains the selected historical YAML files

No file under `AGI/workflows` is discovered as a GitHub Actions workflow, because GitHub Actions reads `.github/workflows` instead

The pinned Git commit and repository path remain the canonical historical source

## Selection rule

A historical commit is promoted to a recovered generation only when it marks a material workflow role or execution-contract transition

Routine syntax, checkout, autostash, path and race-condition fixes remain visible in Git history but are not promoted into separate architecture generations

## Reviewed history

The [complete revision inventory](revisions/README.md) records every historical workflow-file change, including ordinary fixes, exact source blob identities, static syntax results and byte-identical AGI backups

The complete path history reviewed on 2026-10-09 contains:

- 5 commits for `.github/workflows/brain_evolution.yml`
- 27 commits for `.github/workflows/nexus-life-cycle.yml`

The reviewed path history spans 2026-02-15 through 2026-08-31

## Selected generations

1. `brain-evolution/recovered-2026-02-15`
   - Earliest verified executable precursor
   - Workflow name: `Brain Evolution`
   - Role: external evidence harvesting with a review-gated pull request

2. `nexus-life-cycle/recovered-2026-03-09`
   - First verified workflow formally named `NEXUS CORTEX Life Cycle`
   - Role: unified rebuild, ingest, ponder, evolve and persistence loop

3. `nexus-life-cycle/recovered-2026-03-15`
   - First selected synchronized and main-branch-explicit generation
   - Role: world-line synchronization, bot identity and branch-explicit persistence

4. `nexus-life-cycle/recovered-2026-03-31`
   - First selected external fact-harvesting generation
   - Role: add harvesting between memory rebuilding and self-ingestion

5. `nexus-life-cycle/recovered-2026-07-11`
   - First selected profile-driven harvesting generation
   - Role: profile-governed external document harvesting and a focused contract test before ingestion

6. `nexus-life-cycle/recovered-2026-08-31-deterministic`
   - First selected read-only validation and guarded apply generation
   - Role: deterministic candidate and write-boundary contract

7. `nexus-life-cycle/recovered-2026-08-31-receipt`
   - First selected layered human-receipt generation
   - Role: baseline capture and human-readable validation/apply receipts

8. `nexus-life-cycle/original-2026-10-07`
   - First baseline formally recorded in the AGI workflow-history surface
   - Role: frozen reference to the mature bounded lifecycle

## Lineage

`Brain Evolution 2026-02-15` -> `NEXUS CORTEX 2026-03-09` -> `synchronized lifecycle 2026-03-15` -> `external harvesting 2026-03-31` -> later Git evolution -> `profile-driven harvesting 2026-07-11` -> later Git evolution -> `deterministic guarded lifecycle 2026-08-31` -> `layered human receipt 2026-08-31` -> `AGI original baseline 2026-10-07`

The 2026-10-07 original AGI baseline and the 2026-08-31 receipt generation share the same workflow Git blob; the former is a later capture checkpoint, not a new YAML modification

Intermediate commits remain primary evidence for the transition and are listed in the [complete revision inventory](revisions/README.md)

## External registration status

As checked on 2026-10-12, the standalone Brain Evolution precursor is registered at [WorkflowHub Version 1](https://workflowhub.eu/workflows/2337?version=1), DOI `10.48546/workflowhub.workflow.2337.1`

The welcome NEXUS CORTEX lineage registers the selected 2026-03-09, 2026-03-15 and 2026-03-31 generations as [Version 3](https://workflowhub.eu/workflows/2332?version=3), [Version 4](https://workflowhub.eu/workflows/2332?version=4) and [Version 5](https://workflowhub.eu/workflows/2332?version=5) respectively

Versions 1 and 2 are earlier external registrations of the 2026-10-07 baseline and do not change the historical chronology

The selected 2026-07-11 generation is not asserted here to have its own WorkflowHub version

Registration statements in older frozen manifests record their creation-time state; this index reports the later external registrations without rewriting those manifests

A WorkflowHub revision comment is an external identity reference, not a replacement for the canonical Git commit and workflow content hash

## Backup status

The selected-generation backup inventory remains under [`backups`](backups/README.md); the [complete revision inventory](revisions/README.md) preserves every other historical YAML revision without promoting every repair to a new architecture generation

As of 2026-10-12, the selected historical YAML files are also stored under [`AGI/workflows/backups`](backups/README.md), with each backup linked to its source commit, Git blob, SHA-256, description and WorkflowHub registration status

The older frozen manifests truthfully described their creation-time state before these later backups existed; they are not rewritten

Backups and future AGI experiments remain separate from the active `.github/workflows` lifecycle

## Boundary

These records do not alter workflow triggers, permissions, jobs, Actions behavior, task logs, Jules surfaces or Codex maintenance

Publication to WorkflowHub is a separate decision

A recovered generation is not automatically a published version
