# Horizon Cortex Evidence Policy

Status: current repository evidence policy  
Calibration: 2026-08-28

This file defines how committed Horizon artifacts are interpreted against the repository implementation and external evidence that actually exists. It is an evidence contract, not a runtime capability claim.

## 1. Repository realization map

Horizon is one research/evidence surface inside `welcome-to-github`. It is not the host knowledge engine or public presentation layer.

### Presentation

`index.html` and presentation scripts are public UI surfaces. Presentation text does not determine NEXUS or Horizon evidence state.

### NEXUS knowledge lifecycle

`docs/brain/**` contains the host knowledge lifecycle, SQLite/JSONL state, retrieval, graph analysis, and generated memory/dashboard surfaces.

`docs/brain/scholar.py` excludes `horizon-cortex` and `parallax` from its host-code scan and ignores Markdown/research material.

Use:

`HOST_CODE_STRUCTURE_SCAN != HORIZON_RESEARCH_INGESTION`.

A Horizon claim does not become a NEXUS graph fact merely because both live in one repository.

## 2. SQLite and JSONL are distinct host persistence surfaces

The host SQLite and JSONL writes are not one atomic transaction. SQLite can commit before JSONL append is attempted.

Use:

`SQLITE_WRITE_SUCCESS != JSONL_LEDGER_SYNC_VERIFIED`.

and:

`REBUILDABLE_JSONL_SURFACE != PROOF_OF_CONTINUOUS_DB_LEDGER_EQUIVALENCE`.

JSONL append is not cryptographic source authentication or truth proof.

## 3. Host graph/retrieval labels are local heuristics

FTS5 retrieval, entity weights, graph density, orphan counts, PageRank-like centrality, and generated labels describe local indexed state.

They do not independently establish semantic truth, causal importance, safety, adoption, or autonomous intent.

Use:

`LOCAL_RETRIEVAL_OR_GRAPH_SIGNAL / CLAIM_TRUTH_NOT_ESTABLISHED`.

Generated labels such as `Epiphany`, `Ecosystem Choke Point`, or `Self-Driven Goal` are narrative/heuristic output, not cognition or authorized future action.

## 4. Backfilled dashboard dates are not original observations

The host can backfill missing historical dashboard filenames using metrics available during a later run.

Use:

`BACKFILLED_DASHBOARD != ORIGINAL_HISTORICAL_OBSERVATION`.

Keep separate logical/file date, actual generation time, metric observation time, and source state.

## 5. Horizon checker boundary

`horizon-cortex/check.py` validates structural artifact contracts such as filename/task identity, sections, logical date/week, handoffs, Decision/Action IDs, and host-change boundaries.

A checker pass does not establish external factual truth, source independence, source authority, legal correctness, host applicability, production adoption, local incidents, DB/JSONL synchronization, or runtime outcomes.

Use:

`STRUCTURAL_CONTRACT_PASS != CLAIM_VALIDATION`.

## 6. Source authority is claim-specific

Keep distinct:

- `SOURCE_ACCESS_VERIFIED`
- `SOURCE_IDENTITY_VERIFIED`
- `PRIMARY_SOURCE_FOR_CLAIM`
- `SECONDARY_SOURCE`
- `VENDOR_INTERPRETATION`
- `CASE_STUDY`
- `ANALYTICAL_TAXONOMY`
- `CLAIM_SUPPORTED`
- `HOST_APPLICABILITY_UNKNOWN`

A first-party product blog can be primary for that product's own implementation while remaining secondary/interpretive for a protocol-wide or market-wide proposition.

Directly opening a secondary article does not make it primary.

## 7. Daily H1 → H2 evidence SOP

### H1 Observe

H1 should record separately:

1. source access
2. source identity
3. source authority for the exact proposition
4. source publication/version/check time
5. raw observed proposition
6. uncertainty/noise
7. whether independent H2 verification is needed

A vendor classification or market map should remain an `ANALYTICAL_TAXONOMY` unless primary evidence supports a stronger claim.

### H2 Orient

H2 may add independent evidence and narrow/promote an H1 signal.

It must not:

- treat H1 repetition as independent corroboration
- convert a protocol release into a host migration instruction
- convert protocol statelessness into application statelessness
- convert vendor/community layering into a universal normative architecture
- use `must`, host-required, or “completely disproved” language without an authorized local decision/evidence surface

Use:

`H2_RESTATEMENT_DOES_NOT_UPGRADE_H1_EVIDENCE`.

## 8. MCP 2026-07-28 source hierarchy and current interpretation

The final 2026-07-28 specification release is a primary protocol-version fact.

Current primary-supported features include:

- stateless protocol core
- retirement of initialize/initialized and protocol session ID for the new core
- self-describing requests
- header-based routing
- Multi Round-Trip Requests
- cacheable/deterministic list behavior
- formal extensions framework, including Tasks
- authorization hardening
- formal deprecation policy

The May 21 material is a **release candidate**; the July 28 maintainer release is the stronger authority for final-version claims.

Use:

`MCP_2026_07_28_FINAL_RELEASE_FACT`.

Keep:

`PROTOCOL_STATELESSNESS != APPLICATION_STATELESSNESS`.

The release candidate explicitly distinguished a stateless protocol from stateful applications. Therefore no Horizon artifact may infer that application state, durable task state, or host-local state management is obsolete merely from the protocol revision.

MRTR supports multi-round interactions without constantly open bidirectional streams; it does not establish zero latency, automatic client correctness, or host implementation.

## 9. A2A v1.0 source hierarchy and current interpretation

Current official A2A materials identify v1.0.0 as the latest released version and position A2A as an open standard for agent interoperability, discovery, collaborative task management, and communication across heterogeneous systems.

Official v1.0 material also states that A2A and MCP are complementary: MCP commonly serves tool/context integration at an individual-agent level while A2A focuses on agent-to-agent communication/coordination.

Use:

`A2A_MCP_COMPLEMENTARITY_PRIMARY_SUPPORTED`.

This does not create a universal multi-protocol stack law involving every other protocol.

Use:

`ANALYTICAL_BOUNDARY_SUPPORTED / NORMATIVE_LAYERING_NOT_ESTABLISHED`.

## 10. Sequential repetition and Weekly inheritance

H1 may feed H2 and Daily artifacts may feed H3/H4. Repetition across that chain is inheritance, not independent corroboration.

`WEEKLY_INHERITANCE_DOES_NOT_UPGRADE_EVIDENCE`.

A later artifact adds evidence only when it actually adds an independent source, implementation observation, or checked surface.

## 11. Weekly H3/H4 SOP

A weekly synthesis must preserve source lineage and Daily uncertainty.

It may:

- cluster repeated themes
- downgrade weak/duplicated signals
- add independent evidence
- record a bounded decision/action when the weekly task actually occurs

It may not:

- manufacture missing Daily evidence
- turn repeated Daily discussion into adoption frequency
- erase historical blocked/missing states
- claim a week-complete H3/H4 before the weekly lifecycle produces one

At the 2026-08-27 cutoff W35 is:

`IN_PROGRESS`.

See `2026-W35-partial-reconciliation.md`.

## 12. Historical execution, delivery, and current presence are distinct

Keep separate:

- logical date/week
- original execution state
- generation/commit evidence
- delivery/merge visibility
- aggregation-snapshot visibility
- current path presence

A later file cannot retroactively turn an earlier `BLOCKED` run into success.

If retained artifacts disagree about historical input state, preserve:

`HISTORICAL_INPUT_STATE_MISMATCH`.

## 13. Support, deployment, adoption, and dominance are different claims

Do not collapse:

- specification exists
- implementation supports it
- named deployment exists
- production use exists
- broad adoption exists
- dominance/universality exists

A support/participation count is not automatically a production-user count.

## 14. Benchmarks, observability, threats, and legal claims remain scoped

A benchmark/vendor study cannot create universal thresholds.

OpenTelemetry semantic conventions, framework-specific tracing guidance, and governance features remain distinct evidence surfaces.

External security analysis supports threat-model hypotheses, not local host incidents.

Vendor compliance interpretation does not create a legal architecture mandate.

## 15. Historical correction method

Historical H1–H4 files remain point-in-time evidence.

Later reconciliation records:

- historical wording/state
- stronger later evidence
- current bounded interpretation
- unresolved dimensions

It does not rewrite the historical artifact.

Current August stage authority: `2026-08-through-27-stage-audit.md`.

Formal August H5/H6 remains `OPEN` until the natural monthly lifecycle has actual evidence.

## 16. Active daily and weekly record contract

New H1 and H2 records identify source identity, authority for the exact claim, independent verification, host applicability, evidence-upgrade basis, original execution status, current path status, and record provenance.

New H3 and H4 records provide a Daily coverage matrix, inherited and newly independent evidence, preserved missing inputs, decision evidence basis, historical execution state, and current delivery state.

Substitutes and reconstructions use their real agent identity. A reconstruction cannot claim original success. Historical records remain byte-preserved and known legacy schema defects are interpreted through reconciliation records.

`CURRENT_PATH_PRESENT != ORIGINAL_EXECUTION_SUCCESS`.

`EXTERNAL_PROTOCOL_FACT != HOST_ADOPTION_REQUIREMENT`.
