# Open Research / 开放科研

Status: durable open-research production guide
Scope: repository-level research positioning, research-production method, scholarly-metadata boundaries, and semantic-drift governance

## Language policy / 语言政策

English is the canonical and default language for this open-research contract. Chinese text is provided as an accessibility and interpretation aid. If a wording conflict appears, the English normative text governs; repository evidence and current owning contracts still outrank either translation.

英文是本开放科研契约的默认与规范语言；中文用于辅助理解与可访问性。若中英文表述发生冲突，以英文规范文本为准，但仓库事实与当前 owning contract 的权威仍高于任何翻译。


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

## Positioning and research execution / 定位与科研执行

Repository purpose, the implemented or studied research object, subject-specific methodology/contracts, and version-matched canonical metadata define repository positioning. Read README, this guide, CITATION.cff, CodeMeta, current implementation, and the applicable research contracts together for the question and version being examined. A fixed cross-repository file ranking is not a substitute for their native authority rules.

```text
Repository Positioning
= repository purpose + implementation or research object
+ applicable research methodology/contracts + version-matched canonical metadata

Execution provider, scheduling, maintenance cadence, and delivery mechanism
do not independently define repository type, primary domains, subjects, or keywords
```

GPT automation, Jules periodic SOPs, maintenance cadence, Sentinel scheduling, and PR/delivery mechanics do not become research domains merely because they operate a repository. Classify by the actual subject and method, not by provider names, file locations, workflow labels, or task frequency.

A repository-owned workflow can itself implement a research method or study a research object. Its substantive implementation, method, and evidence contract remain part of repository-native research where applicable. Its trigger, schedule, and delivery mechanics are operational facts. Execution evidence supports only the property actually observed; workflow presence or a successful run does not independently prove scientific validity.

仓库定位按研究目的、实现或研究对象、适用方法契约及对应版本的元数据判断，不按执行者、平台名称或任务频率投票；自有工作流中的科研实现、方法与证据契约仍属于科研本体，触发、调度和投递机制分别记录

For welcome-to-github and Zero-Entropy Lab, repository-owned GitHub Actions are also research workflows. Preserve their research role; do not subtract them as an automation layer. Assess the implemented knowledge/state lifecycle, method, and evidence contract separately from scheduling or delivery. In this repository, [the native lifecycle workflow](.github/workflows/nexus-life-cycle.yml) is a versioned implementation surface; reading its source is not evidence that a run executed.

本仓自有 GitHub Actions 也承载科研，不能整体排除或当作需要扣掉的自动化影响；科研内容与调度、投递机制按职责区分

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


## 中文摘要

本文件定义的是仓库长期开放科研方法，而不是新的总宪法。共同骨架包括：研究问题、可证伪假设、证据与来源身份、固定对象/版本/环境、实际执行程序、原始观测、反例检查、有界结论、研究增量与复验条件。

仓库仍由自身 implementation、methodology、evidence、history 等原生权威文件定义；OpenAlex、OpenAIRE、Zenodo、DataCite 等外部系统只能派生或传播仓库语义，不能反向定义仓库身份。

未来 scholarly metadata 应保持 canonical type、one-line positioning、primary domains、non-goals、少量高质量 subjects 与 5–7 个定义性 keywords。若外部分类偏移，先判断是否存在仓库自身歧义；没有歧义则记录为 downstream classifier noise，不为了分类器重写仓库本体。
