# 外部摄取与归档契约

## 目标

本契约约束外部文档摄取、当前快照、历史归档、机器账本和人类阅读稿之间的关系.

系统优先保证证据完整、结果确定、格式可读和失败可见.

## 数据分层

| 路径 | 职责 | 修改规则 |
| --- | --- | --- |
| `current/` | 每个来源路径唯一的当前有效快照 | 新版本替换后将旧版本迁入 archive |
| `archive/` | 失效快照和历史输入 | 只追加，不覆盖，不删除 |
| `.raw_cache/` | 计算下一次 Diff 的原文基线 | 仅清理状态未引用的孤立缓存 |
| `.harvester_state.json` | 来源 SHA、内容哈希和相对输出路径 | 原子写入，禁止保存 Runner 绝对路径 |
| `knowledge/**/*.jsonl` | 可回放事实账本 | 逐行校验、稳定排序、确定性去重 |
| `cortex.db` | 可重建查询索引 | 可以重建和压缩，不作为唯一事实源 |

## 人类阅读格式

当前快照必须依次提供一眼看懂、本次变化、阅读导航、折叠原文和折叠 Diff.

本体系拥有的中文说明只使用英文句号.

外部原文保持来源原貌，不修改其语言、标点和内容.

## 失败协议

Profile 不合法、GitHub Tree 截断、Blob 编码异常、来源网络失败、JSONL 非法或报告格式违规时，Action 必须失败.

不得吞掉失败后继续生成成功提交.

不得通过全局选择冲突一侧掩盖并发变更.

## Jules 边界

`horizon-cortex/**` 由 Jules 外部 SOP 生成并由人类审核 PR.

本生命周期不格式化、不清理、不自动改写该目录.

## GitHub Actions 生命周期

本生命周期是确定性仓库维护程序，不是 Agent，也不代替 Jules 或 GPT 的独立维护体系.

- Push 与 Pull Request 只执行只读校验，不摄取、不生成、不提交.
- 手动运行默认只读，只有明确选择 apply 才进入候选生成链.
- 每日计划运行以北京时间 06:00 对应的名义时隙作为 Logical Cycle Time，Runner 延迟不改变周期身份.
- Source Time、Observed Time、Logical Cycle Time 与 Applied Time 分开记录，不用执行时间冒充来源时间.
- 同一基础提交、逻辑周期、候选路径、语义增量和指标快照生成同一 Idempotency Key.
- 上游仓库只变更 commit 或 tree 而目标 Blob 内容未变时，不改写活动采集状态.
- 运行期间 main 发生变化时，不 rebase、不 autostash、不覆盖，结果记为 `CONFLICTED_WORLD_LINE_NO_APPLY`.
- 没有有效候选时保持绿色并记为 `NO_MEANINGFUL_DELTA`.
- 只有来源内容、知识账本或人类投影的允许路径可以进入候选提交.
- Lifecycle Manifest 作为运行 Artifact 与 Job Summary 保存，不写入知识图谱.
- Action 提交固定使用 `github-actions[bot]` 身份.

结构校验失败、账本破损、越界写入和测试失败仍然必须红灯终止.

安全的无变化与并发避让不是失败，不建立 Branch Protection、Required Check、Environment 或强制 Review 门禁.

## Active ledger maintenance

- current/ is the only external snapshot set projected into the active graph.
- External repository and document identifiers are stable across source revisions.
- Original ledgers are preserved byte for byte under knowledge/archive/pre-canonical-2026-07-13/.
- The archive manifest records relative path, byte size, SHA-256 and line count.
- Active ledgers contain one record per entity ID and one record per relation triple.
- Relations with missing endpoints remain available in the sealed archive and do not enter the active graph.
- Repeating the same lifecycle does not append an equivalent entity or relation.
- Cache cleanup is limited to unreferenced raw-cache files and empty cache directories.
- The active database is a rebuildable index and is never the sole source of truth.
- horizon-cortex and parallax remain outside this lifecycle.
