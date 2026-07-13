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
- horizon-cortex and aegis-cortex remain outside this lifecycle.
