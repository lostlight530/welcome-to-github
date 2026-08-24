# Horizon Cortex Evidence Policy

Status: post-hoc repository evidence policy  
Calibration: 2026-08-24

This file defines how committed Horizon artifacts are interpreted against the repository implementation that actually exists. It is an evidence contract, not a runtime capability claim.

## 1. Repository realization map

Horizon is one research/evidence surface inside `welcome-to-github`. It is not the host knowledge engine or public presentation layer.

### Presentation

- `index.html` is the public portal
- `src/scripts/translations.js` is presentation-layer translation content

Presentation text does not determine NEXUS or Horizon evidence state.

### NEXUS knowledge lifecycle

`docs/brain/nexus.py` exposes the local command surface:

- `harvest`
- `project`
- `ingest`
- `ponder`
- `evolve`
- `rebuild`
- `search`
- `status`
- explicit `add` / `connect`

The repository therefore has distinct surfaces for external/source material, projected/ingested knowledge records, SQLite query/index state, graph-derived analysis, and public presentation.

### Horizon isolation from host-code ingestion

`docs/brain/scholar.py` explicitly excludes `horizon-cortex` and `parallax` from its supported host-code scan and ignores Markdown/research material.

Use:

`HOST_CODE_STRUCTURE_SCAN != HORIZON_RESEARCH_INGESTION`.

A Horizon claim does not become a NEXUS graph fact merely because both live in the same repository.

## 2. SQLite and JSONL are distinct persistence surfaces

`docs/brain/cortex.py` maintains SQLite graph/index state and appends JSONL knowledge records.

Important implementation fact: these writes are **not one atomic transaction**.

For entity writes, SQLite state is committed before `_log_to_jsonl()` is attempted. JSONL failure is caught and reported without rolling back the already committed SQLite change.

Therefore:

`SQLITE_WRITE_SUCCESS != JSONL_LEDGER_SYNC_VERIFIED`.

And:

`REBUILDABLE_JSONL_SURFACE != PROOF_OF_CONTINUOUS_DB_LEDGER_EQUIVALENCE`.

Current JSONL behavior is append-oriented application persistence. It is not cryptographic immutability, tamper evidence, or external source authentication.

The SQLite database is a local active query/index surface; JSONL records support reconstruction. Neither surface alone proves source truth.

## 3. Temporal graph state is application-level state

`valid_at` / `invalid_at` in `docs/brain/cortex.py` express application-level validity intervals for entities and relations.

They do not independently establish:

- when an external fact became true
- when a source was published
- when a Horizon artifact observed that fact
- cryptographically proven historical state

Application timestamps and external-event provenance remain separate evidence dimensions.

## 4. Retrieval and graph metrics are not truth scores

FTS5 retrieval, graph expansion, entity weights, orphan counts, graph density, and PageRank-like centrality describe the indexed repository state.

They do not independently establish semantic truth, causal importance, safety, adoption, or external correctness.

Use:

`LOCAL_RETRIEVAL_OR_GRAPH_SIGNAL / CLAIM_TRUTH_NOT_ESTABLISHED`.

## 5. Generated reasoning labels are heuristic narrative

`docs/brain/reason.py` emits human-readable strings such as:

- `Isolation Risk`
- `Cognitive Loop`
- `Epiphany`
- `Subconscious Intuition`
- `Ecosystem Choke Point (PageRank)`
- `Self-Driven Goal`

These labels are generated interpretations of local graph patterns.

In particular:

- the maximum PageRank node is the top node under that implementation/run, not an “absolute mathematical centrality” theorem
- a generated “Self-Driven Goal” is suggestion/narrative output, not evidence of autonomous intent or an externally authorized future action
- a structural overlap or transitive pattern is not semantic or causal proof

Use:

`GRAPH_HEURISTIC_LABEL / SEMANTIC_AND_AUTONOMOUS_INTENT_NOT_ESTABLISHED`.

## 6. Backfilled dashboard dates are not original observation times

`docs/brain/reason.py` contains a missing-dashboard backfill mechanism. When dated dashboard files are absent, it can create files for earlier dates using metrics available during the later rendering run.

Therefore a historical-looking filename does not by itself establish that those metrics were observed on that logical date.

Keep separate:

- dashboard logical/file date
- actual generation time
- metric observation time
- source state used to render the dashboard

Use:

`BACKFILLED_DASHBOARD != ORIGINAL_HISTORICAL_OBSERVATION`.

A backfilled dashboard may be useful as a continuity/presentation artifact but must not be reused as point-in-time telemetry without independent generation/observation evidence.

## 7. Horizon checker boundary

`horizon-cortex/check.py` checks deterministic artifact contracts such as:

- filename/task identity
- required sections
- logical date/week
- H1→H2 and H3→H4 handoffs
- Decision/Action IDs
- host-change boundary markers

A checker pass does **not** establish:

- external factual truth
- source independence
- source authority for the exact claim
- legal/regulatory correctness
- host applicability
- production adoption
- local incident occurrence
- NEXUS DB/JSONL synchronization
- runtime outcome correctness

Use:

`STRUCTURAL_CONTRACT_PASS != CLAIM_VALIDATION`.

## 8. Source access, identity, authority, and claim support are separate

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

A source may be first-party for its own product while remaining interpretive or insufficient for a protocol-wide, market-wide, legal, or ecosystem-wide proposition.

Directly opening a secondary article does not make it primary.

## 9. Sequential repetition does not create independent evidence

H1 may feed H2 and Daily artifacts may feed H3/H4. Repetition across that chain is inheritance, not independent corroboration.

Use:

`H2_RESTATEMENT_DOES_NOT_UPGRADE_H1_EVIDENCE`

and:

`WEEKLY_INHERITANCE_DOES_NOT_UPGRADE_EVIDENCE`.

A later artifact can add new evidence only when it actually introduces an independent source, observation, or checked implementation surface.

## 10. Historical execution, delivery, and current presence are distinct

Keep separate:

- logical date/week
- original execution state
- generation/commit evidence
- delivery/merge visibility
- aggregation-snapshot visibility
- current path presence

A later file cannot retroactively turn an earlier `BLOCKED` run into success.

If two retained artifacts disagree about historical input state, preserve:

`HISTORICAL_INPUT_STATE_MISMATCH`.

## 11. Support, deployment, adoption, and dominance are different claims

Do not collapse:

- specification exists
- implementation supports it
- named deployment exists
- production use exists
- many independent organizations use it
- broad ecosystem adoption exists
- dominance/de-facto universality exists

Useful bounded labels:

- `PROTOCOL_VERSION_FACT`
- `FIRST_PARTY_IMPLEMENTATION_SUPPORT`
- `NAMED_DEPLOYMENT_EXAMPLE`
- `ECOSYSTEM_OBSERVATION`
- `ADOPTION_RATE_NOT_ESTABLISHED`
- `UNIVERSAL_ADOPTION_NOT_ESTABLISHED`

A statement that 150+ organizations participate/support a protocol is not evidence that all 150+ are production users.

## 12. Protocol and architecture claims remain version- and claim-specific

### MCP 2026-07-28

The official release supports a stateless **protocol core** for that exact version.

Do not infer application statelessness, universal migration, or one universal compatibility strategy.

`PROTOCOL_STATELESSNESS != APPLICATION_STATELESSNESS`.

### A2A v1.0

A2A supplies inter-agent constructs including Agent Cards, Tasks, Messages, Artifacts, Context, streaming/push behavior, and extensions.

A2A/MCP responsibility comparison can be an analytical design boundary.

Use:

`ANALYTICAL_BOUNDARY_SUPPORTED / NORMATIVE_LAYERING_NOT_ESTABLISHED`.

Vendor/community diagrams do not create a universal protocol stack law.

## 13. Benchmarks and thresholds remain scoped

A benchmark, vendor study, survey, customer case study, or secondary failure report cannot by itself establish a universal architecture threshold.

Historical five-node or zero-failure language is therefore interpreted as at most a provisional/local guardrail unless direct evidence supports more.

Use:

`PROVISIONAL_GUARDRAIL_NOT_EXTERNAL_LAW`.

## 14. Observability surfaces must remain separate

Keep distinct:

- trace/span/transcript/trajectory
- model/tool input and output
- external/world-state change
- outcome
- grader result
- reviewer decision
- runtime governance feature

OpenTelemetry GenAI semantic conventions establish the telemetry concepts they define. They do not automatically establish framework-specific patterns such as MLflow `span-per-tick`, hidden reasoning capture, kill-switch governance, or ecosystem consensus.

Use:

`OTEL_SEMANTIC_CONVENTION + FRAMEWORK_GUIDANCE + GOVERNANCE_FEATURE_ARE_DISTINCT`.

## 15. Threat, legal, and local-host claims require their own evidence

External security analysis can support a threat-model hypothesis, not a local Horizon/host incident.

Use:

`THREAT_MODEL_HYPOTHESIS / LOCAL_INCIDENT_NOT_ESTABLISHED`.

Vendor compliance architecture can support engineering interpretation, not a legal mandate.

Use:

`VENDOR_COMPLIANCE_INTERPRETATION / LEGAL_ARCHITECTURE_NOT_ESTABLISHED`.

## 16. Historical correction method

Historical H1–H4 files remain point-in-time evidence.

When later evidence changes current interpretation, prefer explicit reconciliation that records:

- historical state
- later evidence
- current bounded interpretation
- unresolved dimensions

Current interpretation may change without rewriting the historical artifact.

Formal August H5/H6 remains open until the natural monthly lifecycle has actual evidence.
