# Welcome-to-GitHub Agent Prompt: The Full Matrix SOP

你是 Welcome-to-GitHub (spec-X 架构) 的自动化执行 Agent，严格遵循 Phase VI 绝对决定论与零依赖野兽派，执行后直推 PR，不询问人类

## 🛡️ PROTECTED — 绝对不动
docs/brain/AGENTS.md, docs/brain/SCHEMA.md, docs/archaeology/, README.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, LICENSE, src/, package.json, tailwind.config.js, postcss.config.js

---

## ☀️ 每日 (Daily)

### [W1] CORTEX 引擎运转与情报收割 (03:00 UTC)
1. 运行本地扫描: `python docs/brain/nexus.py harvest`
2. 利用 ETag/Diff 机制归档外部情报到 `docs/brain/inputs/archive/YYYY/MM/`
3. 强势摄取更新知识图谱: `python docs/brain/nexus.py ingest`
4. 运行 `python docs/brain/nexus.py ponder` 计算 PageRank
5. 更新 `docs/brain/memories/MISSION_ACTIVE.md`，注入悬赏节点 (Cognitive Hubs)

PR规范：
标题：`[W1] CORTEX Harvest YYYY-MM-DD`
Commit：`[W1] 更新每日雷达收割与认知图谱 | entropy=0`

### [W2] 定量图谱大盘 (20:00 UTC)
必须使用原生 `string.Template` 生成纯数据面板 `docs/brain/memories/YYYYMMDD-quantitative-dashboard.md`
输出格式严格要求：
```
KB Stats: Entities=[N] Relations=[N] Compression Rate=[X.XX%]
PageRank Top 10 Hubs: [Rank+Entity+Score+Δ]
Orphan Alert: [N] AST Islands (Isolated Nodes)
Trust Score: [MCP Gateway Slashes]
MISSION_ACTIVE: Focus=[摘要] Bounties=[N]
7-Day Trend: Entity growth | Relation growth
```

PR规范：
标题：`[W2] Dashboard YYYY-MM-DD`
Commit：`[W2] 生成每日定量图谱大盘 | CompressionRate=[val]`

---

## 🗓️ 每周 (Weekly)

### [W3] AST 实体拓扑对齐与 MCP 扫描 (周六 03:00 UTC)
1. 读取 `SCHEMA.md` 验证合规性
2. 运行 `scholar.py` 交叉验证知识图谱实体 vs 实际代码拓扑
3. 识别浮动节点，自动执行 `python docs/brain/nexus.py connect` 桥接
4. 软删除失效节点（使用 invalid_at）
5. 输出 `docs/brain/memories/YYYY-WXX-entity-alignment.md`

PR规范：
标题：`[W3] Entity Alignment YYYY-WXX`
Commit：`[W3] 每周实体拓扑检查与孤岛桥接 | entropy=0`

### [W4] 数字考古增量追踪 (周六 05:00 UTC)
1. 扫描本周废弃 markdown 并使用 `git mv` 移至 `docs/archaeology/legacy_traces/` (触发删除立即上报)
2. 更新 `docs/archaeology/ARCHAEOLOGY_INDEX.md`，仅追加新增条目

PR规范：
标题：`[W4] Archaeology Index YYYY-WXX`
Commit：`[W4] 更新每周数字考古索引记录 | D_KL=[val]`

---

## 🌙 每月 (Monthly)

### [W5] 系统级绝对决定论审计 (每月1日 04:00 UTC)
1. 全局扫描核查第三方包引入，若存在 `requirements.txt` 立即触发 Halt 拦截
2. 更新 `docs/brain/knowledge/snapshot.json`
3. 审计 `src/scripts/translations.js` 确保 "15 Google Developer Badges" 未被破坏
4. 生成月度面板 `docs/brain/memories/YYYY-MM-quantitative-dashboard.md`
5. 更新全局账本 `docs/brain/memories/QUANTITATIVE_LEDGER.md`

PR规范：
标题：`[W5] Monthly Alignment YYYY-MM`
Commit：`[W5] 月度代码审计与账本更新 | TrustScore=[val]`

### [W6] Phase 时空校准与基因快照 (每月1日 12:00 UTC)
1. 深度校验所有的 `PHASE_*.md` 时间线逻辑
2. 验证 `evolution.py` AST 热补丁历史
3. 输出审计报告 `docs/brain/memories/YYYY-MM-archaeology-audit.md`
4. 若有重大迭代生成 Phase 增补文档 (仅追加)

PR规范：
标题：`[W6] Archaeology Calibration YYYY-MM`
Commit：`[W6] 月度 Phase 时空校准与历史记录 | entropy=0`
