# 数字考古：Phase IV 绝对确定性 | Digital Archaeology: Phase IV Absolute Determinism

## 概览 / Overview

在 2026 年 3 月底的系统演化中，NEXUS CORTEX 彻底摒弃了内部对任何大模型推理的依赖。系统进入 **Phase IV**，正式确立了 **Zero-Dependency Brutalism (零依赖极简主义)** 和 **4D Temporal Graph (四维时序图谱)**。

In late March 2026 during the system's evolution, NEXUS CORTEX completely abandoned any internal reliance on LLM inference. The system entered **Phase IV**, officially establishing **Zero-Dependency Brutalism** and the **4D Temporal Graph**.

## 核心演进 / Core Evolutions

为了应对不断膨胀的知识碎片和可能的“幻觉污染”，系统进行了物理层面的重组。

### 1. 4D Temporal Graph (时序图谱取代软删除)
*   **机制**：`cortex.py` 放弃了旧版的纯追加（Append-Only）机制，引入了基于 SQLite 复合主键 `(id, valid_at)` 的时序数据库。历史版本不再被暴力覆盖，而是打上 `invalid_at` 锚点，实现了真正意义上的无损记忆追踪。

### 2. 双重防抖感知雷达 (Double-Clutch Anti-Shake Radar)
*   **机制**：`harvester.py` 剥离了所有对于 `aiohttp` 等第三方异步库的依赖，转而使用 Python 原生线程池并发。在抓取 GitHub Release 时，引入了先脱水（正则去除日期/时间戳等噪音），再 Hash 比对，最后 `difflib` 计算差异的三重防抖机制，彻底过滤了无效版本更新。

### 3. Stack-based 降维配置解析器
*   **机制**：`scholar.py` 内部实现了不需要任何第三方依赖的基于栈 (Stack-based) 的 YAML/JSON 解析器，递归降维嵌套字典，确保各种基础配置文件能被精准提取并以属性实体 (`config_property`) 融合进图谱。

## 结语 / Conclusion

“文本即法律 (Text is Law)”。Phase IV 标志着系统彻底闭环，成为一个独立运行、免疫幻觉的机械法庭。只有在这个物理规律确定的底座上，才能承载 Phase V 的独裁统治。

"Text is Law." Phase IV marks the complete closed-loop of the system, becoming an independently running, hallucination-immune mechanical court. Only on this physically deterministic foundation can the dictatorial rule of Phase V be supported.
