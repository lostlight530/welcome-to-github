# Proposed next-generation portable NEXUS workflow — welcome-to-github

> **DRAFT / UNREGISTERED / NOT EXECUTABLE** — an evidence-backed forward design candidate dated 2026-11-06, not a new WorkflowHub release and not a validation claim for any portable NEXUS implementation

## Why this proposal is newly actionable

The [life-science-ecosystem-lab native validation run #42030165535](https://github.com/lostlight530/life-science-ecosystem-lab/actions/runs/42030165535) executed its **Knowledge Workflow** CWL replay, **Portable package** build/extraction and independent replay, **Repository contracts**, **Evidence Tool** and aggregate `validate` gate, each successfully. This is evidence that a **separately implemented portable computation** can coexist with native GitHub Actions in that repository — not evidence that a NEXUS workflow already has the same portability

The legacy NEXUS WorkflowHub [#2332](https://workflowhub.eu/workflows/2332) line preserves historical GitHub Actions generations. Current active source on `main` at the proposal cutoff:

- Git commit: `af7337d378613007289e5e13514e124ca259dca5`
- Canonical Actions definition: `.github/workflows/nexus-life-cycle.yml`
- Git Blob: `c8fc0f838b03333231c82c9abf20e54370629cd0`
- Historical pinned content SHA256: `90519c058d6e2f2c1fa9701a682736dca429a57094e3593b792bcfb9f6760c18`
- Existing native jobs: **`validate`** (read-only) and **`apply`** (conditional authorized write)
- Repository tests: `python -m unittest discover -s tests -p 'test*.py'`

The identical active-workflow blob and historical AGI baseline identity are the provenance anchor for **this proposal only**. No implication is made that later GitHub revisions or WorkflowHub version numbering remain frozen

## Proposed authority split

| Plane | Future interface / allowed evidence | No-go boundary |
| --- | --- | --- |
| Native GitHub Actions | `validate`, conditional `apply`, existing triggers, permissions, world-line, verification and human receipts | Do not duplicate executable YAML in `AGI/**`; do not change main schedules |
| Portable verification sub-workflow | Fixture-bound offline validation, read-only projection/graph calculation and bounded result verification, in disposable isolated workspace | Must not run `harvest` against live sources or commit back to main |
| Test/receipt | Independently executed CLI/CWL test, negative-case output, exact code+fixture hashes, deterministic rerun receipts and final fail-closed gate | A green GitHub job alone is not proof that a portable artifact was executed |
| Registry publication | Workflow RO-Crate linking an **actual** main executable, dependencies, synthetic fixtures and tests; new external revision only after validation + maintainer review | A prospective version ID, DOI, test-pass badge or publication must not be invented |

The `AGI/workflows` directory is a historical/research documentation surface. The canonical executable remains `.github/workflows/nexus-life-cycle.yml`. A future portable artifact must be independently implemented and tested in a **new** forward directory, not by moving or editing frozen AGI records

## Execution contract to implement in a later code PR

```text
Git commit + byte-pinned synthetic fixtures
  -> schema/profile qualification (offline)
  -> read-only computed candidate / graph projection (isolated)
  -> source-identity and expected-output verification
  -> negative-case and idempotent replay checks
  -> gate verdict + reproducible receipt
  -> Workflow RO-Crate candidate (unpublished)
  
GitHub-native apply authority remains separate and is NOT callable from this package
```

The result ledger must retain distinct `NOT_EXECUTED`, `BLOCKED`, `FAILED`, `PASSED_WITHIN_SCOPE`, `REJECTED` and `INDETERMINATE` states, plus exit code, committed code SHA, test fixture SHA, exact command and job/run identifiers. A skipped job is never a silent pass

**Host-specific limit:** Source harvesting is network dependent. An offline replay must use immutable fixture inputs rather than mutable upstream sources. The separately proposed DeerFlow large-source correction in PR #915 is not part of this frozen source revision.

## Concrete acceptance criteria before any external update

- [ ] Implement a portable program/workflow with a named main entrypoint, dependency lock or pinned image and test fixture, without borrowing native `apply` credentials
- [ ] Execute that portable entrypoint on an isolated checkout, twice, compare normalized outputs and retain exact diagnostics
- [ ] Exercise at least one invalid fixture; fail-closed or explicit rejection must be visible to the aggregate gate
- [ ] Verify exact source SHA, fixture digests and bounded artifact contents; ensure no live source collection and no writes to the accepted production graph
- [ ] Build and unpack a deterministic Workflow RO-Crate containing runnable code, tests, metadata and public synthetic fixtures; test **the distributed package**, not only the source tree
- [ ] Review actual WorkflowHub registry current version and proposed changelog at publication time; only then request an external new version via authorized account
- [ ] Compare the published asset's downloaded bytes and metadata to the audited package; keep original workflow IDs #2332 and historical versions unchanged

## Current evidence disposition

- `OBSERVED`: NEXUS native two-job source and historical Git/WorkflowHub lineage; LS's successful reference CI in its **own** repository
- `PROPOSED`: splitting the read-only portable computation/verification from native apply, with explicit report and package identity
- `NOT_IMPLEMENTED / NOT_TESTED`: any NEXUS-specific CWL/RO-Crate portable replay or external new revision
- `DO_NOT_INFER`: LS passed == NEXUS portable passed; a historical WorkflowHub registration == new release; the GitHub Action YAML alone == self-contained externally executable workflow

Only this forward proposal and its corresponding machine-readable manifest are modified in this Draft PR. No current workflow, source runtime, tests, old AGI manifest/backups, GitHub Actions schedule or unrelated research is touched
