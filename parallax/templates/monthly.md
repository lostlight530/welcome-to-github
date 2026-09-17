# 周期整理模板

## 覆盖区间

记录上海逻辑归属日期范围与实际执行日期范围.

自然月结束前只使用 as-of synthesis, 不提前写成 sealed final month.

## 记录构成

分别记录 Daily assigned-date coverage, actual execution-date coverage, native/substitute/reconstruction provenance, research batches, Trials, independent execution windows, Specials 与 derived audits.

每日没有阳性发现仍必须有真实研究产出. `UNKNOWN`, `DEGRADED`, `PARTIAL`, `UNVERIFIED`, `EVIDENCE_INSUFFICIENT` 与 `NO_CONCLUSION` 都是合法 Daily outcome, 但不自动计长期支持.

Special 不替代 Daily continuity. Audit 增加 0 research batches, 0 Trials, 0 independent execution windows.

## 每日研究覆盖

列出每日研究问题, Research Surface, current boundary 与实际 execution date.

## 特殊专题

分别统计特殊专题并说明其独立研究价值. 特殊专题不因为存在就自动升级 CASE 或 NOTES.

## 证据覆盖

按 claim-specific authority 总结公开权威来源, runtime evidence, benchmark/evaluator evidence, dynamic evidence, counterexample 与 unavailable primary evidence.

明确 publisher count 与 independent source count, current page 与 historical snapshot, protocol 与 runtime result 的边界.

## Research surfaces

按本周期真实研究分布总结.

- Evidence identity and support
- Temporal and current-state correctness
- Execution / harness / evaluator provenance
- Capability / deployment / semantic outcome
- Delegated evidence or multi-agent evidence chain
- Other emerging surface

只总结实际发生的研究, 不为了覆盖所有类别制造内容.

## Identity coverage

记录本周期实际区分过的 identity.

`claim / object / publisher / evidence artifact / benchmark / dataset / model configuration / execution / harness / evaluator / temporal / current-state / correction relation`

说明哪些 identity 仍缺失或只能部分建立.

## 已复验发现

只列出满足 METHOD 门槛的发现.

每项必须回指支持记录与实际执行窗口.

没有新发现时明确写 `NO_NEW_FINDING`, 不从 Daily 数量推导长期结论.

## 候选与观察

分别列出尚未达到长期门槛的案例, current evidence boundary 与下一复验条件.

## 未解决矛盾与 Unknown

保留不能被现有证据解释的差异, source conflict, missing identity, unresolved current state 与 unavailable execution.

## 失效记录

记录被新证据推翻的旧判断, invalidation date, impact scope 与 replacement evidence.

## 稳定性与质量

分别总结 judgment stability, unsupported claims, rational refusal, evidence identity preservation, source independence 与 verification burden.

不压缩成综合分数.

## 有效速度

只记录完成 source verification, counterexample 与必要 validation 后的有效耗时或无效工作. 不把省略验证当作提速.

## AGI-scale research synthesis

只基于本周期真实研究回答.

1. 哪些 epistemic failures 会在长期自主 Agent 中被放大
2. 哪些 evidence identity 已经能够稳定保持
3. 哪些 world-state / execution / evaluator identity 仍需要直接实验
4. 哪些问题值得进入下一周期 Daily frontier

本节不得把 research relevance 写成 AGI capability claim.

## 下一周期问题

选择最能证伪现有候选或暴露新 identity collapse 的问题.

优先真实执行机会, strong counterexample 与 independent evidence, 不追逐热点数量.

## 派生审计状态

审计只作为 derived review 索引. 审计增加 0 research batches, 0 Trials, 0 independent execution windows.

Daily research production 不以 audit 是否存在为前置条件.

## Monthly maintenance ledger

Maintenance 与 research production 分离. 只有真实维护任务运行时填写本节.

Monthly Maintenance Status: NOT_RUN
Maintenance Coverage: TODO
Maintenance Change Log: TODO
Maintenance Validation: NOT_RUN
Maintenance Unresolved: Full monthly maintenance has not run.

如果 maintenance 实际运行, 记录真实 scoped inventory, correction 与 validation. 不允许用 maintenance 状态覆盖 Daily research facts, 也不允许让 later source 看起来在 earlier run 时已经可用.
