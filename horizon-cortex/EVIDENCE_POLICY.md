# Horizon Cortex Evidence Policy

Status: independent post-hoc interpretation policy
Maintenance calibration: 2026-08-24

This file documents how maintainers should interpret committed Horizon H1–H6 artifacts. It is not a Jules prompt, memory entry, cadence rule, scheduler configuration, CI gate, GitHub Action, host-repository instruction, or hidden producer rule.

## 1. Structural checker boundary

`horizon-cortex/check.py` validates deterministic artifact contracts such as names, required sections, logical dates/weeks, handoffs, decision/action IDs, and repository-boundary markers.

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

Structural validity and evidentiary validity are separate states.

## 2. Evidence states must not be collapsed

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
- `HOST_APPLICABILITY_UNKNOWN`: host code/configuration was intentionally not inspected

A source can be official for its own product while still being secondary or interpretive for a protocol-wide, market-wide, legal, or cross-ecosystem proposition.

Directly opening a secondary article does not turn it into a primary source.

## 3. Source authority is claim-specific

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

## 4. Repetition and inheritance do not upgrade evidence

Horizon is a sequential research stream. H1 can feed H2; Daily artifacts can feed H3/H4; older H4/H6 can influence later search focus.

Therefore repeated wording is **not independent corroboration**.

Rules:

- H2 repeating H1 does not create a second source
- H3 synthesizing seven H2 files does not increase authority if those files inherit the same weak upstream proposition
- H4 acting on H3 does not upgrade a provisional decision into an externally established law
- H6 memory does not become evidence for the external claim merely because later Daily artifacts compare against it
- a later Daily record saying an older decision was “validated” does not establish validation unless fresh claim-level evidence actually supports the older proposition

Use: `WEEKLY_INHERITANCE_DOES_NOT_UPGRADE_EVIDENCE`.

When a later reconciliation narrows an upstream proposition, downstream inherited wording is interpreted through the narrowed proposition even if the historical downstream file remains unchanged.

## 5. Historical input state and delivery state

When they differ, record separately:

- logical date / target week
- actual execution time
- generation/commit evidence
- merge/delivery visibility
- weekly/monthly aggregation snapshot visibility
- current repository presence

`missing at the aggregation snapshot` is not automatically `never generated`.

A later merge can repair final delivery without retroactively changing an earlier `BLOCKED` run to `SUCCESS`.

If one historical artifact states an upstream file was `INPUT_MISSING` while the retained upstream artifact records `SUCCESS`, do not silently choose one. Record:

`HISTORICAL_INPUT_STATE_MISMATCH`

and preserve both artifacts unless stronger timestamped delivery evidence resolves the discrepancy.

## 6. Support, deployment, adoption, and dominance are different claims

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

## 7. Legal and compliance claims

Vendor compliance guidance may be useful as an engineering interpretation, but it cannot by itself establish that a statute or regulation mandates the vendor's preferred architecture.

Use:

- `VENDOR_COMPLIANCE_INTERPRETATION`
- `LEGAL_REQUIREMENT_REQUIRES_PRIMARY_LAW_SOURCE`
- `LEGAL_ARCHITECTURE_NOT_ESTABLISHED`

Do not infer that a Context Layer, MCP server, PDP, specific data platform, or other technical pattern is legally mandatory unless the primary legal/regulatory text directly supports that requirement.

## 8. Protocol calibration — MCP 2026-07-28

The official MCP 2026-07-28 release establishes a stateless **protocol core** for that version. It removes the prior required `initialize` / `initialized` exchange and protocol-level session mechanism, and adds/changes features including discovery/routing/cacheability/extensions/authorization/deprecation mechanisms described by that release.

Current interpretation rules:

- protocol statelessness is not application statelessness
- a stateful application can still maintain explicit application state
- vendor deployment examples do not prove ecosystem-wide migration
- third-party migration guides do not become official compatibility guarantees
- `_meta`, HTTP routing headers, auth headers, and application handles must not be collapsed into one generic “header/state” mechanism
- exact header/extension claims should remain tied to the exact specification/source that defines them

Historical shorthand such as `MCP 2.0`, “fully stateless application”, “all servers must migrate”, or an assumed universal compatibility shim is not authoritative merely because it appears repeatedly in H1/H2/H3/H4.

## 9. A2A / MCP relationship

A2A v1.0 is a stable agent-to-agent interoperability protocol with Agent Cards, Tasks, Messages, Artifacts, Context, streaming/push mechanisms, and extensions.

It is reasonable to compare A2A and MCP as different responsibility surfaces.

Do **not** promote ecosystem diagrams or vendor blogs into a normative universal layering law such as:

- `MCP = mandatory low/tool layer`
- `A2A = mandatory high/coordination layer`
- `ACP/UCP = mandatory business layer`

Use:

`ANALYTICAL_BOUNDARY_SUPPORTED / NORMATIVE_LAYERING_NOT_ESTABLISHED`.

## 10. Research result and architecture-threshold boundary

A bounded benchmark, internal eval, customer case study, survey, vendor benchmark, or secondary article cannot by itself establish a universal architecture threshold.

In particular:

- Anthropic's reported multi-agent research result remains scoped to its reported research system/eval
- a customer productivity anecdote is a separate evidence object
- secondary summaries of multi-agent failure studies do not establish a universal “five-node law”
- a fixed node/step limit can be a provisional local guardrail only if clearly labeled as such
- no external evidence reviewed in this August stage establishes a universal zero-failure architecture or a universal optimal agent count

Use:

`PROVISIONAL_GUARDRAIL_NOT_EXTERNAL_LAW`.

## 11. Observability and evaluation vocabulary

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

OpenTelemetry GenAI semantic conventions can establish supported telemetry concepts/attributes where defined; they do not by themselves establish every framework-specific tracing pattern, hidden reasoning capture, or operational governance feature such as a kill switch.

Use:

- `OTEL_SEMANTIC_CONVENTION`
- `FRAMEWORK_ENGINEERING_GUIDANCE`
- `GOVERNANCE_FEATURE_SEPARATE_FROM_TELEMETRY_STANDARD`

## 12. Threat-model and security-analysis boundary

A security vendor can identify plausible attack surfaces or control considerations. Unless independently demonstrated, keep these as threat-model hypotheses.

Do not transform:

- header/body mismatch analysis
- stale capability/cache analysis
- authorization architecture suggestions
- an external OWASP-style category

into a local incident, local vulnerability, or mandatory host remediation.

Use:

`THREAT_MODEL_HYPOTHESIS / LOCAL_INCIDENT_NOT_ESTABLISHED`.

## 13. Historical corrections

Prefer reconciliation when later evidence changes interpretation but the original execution record remains useful.

A reconciliation should state:

- original run state
- later evidence
- current calibrated interpretation
- what is superseded
- what remains unresolved

Do not rewrite history to pretend the later evidence was visible during the original task.

Current interpretation may supersede historical wording without deleting the evidence that the wording was generated.

## 14. GPT/Parallax quality transfer

The separate Parallax research method provides useful reviewer-side disciplines that Horizon can reuse **as interpretation principles**, without merging control planes:

- assigned/logical date differs from actual execution date
- source reachability differs from source authority
- facts, inferences, and unverified items are separate
- later backfill cannot masquerade as same-day observation
- repeated source count differs from source independence
- weekly/monthly views are derived views and do not replace atomic evidence

Horizon remains a Jules OODA-style research stream. Parallax remains a separate GPT-maintained research stream.

A reviewer-side policy appearing later in the repository does not prove Jules consumed or enforced it during earlier runs.

## 15. Boundary

This policy changes no host code, frontend, automation, scheduler, prompts, memory, GitHub Actions, CI, deployment, dependency, or runtime behavior.

Documentation/evidence maintenance may state `tests not run — documentation/evidence only` when executable behavior is untouched. That statement is not test evidence and does not upgrade implementation status.
