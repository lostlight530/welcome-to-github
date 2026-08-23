# Horizon Cortex

Horizon Cortex is the repository-local research record for the H1–H6 periodic lifecycle.

This directory preserves both **point-in-time Jules research artifacts** and **later evidence-maintenance records**. Those two classes must not be collapsed into one history.

## Cadence and canonical artifacts

| Layer | Cadence | Canonical filename | Role |
|---|---|---|---|
| H1 | Daily | `YYYY-MM-DD-H1-signal-observe.md` | Observe external signals and source evidence |
| H2 | Daily | `YYYY-MM-DD-H2-horizon-orient.md` | Orient same-day H1 evidence without making weekly decisions |
| H3 | Weekly | `YYYY-Www-H3-position-decide.md` | Synthesize the ISO-week signal set and record bounded decisions |
| H4 | Weekly | `YYYY-Www-H4-narrative-act.md` | Map H3 decisions into bounded research actions / next-week notes |
| H5 | Monthly | `YYYY-MM-H5-signal-reflect.md` | Reflect on the natural-month signal history |
| H6 | Monthly | `YYYY-MM-H6-horizon-memorize.md` | Record bounded durable/expiring horizon memory |

Weekly logical time uses `Asia/Shanghai` and ISO Monday–Sunday windows under the existing artifact contract.

## Read order and authority

When records appear to disagree, use this order:

1. **Original H1–H6 artifact** — authoritative for what that run recorded at that point in time
2. **Explicit reconciliation / erratum** — authoritative for later interpretation of the named issue, but never retroactive execution success
3. [`EVIDENCE_POLICY.md`](./EVIDENCE_POLICY.md) — current reviewer-side evidence semantics
4. **Stage audit** — inventory/synthesis of a declared time window; not a substitute for the original run
5. **Current external source** — used to revalidate a material external claim when version/date drift matters

A later reconciliation can supersede an interpretation. It cannot rewrite the fact that an earlier H4 was blocked, an input was missing at a snapshot, or a source claim had not yet been revalidated.

## August 2026 reference records

- [`2026-08-through-23-stage-audit.md`](./2026-08-through-23-stage-audit.md) — provisional 2026-08-01 through 2026-08-23 lifecycle/evidence audit
- [`2026-W33-reconciliation.md`](./2026-W33-reconciliation.md) — W33 post-hoc evidence calibration
- [`2026-W34-reconciliation.md`](./2026-W34-reconciliation.md) — W34 delivery-order and protocol-evidence reconciliation
- [`EVIDENCE_POLICY.md`](./EVIDENCE_POLICY.md) — durable interpretation rules derived from the August review

The formal August H5/H6 lifecycle remains separate from the provisional stage audit. A pre-month-end audit must never be relabeled as the final monthly record.

## Coverage semantics

Keep these dimensions separate whenever they differ:

- logical date / week / month
- actual execution time
- generation evidence
- commit / merge / delivery visibility
- weekly or monthly aggregation-snapshot visibility
- current repository path presence
- substantive source/evidence completeness

`CURRENTLY_PRESENT` does not imply `AVAILABLE_AT_ORIGINAL_SNAPSHOT`, `EXECUTION_SUCCESS`, or `EVIDENCE_COMPLETE`.

## Checker boundary

`check.py` validates deterministic repository structure and handoff contracts. It does **not** establish the truth, independence, freshness, adoption breadth, or causal meaning of external research claims.

A checker pass is structural evidence only.

## Repository boundary

This directory is a research/evidence surface. Documentation maintenance here does not by itself authorize changes to host code/frontend, Jules prompts/memory/cadence/scheduler, GPT/Parallax controls, `.github/**`, Actions/CI, deployment/runtime behavior, or merge gates.

Preserve original execution history; add reconciliation when interpretation changes.