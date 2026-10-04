# Research Template / 科研记录模板

Status: canonical open-research entry and research-record template
Scope: prospective research production and repository-level open-research guidance
Historical records are not rewritten by this template

## Open research contract / 开放科研契约

Canonical Type: Open research software portal and agent-systems evidence infrastructure

This file is intentionally two-in-one:

1. the durable entry point for how this repository conducts open research; and
2. the reusable template for future bounded research records.

It does **not** replace implementation, architecture, methodology, evidence, maintenance, release, or historical authority. Detailed operational semantics remain owned by `parallax/METHOD.md`, `parallax/templates/**`, Horizon research surfaces, and other stricter repository-native contracts.

### Authority and ownership

```text
current repository truth
        ↓
repository-native implementation / methodology / evidence contracts
        ↓
this open-research entry
        ↓
individual prospective research records
        ↓
scholarly metadata and downstream indexes
```

If a stricter native contract exists, it wins. Research-production guidance does not silently redefine runtime behavior, historical evidence, maintenance cadence, publication identity, or archived releases.

### Minimum research unit

Every new substantive research unit should make recoverable, when applicable:

- research question;
- falsifiable hypothesis or bounded judgment;
- source/evidence identity and independence;
- fixed object/revision/environment identity;
- procedure actually executed or inspection actually performed;
- raw observation separated from interpretation;
- counterexample or disconfirming-evidence check;
- bounded conclusion and unresolved uncertainty;
- research increment;
- retest condition.

A cadence event may legitimately produce `NONE`, `NO_CONCLUSION`, `UNKNOWN`, `DEGRADED`, or another non-positive result. Cadence completion is not evidence of scientific progress.

### Open-science and scholarly-identity surfaces

Repository-owned open-science infrastructure includes, where present, `README.md`, `AUTHORS`, `LICENSE`, `CITATION.cff`, `codemeta.json`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, and `RELEASE_POLICY.md`.

These surfaces support attribution, reuse, citation, contribution, security, and archival identity. They do not establish scientific validity, execution success, adoption, citation impact, or reproduction.

### Canonical positioning and semantic-drift prevention

Before future scholarly-metadata publication or revision, preserve:

- **Canonical Type**;
- **One-line Positioning**;
- **Primary Domains**;
- **Non-goals**;
- a small set of accurate structured subjects where supported;
- 5–7 defining keywords rather than keyword stuffing.

Description text should remain technically accurate rather than being rewritten to satisfy a downstream classifier.

For a pre-publication shadow classification, compare candidate title + abstract/description against repository positioning. Classification disposition is limited to:

```text
ALIGNED
PARTIALLY_ALIGNED
MISCLASSIFIED
CLASSIFIER_NOISE
```

Record whether the check was run separately; `NOT_RUN` is an execution state, not a fifth classification result.

If repository wording is genuinely ambiguous, repair the owning metadata layer. If repository positioning is already explicit and downstream inference still drifts, preserve repository identity and record downstream classifier noise.

A periodic semantic-drift review may compare `CITATION.cff`, CodeMeta, archive metadata, DOI metadata, OpenAIRE, and OpenAlex representations, but external classification never becomes repository authority.

```text
External Classification != Repository Identity
Inferred Topic != Canonical Research Domain
Keyword Match != Project Purpose
Scholarly Graph Representation != Repository Self-Definition
```

### Historical and correction boundary

New findings must not silently rewrite point-in-time research history. Later evidence, later source availability, later execution success, or later metadata repair may change current interpretation only through an explicit correction, reconciliation, or new timepoint record.

```text
CURRENT_STATE != TASK_TIME_STATE
LATER_SUCCESS != EARLIER_SUCCESS
PUBLICATION_IDENTITY != CURRENT_MAIN
RESEARCH_PRODUCTION != MAINTENANCE != PERIODIC_AUDIT
```


## Repository positioning boundary / 仓库定位边界

Canonical repository positioning:
> Agent-systems evidence and research infrastructure for evidence stability, provenance, research continuity, and bounded interpretation

Primary research domains:
agent systems; research infrastructure; provenance; reproducibility; knowledge lifecycle

Explicit non-goals / disallowed interpretations:
generic GitHub tutorial; business-process product; capability benchmark; autonomous-agent product

This repository defines its own research identity through current repository contracts, implementation, methodology, and maintained metadata

```text
External Classification != Repository Identity
Inferred Topic != Canonical Research Domain
Keyword Match != Project Purpose
Indexing Ontology != Repository Architecture
Scholarly Graph Representation != Repository Self-Definition
```

External systems such as Zenodo, DataCite, OpenAlex, OpenAIRE, search engines, citation indexes, or automated classifiers are downstream representations
They may be recorded as observations but never silently redefine this repository

### External classification check

- Channel / platform:
- Observed classification:
- Observation time:
- Compared against canonical positioning:
- Check status: RUN / NOT_RUN
- Alignment (only when RUN): ALIGNED / PARTIALLY_ALIGNED / MISCLASSIFIED / CLASSIFIER_NOISE
- Required repository change: NONE unless the repository's own canonical positioning is actually wrong
- Downstream correction candidate:

A downstream misclassification is evidence about the classifier or metadata projection, not evidence that the repository should change research identity

## Research identity / 研究身份

- Research record ID:
- Record type: Daily / Weekly-derived / Monthly-derived / Special / Experiment / Other
- Logical date or period:
- Actual execution date:
- Execution window:
- Record provenance:
- Base revision:
- Observed branch/ref snapshot:
- Research object identity:
- Evidence/source identity:
- Runtime/environment identity:
- Current-state cutoff:
- Prior related record:

Use `UNKNOWN`, `NOT_APPLICABLE`, `NOT_EXECUTED`, or `NOT_OBSERVED` instead of inference from neighboring fields

## Research question / 研究问题

State one question that can be contradicted by evidence

## Falsifiable hypothesis or judgment under test / 可证伪假设

- Proposed explanation:
- Support condition:
- Falsifier:

## Evidence or source basis / 证据基础

For each material source or input record identity, authority, time, supported proposition, limitation, and independence where relevant

Repository publication, DOI presence, index inclusion, or classifier labels do not create scientific validity by themselves

## Identity boundary / 身份边界

List identities that must not collapse in this study, such as object, source, dataset, configuration, run, Git ref, store, target, evaluator, timestamp, or version

## Controls / 控制条件

- Held constant:
- Changed:
- Baseline:
- Known confounders:

## Trial or bounded evidence procedure / 实验或有界证据过程

Describe exactly what was executed or inspected

If no execution occurred, say so explicitly

## Raw observations / 原始观测

Record direct observations only

```text
raw observation != interpretation
source existence != source truth
checker present != checker executed
checker pass != scientific truth
```

## Counterexample / 反例检查

Attempt at least one condition that would break the preferred interpretation
If not executable, record why

## Interpretation / 解释

Separate verified facts, evidence-based inference, and unknowns

## Provisional conclusion / 暂时结论

Allowed states include
- OBSERVATION
- CANDIDATE
- FINDING where repository-specific thresholds are satisfied
- NO_CONCLUSION
- UNKNOWN
- PARTIAL
- DEGRADED
- REFUTED
- INVALIDATED

Do not manufacture a positive conclusion for cadence completeness

## Research increment / 研究增量

Record only what this study actually added
- new evidence
- new counterexample
- narrower boundary
- reusable case
- corrected interpretation
- invalidated claim
- new uncertainty
- NONE

Research activity itself does not imply implementation, validation, reproduction, adoption, or impact

## Retest condition / 复验条件

State what must change, what must remain fixed, and what stronger evidence would alter the conclusion

## Repository-specific research surfaces
- evidence identity and support calculus
- temporal and current-state correctness
- execution, harness, and evaluator provenance
- capability, deployment, and semantic-outcome separation
- delegated evidence chains and world-state drift

Use `parallax/METHOD.md` and `parallax/templates/**` as the detailed operational contract

## Permanent separation rules

```text
research record != capability claim
repository self-definition != external ontology assignment
current truth != historical truth
publication != validation
usage != adoption
citation != reproduction
metadata consistency != scientific correctness
```

This template complements repository-native METHOD, METHODOLOGY, SOP, evidence contracts, and executable checks
When a repository-specific contract is stricter, the stricter repository-specific rule wins
