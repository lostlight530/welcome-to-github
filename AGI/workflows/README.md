# Workflow Lineage Index

## Scope

This index records selected architecture generations recovered from Git history

It is an identity, provenance and recovery surface only

No file under `AGI/workflows` is an executable GitHub Actions workflow

The canonical executable remains at the recorded Git commit and repository path

## Selection rule

A historical commit is promoted to a recovered generation only when it marks a material workflow role or execution-contract transition

Routine syntax, checkout, autostash, path and race-condition fixes remain visible in Git history but are not promoted into separate architecture generations

## Reviewed history

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

3. `nexus-life-cycle/original-2026-10-07`
   - First baseline formally recorded in the AGI workflow-history surface
   - Role: frozen reference to the mature bounded lifecycle

## Lineage

`Brain Evolution 2026-02-15` -> `NEXUS CORTEX Life Cycle 2026-03-09` -> later Git evolution -> `AGI original baseline 2026-10-07`

Intermediate commits remain primary evidence for the transition and are listed in each recovered record

## Boundary

These records do not alter workflow triggers, permissions, jobs, Actions behavior, task logs, Jules surfaces or Codex maintenance

Publication to WorkflowHub is a separate decision

A recovered generation is not automatically a published version
