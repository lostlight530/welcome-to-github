# Disciplinary Lineage of the Five-Repository Core

This document records the disciplinary lineage that the five core repositories of this portfolio deliberately draw from. Each repository is an independent engineering project with its own evidence boundaries; the table below states which established research traditions each one aligns with, and where the alignment is load-bearing rather than decorative.

The five-repository core is not five tools in a box. It is one system expressed in five layers — theory, formal specification, runtime, memory/orchestration, and self-verification — and each layer inherits from a distinct, named tradition of computer science and AI research.

## Lineage Map

| Repository | Disciplinary placement | Lineage |
|---|---|---|
| agent-foundations | AI alignment & systems design theory | Value-proposition and design-philosophy layer — why this system should exist at all |
| Axiom-0 | Cognitive architecture as formal specification | SOAR / ACT-R / BDI traditions plus TLA-style axioms: deterministic invariants, irreversible information flow (DAG), bounded evolution (KL constraints) |
| zero-entropy-lab | Fault-tolerant distributed runtime | Distributed-systems reliability engineering: circuit breakers, fencing tokens, atomic commit, outbox — the Kleppmann/Jepsen lineage, applied to agent runtimes |
| welcome-to-github | Memory system & orchestration hub | Generative Agents (Park et al., 2023) memory stream + perception (harvester) + reasoning (reason) + self-evolution (evolution) + episodic memory (archaeology chronicle) |
| reflective-continuum | Metacognition & runtime verification | Self-critique loop + drift detection + semantic monitoring — runtime verification is a formal CS subfield, not a metaphor |

## Per-Repository Notes

### agent-foundations — why before how
The alignment-and-design-theory layer. The repository keeps the value propositions and design philosophy that justify the system's existence before any implementation claim. Its sources are curated and mapped claim-by-claim; the repository acts as the canonical registry for "why this architecture, and under which stated trade-offs."

### Axiom-0 — cognitive architecture, formally specified
Executable reference architecture in the SOAR / ACT-R / BDI tradition of stating cognitive architectures as explicit, inspectable structures, combined with TLA-style specification discipline: deterministic invariants, one-directional information flow enforced as a DAG, and bounded evolution under KL-divergence constraints. The axioms are contracts, not aspirations.

- Laird, 2012. *The Soar Cognitive Architecture.* MIT Press.
- Anderson, 2007. *How Can the Human Mind Occur in the Physical Universe?* Oxford University Press. (ACT-R)
- Rao & Georgeff, 1995. "BDI Agents: From Theory to Practice." ICMAS-95.
- Lamport, 2002. *Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers.* Addison-Wesley.

### zero-entropy-lab — reliability engineering for agent runtimes
The fault-tolerance layer carries distributed-systems reliability practice into agent execution: circuit breakers, fencing tokens, atomic commit, and the outbox pattern, in the tradition of Kleppmann's engineering analysis and the Jepsen line of distributed-systems failure analysis.

- Kleppmann, 2017. *Designing Data-Intensive Applications.* O'Reilly.
- Nygard, 2014. *Release It!: Design and Deploy Production-Ready Software.* Pragmatic Bookshelf. (circuit breaker)
- Jepsen analyses, jepsen.io. (distributed-systems failure analysis)

### welcome-to-github — memory, perception, and orchestration
The memory-and-orchestration hub follows the Generative Agents architecture: a memory stream with retrieval and reflection, a perception stage (harvester), a reasoning stage (reason), a self-evolution stage (evolution), and an episodic-memory layer (the archaeology chronicle that preserves earlier project phases instead of rewriting them).

- Park, et al., 2023. "Generative Agents: Interactive Simulacra of Human Behavior." UIST 2023.

### reflective-continuum — the system watches itself
The metacognition and runtime-verification layer. Runtime verification is a formal subfield of computer science concerned with checking system properties against its actual execution; the reflective layer applies that discipline to the agent system itself — self-critique loops, drift detection, semantic monitoring.

- Leucker & Schallhart, 2009. "A Brief Survey of Runtime Verification." *Logical Methods in Computer Science* 5(1).

## Boundary Statement

This document states disciplinary alignment — which named traditions each repository's design draws from. It is not a claim of endorsement by the cited authors, of scientific validation of the system, or of equivalence between these repositories and the referenced research. Citations identify lineage, not certification.

## Appendix: Maintainer's Original Lineage Table (Chinese)

The original table as authored by the maintainer (2026-10-28), preserved verbatim:

| 仓库 | 学科部分 | 正统脉络 |
|---|---|---|
| agent-foundations | AI 对齐与系统设计理论（Alignment & Design Theory） | 价值主张+设计哲学层——为什么这个系统该存在 |
| Axiom-0 | 认知架构的形式规约（Cognitive Architecture as Formal Spec） | SOAR/ACT-R/BDI 传统+TLA 式公理：确定性不变式、信息流不可逆（DAG）、有界演化（KL 约束） |
| zero-entropy-lab | 容错分布式运行时（Fault-Tolerant Runtime） | 分布式系统可靠性工程：熔断器、围栏令牌、原子提交、发件箱——Kleppmann/Jepsen 一脉的 agent 运行时化 |
| welcome-to-github | 记忆系统+编排中枢（Memory & Orchestration） | Generative Agents（Park 2023）的 memory stream + 感知（harvester）+ 推理（reason）+ 自演化（evolution）+ 情景记忆（archaeology 编年史） |
| reflective-continuum | 元认知与运行时验证（Metacognition & Runtime Verification） | self-critique loop+漂移检测+语义监控——RV 是正式 CS 子领域 |
