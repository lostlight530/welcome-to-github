# Horizon Cortex Evidence Policy

Status: current repository evidence policy  
Calibration: 2026-09-02

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

Authorized corrections may minimally update erroneous prose with an explicit maintenance log. Original execution facts remain unchanged.

The Aug 27 stage audit is an as-of snapshot, not the final authority for later delivery or correction. See `2026-09-02-maintenance-log.md` for this pass and its limits.

At the Aug 27 cutoff the August monthly surface was OPEN. Later file delivery does not by itself establish completed content maintenance.

## 16. Active daily and weekly record contract

New H1 and H2 records identify source identity, authority for the exact claim, independent verification, host applicability, evidence-upgrade basis, original execution status, current path status, and record provenance.

New H3 and H4 records provide a Daily coverage matrix, inherited and newly independent evidence, preserved missing inputs, decision evidence basis, historical execution state, and current delivery state.

Substitutes and reconstructions use their real agent identity. A reconstruction cannot claim original success. Historical execution facts remain preserved. Authorized prose corrections are logged, and legacy schema defects are not disguised as original compliant execution.

`CURRENT_PATH_PRESENT != ORIGINAL_EXECUTION_SUCCESS`.

`EXTERNAL_PROTOCOL_FACT != HOST_ADOPTION_REQUIREMENT`.

## 17. August closure and forward contract

The 2026-08-01 through 2026-08-31 Daily surface contains 31 H1/H2 pairs.

The files from 2026-08-29 through 2026-08-31 were generated after the active provenance contract was defined but do not contain its fields. Their original execution facts remain point-in-time evidence and are calibrated by `2026-08-month-end-reconciliation.md`.

W35 contains no H3. Its H4 is a retained fail-closed execution record with `DECISION_INPUT_MISSING`, `BLOCKED`, and `NO_ACTIONABLE_DECISION`. A missing H3 is acceptable only under that complete fail-closed state.

Beginning with logical date 2026-09-01 and logical week 2026-W36, the checker requires the active contract even when a generator omits `Record Provenance` entirely.

Monthly H5/H6 records require Daily and Weekly coverage matrices, inherited and independent evidence separation, preserved missing inputs, claim calibration, execution and path state separation, and real record provenance.

H5 may claim complete coverage only after the Shanghai calendar month ends and every calendar-day H1/H2 input has an explicitly reviewed delivery and quality state. File presence alone is insufficient. H6 must name the same-month H5 and may retain only bounded doctrine that survived H5 calibration.

`DAILY_COMPLETE != WEEKLY_DECISION_COMPLETE`.

`WEEKLY_CLOSED != MONTHLY_CLOSED`.

`MONTHLY_COMPRESSION != NEW_INDEPENDENT_EVIDENCE`.

## Monthly maintenance and correction

A monthly summary is not a completed maintenance pass. Calendar closure, input delivery, original execution and current content quality are separate states.

Within this maintenance surface only:

1. Inventory every logical date, intersecting ISO week, monthly record and cited special/audit in the review window. Identify each input by path and immutable commit or PR head. Record delivered-but-unmerged separately from absent and unknown. A cross-month week keeps its full natural-week boundary and an explicit as-of cutoff.
2. Check actual source access, publication time, claim authority, publisher independence and local applicability. Repeated Daily, Weekly and Monthly wording does not add evidence. A search query, abstract or retrieval hash does not prove a full-text review or an experiment.
3. Correct confirmed wording, arithmetic, links and unsupported promotions in the original document with the smallest scoped edit. Preserve original author, logical date, execution timestamps, provenance and blocked state. Record the old claim, corrected claim, evidence, original commit, reviewer and real correction time in the maintenance log. Never make a later source look available to an earlier run.
4. Trace each corrected claim through downstream daily handoffs, weekly decisions, monthly synthesis, durable findings and indexes. Update affected current interpretations and mark remaining dependencies unresolved. Do not silently repair a missing historical Decision ID by inventing a decision.
5. Adjust active rules, templates and offline checks only for demonstrated recurring defects. Recheck unchanged boundaries. This process does not authorize host runtime, data, frontend, Actions or scheduler changes.
6. Run the existing checks and proportionate regression tests. Log commands, results, skipped checks and remaining evidence gaps. No blanket completion from file counts, a green checker or an old audit alone.

New monthly records use the following compact ledger. A NOT_RUN or PARTIAL result is valid and must not be promoted by the next summarizer.

- `Monthly Maintenance Status`: NOT_RUN, PARTIAL or COMPLETED.
- `Maintenance Coverage`: an exact path inventory and per-file disposition, including weekly/monthly dependencies.
- `Maintenance Change Log`: the dated log, with original identity and before/after reasoning, or an explicitly documented no-change review.
- `Maintenance Validation`: actual commands/results and semantic review limits.
- `Maintenance Unresolved`: precise outstanding items, or NONE only after all scoped work is resolved.

COMPLETED requires the complete scoped inventory, correction propagation, logged validation and no unresolved items. It does not certify universal correctness. A calendar month may be CLOSED while the review task remains BLOCKED or maintenance remains PARTIAL.

Calendar closure uses the original Shanghai execution time, not the date a file was later merged or corrected. Before the first instant of the following month, use OPEN for the as-of snapshot. Missing legacy timestamps remain unknown, not fabricated.

The offline checker validates declared ledger structure, not whether the linked evidence is true, independent or sufficient. The maintainer must read that evidence.
