# Parallax

Parallax 是长期自主系统的 evidence identity、判断稳定性与反例边界研究系统

它研究同一判断在 publisher、object、time、execution/harness、source independence、current state 与 correction relation 变化时是否仍然成立, 不以 benchmark 排名或模型名称替代真实运行证据, 也不宣称已经实现 AGI

## 核心任务

每个 Asia/Shanghai 逻辑日期必须产生一个真实可证伪的 Daily research unit, 即使结果是 PARTIAL、UNKNOWN、DEGRADED、UNVERIFIED 或 NO_CONCLUSION, 同日 rerun 只能补强原 Daily

固定研究链为 research question -> falsifiable hypothesis -> controls -> Trials or bounded evidence procedure -> raw observations -> counterexample -> provisional conclusion -> retest condition

formal contract 不等于 runtime behavior, test source 不等于 test execution, merged state 不等于 review approval, current snapshot 不等于完整历史, 同一 publisher 的多个页面不自动构成独立来源

## 当前入口

- 最新每日归属日期: 2026-10-25
- 最新每日研究: [Pages artifact custody versus deployment-run continuity](records/2026-10/2026-10-25.md)
- 每日专题: 95
- 特殊专题: 17
- 当前专题研究批次: 112
- 当前专题独立执行日期窗口: 90
- 当前观察案例: 0
- 当前候选案例: 0
- 当前长期结论: 5
- 周期审计: 8
- 最新周期审计: [2026-W43 Sunday as-of](audits/2026-W43.md)
- 当前月度事实源: [2026-10](records/2026-10.md)
- 当前方法: [METHOD.md](METHOD.md)
- 控制案例: [CASES.md](CASES.md)
- 长期发现: [NOTES.md](NOTES.md)
- 当前日记录模板: [templates/daily.md](templates/daily.md)
- 当前周期整理模板: [templates/monthly.md](templates/monthly.md)
- 特殊专题: [specials/README.md](specials/README.md)
- 周期审计: [audits/README.md](audits/README.md)
- 历史 README 原样快照: [2026-10-21 archive](README-history-through-2026-10-21.md)

## 研究面

- Evidence identity: 同一 URL、publisher、benchmark 名称与 run identity 不可混同
- Temporal correctness: historical truth、current state、decision-time 与 execution-time truth 分离
- Execution provenance: model、harness、tool、workflow、evaluator 与 actual run 需各自存证
- Capability semantics: intended use、deployment、tool effect、semantic success 与 client acceptance 分离
- Delegated evidence: Agent 间 summary、tool response、source identity 与 authorization 不能互相替代
- Human collaboration: producer delivery、review submission、off-platform human authority 与 merge effect 分离

## 记录与计数合同

Daily 是 mandatory primary research, Special 是独立公共事件研究, Audit 是 derived review

一个有效 Daily 或 Special 各计一个 research batch, 一个实际执行日期计一个 independent execution window, 同日多个 Trial 不重复计 batch 或 window

历史 RECONSTRUCTION/NOT_RUN/UNVERIFIED 只能按其实际 provenance 保留, 不能被后续 evidence 冒充为原生执行

CASES 只在当前控制案例满足真实支持门槛时增加, NOTES 仅收录至少三个独立实验、跨至少两个实际执行窗口且完成反例检查的发现

## 当前研究边界 — 2026-10-25

本日固定对照两个 GitHub Pages deploy run 39977997855 与 40062316438, 均有 completed/success job 与成功上传日志, 同名 `github-pages` ZIP 均为 13925 bytes 但报告 SHA256 不同, 旧 run 的历史上传日志仍在但当前 artifact list 为空且下载 API 返回 HTTP 404, 新 run 的 artifact list 含一个 expired=false 对象, 已实际下载新 ZIP 并用 Python 3.13.5 独立验证 13925 bytes 与 SHA256 25f845059ba338a34f9842c5f3d1071a0ca84157d73b8042715c217feb6d8a97, ZIP CRC 与 TAR 成员读取成功, GitHub 单一 publisher, 结论 PARTIAL

`RUN_SUCCESS != CURRENT_ARTIFACT_LISTED != CURRENT_PUBLIC_SITE_VERIFIED`

`SAME_ARTIFACT_NAME_AND_SIZE != SAME_ARCHIVE_DIGEST != SAME_RENDERED_BYTES`

本日 native Daily 1、research batch 1、independent execution window 1, 无 CASE/NOTES/Special/Audit 增加, derived synchronization 研究 credit 为 0, exact native checker 未执行, 下载 ZIP 字节的独立复核不等于公共 Pages 内容验证

## 前序研究边界 — 2026-10-24

本日以两个固定 Git commits e5a8cd71 与 75ac544d 对照路径级 blob identity, 16 个 intervening commits 与 27 个 changed paths 不意味着每个文件内容变化, checker 与 2026-10-22 Daily blob 相同, README blob 不同, 本地 Python 3.13.5 synthetic fixture 18 项断言通过, GitHub 与 Git upstream 文档两个独立 publisher, 结论 PARTIAL

`BRANCH_TIP_CHANGED != ALL_PATH_BLOBS_CHANGED`

`SAME_PATH_BLOB_SHA_AT_TWO_REFS != SAME_COMMIT_OR_REPOSITORY_STATE`

本日 native Daily 1、research batch 1、independent execution window 1, 无 CASE/NOTES/Special/Audit 增加, derived synchronization 研究 credit 为 0, exact native checker 未执行

## 前序研究边界 — 2026-10-23

本日对 PR #807 及对照 PR #806 的 exact Git commit graph 执行只读 bounded procedure, #807 记录 base d32c943e 与合并第一父 b665119a 不同, 其间 6 个主线提交影响 10 个非 Parallax 路径, 合并第一父到 merge commit 的变化只有 4 个 Parallax 文件, 而 PR head 到 merge commit 的比较展示 10 个主线侧路径

`PR_RECORDED_BASE != MERGE_TIME_FIRST_PARENT`

`PR_HEAD != MERGE_COMMIT != POST_MERGE_MAIN_SNAPSHOT`

本日 native Daily 1、research batch 1、independent execution window 1, GitHub 单一 publisher, 结论 PARTIAL, 无 CASE/NOTES/Special/Audit 增加, derived synchronization 研究 credit 为 0, exact native checker 未执行

## 前序研究边界 — 2026-10-22

本日只读检查三个已合并 PR #786、#795、#806 的固定 head 与 GitHub REST/GraphQL review submission、thread、comment surfaces, 三者 merged=true 但平台 review submissions 均为空, 只能否定 merge 自动蕴含 recorded APPROVED review 的推断, 不能否定线下人工审查

当前 main protected=false 仅属于 2026-10-22 access cut, 不能还原这些 PR 合并时的 ruleset 或 branch protection 配置

`MERGED_TRUE != RECORDED_APPROVED != OFF_PLATFORM_HUMAN_REVIEW`

`CURRENT_BRANCH_PROTECTION != HISTORICAL_MERGE_POLICY`

本日一个 native Daily、一个 research batch、一个 independent execution window, 单一 GitHub publisher, bounded API evidence, 结论 PARTIAL, 不新增 CASE/NOTES/Special/Audit, derived index synchronization 额外研究 credit 为 0

## 2026-W43 周级派生审查 — 2026-10-25 as-of

- [W43 七日研究、证据身份与 checker 契约修正审查](audits/2026-W43.md) 纳入 2026-10-19 至 2026-10-25 的七份 native Daily, 七个实际执行窗口、七个研究批次、14 个 Daily 内已登记 Trials, 0 个新 Special
- 10-25 同日 artifact ZIP 完整性验证后残留的 Trial A 旧限制已对齐, 未更改 Daily 本身的执行日期、Record ID、研究批次或 publisher count
- 当前 checker 已区分 Audit record-reference 解析与 NOTES support gate, 可识别新式 FRONTIER Daily ID, 保留旧式 P 系列控制案例与原有 NOTES 门槛
- 周日 as-of 表示 W43 当天已产出七条 Daily 但自然周尚未正式结束, 不视为 sealed week, 审计本身增加 0 research batch、0 Trial、0 independent execution window、0 finding
- exact `python parallax/tools/check.py` 的完整树原生执行状态必须以实际执行日志为准, 本次针对 checker 规则的独立 Python fixture 不等于 native checker PASS

## 历史与验证边界

2026-07 至 2026-10-21 的全部原始 Daily、Special、Audit、METHOD、CASES、NOTES 与月度记录仍以各自文件为权威

本次仅将旧 README 的历史 current pointers、维护注释与当时统计口径整体移入 [只读历史快照](README-history-through-2026-10-21.md), 不修改其历史语义, 当前入口不再在一页中重复堆叠旧时点状态

原生结构检查命令为 `python parallax/tools/check.py`, checker PASS 仅表示结构合同部分成立, 不证明外部事实、publisher independence 或 runtime correctness

当前 native checker 是否执行须以具体 Daily 和 PR 验证记录为准, 不能从 GitHub CodeQL success 推断
