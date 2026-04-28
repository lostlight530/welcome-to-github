# 第四纪元：绝对决定论 (Phase IV: Absolute Determinism)

> **"Eradicate the hallucination. In pure math we trust."**
> **Epoch Marker**: 2026-04-24

## 1. 历史背景 (Historical Context)
随着对系统可控性的极致追求，我们发现即使是最少量的 LLM 推理也可能导致不可复现的结构漂移。系统需要走向一条绝对确定的物理学演进之路。

## 2. 时空图谱重构 (Temporal Knowledge Graph)
- **4D 时空架构**: 废除了破坏性的覆盖更新，在底层 SQLite 数据库中引入 `valid_at` 与 `invalid_at` 字段。所有知识更新都遵循 **附加写入法 (Append-Only, ADR-0001)**，旧知识被标记为无效而非删除。
- **关联搜索**: 彻底封杀大模型的时空错乱幻觉，所有的图谱查询变成确定性的时态 SQL 过滤。

## 3. 防抖雷达 (Double-Clutch Anti-Shake)
外部情报抓取（Harvester）实现了严密的算力熔断：
- 第一层 HTTP ETag 缓存阻挡。
- 第二层使用 SHA-256 以及去除时间噪音后的纯文本 Diff 对比。
只有物理内容发生实质改变时，才会向下游传递，彻底扼杀了 API 轮询带来的算力浪费与伪更新。
