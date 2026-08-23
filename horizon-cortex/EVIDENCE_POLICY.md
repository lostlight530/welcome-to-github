# Horizon Cortex Evidence Policy

Status: independent post-hoc interpretation policy

This file documents how maintainers should interpret committed Horizon H1–H6 artifacts. It is not a Jules prompt, memory entry, cadence rule, scheduler configuration, CI gate, GitHub Action, or host-repository instruction.

## 1. Checker boundary

`horizon-cortex/check.py` validates deterministic file contracts: names, required sections, logical dates/weeks, handoffs, decision/action IDs, and repository-boundary markers.

A checker pass does **not** establish that an external source is correct, independent, current, or sufficient for the strength of a research conclusion.

Structural validity and factual validity are separate states.

## 2. Time and delivery dimensions

When they differ, record separately:

- logical date / target week
- actual execution time
- generation/commit evidence
- merge/delivery visibility
- weekly/monthly aggregation snapshot visibility
- current repository presence

`missing at the aggregation snapshot` is not automatically `never generated`.

A later merge can repair final delivery without retroactively changing an earlier `BLOCKED` run to `SUCCESS`.

## 3. Source hierarchy

For a material protocol or product claim prefer, in order:

1. current official specification / primary protocol release
2. official SDK or first-party technical documentation
3. official deployment/product documentation
4. original research
5. secondary/vendor commentary

Multiple pages repeating one upstream claim do not automatically create independent corroboration.

## 4. Claim strength

Horizon may observe an external mechanism without asserting universal adoption.

Use bounded forms such as:

- `PROTOCOL_VERSION_FACT`
- `FIRST_PARTY_IMPLEMENTATION_SUPPORT`
- `ECOSYSTEM_OBSERVATION`
- `ANALYTICAL_BOUNDARY`
- `UNIVERSAL_ADOPTION_NOT_ESTABLISHED`

Avoid turning a concrete implementation example into an industry-wide topology law.

## 5. Protocol calibration — 2026-08-24

### MCP 2026-07-28

The official MCP 2026-07-28 release establishes a stateless **protocol core** for that version. It retires the previous required `initialize`/`initialized` exchange and `Mcp-Session-Id`, adds optional `server/discover`, MRTR, routable headers, cacheable list semantics, an extensions framework, authorization hardening, and formal deprecations.

This does not imply that applications built above MCP are stateless or that every ecosystem deployment has migrated.

### A2A v1.0

A2A v1.0 is the stable production-ready protocol line for agent-to-agent interoperability. It defines Agent Cards, stateful Tasks, Messages, Artifacts, optional Context, streaming, push updates, and extensions.

It is reasonable to analyze A2A and MCP as different protocol responsibility surfaces, but `A2A = high layer` and `MCP = low layer` is an architectural interpretation, not a normative layering rule imposed by either specification.

## 6. Historical corrections

Prefer reconciliation when later evidence changes interpretation but the original execution record remains useful.

A reconciliation should state:

- original run state
- later evidence
- current calibrated interpretation
- what is superseded
- what remains unresolved

Do not rewrite history to pretend the later evidence was visible during the original task.

## 7. GPT/Parallax quality transfer

The separate Parallax research method provides useful reviewer-side disciplines that Horizon can reuse **as interpretation principles**, without merging the two control planes:

- assigned/logical date differs from actual execution date
- source reachability differs from source authority
- facts, inferences, and unverified items are separate
- later backfill cannot masquerade as same-day observation
- repeated source count differs from source independence
- monthly/weekly views are derived views and do not replace atomic evidence

Horizon remains a separate Jules OODA-style research stream. Parallax remains a separate GPT-maintained research stream.

## 8. Boundary

This policy changes no host code, frontend, automation, scheduler, prompts, memory, Actions, CI, deployment, or runtime behavior.
