# Layered Human Receipt — 2026-08-31
## Historical identity
- Repository: `lostlight530/welcome-to-github`
- Source commit: [`3c7ebfb49f69f0f015075a98b869437265651001`](https://github.com/lostlight530/welcome-to-github/commit/3c7ebfb49f69f0f015075a98b869437265651001)
- Source time: `2026-08-31T12:53:56Z`
- Canonical historical path: `.github/workflows/nexus-life-cycle.yml`
- Git blob: `c8fc0f838b03333231c82c9abf20e54370629cd0`
- Content SHA-256: `90519c058d6e2f2c1fa9701a682736dca429a57094e3593b792bcfb9f6760c18`
- Byte-identical AGI backup: [`AGI/workflows/revisions/snapshots/nexus-life-cycle/2026-08-31-3c7ebfb49f69/nexus-life-cycle.yml`](../../revisions/snapshots/nexus-life-cycle/2026-08-31-3c7ebfb49f69/nexus-life-cycle.yml)
## Architecture transition
Added human baseline capture and always-published lifecycle receipts to both validation and apply jobs, while preserving the guarded apply architecture
This is the next selected generation after the deterministic split, not a new active workflow path
Previous selected AGI generation: `AGI/workflows/nexus-life-cycle/recovered-2026-08-31-deterministic`
The later 2026-10-07 AGI original baseline captures this same workflow Git blob; it is a later identity checkpoint, not another YAML revision
## Verification evidence
- Exact source commit workflow YAML passed static PyYAML syntax parsing and its AGI backup reuses the same Git blob
- No successful NEXUS run at this exact commit was identified by the current head-SHA query; this is not proof that none existed
- A [later scheduled run](https://github.com/lostlight530/welcome-to-github/actions/runs/38190365573) with the same workflow Git blob completed validation and guarded apply successfully on 2026-10-12; later code and data may differ
- Static parsing and historical runs do not establish present-day compatibility for replay
## Boundary
This AGI record and backup do not change `.github/workflows`, GitHub Actions triggers, Jules tasks or Codex maintenance
A replay or experimental successor needs its own safety validation and explicit execution decision