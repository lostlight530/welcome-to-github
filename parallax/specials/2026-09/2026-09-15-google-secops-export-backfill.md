# 特殊专题｜2026-09-15 Google SecOps BigQuery export backfill 与 mitigation 后 durable completion 边界

## 记录信息

- 记录 ID: PX-S-20260915-P04
- 记录类型: 特殊专题
- 事件日期: 2026-09-15
- 实际核验日期: 2026-09-20
- 独立时间窗口: 2026-09-20
- 案例 ID: P-04
- Research Surface: mitigation vs backfill completion / export object identity / current-state replacement
- 实验类型: production incident reality mapping / backlog remediation
- 当前状态: 观察, mitigation 与 historical backlog completion 分离
- 前序记录: [2026-09-17 Daily](../../records/2026-09/2026-09-17.md)
- 关联记录: [2026-W38 derived audit](../../audits/2026-W38.md)
- Record Provenance: NATIVE_SPECIAL / independent official incident verification on 2026-09-20
- 原始发布者集合: Google Security Products Status Dashboard
- 独立来源数量: 1
- Evidence Identity Tuple: publisher=Google; object=Google SecOps BigQuery export incident WqdZVCTLVA3cMSZzhKhb; scope=US multi-region; affected_surface=managed BigQuery/BYOBQ exports; remediation=mitigation plus backfill
- Current State Cut: current incident history records mitigation and historical backfill obligation

## 研究摘要

该事件比普通 `Resolved` 更适合研究 recovery semantics, 因为 Google 明确把 current mitigation 与 historical data backfill 分成两个阶段

provider update 说明 issue mitigated, 18:43 PDT 之后新 events 正常 populated, 同时 07:00–18:43 PDT 的 historical events 仍在 backfill, expected next 24 hours

因此可以直接观察

```text
new-path recovery
!= historical backlog remediation complete
```

## 研究问题

当 provider 已修复新流量路径并开始 backfill historical missing exports 时, 能否把 mitigation time 当成整个 incident 的 durable completion time

## 可证伪假设

- 支持条件: source 明确区分 post-mitigation new events 与 historical backfill
- 推翻条件: authoritative update 明确 backfill complete 且覆盖全部 affected interval

## 历史背景

Google SecOps incident began 2026-09-15 00:28 PDT

用户可能看到 managed BigQuery 与 BYOBQ export 中 UDM events 不完整

Google 后续 identified root cause, mitigated current issue, 并说明 18:43 PDT 之后 new events 正常, 但 07:00–18:43 PDT historical events 正在 backfill

这提供现实世界中的 two-phase recovery object

## 证据矩阵

| 证据 | 发布者 | 标题 | 页面时间 | 访问日期 | 链接 | 支持事实 | 作用 | 限制 | 独立来源 | 动态页面 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | Google | Google SecOps managed BigQuery / BYOBQ export incident | 2026-09-15 | 2026-09-20 | https://status.cloud.google.com/security/incidents/WqdZVCTLVA3cMSZzhKhb | incomplete exports, mitigation, post-18:43 new events healthy, earlier interval backfill | primary remediation chronology | provider aggregate, no per-event backfill ledger | YES | YES |
| E2 | Parallax | 2026-09-17 Daily | 2026-09-17 | 2026-09-20 | ../../records/2026-09/2026-09-17.md | aggregate recovery vs queued processing boundary | conceptual predecessor | different Google incident | NO | NO |

## Identity boundary

- current export path state
- historical affected interval
- missing/backfill event membership
- per-event export completion
- mitigation time
- backfill completion time
- incident notification time

```text
mitigated current path
!= historical gap repaired

new events healthy
!= old events backfilled

backfill started
!= backfill completed
```

## 控制条件

保持 same provider and incident

对比

A: current new-event path after 18:43 PDT

B: historical 07:00–18:43 PDT data requiring backfill

## 实验设计

### Trial A

- 目的: 测试 mitigation 是否等价 durable historical completion
- 保持条件: incident and provider
- 改变条件: temporal slice current vs historical backlog
- 预期支持结果: current path recovered while historical completion remains pending
- 预期反证结果: source states complete backfill for full interval

NO_NEW_CASE_TRIAL

## 原始观测

- incomplete UDM exports affected defined surfaces
- advanced BQ exports were stated not impacted
- root cause identified
- current issue mitigated
- events after 18:43 PDT expected to populate normally
- earlier interval had active backfill
- source expected backfill completion later
- no per-event completion ledger exposed in checked page

## 试验比较

| Trial | 核心判断 | 使用证据 | 判断边界 | 约束保持 | 拒绝情况 | 无依据声明 | 与基线差异 | 差异解释 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | mitigation vs historical completion | E1 | temporal split | same incident | reject one-time completion collapse | mitigation means all history repaired | stronger than generic Resolved | source explicitly names backfill |

## 历史比较

09-13 incident 说明 safely queued / no data lost

09-15 incident 更进一步, 直接把 historical backfill 暴露为独立 remediation phase

因此它是 per-object completion frontier 的更明确现实映射, 但 Special 自身不增加 P-04 CASE 正式 support count

## 指标结果

PARTIAL

可直接识别 affected historical interval, 但没有公开 exact missing-event denominator 或 final completed-event numerator

## 反例检查

如果后续 official update 明确全部 backfill completed, current conclusion应更新为 historical remediation completed

即使如此, earlier period `backfill pending` 仍保留为 historical truth

## 暂时结论

```text
current path mitigation
!= historical backlog completion
```

在 source 明确拆分两阶段时, completion 判断必须保留 temporal membership

## 与 Daily 的关系

关联 [2026-09-17 Daily](../../records/2026-09/2026-09-17.md) 的 queued-processing boundary

Special 提供另一个 reality object, 但不自动扩展 N-03 或 P-04 formal support

## AGI-scale relevance boundary

长期 Agent 可能依赖异步索引, export, vector store 或 audit log

新请求恢复不代表历史上下文已经补齐

如果 Agent 在 backfill 前读取数据, world state 与 evidence set 仍可能 partial

## 历史关系

后续 backfill completion如果出现, 应以前向 correction 更新, 不删除本 Special 记录的 pending phase

## 复验条件

- final provider backfill-complete update
- exact affected event count
- per-event export completion evidence
- independent consumer query showing historical interval complete

## 验证结果

- 2026-09-20 核验 Google official incident page
- mitigation/backfill split verified
- exact final backlog denominator unavailable in checked source
- no production account replay
- no checker PASS claimed at source-verification stage
