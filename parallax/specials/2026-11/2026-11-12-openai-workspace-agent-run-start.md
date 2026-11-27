# 特殊专题｜2026-11-12 Workspace Agent 新运行启动故障

## 记录信息

- 记录 ID: PX-S-20261112-P04
- 记录类型: 特殊专题
- 事件日期: 2026-11-12
- 实际核验日期: 2026-11-27
- 独立时间窗口: 2026-11-27
- 案例 ID: P-04
- Research Surface: run admission / existing run / aggregate terminal status
- 实验类型: retrospective public incident reality mapping
- 当前状态: 部分 / PARTIAL
- 前序记录: [2026-11-12 Daily](../../records/2026-11/2026-11-12.md)
- 关联记录: [P-04 时间替换](../../CASES.md)
- Record Provenance: NATIVE_SPECIAL / retrospective source verification 2026-11-27, not event-day execution
- 原始发布者集合: OpenAI Status
- 独立来源数量: 1
- Evidence Identity Tuple: publisher=OpenAI Status; object=https://status.openai.com/incidents/01M76CW2D7FM7K7F8NJ4W0G08N; surface=ChatGPT Agent / new Workspace Agent runs; access=2026-11-27
- Current State Cut: 2026-11-27 Asia/Shanghai, public provider report only

## 研究摘要

11-12 官方事件调查描述无法启动新的 Workspace Agent runs，之后状态为 Resolved.页面列出受影响组件 Agent；未提供已有运行或具体 run ID 的结果.

研究边界：新运行启动受阻是否等同已有运行失败，以及服务恢复能否证明故障期请求全部完成.本专题保存公开事件的 proposition identity，不把恢复词汇传播到未被证据覆盖的对象.

## 研究问题

新运行启动受阻是否等同已有运行失败，以及服务恢复能否证明故障期请求全部完成？

## 可证伪假设

- 支持条件: 同一 canonical incident 的状态更新仅覆盖明确命名的对象与阶段，其他对象仍需单独证据.
- 推翻条件: 同一权威来源给出完整 affected-object set 与逐对象、逐阶段终态回执，且可以绑定原请求身份.

## 历史背景

事件归属 2026-11-12，实际研究发生在 2026-11-27.当前读取的报告包含后续更新，不是事件当日保存的页面快照.不得用后续恢复或归因倒写早期认知.

## 证据矩阵

| 证据 | 发布者 | 标题 | 页面时间 | 访问日期 | 链接 | 支持事实 | 作用 | 限制 | 独立来源 | 动态页面 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | OpenAI Status | Workspace Agent 新运行启动故障 | 2026-11-12 起的事件及后续更新 | 2026-11-27 | https://status.openai.com/incidents/01M76CW2D7FM7K7F8NJ4W0G08N | ChatGPT Agent / new Workspace Agent runs 的供应商事件叙述 | primary incident chronology | 无逐对象原始回执 | YES | YES |
| E2 | Parallax | 2026-11-12 Daily | 2026-11-12 | 2026-11-27 | ../../records/2026-11/2026-11-12.md | effect closure 与 query snapshot identity | repository comparison context | 不是该事件独立来源 | NO | NO |

## Identity boundary

必须区分 run admission / existing run / aggregate terminal status.事件级报告主体、受影响范围、个体对象、状态变更时间与读取时间不可合并.页面更新只授权改变其明确支持的命题.

## 控制条件

固定 Workspace Agent incident，比较 new-run admission、已有 run、task settlement 三个 proposition.

## 实验设计

NO_DIRECT_EXPERIMENT.实际执行为只读公开报告核验及命题边界对照，不运行生产服务、不模拟一个新的 Trial，不计 CASE support.

## 原始观测

- E1 可定位到明确 incident，报告主体和范围如上.
- 事件明确限定新运行启动；缺乏已有 run 的状态明细，不支持扩大故障范围或补全结果.
- 个别请求是否建立 run ID、调度重试、已有运行状态及最终工具 effect 不在可见证据链内.

## 试验比较

| 对照 | 核心判断 | 证据 | 拒绝的扩张 |
| --- | --- | --- | --- |
| A | provider event-level state | E1 | 将范围扩大到全部服务或所有对象 |
| B | object-level result | E1 与 E2 的概念对照 | 将 aggregate recovery 代替个体结果 |

## 历史比较

关联原有 P-04 time replacement 与 [Daily](../../records/2026-11/2026-11-12.md)；本事件是新的对象，不是原 Daily 的独立重放.effect closure 与 query snapshot identity 仅为研究关联，不建立历史因果关系.

## 指标结果

未公布启动失败率、受影响 run 数或逐任务完成分母；NOT_APPLICABLE.

## 反例检查

事件明确限定新运行启动；缺乏已有 run 的状态明细，不支持扩大故障范围或补全结果..如果未来取得完整逐对象状态证据，应重新评估相应命题，而非把当前 UNKNOWN 解释为永远失败.

## 暂时结论

PARTIAL.事件级事实有一手来源，个别请求是否建立 run ID、调度重试、已有运行状态及最终工具 effect 保持 UNKNOWN.未建立第二独立发布者、独立 evaluator 或真实执行证明.

## 与 Daily 的关系

[2026-11-12 Daily](../../records/2026-11/2026-11-12.md) 提供相邻研究问题；该专题不替代 Daily，不增加 CASE 支持或 NOTES.

## AGI-scale relevance boundary

长期 Agent 需要在证据传递中保留 run admission / existing run / aggregate terminal status，防止聚合状态替代对象级结算；仅为研究尺度，不是 AGI capability claim.

## 历史关系

本文件事件日期为 2026-11-12，实际核验为 2026-11-27，与当日 Daily 共享执行日期窗口.后续 correction 保留本次来源切片.新 Special research batch 1，新增独立窗口 0.

## 复验条件

Workspace run store、调度 receipt、工具 effect sink 与用户授权各自独立，公开事件没有逐项数据. 若可取得对象级证据，按原始身份和时间重核.模拟 admission response lost、未建 run、已建 run 三种路径，注入服务恢复后重试，检查是否重复启动或错误结算.

## 验证结果

EXECUTED: 2026-11-27 公开 canonical incident 页面直接读取、事件范围及命题对照.NOT_EXECUTED: 独立服务调用、历史对象重放、完整原生 Python checker.NO_DIRECT_EXPERIMENT / no CASE or NOTES promotion.
