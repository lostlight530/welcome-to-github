# 周期审计模板

## 审计信息

- 审计 ID:
- 记录类型: 周期审计
- 审计日期:
- 归属日期范围:
- 实际执行日期:
- 当前状态:
- 月度索引:
- Record Provenance:
- 派生审计: YES
- 新增实验数量: 0
- 新增长期结论数量: 0

## 覆盖区间

记录归属日期范围与实际执行日期范围.

Daily 与 Special 分别计数.

本文件只复核已经存在的研究, 不补研究缺口, 不替代 Daily production.

## 纳入记录

列出 record ID, record type, assigned/event date, actual execution date 与 independent execution window.

如果某日期没有对应 formal audit predecessor, 不从 Daily coverage 推导 audit execution.

## 覆盖情况

分别统计 Daily, Special, research batches, Trials 与 independent execution windows.

Audit 自身固定增加 0 batch, 0 Trial, 0 independent window.

历史补录不得计为 assigned date 当天的 execution window.

## 重复信号

列出跨研究批次重复出现的 observation.

明确这些重复是否跨实际 execution windows, publisher, object, benchmark, harness 或 evaluator identity.

相似主题不自动等于 independent replication.

## 冲突与漂移

列出 source conflict, current-state drift, benchmark/evaluator identity drift, missing fields 与无法复现内容.

保留 UNKNOWN 与 NO_CONCLUSION, 不为了周期整理压平冲突.

## 特殊专题维护

只说明 Special 的 current evidence relation 与 Daily research relation.

Special maintenance 不自动增加 research batch 或 Trial.

## 反例检查

记录本周期最强 counterexample 以及是否推翻, 收窄或保持当前判断.

## 状态决定

分别记录 observation, candidate, finding, invalidation, no conclusion 与 unchanged research boundary.

任何 promotion 必须满足 METHOD 的独立批次和 execution-window 门槛, audit 本身不提供 promotion evidence.

## 下一阶段控制项

只保留能够缩小 uncertainty 或攻击 strongest current explanation 的 experiment.

优先 real execution, independent evidence, delegated evidence, world-state drift, per-object completion 与 cross-evaluator relation.

## 验证结果

记录实际执行的 structural check, source verification 与未执行项.

Checker PASS 不等于 external truth, source independence 或 research conclusion PASS.
