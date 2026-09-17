# Horizon Cortex / 地平线研究层

Horizon Cortex is the repository's long-lived **research/evidence surface for external technical signals and bounded interpretation**. It is not the NEXUS knowledge runtime, the public portal, or a proof that an observed external capability is deployed locally.

## Read this directory by role

### Current long-lived contract

- [`EVIDENCE_POLICY.md`](./EVIDENCE_POLICY.md) — current source-authority, claim-support, host-applicability, execution/provenance, and interpretation boundaries.

The policy is the durable semantic entry point for Horizon evidence. Its time-scoped examples and historical cutoff statements retain their own recorded dates; current repository state must be recovered from current `main` and the most specific current source/implementation evidence.

### Time-scoped research artifacts

Dated H1/H2 and week/month H3–H6 artifacts record what was observed, interpreted, decided, reflected, or retained at their declared logical period. They are **point-in-time research evidence**, not a current-status database.

A later file, correction, merge, or stronger source can change current interpretation without changing what an earlier run actually observed or produced.

### Structural checker

`check.py` defines structural checks for Horizon artifacts. Checker presence is not checker execution; a structural pass is not external factual validation or proof of source independence.

## Repository boundaries

Keep these systems separate:

```text
Horizon research/evidence
!= docs/brain NEXUS knowledge lifecycle
!= root/public portal presentation
!= Parallax research production
!= repository maintenance/governance
```

`docs/brain/**` owns the host knowledge-lifecycle implementation. Horizon does not become NEXUS state merely because both live in this repository.

Parallax has its own method, cases, notes, records, and research identity. Horizon evidence does not automatically become Parallax evidence, and vice versa.

## Evidence invariants

Horizon uses claim-specific authority rather than source prestige alone.

```text
source accessible
!= source identity verified
!= primary for this proposition
!= claim supported
!= host implementation
!= host execution
```

Repeated citation through Daily/Weekly/Monthly inheritance is one source lineage unless genuinely independent evidence is added.

Protocol publication, implementation support, production deployment, adoption, and dominance are different claims. Protocol state semantics must not be generalized into application or host-runtime semantics without evidence.

## Current versus historical reading

Use the current policy and current repository implementation for present interpretation. Use dated artifacts, reconciliations, or audits only for the time window they actually record.

Do not infer:

- original execution success from current path presence;
- current host adoption from an external protocol release;
- independent corroboration from restating the same source;
- scientific or operational truth from a green structural checker.

## Publication identity

The host repository has its own software DOI and publication metadata at the repository root. That publication identity is **not** an external source for Horizon claims and does not add independent corroboration to Horizon research.

For the current repository-wide public map, see [`../README.md`](../README.md). For current Horizon evidence semantics, start with [`EVIDENCE_POLICY.md`](./EVIDENCE_POLICY.md).
