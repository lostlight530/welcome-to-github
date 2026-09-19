# 特殊专题｜2026-09-14 OpenAI Agents API managed-session degradation 与 event-level recovery 边界

## 记录信息

- 记录 ID: PX-S-20260914-P04
- 记录类型: 特殊专题
- 事件日期: 2026-09-14
- 实际核验日期: 2026-09-20
- 独立时间窗口: 2026-09-20
- 案例 ID: P-04
- Research Surface: production runtime transition / managed-session identity / aggregate recovery / per-session completion
- 实验类型: production incident reality mapping / no new CASE count
- 当前状态: 观察, N-03 现实事件映射, per-session completion 未验证
- 前序记录: [2026-09-16 Daily](../../records/2026-09/2026-09-16.md)
- 关联记录: [2026-W38 derived audit](../../audits/2026-W38.md)
- Record Provenance: NATIVE_SPECIAL / post-event independent source verification on 2026-09-20
- 原始发布者集合: OpenAI Status
- 独立来源数量: 1
- Evidence Identity Tuple: publisher=OpenAI Status; object=Agents API managed-session incident 01M2H3J1D6Y7RHAP49GRWGJAY0; event_scope=managed sessions; event_state=Resolved; temporal_identity=2026-09-14 PDT
- Current State Cut: incident page currently shows final Resolved state while preserving Monitoring updates

## 研究摘要

2026-09-14 OpenAI Agents API 事件给出一个非常干净的 runtime state transition

```text
delays / unable to start turns
→ mitigations applied
→ seeing recovery
→ Resolved
→ managed sessions processing turns normally
```

最重要的研究边界不是 status page 是否可信, 而是 incident-level terminal state 能否扩大成每个 historical session / turn 的 direct completion proof

## 研究问题

官方 incident final state 为 Resolved 且 managed sessions processing turns normally 时, 是否可以断言事件期间所有 individual session 与 delayed turn 均已成功完成

## 可证伪假设

- 支持条件: provider page 只证明 aggregate service/event recovery, 没有 per-session terminal evidence
- 推翻条件: authoritative source 提供事件期间完整 session membership 与逐 session/turn terminal result

## 历史背景

OpenAI Status 记录从 2026-09-14 13:30 PDT 起, customers using Agents API experienced delays or were unable to start turns in managed sessions

20:30 PDT update 公开该影响, 23:28 PDT 说明 mitigation 已应用且 seeing recovery but service not fully recovered, 23:39 PDT 标记 Resolved 并称 managed sessions processing turns normally

Daily 2026-09-16 已把该对象纳入 P-04 runtime transition

## 证据矩阵

| 证据 | 发布者 | 标题 | 页面时间 | 访问日期 | 链接 | 支持事实 | 作用 | 限制 | 独立来源 | 动态页面 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | OpenAI | Degraded Performance affecting Agents API | 2026-09-14 | 2026-09-20 | https://status.openai.com/incidents/01M2H3J1D6Y7RHAP49GRWGJAY0 | impact start, managed-session scope, mitigation/recovery, Resolved terminal update | primary runtime chronology | aggregate provider status, no session ledger | YES | YES |
| E2 | Parallax | 2026-09-16 Daily | 2026-09-16 | 2026-09-20 | ../../records/2026-09/2026-09-16.md | P-04 controlled interpretation | repository history | not external independence | NO | NO |

## Identity boundary

分开

- incident object
- Agents API product surface
- managed-session population
- individual session identity
- turn identity
- service event state
- individual turn outcome
- incident current state
- event start/end time
- later observation time

```text
service recovered != individual historical request success
processing turns normally now != every prior turn completed
```

## 控制条件

保持 official incident and managed-session scope

比较 incident-level terminal claim 与 per-session universal completion claim

## 实验设计

### Trial A

- 目的: 测试 aggregate Resolved 是否能补出 per-session success
- 保持条件: same OpenAI event and final status text
- 改变条件: claim granularity from event to individual session/turn
- 预期支持结果: aggregate recovery成立, universal individual success被拒绝
- 预期反证结果: official complete session membership and per-session terminal outcome evidence

NO_NEW_CASE_TRIAL

## 原始观测

- official page records delays or unable-to-start-turns for managed sessions
- mitigations applied
- seeing recovery but not fully recovered existed as intermediate state
- final Resolved says managed sessions processing turns normally
- no session IDs
- no affected-session denominator
- no per-turn terminal outcomes
- no replay ledger
- no statement that every earlier failed/delayed start later succeeded

## 试验比较

| Trial | 核心判断 | 使用证据 | 判断边界 | 约束保持 | 拒绝情况 | 无依据声明 | 与基线差异 | 差异解释 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | event recovery vs session completion | E1 | aggregate service incident | same object/timeline | reject per-session universal success | every impacted session succeeded | none | Special adds event memory only |

## 历史比较

Daily 09-16 已满足新的 production event-level runtime switch

Special 不把 current Agents API documentation 倒写成 09-14 runtime sample

## 指标结果

NOT_APPLICABLE

没有 direct affected-session denominator / terminal-success numerator

## 反例检查

`managed sessions are now processing turns normally` 是最强反例

它证明 current aggregate service state, 但语法与 evidence object 仍不是 historical per-session completion ledger

## 暂时结论

事件级恢复成立

individual session / turn completion 保持 UNVERIFIED

## 与 Daily 的关系

直接关联 [2026-09-16 Daily](../../records/2026-09/2026-09-16.md)

本 Special 单独保存 event identity, 但不增加 P-04 CASE 正式支持计数

## AGI-scale relevance boundary

持久 Agent session 会跨 incident boundary 存活或失败

安全恢复需要 session identity, accepted-turn identity, effect state 与 replay semantics, 不能仅依赖 provider aggregate green status

## 历史关系

earlier degraded state 与 later Resolved 同时保留

later current page 不删除 event chronology

## 复验条件

- per-session status export
- direct failed/accepted turn identity
- durable task/turn receipt
- provider RCA with object-level recovery scope
- independent run reproducing resume/replay behavior

## 验证结果

- 2026-09-20 直接核验 OpenAI Status incident page
- chronology and final wording verified
- no per-session runtime access
- no independent publisher exact incident trace
- no checker PASS claimed at source-verification stage
