# 特殊专题｜2026-11-16 PR merge timeout 与合并结算身份

## 记录信息

- 记录 ID: PX-S-20261116-P04
- 记录类型: 特殊专题
- 事件日期: 2026-11-16
- 实际核验日期: 2026-11-27
- 独立时间窗口: 2026-11-27
- 案例 ID: P-04
- Research Surface: request timeout / merge receipt / commit ancestry / workflow identity
- 实验类型: retrospective public incident reality mapping
- 当前状态: 部分 / PARTIAL
- 前序记录: [2026-11-16 Daily](../../records/2026-11/2026-11-16.md)
- 关联记录: [P-04 时间替换](../../CASES.md)
- Record Provenance: NATIVE_SPECIAL / retrospective source verification 2026-11-27, not event-day execution
- 原始发布者集合: GitHub Status
- 独立来源数量: 1
- Evidence Identity Tuple: publisher=GitHub Status; object=https://www.githubstatus.com/incidents/2zfqmghmg3s3; surface=Pull Requests / Actions start latency; access=2026-11-27
- Current State Cut: 2026-11-27 Asia/Shanghai, public provider report only

## 研究摘要

11-16 09:30–15:55 UTC 部分 PR merge 请求超时，关联 Actions 启动延迟；官方最终报告同时指向 11-13 的前序短事件，归因为存储读取带宽瓶颈，并描述配置修复与负载迁移.

研究边界：合并请求超时或平台恢复是否足以确定具体 PR 是否已经合并及后续 CI 是否运行.本专题保存公开事件的 proposition identity，不把恢复词汇传播到未被证据覆盖的对象.

## 研究问题

合并请求超时或平台恢复是否足以确定具体 PR 是否已经合并及后续 CI 是否运行？

## 可证伪假设

- 支持条件: 同一 canonical incident 的状态更新仅覆盖明确命名的对象与阶段，其他对象仍需单独证据.
- 推翻条件: 同一权威来源给出完整 affected-object set 与逐对象、逐阶段终态回执，且可以绑定原请求身份.

## 历史背景

事件归属 2026-11-16，实际研究发生在 2026-11-27.当前读取的报告包含后续更新，不是事件当日保存的页面快照.不得用后续恢复或归因倒写早期认知.

## 证据矩阵

| 证据 | 发布者 | 标题 | 页面时间 | 访问日期 | 链接 | 支持事实 | 作用 | 限制 | 独立来源 | 动态页面 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | GitHub Status | PR merge timeout 与合并结算身份 | 2026-11-16 起的事件及后续更新 | 2026-11-27 | https://www.githubstatus.com/incidents/2zfqmghmg3s3 | Pull Requests / Actions start latency 的供应商事件叙述 | primary incident chronology | 无逐对象原始回执 | YES | YES |
| E2 | Parallax | 2026-11-16 Daily | 2026-11-16 | 2026-11-27 | ../../records/2026-11/2026-11-16.md | exact MISS watermark 与 named path identity | repository comparison context | 不是该事件独立来源 | NO | NO |

## Identity boundary

必须区分 request timeout / merge receipt / commit ancestry / workflow identity.事件级报告主体、受影响范围、个体对象、状态变更时间与读取时间不可合并.页面更新只授权改变其明确支持的命题.

## 控制条件

固定 PR 操作语义，区分 transport、merged_at、merge commit、main ancestry 与 workflow run.

## 实验设计

NO_DIRECT_EXPERIMENT.实际执行为只读公开报告核验及命题边界对照，不运行生产服务、不模拟一个新的 Trial，不计 CASE support.

## 原始观测

- E1 可定位到明确 incident，报告主体和范围如上.
- 报告同时说明部分 Git 操作仍可用，不能把 merge 超时扩展成所有 Git 写入失败；缺少逐 PR 结算记录.
- 具体 PR merge receipt、actual merge parent、workflow attempt、人工批准与最终应用结果 不在可见证据链内.

## 试验比较

| 对照 | 核心判断 | 证据 | 拒绝的扩张 |
| --- | --- | --- | --- |
| A | provider event-level state | E1 | 将范围扩大到全部服务或所有对象 |
| B | object-level result | E1 与 E2 的概念对照 | 将 aggregate recovery 代替个体结果 |

## 历史比较

关联原有 P-04 time replacement 与 [Daily](../../records/2026-11/2026-11-16.md)；本事件是新的对象，不是原 Daily 的独立重放.exact MISS watermark 与 named path identity 仅为研究关联，不建立历史因果关系.

## 指标结果

11-16 merge attempts 平均超时 2.9%，峰值 7.1%；11-13 为 1.7%.这些是各事件请求指标，不是仓库或 PR 的失败概率.

## 反例检查

报告同时说明部分 Git 操作仍可用，不能把 merge 超时扩展成所有 Git 写入失败；缺少逐 PR 结算记录..如果未来取得完整逐对象状态证据，应重新评估相应命题，而非把当前 UNKNOWN 解释为永远失败.

## 暂时结论

PARTIAL.事件级事实有一手来源，具体 PR merge receipt、actual merge parent、workflow attempt、人工批准与最终应用结果 保持 UNKNOWN.未建立第二独立发布者、独立 evaluator 或真实执行证明.

## 与 Daily 的关系

[2026-11-16 Daily](../../records/2026-11/2026-11-16.md) 提供相邻研究问题；该专题不替代 Daily，不增加 CASE 支持或 NOTES.

## AGI-scale relevance boundary

长期 Agent 需要在证据传递中保留 request timeout / merge receipt / commit ancestry / workflow identity，防止聚合状态替代对象级结算；仅为研究尺度，不是 AGI capability claim.

## 历史关系

本文件事件日期为 2026-11-16，实际核验为 2026-11-27，与当日 Daily 共享执行日期窗口.后续 correction 保留本次来源切片.新 Special research batch 1，新增独立窗口 0.

## 复验条件

PR API、Git commit graph、branch head 与 exact-head Actions；公共报告只支持平台层影响. 若可取得对象级证据，按原始身份和时间重核.模拟 merge commit 已写但客户端 timeout、未提交 timeout 与 base drift；比较 blind retry 和 exact receipt plus authorization fence.

## 验证结果

EXECUTED: 2026-11-27 公开 canonical incident 页面直接读取、事件范围及命题对照.NOT_EXECUTED: 独立服务调用、历史对象重放、完整原生 Python checker.NO_DIRECT_EXPERIMENT / no CASE or NOTES promotion.
