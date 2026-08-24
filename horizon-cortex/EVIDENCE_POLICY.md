# Horizon Cortex Evidence Policy

Status: independent post-hoc interpretation policy
Maintenance calibration: 2026-08-24

This file documents how committed Horizon H1–H6 artifacts are interpreted against the repository that actually exists. It is descriptive repository research, not an instruction surface for artifact producers or the host runtime.

## 1. Repository architecture grounding

Horizon is one evidence/research surface inside a repository with several distinct implementation domains. Claims in Horizon MUST be interpreted against those real boundaries instead of being promoted into a repository-wide architecture claim by default.

### Public presentation surface

- `index.html` is the public portal entry point.
- `src/scripts/translations.js` provides presentation-layer translation content.
- The portal is a display surface; it is not the NEXUS knowledge engine and it is not Horizon.

### NEXUS Cortex knowledge lifecycle

`docs/brain/` contains the repository's implemented local knowledge lifecycle.

`docs/brain/nexus.py` exposes the current command surface:

- `harvest` — synchronize explicitly configured external source material
- `project` — normalize/project current source snapshots into the knowledge layer
- `ingest` — map supported repository code/configuration structures
- `ponder` — compute graph-derived structural signals
- `evolve` — run the local evolution cycle
- `rebuild` — reconstruct the SQLite index from canonical JSONL records
- `search` / `status` — query the local graph/index state

The implementation therefore supports a concrete distinction between:

1. source/input material
2. canonical JSONL knowledge records
3. a rebuildable SQLite/FTS5 query index
4. generated structural observations
5. public presentation

These are not interchangeable evidence surfaces.

### Canonical ledger versus query index

`docs/brain/cortex.py` persists entity/relation records to JSONL while maintaining a SQLite graph/index for active retrieval and structural analysis.

- JSONL records are the durable text-side evidence/knowledge surface used by rebuild.
- `cortex.db` is a local query/index surface and can be reconstructed from the JSONL knowledge records.
- `valid_at` / `invalid_at` fields express application-level temporal validity for active graph state.
- FTS5 and graph expansion support retrieval; retrieval rank or graph weight is not a truth score.
- append-only application behavior is not cryptographic immutability and must not be described as such without a separate integrity mechanism.

### Scholar mapping boundary

`docs/brain/scholar.py` maps supported code/configuration structures into the graph. Its configured ignore/protected paths explicitly exclude research/control-plane directories including `horizon-cortex` and `parallax`, along with generated knowledge/input/memory paths.

That exclusion is an important real architectural boundary:

`HOST_CODE_STRUCTURE_SCAN != HORIZON_RESEARCH_INGESTION`.

A Horizon statement does not automatically become a NEXUS graph fact merely because both live in the same repository.

### Reasoning boundary

`docs/brain/reason.py` computes structural observations such as orphan nodes, reciprocal relations, transitive patterns, PageRank-style centrality, graph-density signals, and generated research prompts/summaries.

Those outputs are graph-derived heuristics over the current indexed state. They are not external-source verification, semantic truth, causal proof, or production telemetry.

Use:

`GRAPH_STRUCTURAL_SIGNAL / CLAIM_TRUTH_NOT_ESTABLISHED`.

### Horizon and Parallax separation

`horizon-cortex/` and `parallax/` are separate research/evidence surfaces. Their presence does not change the executable semantics of `docs/brain/**`, the public portal, or host code unless an explicit repository change does so.

This policy does not publish or encode private maintenance reasoning, hidden prompts, future automation strategy, or unpublished control logic.

## 2. Structural checker boundary

`horizon-cortex/check.py` validates artifact contracts such as names, required sections, logical dates/weeks, handoffs, decision/action IDs, and repository-boundary markers.

A checker pass does **not** establish:

- factual truth of an external claim
- source independence
- source authority for the specific claim
- currentness
- legal or regulatory correctness
- host applicability
- production adoption
- local runtime success
- local incident occurrence
- NEXUS graph correctness beyond the fields actually checked

Structural validity and evidentiary validity are separate states.

## 3. Evidence states must not be collapsed

Use distinct meanings for at least the following states:

- `SOURCE_ACCESS_VERIFIED`: a page or artifact was reachable/read
- `SOURCE_IDENTITY_VERIFIED`: publisher/title/version identity was checked
- `PRIMARY_SOURCE_FOR_CLAIM`: the source is primary for the exact proposition being asserted
- `CLAIM_SUPPORTED`: the exact bounded proposition is supported by the cited evidence
- `SECONDARY_SOURCE`: reporting, aggregation, review, or analysis of another source
- `VENDOR_INTERPRETATION`: first-party or vendor engineering interpretation, positioning, or design guidance
- `CASE_STUDY`: one implementation/deployment example
- `ANALYTICAL_TAXONOMY`: a useful classification that is not a normative standard
- `THREAT_MODEL_HYPOTHESIS`: a plausible risk or attack analysis not yet demonstrated as a local incident
- `LOCAL_INCIDENT_NOT_ESTABLISHED`: no evidence that the discussed external risk occurred in this repository
- `HOST_APPLICABILITY_UNKNOWN`: host code/configuration was not established by the Horizon artifact

A source can be official for its own product while still being secondary or interpretive for a protocol-wide, market-wide, legal, or cross-ecosystem proposition.

Directly opening a secondary article does not turn it into a primary source.

## 4. Source authority is claim-specific

For a material protocol or product claim prefer, in order:

1. current official specification / primary protocol release for normative protocol semantics
2. official SDK or first-party technical documentation for that implementation
3. official deployment/product documentation for that product or service
4. original research for the bounded study result
5. secondary/vendor commentary for interpretation, examples, or watchlist context
6. community aggregators for discovery only unless independently verified

Examples:

- an MCP specification can establish protocol semantics
- a Google or Cloudflare engineering post can establish its own implementation/support, but not universal adoption
- a vendor security post can identify a threat-model hypothesis, but not prove a local vulnerability or incident
- a community directory can establish that it lists a project, but not primary-source project identity, quality, durability, or ecosystem adoption
- a survey article can report survey findings, but it is not automatically the primary survey dataset

## 5. Repetition and inheritance do not upgrade evidence

Horizon is a sequential research stream. H1 can feed H2; Daily artifacts can feed H3/H4; older records can influence later research focus.

Repeated wording is **not independent corroboration**.

Rules:

- H2 repeating H1 does not create a second source
- H3 synthesizing seven H2 files does not increase authority if those files inherit the same weak upstream proposition
- H4 acting on H3 does not upgrade a provisional decision into an externally established law
- a retained historical memory does not become evidence for an external claim merely because a later record compares against it
- a later record saying an older decision was “validated” does not establish validation unless fresh claim-level evidence supports the older proposition

Use:

`WEEKLY_INHERITANCE_DOES_NOT_UPGRADE_EVIDENCE`.

When a later reconciliation narrows an upstream proposition, downstream inherited wording is interpreted through the narrowed proposition even if the historical downstream file remains unchanged.

## 6. Historical input state and delivery state

When they differ, record separately:

- logical date / target week
- actual execution time when available
- generation/commit evidence
- merge/delivery visibility
- weekly/monthly aggregation snapshot visibility
- current repository presence

`missing at the aggregation snapshot` is not automatically `never generated`.

A later merge can repair final delivery without retroactively changing an earlier `BLOCKED` run to `SUCCESS`.

If one historical artifact states an upstream file was `INPUT_MISSING` while the retained upstream artifact records `SUCCESS`, preserve the conflict as:

`HISTORICAL_INPUT_STATE_MISMATCH`.

## 7. Support, deployment, adoption, and dominance are different claims

Never collapse these levels:

- specification exists
- SDK/product supports the specification
- a provider offers an implementation
- a provider uses it in a named environment
- customers use it in production
- many independent organizations use it in production
- the ecosystem has broadly adopted it
- it is dominant or a de facto universal standard

Each stronger level requires its own evidence.

Use bounded labels such as:

- `PROTOCOL_VERSION_FACT`
- `FIRST_PARTY_IMPLEMENTATION_SUPPORT`
- `NAMED_DEPLOYMENT_EXAMPLE`
- `ECOSYSTEM_OBSERVATION`
- `ADOPTION_RATE_NOT_ESTABLISHED`
- `UNIVERSAL_ADOPTION_NOT_ESTABLISHED`

A press release saying a protocol has more than N participating/supporting organizations plus some production use does not establish that all N organizations are production users.

## 8. Legal and compliance claims

Vendor compliance guidance may be useful as an engineering interpretation, but it cannot by itself establish that a statute or regulation mandates the vendor's preferred architecture.

Use:

- `VENDOR_COMPLIANCE_INTERPRETATION`
- `LEGAL_REQUIREMENT_REQUIRES_PRIMARY_LAW_SOURCE`
- `LEGAL_ARCHITECTURE_NOT_ESTABLISHED`

Do not infer that a Context Layer, MCP server, PDP, specific data platform, or other technical pattern is legally mandatory unless the primary legal/regulatory text directly supports that requirement.

## 9. Protocol calibration — MCP 2026-07-28

The official MCP 2026-07-28 release establishes a stateless **protocol core** for that version. It removes the prior required protocol-level initialization/session mechanism and changes/adds the mechanisms described by that exact release.

Current interpretation rules:

- protocol statelessness is not application statelessness
- a stateful application can still maintain explicit application state
- vendor deployment examples do not prove ecosystem-wide migration
- third-party migration guides do not become official compatibility guarantees
- metadata, routing, authorization, application handles, and durable application state must not be collapsed into one generic “state” mechanism
- exact protocol claims remain tied to the exact specification/release that defines them

Historical shorthand such as `MCP 2.0`, “fully stateless application”, “all servers must migrate”, or an assumed universal compatibility shim is not authoritative merely because it appears repeatedly.

## 10. A2A / MCP relationship

A2A v1.0 is a stable agent-to-agent interoperability protocol with Agent Cards, Tasks, Messages, Artifacts, Context, streaming/push mechanisms, and extensions.

It is reasonable to compare A2A and MCP as different responsibility surfaces.

Do **not** promote ecosystem diagrams or vendor blogs into a normative universal layering law.

Use:

`ANALYTICAL_BOUNDARY_SUPPORTED / NORMATIVE_LAYERING_NOT_ESTABLISHED`.

## 11. Research result and architecture-threshold boundary

A bounded benchmark, internal eval, customer case study, survey, vendor benchmark, or secondary article cannot by itself establish a universal architecture threshold.

In particular:

- Anthropic's reported multi-agent research result remains scoped to its reported research system/eval
- a customer productivity anecdote is a separate evidence object
- secondary summaries of multi-agent failure studies do not establish a universal “five-node law”
- a fixed node/step limit can be a provisional local guardrail only if clearly labeled as such
- no external evidence reviewed in this August stage establishes a universal zero-failure architecture or universal optimal agent count

Use:

`PROVISIONAL_GUARDRAIL_NOT_EXTERNAL_LAW`.

## 12. Observability and evaluation vocabulary

Keep these evidence surfaces distinct:

- trace / span / transcript / trajectory
- tool calls and tool results
- model input/output content
- world-state or external-state change
- outcome
- grader result
- reviewer decision
- runtime governance/control feature

A trace proves that something was recorded, not that the outcome was correct.

An observability article's recommended instrumentation pattern is not automatically a normative OpenTelemetry requirement.

OpenTelemetry GenAI semantic conventions can establish supported telemetry concepts/attributes where defined; they do not by themselves establish every framework-specific tracing pattern, hidden reasoning capture, or operational governance feature.

Use:

- `OTEL_SEMANTIC_CONVENTION`
- `FRAMEWORK_ENGINEERING_GUIDANCE`
- `GOVERNANCE_FEATURE_SEPARATE_FROM_TELEMETRY_STANDARD`

## 13. Threat-model and security-analysis boundary

A security vendor can identify plausible attack surfaces or control considerations. Unless independently demonstrated, keep these as threat-model hypotheses.

Do not transform external threat analysis into a local incident, local vulnerability, or mandatory host remediation without local evidence.

Use:

`THREAT_MODEL_HYPOTHESIS / LOCAL_INCIDENT_NOT_ESTABLISHED`.

## 14. Historical corrections

Prefer reconciliation when later evidence changes interpretation but the original execution record remains useful.

A reconciliation should state:

- original run state
- later evidence
- current calibrated interpretation
- what is superseded
- what remains unresolved

Do not rewrite history to pretend later evidence was visible during the original task.

Current interpretation may supersede historical wording without deleting the evidence that the wording was generated.

## 15. Boundary

This policy is documentation/evidence maintenance only. It changes no host code, public portal behavior, NEXUS runtime behavior, dependency set, deployment state, or artifact-production configuration.
