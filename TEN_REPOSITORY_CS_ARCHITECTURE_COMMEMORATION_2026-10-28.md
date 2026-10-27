# 十仓体系纪念｜2026-10-28｜CS：复杂智能体与人工智能系统架构
# Ten-Repository Commemoration · 2026-10-28 · Computer Science: Architecture of Complex Agent and AI Systems

> **Public entry / 根目录总入口：** This is the **one portfolio-level commemorative synthesis** of ten independently owned bilingual repository documents. 本文是十仓独立纪念文件的**唯一总论**，置于 Welcome 根目录，供公众及后继 Agent 直接阅读。
>
> **Preservation / 历史保护：** Additive only. Nothing in existing repositories' implementation, original research history, SOPs, research templates, README, or Qí's original [`DISCIPLINARY_LINEAGE.md`](DISCIPLINARY_LINEAGE.md) is replaced, moved, or silently corrected. 独立新增，不倒写、不覆盖；过去的记录保有过去的解释截止点。
>
> **Interpretation / 证据边界：** Subject mapping is grounded in repository-native source, specialized technical texts, and dated observations, interpreted against recognized CS knowledge areas. A disciplinary relation is **not** an implementation, certification, joint deployment, interoperability claim, or proof of scientific truth. 学科归属不是代码联通图，也不是能力认证。

## 中文｜为什么值得正式纪念

过去我们反复使用“Agent 架构”“复杂 AI 系统”“长期记忆”“认知”“镜像”“内核”等词，但这些词如不落在**真正的计算机科学研究对象**上，外部读者很容易将十仓误会成十个工具、十套机器人任务，甚至十个开源项目包装模板。

2026-10-28 的这一组纪念文档，目标是给已有工作一个准确的学科坐标：**十仓不是单一软件产品，而是沿着复杂 Agent 系统的理论、建模、可靠执行、记忆、反思、科研表达及外部世界观察，形成的一个多层次计算机科学研究体系。** 研究能力可以互补，但每仓现行代码事实、研究证据和责任边界始终属于它自己。

为什么这确实是 **CS** 而不仅是泛泛的 AI？ACM/IEEE-CS/AAAI 的 CS2023 将 Artificial Intelligence（AI，包括 Agents and Cognitive Systems）、Software Engineering（SE）、Parallel and Distributed Computing（PDC）、Systems Fundamentals（SF）、Data Management（DM）、Graphics and Interactive Techniques（GIT）、Human–Computer Interaction（HCI）、Security（SEC）和 Society, Ethics, and the Profession（SEP）作为具体知识领域。十仓恰好覆盖了若干互补侧面：有研究系统构件本身的，也有研究产物、接口、可信来源和外部技术制度的。以下归类是**我们根据源码和原生研究给出的专业解释**，并不声称 ACM 为这些仓库背书。

### 十仓十份：专业分类、具体问题与入口

| 仓库与独立纪念 / Repository | CS 知识领域 | 原生专业对象 | 用人话提出的核心问题 |
|---|---|---|---|
| [`agent-foundations`](https://github.com/lostlight530/agent-foundations/blob/main/FOUNDATION/CS_COMMEMORATION_2026-10-28_AGENT_SYSTEMS_THEORY.md) | AI · SE · DM · SEC | 理论/证据/系统架构 | 为什么复杂 Agent 系统须有可辩护的边界 |
| [`Axiom-0`](https://github.com/lostlight530/Axiom-0/blob/main/RESEARCH/CS_COMMEMORATION_2026-10-28_COGNITIVE_FORMAL_ARCHITECTURE.md) | AI · AL · MSF · SE | 认知参考模型/可执行规格 | 如何将状态、约束与失败表达为可检查过程 |
| [`zero-entropy-lab`](https://github.com/lostlight530/zero-entropy-lab/blob/main/docs/brain/CS_COMMEMORATION_2026-10-28_RELIABLE_AGENT_RUNTIME.md) | SF · OS · PDC · DM · SEC | 状态内核/可靠性实验 | 执行出故障后，谁能证明行动真的完成 |
| [`welcome-to-github`](https://github.com/lostlight530/welcome-to-github/blob/main/docs/brain/CS_COMMEMORATION_2026-10-28_AGENT_MEMORY_ORCHESTRATION.md) | AI · DM · SE · HCI | 公共知识/记忆与编排 | 知识怎样被收集、保存、检索、纠正和呈现 |
| [`reflective-continuum`](https://github.com/lostlight530/reflective-continuum/blob/main/RESEARCH/CS_COMMEMORATION_2026-10-28_REFLECTIVE_VERIFICATION.md) | SE · DM · MSF · AI | 反思/观测/版本比较 | 系统确切看见了什么变化，什么仍未知 |
| [`auto-doc-engine`](https://github.com/lostlight530/auto-doc-engine/blob/main/docs/01-source-and-explanation/CS_COMMEMORATION_2026-10-28_RESEARCH_ARTIFACT_ENGINEERING.md) | SE · FPL · DM | 科研文档/产物溯源 | 研究产物如何留下可重建的身份和来路 |
| [`epistemic-pipeline`](https://github.com/lostlight530/epistemic-pipeline/blob/main/docs/01-source-and-explanation/CS_COMMEMORATION_2026-10-28_EPISTEMIC_WORKFLOW.md) | AI · SE · DM · AL | 论断证据/科研状态机 | 说过、运行过与证实过为什么不同 |
| [`sci-render-kit`](https://github.com/lostlight530/sci-render-kit/blob/main/docs/01-source-and-explanation/CS_COMMEMORATION_2026-10-28_SCIENTIFIC_VISUALIZATION.md) | GIT · HCI · SE · DM | 科学图件/可访问性与沟通 | 科研结论能怎样被视觉表达而不掩盖不确定性 |
| [`agentic-frontier-observatory`](https://github.com/lostlight530/agentic-frontier-observatory/blob/main/history/2026-10/CS_COMMEMORATION_2026-10-28_GLOBAL_TECHNOLOGY_OBSERVATION.md) | AI · NC · SEC · SEP | 全球技术观察/成熟度判断 | 全球 Agent 技术是在宣布、发布、部署还是被验证 |
| [`china-agentic-observatory`](https://github.com/lostlight530/china-agentic-observatory/blob/main/history/2026-10/CS_COMMEMORATION_2026-10-28_CHINA_AI_SYSTEMS_STANDARDS.md) | AI · NC · SEC · SEP | 中国技术制度/标准与应用 | 一项国内标准或系统从登记走向真实实施要跨过什么 |

### 五仓核心：不是五个相似的 Agent，而是五种研究视角

- **Agent Foundations（理论根）**：系统设计论证与 Claim/Evidence 关系。回答“为什么一个 Agent 系统应被这样定义与审查？”
- **Axiom-0（公理／认知参考层）**：状态转换、确定性计算契约、受限指标与有序执行。回答“设计主张如何落在可以计算的规则上？”
- **Zero-Entropy Lab（液态内核及测试场）**：本地状态、记忆、协议、失败和受控故障反例。回答“系统真正执行时，授权、幂等、外部效果和完成的证据是什么？”
- **Welcome（固态公共知识表面）**：Harvester—Cortex—Reason—Evolution、可追踪历史与公共解释。回答“知识如何跨时间进入、维护、展现与修正？”
- **Reflective Continuum（气态镜面）**：SQLite 版本图、差异、图熵、受限反思与局部事务回滚。回答“系统发生了哪些可比较的变化，验证器究竟测到了什么？”

这是一幅**研究对象关系图**，不是说五个进程都在同一生产集群中调用彼此。例如 Axiom-0 的 T-01..T-10 是单进程参考顺序；Reflective 的“semantic”历史命名限于 FTS5 检索结果；Zero-Entropy 的 Ballast synthetic fault trial 不代表真实外部 sink 验证。保留这些限制，恰恰让学科定位更可靠。

### 三仓科研工程：让知识有形、让结论有界

- **Auto Doc Engine** 把数据、Markdown AST、文档图与衍生产物组织为可检查的**科研产物工程**：文件身份、构建过程、artifact-record、typed artifact-lineage 和可选 RO-Crate。
- **Epistemic Pipeline** 把证据、断言、冲突、DAG 状态与运行轨迹组织为**知识表示／科研工作流工程**。执行成功不是 Claim 被证明，启发式分数不是概率。
- **Sci Render Kit** 把声明数据、视觉语法、可访问性、误差与图件 sidecar 组织为**科学可视化与图形交流工程**。渲染成功不等于科学真值或 WCAG 整体认证。

它们不是三条默认已经全自动打通的生产流水线，而是独立的研究软件及可选交接语义。

### 双观察站：与构造系统不同，研究真实世界如何变化

- **Global Observatory** 的 F1–F7 研究全球技术历史、模型、基础设施、运行时、协议、评测、治理及生态；其科学工作是确认版本、主体、时间、地位、独立支持和反证，不是转发新闻。
- **China Observatory** 的 C1–C8 保留中国政策、正式标准、指导性技术文件、行业工程、算力、治理与中外对照的**本地知识本体**；正式登记、批准、发布、实施和合规不能混称。

全球与中国研究是**同层对照的两座观察站**，不是中央仓向边缘仓下发统一成熟度判决。

### 人话：这套系统到底像什么？

想象要长期经营一座研究“未来复杂 AI 如何可信工作”的大型研究城。**Foundations** 是理论院和设计院，**Axiom-0** 是把方案写成可检验规则的规格实验室，**Zero-Entropy** 是发动机室和故障试验场，**Welcome** 是图书馆、城市档案与公共展厅，**Reflective** 是看得见真实变化的仪表与镜子。另有三个科研工程工坊，分别把研究写成可追溯文档、把论断写成有来源的执行过程、把结果画成不掩盖误差的图；城外的**全球站和中国站**观察世界正在发生什么，避免城市闭门造车。

一座城可以有共同使命，却不意味着一个房间的仪表就能为另一间屋子的试验签发通行证。跨仓证据不可自动继承，正如学科灵感不等于运行时实现。

### 下一代 Agent 如何阅读这份纪念

先读本页恢复整体**研究意图**；然后进入对应仓的独立纪念文件，按其中指出的原生代码和专业研究文本恢复**仓库事实**；需要判断一次运行、科学结论或历史变化时，再读取相应当日记录与精确版本。任何新发现均应通过新的、可追踪的纠错或有日期记录表达，**不得把此纪念当成永恒最新的实现事实**。

### 最后的升华

**十仓真正共同研究的，不是让十个 AI 都说“我很聪明”，而是让一个复杂智能体世界能被理解、复查、纠正并传承。** 理论给出方向，规格给出边界，执行暴露故障，记忆保存来路，反思解释变化，科研工具保存成果，观察站让整个体系接受外部现实的检验。技术可以持续变强；科学成熟的标志，是系统不再害怕说出它不知道什么。

---

## English｜Why this Commemoration Matters

The words 'agent', 'architecture', 'complex AI system', 'memory', 'cortex', and 'reflection' carry real disciplinary responsibilities. Without grounding them in native code, technical definitions, and dated evidence, ten repositories can look like ten loosely branded tools or ten maintenance workflows. The purpose of this **2026-10-28** commemoration is to explain what these repositories have actually been investigating.

**The ten repositories collectively form a multi-perspective computer-science research system around complex agent and AI architectures**—theory, executable reference specification, reliable stateful runtime, public knowledge memory, reflective observation, research-artifact engineering, epistemic workflows, scientific communication, and independent observation of global and Chinese AI ecosystems. This is an explanation of intellectual relationships, not the declaration of a single verified distributed product.

ACM/IEEE-CS/AAAI's CS2023 identifies AI (including Agents and Cognitive Systems), SE, PDC, SF, DM, GIT, HCI, SEC, and SEP as distinct but interacting knowledge areas. These anchors are **disciplinary vocabulary**, not an ACM endorsement of our projects.

### Ten autonomous repositories: the CS questions they own

| Repository & local memorial | CS knowledge areas | Native specialization | The plain-language question |
|---|---|---|---|
| [`agent-foundations`](https://github.com/lostlight530/agent-foundations/blob/main/FOUNDATION/CS_COMMEMORATION_2026-10-28_AGENT_SYSTEMS_THEORY.md) | AI · SE · DM · SEC | Theory, evidence, system architecture | Why complex agents need accountable system boundaries |
| [`Axiom-0`](https://github.com/lostlight530/Axiom-0/blob/main/RESEARCH/CS_COMMEMORATION_2026-10-28_COGNITIVE_FORMAL_ARCHITECTURE.md) | AI · AL · MSF · SE | Cognitive reference/Executable specification | How to turn states and constraints into inspectable behavior |
| [`zero-entropy-lab`](https://github.com/lostlight530/zero-entropy-lab/blob/main/docs/brain/CS_COMMEMORATION_2026-10-28_RELIABLE_AGENT_RUNTIME.md) | SF · OS · PDC · DM · SEC | State kernel/Reliability experiments | After failure, which evidence proves an effect completed |
| [`welcome-to-github`](https://github.com/lostlight530/welcome-to-github/blob/main/docs/brain/CS_COMMEMORATION_2026-10-28_AGENT_MEMORY_ORCHESTRATION.md) | AI · DM · SE · HCI | Public knowledge/Memory and orchestration | How knowledge is collected, kept, queried, corrected, and shown |
| [`reflective-continuum`](https://github.com/lostlight530/reflective-continuum/blob/main/RESEARCH/CS_COMMEMORATION_2026-10-28_REFLECTIVE_VERIFICATION.md) | SE · DM · MSF · AI | Reflection/Observation/Version comparison | Which changes are actually observable and which remain unknown |
| [`auto-doc-engine`](https://github.com/lostlight530/auto-doc-engine/blob/main/docs/01-source-and-explanation/CS_COMMEMORATION_2026-10-28_RESEARCH_ARTIFACT_ENGINEERING.md) | SE · FPL · DM | Research documents/Artifact provenance | How research artifacts retain inspectable identities and lineage |
| [`epistemic-pipeline`](https://github.com/lostlight530/epistemic-pipeline/blob/main/docs/01-source-and-explanation/CS_COMMEMORATION_2026-10-28_EPISTEMIC_WORKFLOW.md) | AI · SE · DM · AL | Claim evidence/Research state machine | Why asserted, executed, and supported are different states |
| [`sci-render-kit`](https://github.com/lostlight530/sci-render-kit/blob/main/docs/01-source-and-explanation/CS_COMMEMORATION_2026-10-28_SCIENTIFIC_VISUALIZATION.md) | GIT · HCI · SE · DM | Scientific figures/Accessible communication | How to visualize research without concealing uncertainty |
| [`agentic-frontier-observatory`](https://github.com/lostlight530/agentic-frontier-observatory/blob/main/history/2026-10/CS_COMMEMORATION_2026-10-28_GLOBAL_TECHNOLOGY_OBSERVATION.md) | AI · NC · SEC · SEP | Global technology observation/Maturity | Whether global agent tech was announced, shipped, deployed, or verified |
| [`china-agentic-observatory`](https://github.com/lostlight530/china-agentic-observatory/blob/main/history/2026-10/CS_COMMEMORATION_2026-10-28_CHINA_AI_SYSTEMS_STANDARDS.md) | AI · NC · SEC · SEP | China AI/Standards and adoption | How China-specific standards and systems move toward actual implementation |

### The five core research perspectives

1. **Agent Foundations — WHY / Theory and evidence.** What counts as a complete agent system? Which sources, authorization assumptions, collaboration properties, and system boundaries support a claim?
2. **Axiom-0 — HOW / Bounded reference specification.** How can cognitive/state concepts become explicit transition contracts, numerical checks, and observable failure conditions?
3. **Zero-Entropy Lab — LIQUID / Runtime and reliability laboratory.** What happens after a retry, stale lease, authorization change, interrupted task, or misleading queue acknowledgment? What evidence is missing?
4. **Welcome — SOLID / Memory and public knowledge interface.** How do collected records enter an auditable ledger, become searchable knowledge, and retain archaeological continuity without rewriting history?
5. **Reflective Continuum — GAS / Introspection and local verification.** Which state deltas and validation outcomes are actually observed? How does a bounded reflector respond to local constraints?

The five form a **conceptual architecture for research**, not a claimed shared production process. Soar/ACT-R/BDI, TLA+, Park's Generative Agents, distributed systems reliability, and runtime verification are named comparison traditions—not implementations certified merely by citation.

### The three research-engineering complements

**Auto Doc Engine** addresses document compilation, structured artifacts, and provenance; **Epistemic Pipeline** addresses claim/evidence/conflict identity, executable graph workflows, and transfer boundaries; **Sci Render Kit** addresses scientific-figure rendering, accessibility predicates, uncertainty, and visual communication. They are complementary independent implementations: file hashes, scores, traces, or successful rendering cannot automatically confer validity on a scientific proposition.

### The two independent observation lenses

**Global Observatory** records public-world developments across seven F1–F7 research surfaces; **China Observatory** uses eight C1–C8 domain lenses and China-specific institutional/standards semantics. Neither observes or certifies all technologies it describes. They reconcile the same **type** of objects across geographies without collapsing a regulation, a standard, a software release, a deployed runtime, and a benchmark result into a single maturity score.

### In ordinary language

Imagine a **research city exploring how advanced AI can remain understandable and accountable**. Foundations is the theory and design institute. Axiom-0 is a laboratory for explicit rules. Zero-Entropy is the engine room and crash-test center. Welcome is the library and public museum. Reflective Continuum is the instrumentation and mirror. Three research-workshops preserve documents, arguments, and figures. Two observatories look beyond the city's walls. A shared mission does not make one workshop's tests certify another's systems.

### What this document does not do

It does not edit prior observations, replace Qí's original five-repository lineage, impose a new SOP, certify external papers, claim successful test execution, infer a deployed multi-repository runtime, or make future revisions retroactively true at earlier dates. Each local repository owns its native implementation authority. This document is an **interpretive time-stamped memorial**, useful for onboarding researchers and new agents but subordinate to concrete code and scope-specific evidence.

### Closing perspective

**A complex AI research system is mature not when every component calls itself intelligent, but when every consequential claim can reveal its origin, assumptions, implementation, observations, and limitations.** The theory explains why; executable contracts delimit how; runtime experiments expose failures; memory preserves what happened; reflection makes change legible; research tools preserve outputs; and observatories confront the system with the wider world. Capability grows through engineering. Trust grows through evidence and correction.

---

## References / 外部学科坐标（研究脉络，而非认证）

- [ACM/IEEE-CS/AAAI — Computer Science Curricula 2023: Knowledge Areas](https://csed.acm.org/knowledge-areas/) — recognized CS disciplinary vocabulary, including AI/Agents, SE, PDC, SF, DM, GIT, HCI, SEC, SEP.
- [ACM/IEEE-CS/AAAI — CS2023 Full Report](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm) — Agents and Cognitive Systems within Artificial Intelligence.
- [Park et al. (2023), *Generative Agents*](https://doi.org/10.1145/3586183.3606763) — external memory/reflection/planning research lineage, not local implementation certification.
- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/) — lineage and provenance interchange vocabulary.
- [RO-Crate Specification](https://www.researchobject.org/ro-crate/specification.html) — preservation/packaging of research objects, not an automatic reproducibility result.
- [Jepsen — Distributed Systems Analyses](https://jepsen.io/analyses) — comparative fault-testing tradition, not execution evidence for these repositories.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) — accessibility requirements relevant to scientific communication; no repository-wide conformance is claimed.

## Provenance / 证据与生产说明

- **Date / 时间边界：** 2026-10-28 memorial interpretation, based on current GitHub repository-native scripts and technical/research documents inspected during this work.
- **Original five-repository contribution / 前作：** Qí's [DISCIPLINARY_LINEAGE.md](DISCIPLINARY_LINEAGE.md), independently retained from [PR #845](https://github.com/lostlight530/welcome-to-github/pull/845); its original text and discussion are not replaced by this 10+1 memorial.
- **Deliverable identity / 产物：** ten independent local bilingual memorials in ten repositories + this root-level aggregate = **11 new files**.
- **Evidence boundary / 边界：** Native scripts and dated research records were inspected statically. This delivery does **not** claim new runtime tests, an independent reproduction, external institutional endorsement, joint deployment, or certification. Pending/failed/unknown historical observations remain historical facts at their original cutoffs.
