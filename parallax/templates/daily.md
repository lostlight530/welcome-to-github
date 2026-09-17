# YYYY-MM-DD｜研究标题

## 记录信息

- 记录 ID:
- 记录类型: 每日专题
- 上海归属日期:
- 实际执行日期:
- 独立时间窗口:
- 案例 ID:
- Research Surface: evidence identity / temporal state / execution provenance / capability semantics / delegated evidence / other
- 实验类型:
- 当前状态: 观察 / 候选 / 发现 / 失效 / 无结论 / 未验证 / 降级 / 部分
- 前序记录:
- 关联记录:
- Record Provenance:
- 原始发布者集合:
- 独立来源数量:
- Evidence Identity Tuple:
- Object / Benchmark / System Identity:
- Execution / Harness / Evaluator Identity:
- Current State Cut:
- 拒绝或无结论原因:

## 研究摘要

本节必须说明今天实际研究了什么, 不能用 maintenance/no-change 代替 Daily research production.

即使结果为 UNKNOWN, DEGRADED, PARTIAL, UNVERIFIED, EVIDENCE_INSUFFICIENT 或 NO_CONCLUSION, 仍记录真实研究过程和边界.

## 研究问题

写成能够被证伪的问题.

## 可证伪假设

- 支持条件:
- 推翻条件:

## 历史背景

只使用在当时真实可用或明确标为 fixed historical material 的内容. Later evidence 不倒写成 earlier observation.

## 证据矩阵

| 证据 | 发布者 | 标题 | 页面时间 | 访问日期 | 链接 | 支持事实 | 作用 | 限制 | 独立来源 | 动态页面 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

转载, mirror, 同一发布者的派生页面与 developer summary 不自动增加独立来源数量.

## Identity boundary

明确今天不能坍缩的 identity, 例如 claim, object, publisher, benchmark, dataset, model configuration, run, harness, evaluator, timestamp, current state 或 correction relation.

## 控制条件

## 实验设计

至少一个 Trial 或一个能够被反驳的 bounded evidence procedure.

### Trial A

- 目的:
- 保持条件:
- 改变条件:
- 预期支持结果:
- 预期反证结果:

## 原始观测

只记录本轮直接读取, 直接运行或明确固定的输入产生的观测. 不把解释写成 raw observation.

## 试验比较

| Trial | 核心判断 | 使用证据 | 判断边界 | 约束保持 | 拒绝情况 | 无依据声明 | 与基线差异 | 差异解释 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 历史比较

明确本轮相对前序 Daily, fixed historical material, previous current-state cut 或已有 CASE 的变化. Later evidence 不倒写 earlier observation.

## 指标结果

只记录具有明确分母, metric identity 或可计数 event 的量化结果. 没有合法量化时写 `NOT_APPLICABLE`.

## 反例检查

必须至少尝试一个会让首选解释失败的 counterexample. 如果无法执行, 明确标记未执行原因.

## 暂时结论

结论允许是 `NO_CONCLUSION`, `UNKNOWN`, `PARTIAL` 或 `DEGRADED`. 不为了每日产出制造阳性发现.

## AGI-scale relevance boundary

说明本轮对未来长期自主 Agent 的哪一种 epistemic property 有意义, 例如 evidence delegation, world-state drift, tool/model configuration identity, evaluator independence 或 per-object completion.

本节只解释研究相关性, 不允许写成 AGI capability claim.

## 历史关系

说明本轮是新对象, 复发检查, counterexample, correction relation 还是已有 CASE 的真实核心变化.

## 复验条件

说明下一次改变什么, 保持什么, 需要哪种更强证据.

## 验证结果

分别说明实际执行的 checker/runtime/source verification 与未执行项. Checker PASS 不等于 external truth PASS.
