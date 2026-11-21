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

## 有界活动证据与迁移

- Profile 路径通配只允许 `.md`、`.mdx`、`.markdown`、`.rst`、`.txt`、`.py` 和 `.ipynb` 文本候选，JPG、PDF 等二进制文件不得进入活动快照.
- 候选 Blob 必须严格解码 UTF-8 并拒绝 NUL 字节，不以替换字符伪装不可读来源.
- 原文超过 65,536 字节时，current 只保留来源 Commit、Tree、Blob、规范内容 SHA-256、规模与有界 Diff 预览.
- 原有完整 current 在替换前原样移入只追加 archive，既有 archive 不覆盖、不删除、不重新摄取.
- apply 在投影前重新验证活动路径类型、快照存在性、内容哈希、来源身份与 196,608 字节上限，失败时停止写回.

## 人类阅读格式

当前快照必须依次提供一眼看懂、本次变化、阅读导航、折叠原文和折叠 Diff.

本体系拥有的中文说明只使用英文句号.

外部原文保持来源原貌，不修改其语言、标点和内容.

## 失败协议

Profile 不合法、GitHub Tree 截断、Blob 编码异常、来源网络失败、JSONL 非法或报告格式违规时，Action 必须失败.

不得吞掉失败后继续生成成功提交.

不得通过全局选择冲突一侧掩盖并发变更.

## 独立维护边界

`horizon-cortex/**` 是独立研究维护输出并由人类审核 PR.

本生命周期不格式化、不清理、不自动改写该目录.

## GitHub Actions 生命周期

本生命周期是确定性仓库维护程序，不是 Agent，也不代替独立外部维护或辅助维护体系.

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

## NEXUS GitHub Actions 产物目录与清理边界 (2026-11-21 correction)

- `docs/brain/memories/` 是 lifecycle 真正写回 Git 的 projection / report 目录, 不是 `.github/workflows/` 下的 Runner 缓存. 包含带日期的 Dashboard, `MISSION_ACTIVE.md` 和 append-only `QUANTITATIVE_LEDGER.md`.
- `docs/brain/knowledge/` 是规范事实账本, `docs/brain/inputs/current/` 与 `archive/` 是来源快照和封存档案. 不能因文件数量较多就把它们认定为日志垃圾.
- 只有没有被跟踪或引用的临时缓存, 例如 `__pycache__/`, `.pytest_cache/`, `.raw_cache/` 中的孤立文件, `*.tmp`, 可重建的 SQLite 索引, 才属于候选清理范围; 清理必须确认引用和当前作业边界.
- `$RUNNER_TEMP/lifecycle-manifest.json` 是一次 Runner 内的临时 Manifest; `upload-artifact` 上传后的同名产物和 `$GITHUB_STEP_SUMMARY` 是 GitHub 托管运行证据; GitHub Actions Job Logs 不在 Git Tree 内.
- 日期报告必须来自该日期的实际运行, 不用新一轮指标补写过去缺失日期. 旧报告和历史 PR 维持原始记录, 如有不实内容另行 correction, 不能静默删改.
- 本清理规则不修改 Horizon, Parallax 的独立研究归属, 也不删除 `AGI/workflows/revisions/` 中的工作流历史快照.

## 本仓可执行物理清理验收 (2026-11-21)

- `python docs/brain/nexus.py clean` 仅在关闭当前 Cortex 数据库连接后清理 `docs/brain/cortex.db` 及其同名 `-journal`, `-wal`, `-shm` sidecar. 清理函数先统一拒绝 symlink 或非普通文件, 避免清理一半后才发现越界目标.
- `nexus.py rebuild` 重建 SQLite 前使用同一受控索引清理, 但规范的 `inputs/`, `knowledge/`, `memories/`, `horizon-cortex/`, `parallax/` 不属于该删除函数的作用域.
- `tests/test_brain_cleanup_contract.py` 用临时目录校验严格白名单, 二次调用幂等, symlink fail closed, 以及历史来源和独立研究文件原字节不变.
- Git Tree 中已跟踪的日期报告、历史外部文档、sealed archive 不通过 `.gitignore` 或 `clean` 物理删除. 当前没有证据支持对这些历史文件实施批量删除.

## NEXUS 文件分类与导航 (2026-11-21)

本节是对**现存文件及原有归档规则**的导航校准, 不是新建 Archive owner、来源白名单或允许移动历史证据的授权. 文件数和体积属于有日期的观察结果, 请查阅 [2026-11-21 main Git Tree reconciliation](../../../historical-audits/2026-11/2026-11-21-nexus-brain-data-archive-reconciliation.md), 不从这里推断实时数量.

| 分类 | 当前文件与入口 | 责任 / 时间语义 | 整理边界 |
| --- | --- | --- | --- |
| 宿主使用说明 | [Brain README](../README.md), [SCHEMA](../SCHEMA.md), [AGENTS](../AGENTS.md) | 运行入口与架构/约束文本, 是否生效由当前代码和测试决定 | `AGENTS.md` 与 `SCHEMA.md` 受既有保护边界约束, 不以清理名义覆写 |
| 受控来源清单 | [source_profiles.json](../source_profiles.json), [Harvester](../harvester.py) | Profile 是来源配置, 不等于来源内容真实或已成功摄取 | Profile 改动需要独立审查, 不回填旧来源身份 |
| Harvester 状态 | [inputs/.harvester_state.json](.harvester_state.json) | 当前来源路径、SHA 与输出映射, 不等于工作流运行收据 | 禁止删除、伪造或把历史来源 ID 当作失效缓存 |
| 活动来源快照 | [inputs/current/](current/) | 每个已登记来源路径的当前有效快照 | 只通过受控摄取更新, 旧版本原样进入 Archive |
| 历史外部来源 | [inputs/archive/](archive/) | 原样保留的旧版本与 legacy 历史, 包含外部文档 `README.md__*.md` 包装文件 | 不作为本仓说明文档修改, 不按路径/内容相似度批量删重 |
| 活动事实账本 | [knowledge/entities/](../knowledge/entities/), [knowledge/relations/](../knowledge/relations/) | Canonical JSONL 可回放数据, 有实体/关系约束 | 可按既有 canonical 规则维护, 不把每次重写当作新增知识 |
| 封存事实账本 | [pre-canonical manifest](../knowledge/archive/pre-canonical-2026-07-13/manifest.json) | 旧版 JSONL 原始字节、SHA-256、行数核验入口 | 封存原文不重排、不格式化、不复投影 |
| 运行投影 / Memory | [memories/](../memories/) | 每日 `*-quantitative-dashboard.md`, 早期 `*-radar-broadcast.md`、`*-entity-alignment.md`, 当前任务 `MISSION_ACTIVE.md`, 追加式 `QUANTITATIVE_LEDGER.md` | 日期、原始运行者和观察时间不可互换; 无证据时保留空档, 不回填或删除历史报告 |
| 可重建索引 / 缓存 | `docs/brain/cortex.db`, `inputs/.raw_cache/`, Python 缓存 | SQLite 是可重建查询索引, 不是事实唯一源; raw cache 用于有界 Diff | 仅在持有者确认无使用和引用后按清理白名单操作, 不能误删 State/Archive |
| CI / 工作流证据 | [NEXUS workflow](../../../.github/workflows/nexus-life-cycle.yml), [lifecycle guard](../lifecycle_guard.py), [custody tests](../../../tests/test_nexus_archive_custody.py) | PR 只读验证、定时 apply、Runner 临时 Manifest、上传 Artifact / Job Logs 是不同证据层 | 工作流定义不是 Job Log; CI PASS 不能冒充 production apply |
| 有日期的核验 / 纠错 | [2026-11-21 reconciliation](../../../historical-audits/2026-11/2026-11-21-nexus-brain-data-archive-reconciliation.md), [cleanup tests](../../../tests/test_brain_cleanup_contract.py) | 版本绑定的审计与回归证据, 不占用 Horizon 原生研究身份 | 新结论前向追加, 不能反写旧记录或顶替 Native / A1 / A2 / Periodic |

### 文件名与分类的优先级

- 先按**实际目录 owner + 状态引用 + 生产者代码**分类, 再按扩展名或文件名阅读. `inputs/archive/` 下的 Markdown 是外部来源历史, 不因名为 README 或 CHANGELOG 就归入本仓文档层.
- `memories/` 的同字节 Git blob 不证明运行重复或可以删除; `QUANTITATIVE_LEDGER.md` 的 append-only 脉动也不替代原始 GitHub Actions 执行收据.
- `docs/brain/CS_COMMEMORATION_*.md` 是带日期的解释性记录, 不是运行协议更新; `docs/archaeology/` 与 Horizon、Parallax 仍各有独立治理边界.
- 此导航不要求改写现有 source snapshots、JSONL、Memory、历史 Archive 或受保护的 `AGENTS.md` / `SCHEMA.md`.
