# 特殊专题｜2026-09-18 OpenAI Agent API container overbilling, refund remediation 与 economic effect completion

## 记录信息

- 记录 ID: PX-S-20260918-P04
- 记录类型: 特殊专题
- 事件日期: 2026-09-18
- 实际核验日期: 2026-09-20
- 独立时间窗口: 2026-09-20
- 案例 ID: P-04
- Research Surface: world-state drift / billing effect / remediation completion / incident terminal state
- 实验类型: production incident reality mapping / durable economic effect
- 当前状态: 观察, service recovery 与 refund completion 分离
- 前序记录: [2026-09-20 Daily](../../records/2026-09/2026-09-20.md)
- 关联记录: [2026-W38 derived audit](../../audits/2026-W38.md)
- Record Provenance: NATIVE_SPECIAL / official incident timeline verified 2026-09-20
- 原始发布者集合: OpenAI Status
- 独立来源数量: 1
- Evidence Identity Tuple: publisher=OpenAI Status; object=Agent API hosted-container overbilling incident 01M2VA7X37P1ASADSNZ1CG4N4D; effect=billing charges; remediation=customer identification/refund calculation; current_state=Resolved
- Current State Cut: incident current state Resolved, refund/per-customer completion not established by terminal service wording

## 研究摘要

该事件首次在 September Parallax reality layer 中把 economic side effect 与 runtime recovery 放到同一 timeline

OpenAI Status 先说明 hosted containers 出现 higher-than-expected charges, 同时准备 refunds

后续说明正在 review affected usage, identify impacted customers, calculate refunds

mitigation applied 后 new sessions no longer encounter issue

最终 status 标记 fully recovered

最关键边界

```text
future billing path fixed
!= historical overcharge remediated

service fully recovered
!= every impacted customer refund completed
```

## 研究问题

当 provider status page 最终标记 all impacted services fully recovered, 是否可以把 earlier customer-identification / refund-calculation workflow 推导为每个 impacted account 已完成退款

## 可证伪假设

- 支持条件: terminal wording只针对 impacted services, 没有 direct per-customer refund completion evidence
- 推翻条件: authoritative source 明确给出 affected set closure 与 all refunds completed

## 历史背景

2026-09-18 22:29 PDT OpenAI 开始调查 OpenAI-hosted containers in Agent API higher-than-expected charges

23:22 PDT update 说明继续修复, review affected usage, identify impacted customers and calculate refunds

2026-09-19 01:08 PDT mitigation still implementing

05:00 PDT mitigation applied, new sessions would not run into issue

07:52 PDT all impacted services fully recovered

Daily 2026-09-20 已把该 timeline用于 world-state drift test, 并明确 terminal incident text 不足以补出 every affected customer refund completed

## 证据矩阵

| 证据 | 发布者 | 标题 | 页面时间 | 访问日期 | 链接 | 支持事实 | 作用 | 限制 | 独立来源 | 动态页面 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | OpenAI | Overbilling for OpenAI-hosted containers in the Agent API | 2026-09-18→19 | 2026-09-20 | https://status.openai.com/incidents/01M2VA7X37P1ASADSNZ1CG4N4D | overbilling, refund preparation, affected-usage review, mitigation, final service recovery | primary incident/remediation chronology | no customer-level refund ledger | YES | YES |
| E2 | Parallax | 2026-09-20 Daily | 2026-09-20 | 2026-09-20 | ../../records/2026-09/2026-09-20.md | S0→S1 rebinding test | controlled evidence procedure | not independent source | NO | NO |

## Identity boundary

必须分开

- incident service object
- hosted container session
- billing charge object
- impacted customer identity
- affected usage interval
- refund calculation
- refund issuance
- refund receipt
- new-session billing path
- service incident terminal state

```text
issue mitigated
!= overcharge identified for every customer

customer identified
!= refund calculated

refund calculated
!= refund issued

refund issued
!= customer receipt verified

service recovered
!= economic remediation completed
```

## 控制条件

保持 official incident timeline

比较 current service state claim 与 historical remediation claim

## 实验设计

### Trial A

- 目的: 测试 later Resolved 是否可以 rebinding earlier refund workflow为 completed
- 保持条件: same canonical incident
- 改变条件: proposition from service availability to per-customer economic remediation
- 预期支持结果: service current state updates, refund completion stays unknown
- 预期反证结果: same authority publishes all-refunds-complete evidence

本 Special 不新增 CASE Trial count

## 原始观测

- higher-than-expected charges explicitly stated
- refunds preparation explicitly stated
- affected usage review, customer identification and refund calculation explicitly stated
- mitigation later applied
- new sessions no longer affected after mitigation
- final service status fully recovered
- terminal text does not state all refunds issued/completed
- no customer-level affected set or refund ledger exposed

## 试验比较

| Trial | 核心判断 | 使用证据 | 判断边界 | 约束保持 | 拒绝情况 | 无依据声明 | 与基线差异 | 差异解释 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | current service state vs remediation object state | E1 | proposition-level rebinding | same incident | reject broad terminal inheritance | every refund completed | Daily tested same principle | Special preserves event/economic effect identity |

## 历史比较

09-20 Daily 的 S0→S1 world-state test 强调 later evidence只更新被直接覆盖 proposition

本 Special 把该原则固定到真实 billing/remediation event

```text
Resolved(service)
does not entail
Resolved(refund workflow)
```

## 指标结果

NOT_APPLICABLE

source 不提供 affected-customer denominator, refunded-customer numerator或 refund completion percentage

## 反例检查

`All impacted services have now fully recovered` 是强 terminal wording

但 noun phrase 是 services, 不是 refunds/customers/remediation cases

因此不能跨 object identity 扩张

## 暂时结论

服务 current state 可以更新为 recovered

historical overbilling remediation current state 保持 PARTIAL / UNVERIFIED at per-customer level

## 与 Daily 的关系

直接关联 [2026-09-20 Daily](../../records/2026-09/2026-09-20.md)

Daily 是 FRONTIER-WORLD-STATE research batch

本 Special 用 P-04 reality mapping 保存 time-replacement / object-identity boundary, 不自动给 P-04 增加正式 support count

## AGI-scale relevance boundary

长期自主 Agent 的 effect 不只包括写文件/发请求, 还包括 resource consumption, billing, quota 与 financial remediation

world-state rebinding必须按 proposition/object 更新, 不能把一个 terminal status传播给所有关联责任对象

## 历史关系

original investigating/refund workflow与later service recovery均保留

Special创建于 09-20, 不伪装成09-18当时研究产物

## 复验条件

- OpenAI 发布 refund completion update
- direct affected-customer count
- direct refund-issued/completed count
- account-level remediation evidence
- correction to incident scope

## 验证结果

- 2026-09-20核验 canonical OpenAI Status incident
- event chronology and refund-related wording verified
- no customer/account data accessed
- no independent refund confirmation
- no checker PASS claimed at source-verification stage
