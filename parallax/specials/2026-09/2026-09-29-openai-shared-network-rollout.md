# 特殊专题｜2026-09-29 OpenAI 共享网络容量耗尽与任务恢复

## 记录信息

- 记录 ID: PX-S-20260929-P04
- 记录类型: 特殊专题
- 事件日期: 2026-09-29
- 实际核验日期: 2026-11-27
- 独立时间窗口: 2026-11-27
- 案例 ID: P-04
- Research Surface: shared dependency / partial mitigation / task lifecycle
- 实验类型: retrospective bounded public evidence procedure
- 当前状态: 部分 / PARTIAL
- 前序记录: [2026-09-29 Daily](../../records/2026-09/2026-09-29.md)
- 关联记录: [CASES](../../CASES.md)
- Record Provenance: NATIVE_SPECIAL / retrospective public source review, not event-day execution
- 原始发布者集合: OpenAI Status
- 独立来源数量: 1
- Evidence Identity Tuple: publisher=OpenAI Status; object=https://status.openai.com/incidents/01M3Q4RK1SM4EMK445GGPG7C0N/write-up; surface=ChatGPT / Codex / Agents API; observed=2026-11-27
- Current State Cut: 2026-11-27 Asia/Shanghai, public report only

## 研究摘要

9月29日约10:30 PDT 出现错误；功能变更触发重复后台检查并耗尽共享连接容量；约11:00多数影响缓解，部分服务残余降级持续至约16:07

本次将事件状态与具体 evidence object 拆分，拒绝把 aggregate recovery 直接转移为 per-object truth

## 研究问题

多数影响缓解能否推出未完成的 agent tasks 都已恢复或补偿？

## 可证伪假设

- 支持条件: 公开来源的 recovery predicate 仅覆盖其命名对象和阶段，未覆盖对象保持 UNKNOWN
- 推翻条件: 同一 authority 提供完整 affected set、原始请求身份与逐对象结算证据，覆盖当前待判命题

## 历史背景

事件归属采用来源所载日期，实际读取于 2026-11-27，后续更新不是事件当日已保存的历史快照
9月29日约10:30 PDT 出现错误；功能变更触发重复后台检查并耗尽共享连接容量；约11:00多数影响缓解，部分服务残余降级持续至约16:07

## 证据矩阵

| 证据 | 发布者 | 页面时间 | 访问日期 | 链接 | 支持事实 | 限制 | 独立来源 | 动态页面 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | OpenAI Status | 2026-09-29 及后续报告 | 2026-11-27 | [官方来源](https://status.openai.com/incidents/01M3Q4RK1SM4EMK445GGPG7C0N/write-up) | ChatGPT / Codex / Agents API 的公开事件叙述 | 无逐对象完整证据 | YES | YES |
| E2 | Parallax | 2026-09-29 | 2026-11-27 | [同期 Daily](../../records/2026-09/2026-09-29.md) | 本仓同期研究背景 | 不证明现实事件且非独立来源 | NO | NO |

## Identity boundary

shared dependency / partial mitigation / task lifecycle 必须分离，包含对象范围、来源身份、实际事件时间、当前读取时间与结算对象

## 控制条件

同一报告区分启动、恢复、完成以及共享依赖容量

## 实验设计

NO_DIRECT_EXPERIMENT. 对公开报告的直接读取执行 bounded evidence comparison，不运行受控 Trial，不产生新 CASE support
对照 A 保持事件及 publisher，读取直接支持的状态命题；对照 B 改变 proposition 为个体完成或权限，检验是否存在额外证据

## 原始观测

- 9月29日约10:30 PDT 出现错误；功能变更触发重复后台检查并耗尽共享连接容量；约11:00多数影响缓解，部分服务残余降级持续至约16:07
- 官方明确部分任务不能启动、恢复或完成且存在残余降级
- 未获 每个 task ID 的重试、tool effects、历史授权、终态

## 试验比较

| 对照 | 判断 | 证据 | 结论边界 |
| --- | --- | --- | --- |
| A | 事件级范围和时间 | E1 | 仅直接支持公开命题 |
| B | 个体完成及持续状态 | E1 | 缺少绑定回执，UNKNOWN |

## 历史比较

P-04 time replacement 只允许 later evidence 更新直接覆盖命题；本次报告为新对象，不追溯改变同期 Daily

## 指标结果

约30分钟到多数影响缓解与约337分钟到残余降级结束是两种指标，不能相加

## 反例检查

官方明确部分任务不能启动、恢复或完成且存在残余降级
强反例要求 任务调度、工具 sink、用户可见结果和独立 completion store 的对象级记录与当前命题绑定，不能仅增加 URL

## 暂时结论

PARTIAL. 每个 task ID 的重试、tool effects、历史授权、终态 保持 UNKNOWN，公开报告可支持事件层但不能给出独立 runtime 或 evaluator 证明

## 与 Daily 的关系

[同期 Daily](../../records/2026-09/2026-09-29.md) 为时间锚点；不声称该 Daily 实验由本事件触发或测试了本事件

## AGI-scale relevance boundary

长时自主 Agent 的证据传递需保存 shared dependency / partial mitigation / task lifecycle 的独立身份，不能把同一 recovery label 广播为全部任务终态；不构成 AGI capability claim

## 历史关系

事件日期 2026-09-29，本次实际核验日期 2026-11-27，与当日已有 Daily 共享执行窗口；新增一个 Special batch，新增全局独立窗口、Trial、CASE、NOTES 均为 0

## 复验条件

注入共享依赖耗尽与 lost acknowledgement，先查任务和 effect receipts，限制重试预算，未对账保持 UNKNOWN
只有 任务调度、工具 sink、用户可见结果和独立 completion store 能够提供对应对象证据时才扩大命题

## 验证结果

EXECUTED: official public report source read and bounded proposition comparison 2026-11-27
NOT_EXECUTED: production replay, independent second publisher, native full checker. No new finding
