# Open Research / 开放科研

Status: durable open-research production guide
Scope: repository-level research positioning, research-production method, scholarly-metadata boundaries, and semantic-drift governance

## 1. Authority

This file explains how open research is produced and reviewed in this repository. It does not replace implementation, architecture, methodology, evidence, maintenance, release, or historical authority.

```text
current repository truth
        ↓
repository-native implementation / methodology / evidence contracts
        ↓
OPEN_RESEARCH.md
        ↓
RESEARCH_TEMPLATE.md
        ↓
prospective research records
        ↓
scholarly metadata / downstream indexes
```

When a repository-native contract is stricter, the stricter rule wins.

## 2. Canonical positioning

**Canonical Type:** Open research software portal and agent-systems evidence infrastructure

**One-line positioning:** Agent-systems evidence and research infrastructure for evidence stability, provenance, research continuity, and bounded interpretation.

**Primary domains:** agent systems; research infrastructure; provenance; reproducibility; knowledge lifecycle.

**Non-goals:** generic GitHub tutorial; business-process product; capability benchmark; autonomous-agent product.

Repository identity is owned here by repository truth, not by an external classifier.

```text
External Classification != Repository Identity
Inferred Topic != Canonical Research Domain
Keyword Match != Project Purpose
Scholarly Graph Representation != Repository Self-Definition
```

## 3. Open-research production model

The common epistemic skeleton is shared across the ten-repository research system, while this repository retains its own method, vocabulary, evidence boundaries, and operational contracts.

A substantive research unit should make recoverable, when applicable:

1. research question;
2. falsifiable hypothesis or bounded judgment;
3. source/evidence identity and independence;
4. fixed object, revision, environment, or execution identity;
5. procedure actually executed or inspection actually performed;
6. raw observation separated from interpretation;
7. counterexample or disconfirming-evidence check;
8. bounded conclusion and unresolved uncertainty;
9. research increment;
10. retest condition.

A cadence event may validly yield `NONE`, `NO_CONCLUSION`, `UNKNOWN`, `PARTIAL`, `DEGRADED`, `REFUTED`, or `INVALIDATED`. Cadence completion is not itself scientific progress.

## 4. Repository-specific method

Detailed operational semantics remain owned by `parallax/METHOD.md`, `parallax/templates/**`, Horizon research surfaces, and other stricter repository-native contracts.

Relevant research surfaces include evidence identity and support calculus, temporal/current-state correctness, execution/harness/evaluator provenance, capability/deployment/semantic-outcome separation, delegated evidence chains, and world-state drift.

```text
same logical date != same Git snapshot
source presence != source support
execution success != scientific validity
later evidence != earlier availability
```

## 5. Evidence and execution discipline

Record direct observations before interpretation. Unknown, unavailable, unexecuted, and unobserved states remain explicit.

```text
raw observation != interpretation
source existence != source truth
checker present != checker executed
checker pass != scientific truth
repository publication != external corroboration
```

Research records must not claim execution, reproduction, validation, adoption, citation impact, or external review that was not actually observed.

## 6. Open-science foundation

The repository's public open-science surfaces include, where present:

- `README.md` for public orientation;
- `OPEN_RESEARCH.md` for durable research-production guidance;
- `RESEARCH_TEMPLATE.md` for prospective research records;
- `AUTHORS` for authorship identity;
- `LICENSE` for repository-owned reuse terms;
- `CITATION.cff` and `codemeta.json` for citation/software metadata;
- `CONTRIBUTING.md` for contribution workflow;
- `CODE_OF_CONDUCT.md` and `SECURITY.md` for community and security governance;
- `RELEASE_POLICY.md` for release/archive semantics;
- `.github/ISSUE_TEMPLATE/**` and the pull-request template for reviewable change intake.

These files support openness, attribution, reuse, citation, review, and archival identity. They do not establish scientific validity by themselves.

## 7. Scholarly metadata discipline

Before a future scholarly-metadata publication or revision, preserve:

- Canonical Type;
- One-line Positioning;
- Primary Domains;
- Non-goals;
- a small set of accurate structured subjects where supported;
- 5–7 defining keywords rather than keyword stuffing.

Descriptions remain technically accurate rather than being rewritten for a downstream classifier.

## 8. Shadow classification

A pre-publication shadow check may compare candidate title + abstract/description with downstream topic/keyword inference.

Allowed dispositions:

```text
ALIGNED
PARTIALLY_ALIGNED
MISCLASSIFIED
CLASSIFIER_NOISE
```

Whether the shadow check ran is recorded separately as `RUN` or `NOT_RUN`.

If repository wording is genuinely ambiguous, repair the owning metadata layer. If canonical positioning is already explicit and downstream inference still drifts, preserve repository identity and record classifier noise.

## 9. Semantic drift audit

A periodic semantic-drift review may compare:

```text
repository canonical positioning
CITATION.cff
CodeMeta
archive metadata
DOI metadata
OpenAIRE representation
OpenAlex representation
```

Classify drift by owner:

- **CANONICAL_DRIFT** — repository-owned positioning surfaces disagree;
- **TRANSPORT_DRIFT** — repository metadata is correct but an archival/DOI projection loses or alters meaning;
- **DERIVATION_DRIFT** — upstream metadata is coherent but a downstream classifier infers a misleading topic;
- **VERSION_SKEW** — archived/versioned scholarly representations are confused with later current `main`.

`DERIVATION_DRIFT != REPOSITORY_DEFECT`.

## 10. History and correction

New results do not silently rewrite point-in-time research history.

```text
CURRENT_STATE != TASK_TIME_STATE
LATER_SUCCESS != EARLIER_SUCCESS
PUBLICATION_IDENTITY != CURRENT_MAIN
RESEARCH_PRODUCTION != MAINTENANCE != PERIODIC_AUDIT
```

Later evidence, later source availability, later execution success, or metadata repair changes current interpretation only through an explicit correction, reconciliation, or new timepoint record.

## 11. Contribution and review

Research contributions should identify the owning surface, preserve exact evidence and identity boundaries, state verification actually performed, disclose unexecuted checks, and keep historical impact explicit.

Use `RESEARCH_TEMPLATE.md` for new bounded research records. Do not retrofit historical records merely to match the current template.

## 12. Permanent boundary

```text
research record != capability claim
publication != validation
usage != adoption
citation != reproduction
metadata consistency != scientific correctness
external indexing != repository self-definition
```
