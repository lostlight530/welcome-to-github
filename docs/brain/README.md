# NEXUS CORTEX 认知合成协议

> **"The evidence and knowledge layer of the lostlight portal."**

此目录维护一个有状态、可重建的知识图谱. 原始输入、规范活动账本、历史归档和临时 SQLite 索引承担不同职责，不把任何单一报告直接视为事实.

## 系统架构

### 记忆层

- JSONL 是可审计的事实账本.
- SQLite 是可删除并重建的查询索引.
- 历史归档保持来源原貌，活动图谱只保留当前规范记录.

### Cortex 引擎

- 提供知识检索、关系映射和结构指标.
- 只从受约束的活动账本重建状态.

### Scholar 结构扫描

- 使用 AST 映射当前代码结构.
- 生成内容必须经过活动图谱规范化与写入边界检查.

### Reason 推演

- 计算知识密度、孤立节点和可验证的结构信号.
- 输出是待审核的研究结果，不是来源真实性证明.

### Nexus 生命周期

- 统一编排收割、投影、规范化、重建、推演与报告.
- 拒绝未声明的写入路径.
- 不提供公共网络服务或自动安全裁决.

## 使用指南

所有命令通过 `nexus.py` 执行.

### 更新与推演

```bash
# Map the current codebase through AST
python docs/brain/nexus.py ingest

# Calculate structural signals
python docs/brain/nexus.py ponder

# Run the local evolution cycle
python docs/brain/nexus.py evolve

# Synchronize approved profile sources
python docs/brain/nexus.py harvest
```

### 观察与读取

```bash
# Inspect current graph health
python docs/brain/nexus.py status

# Search indexed concepts
python docs/brain/nexus.py search "android"
```

### 清理与恢复

```bash
# Clear declared temporary cache targets
python docs/brain/nexus.py clean

# Rebuild SQLite from the canonical JSONL ledger
python docs/brain/nexus.py rebuild
```

## 图谱规则

See [SCHEMA.md](./SCHEMA.md) for the active schema.

- 历史证据不做破坏性覆写.
- 活动关系必须指向活动实体.
- 归档、活动账本和临时索引不得混用.
- 自动生成结果必须保留可追溯来源和明确边界.

## 自动化

`.github/workflows/nexus-life-cycle.yml` 在计划任务或相关代码变化时运行统一生命周期.

它会验证当前 Python 文件和测试、同步批准来源、规范活动账本、重建临时索引、运行结构分析并检查最终写入边界.

只有 `main` 分支允许自动提交声明范围内的生成产物. 分支和 PR 运行只验证，不写回仓库.

## 安全边界

- 外部文档属于不可信输入，即使来源在允许列表中也不自动获得真实性.
- 内容哈希只证明字节身份，不证明作者身份、授权或可信度.
- 自动化验证不能替代人类 Review.
- 漏洞必须按照仓库根目录 [SECURITY.md](../../SECURITY.md) 私密报告.
