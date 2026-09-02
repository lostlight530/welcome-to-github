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

原文可从 [基础提交](https://github.com/lostlight530/welcome-to-github/tree/e6324b8074453cd62c1dc9023737f2f031f3bd25/parallax) 及本 PR diff 逐项回读. 修改时间属于本次复核,不是历史任务时间. 修改文件中的中文句号统一为英文句号,不改作者身份.

| 文件 | 原问题与修正依据 |
| --- | --- |
| [METHOD.md](METHOD.md) | Add monthly end-to-end repair and logged in-place correction to the existing method |
| [monthly.md](templates/monthly.md) | Extend existing monthly template with actual repair coverage, change log and completion boundary |
| [README.md](README.md) | Expose monthly maintenance and current correction log without changing schedules |
| [2026-08-26.md](records/2026-08/2026-08-26.md) | Separate METR GPT evaluation from the unresolved Anthropic incident review gate |
| [2026-08.md](records/2026-08.md) | Propagate the specific P-05 event-identity correction; no new experiment or historical execution claimed |
| [CASES.md](CASES.md) | Propagate the specific P-05 event-identity correction; no new experiment or historical execution claimed |

检查器只做结构防错. 本轮新增月度维护日志合同、日历与任务状态分离,并防止空字段吞掉下一行. 不建立新的宿主运行机制或强制 CI 闸门.

## 文件覆盖清单

| 路径 | 本轮处置 |
| --- | --- |
| [2026-08-month-end-reconciliation.md](2026-08-month-end-reconciliation.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [audits/2026-W31.md](audits/2026-W31.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [audits/2026-W32.md](audits/2026-W32.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [audits/2026-W33.md](audits/2026-W33.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [audits/2026-W34.md](audits/2026-W34.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [audits/2026-W35.md](audits/2026-W35.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08.md](records/2026-08.md) | 已做表中限定的正文修正,不代表其余全部主张重验 |
| [records/2026-08/2026-08-01.md](records/2026-08/2026-08-01.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-02.md](records/2026-08/2026-08-02.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-03.md](records/2026-08/2026-08-03.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-04.md](records/2026-08/2026-08-04.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-05.md](records/2026-08/2026-08-05.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-06.md](records/2026-08/2026-08-06.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-07.md](records/2026-08/2026-08-07.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-08.md](records/2026-08/2026-08-08.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-09.md](records/2026-08/2026-08-09.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-10.md](records/2026-08/2026-08-10.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-11.md](records/2026-08/2026-08-11.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-12.md](records/2026-08/2026-08-12.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-13.md](records/2026-08/2026-08-13.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-14.md](records/2026-08/2026-08-14.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-15.md](records/2026-08/2026-08-15.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-16.md](records/2026-08/2026-08-16.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-17.md](records/2026-08/2026-08-17.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-18.md](records/2026-08/2026-08-18.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-19.md](records/2026-08/2026-08-19.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-20.md](records/2026-08/2026-08-20.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-21.md](records/2026-08/2026-08-21.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-22.md](records/2026-08/2026-08-22.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-23.md](records/2026-08/2026-08-23.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-24.md](records/2026-08/2026-08-24.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-25.md](records/2026-08/2026-08-25.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-26.md](records/2026-08/2026-08-26.md) | 已做表中限定的正文修正,不代表其余全部主张重验 |
| [records/2026-08/2026-08-27.md](records/2026-08/2026-08-27.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-28.md](records/2026-08/2026-08-28.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-29.md](records/2026-08/2026-08-29.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-30.md](records/2026-08/2026-08-30.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-08/2026-08-31.md](records/2026-08/2026-08-31.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [records/2026-09/2026-09-01.md](records/2026-09/2026-09-01.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [specials/2026-08/2026-08-04-openai-chatgpt-conversation-errors.md](specials/2026-08/2026-08-04-openai-chatgpt-conversation-errors.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [specials/2026-08/2026-08-04-openai-third-party-cyber-evaluations.md](specials/2026-08/2026-08-04-openai-third-party-cyber-evaluations.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [specials/2026-08/2026-08-05-openai-service-events.md](specials/2026-08/2026-08-05-openai-service-events.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [specials/2026-08/2026-08-13-frontier-model-evaluation-comparability.md](specials/2026-08/2026-08-13-frontier-model-evaluation-comparability.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [specials/2026-08/2026-08-21-anthropic-chive-counterfactual-explanations.md](specials/2026-08/2026-08-21-anthropic-chive-counterfactual-explanations.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [specials/2026-08/2026-08-21-deepmind-sima-eve-research-boundary.md](specials/2026-08/2026-08-21-deepmind-sima-eve-research-boundary.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [specials/2026-08/2026-08-26-openai-hugging-face-final-incident-report.md](specials/2026-08/2026-08-26-openai-hugging-face-final-incident-report.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |
| [specials/2026-08/2026-08-28-x-ai-social-summary-source-boundary.md](specials/2026-08/2026-08-28-x-ai-social-summary-source-boundary.md) | 纳入范围与结构扫描,逐命题内容认证未完成 |

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

- Aug 26 的 METR GPT-5.6 Sol 公开评估与 Aug 20 等待的 Anthropic 事故复核是不同对象. 修正日记录、月度索引及 CASES 中的歧义,不增加实验计数.
- 其余 Trial 的独立复现与原始输出完整性未在本轮逐项认证,不以结构检查替代.
