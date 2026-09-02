# 2026-09-02 维护修正日志

Review Date: 2026-09-02
Review Checkpoint Asia/Shanghai: 2026-09-02T13:34:52+08:00
Reviewer: Codex
Review Window: 2026-08-01 through 2026-09-01 inclusive
Base Commit: e6324b8074453cd62c1dc9023737f2f031f3bd25
Monthly Maintenance Status: PARTIAL
Maintenance Coverage: 下方文件清单,区分结构检查与逐项内容复核.
Maintenance Change Log: 本文件的改动表和对应 Git diff.
Maintenance Validation: 验证结果见末节,未运行项不得视为通过.
Maintenance Unresolved: 全月逐命题外部复核及其全部下游传播尚未认证完成.

## 本轮已做与边界

本次补齐的是月度完整维护流程,并对已经确认的错误做正文微调,不是重新生成历史任务. 既有逻辑日期、原始执行时间、作者、provenance 与阻塞事实保留. 未合并 PR 不能标为未产出,当前路径存在也不能证明原执行成功.

以下清单的“结构检查”只证明路径与适用的离线合同被检查,不等于逐篇外部来源、实验重放或所有结论均获验证. 没有新独立实验或时间窗口计数.

## 改动表

原文可从 [基础提交](https://github.com/lostlight530/welcome-to-github/tree/e6324b8074453cd62c1dc9023737f2f031f3bd25/horizon-cortex) 及本 PR diff 逐项回读. 修改时间属于本次复核,不是历史任务时间. 修改文件中的中文句号统一为英文句号,不改作者身份.

| 文件 | 原问题与修正依据 |
| --- | --- |
| [sample-2026-07-H5-signal-reflect.md](sample-2026-07-H5-signal-reflect.md) | Extend existing monthly template with actual repair coverage, change log and completion boundary |
| [EVIDENCE_POLICY.md](EVIDENCE_POLICY.md) | Define full monthly repair, retain historical execution facts and supersede audit-only guidance |
| [sample-2026-07-H6-horizon-memorize.md](sample-2026-07-H6-horizon-memorize.md) | Extend existing monthly template with actual repair coverage, change log and completion boundary |
| [2026-08-H5-signal-reflect.md](2026-08-H5-signal-reflect.md) | Correct premature calendar closure without changing original execution timestamp, author or task status; monthly maintenance remains partial |
| [2026-08-H6-horizon-memorize.md](2026-08-H6-horizon-memorize.md) | Correct premature calendar closure without changing original execution timestamp, author or task status; monthly maintenance remains partial |
| [2026-09-H6-horizon-memorize.md](2026-09-H6-horizon-memorize.md) | Correct premature calendar closure without changing original execution timestamp, author or task status; monthly maintenance remains partial |
| [2026-09-01-H1-signal-observe.md](2026-09-01-H1-signal-observe.md) | Remove false August H6 migration mandate and unsupported automatic reliability claims |
| [2026-09-01-H2-horizon-orient.md](2026-09-01-H2-horizon-orient.md) | Propagate corrected H6 interpretation through H2 classification and weekly handoff |

检查器只做结构防错. 本轮新增月度维护日志合同、日历与任务状态分离,并防止空字段吞掉下一行. 不建立新的宿主运行机制或强制 CI 闸门.

## 文件覆盖清单

| 路径 | 本轮处置 |
| --- | --- |
| [2026-08-01-H1-signal-observe.md](2026-08-01-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-01-H2-horizon-orient.md](2026-08-01-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-01-through-28-daily-weekly-reconciliation.md](2026-08-01-through-28-daily-weekly-reconciliation.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-02-H1-signal-observe.md](2026-08-02-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-02-H2-horizon-orient.md](2026-08-02-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-03-H1-signal-observe.md](2026-08-03-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-03-H2-horizon-orient.md](2026-08-03-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-04-H1-signal-observe.md](2026-08-04-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-04-H2-horizon-orient.md](2026-08-04-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-05-H1-signal-observe.md](2026-08-05-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-05-H2-horizon-orient.md](2026-08-05-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-06-H1-signal-observe.md](2026-08-06-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-06-H2-horizon-orient.md](2026-08-06-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-07-H1-signal-observe.md](2026-08-07-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-07-H2-horizon-orient.md](2026-08-07-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-08-H1-signal-observe.md](2026-08-08-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-08-H2-horizon-orient.md](2026-08-08-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-09-H1-signal-observe.md](2026-08-09-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-09-H2-horizon-orient.md](2026-08-09-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-10-H1-signal-observe.md](2026-08-10-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-10-H2-horizon-orient.md](2026-08-10-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-11-H1-signal-observe.md](2026-08-11-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-11-H2-horizon-orient.md](2026-08-11-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-12-H1-signal-observe.md](2026-08-12-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-12-H2-horizon-orient.md](2026-08-12-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-13-H1-signal-observe.md](2026-08-13-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-13-H2-horizon-orient.md](2026-08-13-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-14-H1-signal-observe.md](2026-08-14-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-14-H2-horizon-orient.md](2026-08-14-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-15-H1-signal-observe.md](2026-08-15-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-15-H2-horizon-orient.md](2026-08-15-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-16-H1-signal-observe.md](2026-08-16-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-16-H2-horizon-orient.md](2026-08-16-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-17-H1-signal-observe.md](2026-08-17-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-17-H2-horizon-orient.md](2026-08-17-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-18-H1-signal-observe.md](2026-08-18-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-18-H2-horizon-orient.md](2026-08-18-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-19-H1-signal-observe.md](2026-08-19-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-19-H2-horizon-orient.md](2026-08-19-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-20-H1-signal-observe.md](2026-08-20-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-20-H2-horizon-orient.md](2026-08-20-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-21-H1-signal-observe.md](2026-08-21-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-21-H2-horizon-orient.md](2026-08-21-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-22-H1-signal-observe.md](2026-08-22-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-22-H2-horizon-orient.md](2026-08-22-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-23-H1-signal-observe.md](2026-08-23-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-23-H2-horizon-orient.md](2026-08-23-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-24-H1-signal-observe.md](2026-08-24-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-24-H2-horizon-orient.md](2026-08-24-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-25-H1-signal-observe.md](2026-08-25-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-25-H2-horizon-orient.md](2026-08-25-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-26-H1-signal-observe.md](2026-08-26-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-26-H2-horizon-orient.md](2026-08-26-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-27-H1-signal-observe.md](2026-08-27-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-27-H2-horizon-orient.md](2026-08-27-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-28-H1-signal-observe.md](2026-08-28-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-28-H2-horizon-orient.md](2026-08-28-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-29-H1-signal-observe.md](2026-08-29-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-29-H2-horizon-orient.md](2026-08-29-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-30-H1-signal-observe.md](2026-08-30-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-30-H2-horizon-orient.md](2026-08-30-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-31-H1-signal-observe.md](2026-08-31-H1-signal-observe.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-31-H2-horizon-orient.md](2026-08-31-H2-horizon-orient.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-H5-signal-reflect.md](2026-08-H5-signal-reflect.md) | 已做表中限定的正文修正,不代表其余全部主张重验 |
| [2026-08-H6-horizon-memorize.md](2026-08-H6-horizon-memorize.md) | 已做表中限定的正文修正,不代表其余全部主张重验 |
| [2026-08-month-end-reconciliation.md](2026-08-month-end-reconciliation.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-through-23-stage-audit.md](2026-08-through-23-stage-audit.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-08-through-27-stage-audit.md](2026-08-through-27-stage-audit.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-09-01-H1-signal-observe.md](2026-09-01-H1-signal-observe.md) | 已做表中限定的正文修正,不代表其余全部主张重验 |
| [2026-09-01-H2-horizon-orient.md](2026-09-01-H2-horizon-orient.md) | 已做表中限定的正文修正,不代表其余全部主张重验 |
| [2026-W31-H3-position-decide.md](2026-W31-H3-position-decide.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-W31-H4-narrative-act.md](2026-W31-H4-narrative-act.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-W32-H3-position-decide.md](2026-W32-H3-position-decide.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-W32-H4-narrative-act.md](2026-W32-H4-narrative-act.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-W33-H3-position-decide.md](2026-W33-H3-position-decide.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-W33-H4-narrative-act.md](2026-W33-H4-narrative-act.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-W33-reconciliation.md](2026-W33-reconciliation.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-W34-H3-position-decide.md](2026-W34-H3-position-decide.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-W34-H4-narrative-act.md](2026-W34-H4-narrative-act.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-W34-reconciliation.md](2026-W34-reconciliation.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-W35-H4-narrative-act.md](2026-W35-H4-narrative-act.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [2026-W35-partial-reconciliation.md](2026-W35-partial-reconciliation.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |

## 仍需维护的项目

- 完整来源复验应核对命题、对象、时间、出处和真正独立性,不能仅凭 URL 可访问.
- 历史实验的输入、执行者、实际输出、控制变量和评判依据需按记录逐项复核,缺项保持未验证.
- 周度与月度继承关系必须按原始输入快照核对,不能把后续文件倒推成先前成功.
- 只处理本维护目录及适用检查器和测试. 不改宿主 Actions、运行时、数据、前端、调度配置或版本.

## 验证结果

- Horizon 检查器扫描 158 个 dated 路径通过; Parallax 全目录检查通过,79 个文件、44 个每日专题、13 个特殊专题和 6 个审计.
- python -m unittest discover -s tests -p 'test*.py': 58 tests passed.
- 本轮新增回归测试 13 项通过,覆盖月末边界、维护状态、空字段.
- 首次完整测试受到 Windows 临时目录权限限制; 使用本轮工作目录作为临时路径重跑后通过. 未安装依赖或修改系统配置.
- Git diff whitespace check passed.
- 历史文件 SHA-256 核对: 224 项中 217 项未变,7 项为本日志列出的已授权正文修正.
- 两仓根 README 与 CONTRIBUTING 已检查,本轮不加入 SOP 内部规则或记忆,保持原文.
- 这些结果证明本轮改动的结构与回归检查通过,不认证未执行的历史实验重放或全量外部事实复核.

## 本次明确校准

- Aug H5/H6 和 Sep H6 的 CLOSED 早于原执行时的月末边界,修为 OPEN. 原 Task Status 和时间不改,历史阻塞不重放.
- Sep 1 H1/H2 错把 Aug H6 解释为迁移要求,现按 H6 原文纠正并同步 handoff.
- 外部机制核对 [MCP 维护者发布](https://blog.modelcontextprotocol.io/posts/2026-07-28/). 协议机制不等于宿主采用或故障恢复已验证.
