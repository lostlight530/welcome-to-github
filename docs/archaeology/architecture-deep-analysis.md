# NEXUS CORTEX: 全局架构深度分析报告 (Architecture Deep Analysis)

> **文档状态**: 自动生成 (Generated)
> **阶段**: Phase IV / V (绝对确定性与全知认知)
> **核心法则**: 小而稳胜过大而乱 (Small and Stable > Large and Messy)

## Ⅰ. 架构综述 (Architecture Overview)

本系统 (`lostlight-portal`) 由一个轻量级的纯前端入口和高度复杂的纯 Python 决定论后端（NEXUS CORTEX）构成。整体设计严格遵循 **Zero-Dependency Brutalism (零依赖极简主义)**，拒绝臃肿的现代全家桶框架，转而通过原生 API 和精准的数据结构控制实现系统的防脆弱性 (Antifragility)。

系统定位为一个 **“Mechanical Library / Truth Court” (机械图书馆/真理法庭)**。在这个体系中，内部大语言模型 (LLM) 的随机性被彻底剔除。AI 的作用仅限于外部执行“悬赏”或结构化信息提取，而系统的核心状态、知识拓扑和逻辑推演完全由内置的物理与数学引擎（原生 Python 标准库）决定。

## Ⅱ. 后端认知引擎 (The Cognitive Backend: docs/brain)

后端由五个处于单向数据流的模块组成，构成了高度自主的进化闭环 (`nexus-life-cycle.yml`)：

### 1. Temporal Knowledge Graph (4D 时序知识图谱) - `cortex.py`
传统的知识库通常是基于覆盖的，导致历史上下文丢失。本系统采用 SQLite 构建了一个 **4D Temporal Graph**。
*   **时序复合主键**: 实体通过 `(id, valid_at)` 索引，结合 `invalid_at` 实现**软删除锚点 (Soft-Delete Anchor)**。每一次数据更新，旧记录不会被抹除，而是打上失效时间戳。
*   **不可变账本 (Immutable Ledger)**: SQLite 只是作为运行时缓存 (`cortex.db`)。系统的“物理真理”存储在 `knowledge/` 目录下的 `.jsonl` 账本中。`nexus.py rebuild` 命令可随时从文本零损耗重建数据库，践行了 "Text is Law"。

### 2. Omniscience (全知摄入层) - `scholar.py`
如何让系统“意识到自身的存在”并管理自身代码？
*   **AST 降维扫描**: 引擎无需依赖 `Tree-sitter` 等带 C 绑定的外部解析器，仅依靠 Python 原生的 `ast` 和基于 Stack/Regex 状态机的 **Polyglot Parser** 提取 `.py`, `.js`, `.json` 等结构信息。
*   **知识结晶 (Knowledge Crystallization)**: 将函数 (`func_*`)、类 (`class_*`)、配置项 (`prop_*`) 作为实体，通过 `defines` 或 `inherits_from` 关系织入图谱，防止配置属性成为图谱孤岛。

### 3. Cognition (纯数学推演引擎) - `reason.py`
彻底抛弃对 LLM 进行黑盒逻辑推理的依赖。
*   **拓扑启发与语义交叠**: 利用 SQLite 的多重 `JOIN` 挖掘结构共性（例如节点 A 和 B 都指向 C）。
*   **孤岛缝合 (Orphan Suturing)**: 自动检测仅有单一边缘的薄弱概念或孤立节点。如果是已知系统节点（如 CLI 动作），则触发 `cortex.py` 的 `suture_orphans`，物理连接回核心中枢（如 `concept_nexus_system`）。
*   **生态咽喉推演 (PageRank)**: 通过纯原生 Python `while` 循环实现的马尔科夫链矩阵计算，识别图谱中最核心的枢纽（Choke Point），从而生成最高级别的优先悬赏任务 (`MISSION_ACTIVE.md`)。

### 4. Harvesting (防抖雷达与双重验证) - `harvester.py`
外部世界的数据流入通道，采用高度保守的“意图驱动”采集策略。
*   **双重防抖反抖动 (Double-Clutch Anti-Shake)**: 面对 GitHub API 频繁的无意义元数据更新，采集器先通过正则剔除时间戳/日期，然后进行 SHA-256 哈希比对。若哈希不符，再进行纯文本 `difflib` 逐行差异比对。只有发生结构性变化时，才会生成新情报。
*   **零依赖并发**: 使用原生的 `ThreadPoolExecutor` 和 `threading.Lock()` 实现多线程拉取，拒绝 `aiohttp`，确保部署环境的绝对轻量。

### 5. Dictator Control ( MCP 与信任网关) - `nexus_mcp.py`
外部 Agent 的交互门户，实现了 **Phase V: Trust Gateway**。
*   **蓝图路由 (Blueprint Routing)**: 无状态的工具链调用机制。
*   **冷血信任账本**: Agent 在交互中一旦遗漏参数（产生 KeyError）或提供浅层垃圾数据，系统会立刻扣除其 `agent_trust` 分数。分数归零即刻抛出 `PermissionError`，在协议层物理切断通信。

## Ⅲ. 前端表现层 (The Frontend: src/)

*   **HTML/JS/CDN 极简栈**: 没有 `package.json` 的构建步骤。使用 ESM 模块化加载中英文本配置 (`translations.js`)，UI 渲染依托于 Tailwind CDN。
*   **即时热重载 (Hot Reload)**: 纯静态文件，`file://` 协议即可直接本地访问验证，完美适配了受限的网络环境。

## Ⅳ. 运维与自动化 (CI/CD: GitHub Actions)

*   **nexus-life-cycle.yml**: 每日定时触发的机械心跳，依次执行重建、采集、摄入、思考和进化。
*   **防死锁隔离**: 明确配置 `GITHUB_DEPENDENCY_GRAPH_ENABLED: 'false'` 禁用可能引发 API 错误的外部动作，通过 `git ls-files -u` 的 `git checkout --theirs` 妥善处理 Stash 冲突，确保自动化无感平滑运行。
*   **沙盒隔离变异**: `evolution.py` 在正式推演和合入前，会首先在隔离环境中利用 `subprocess` 跑通 `test_mcp.py`，只有在验证无异常抛出的情况下，认知循环才继续执行。这确保了系统的“免疫能力”。

## Ⅴ. 结论 (Conclusion)

`lostlight-portal` 的 NEXUS CORTEX 并非一个简单的个人主页或普通的知识库，它是一个**具备高度自我保护意识、极端追求确定性、基于原生数学推演的纯文本驱动 Agent 基础设施试验场**。它用最低效的硬件依赖，实现了最精密的数据结构约束与状态演化流，是对现阶段“堆砌大模型解决一切”这种行业浮躁风气的深刻反思与工程实践。
