# 特殊专题｜2026-11-25 Git LFS 自动重试与对象完整性

## 记录信息

- 记录 ID: PX-S-20261125-P04
- 记录类型: 特殊专题
- 事件日期: 2026-11-25
- 实际核验日期: 2026-11-27
- 独立时间窗口: 2026-11-27
- 案例 ID: P-04
- Research Surface: LFS object identity / client retry / Git pointer
- 实验类型: retrospective bounded public evidence procedure
- 当前状态: 部分 / PARTIAL
- 前序记录: [2026-11-25 Daily](../../records/2026-11/2026-11-25.md)
- 关联记录: [CASES](../../CASES.md)
- Record Provenance: NATIVE_SPECIAL / retrospective public source review, not event-day execution
- 原始发布者集合: GitHub Status
- 独立来源数量: 1
- Evidence Identity Tuple: publisher=GitHub Status; object=https://www.githubstatus.com/incidents/m0wvf9pt3l0l; surface=Git LFS upload / download; observed=2026-11-27
- Current State Cut: 2026-11-27 Asia/Shanghai, public report only

## 研究摘要

11月25日21:30 UTC至26日00:28 UTC，LFS 操作降级，部分失败请求经客户端重试成功；流量迁移后错误率恢复，其他 Git 操作未受影响

本次将事件状态与具体 evidence object 拆分，拒绝把 aggregate recovery 直接转移为 per-object truth

## 研究问题

客户端重试或普通 Git 操作成功是否证明 LFS 对象已完整可用？

## 可证伪假设

- 支持条件: 公开来源的 recovery predicate 仅覆盖其命名对象和阶段，未覆盖对象保持 UNKNOWN
- 推翻条件: 同一 authority 提供完整 affected set、原始请求身份与逐对象结算证据，覆盖当前待判命题

## 历史背景

事件归属采用来源所载日期，实际读取于 2026-11-27，后续更新不是事件当日已保存的历史快照
11月25日21:30 UTC至26日00:28 UTC，LFS 操作降级，部分失败请求经客户端重试成功；流量迁移后错误率恢复，其他 Git 操作未受影响

## 证据矩阵

| 证据 | 发布者 | 页面时间 | 访问日期 | 链接 | 支持事实 | 限制 | 独立来源 | 动态页面 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | GitHub Status | 2026-11-25 及后续报告 | 2026-11-27 | [官方来源](https://www.githubstatus.com/incidents/m0wvf9pt3l0l) | Git LFS upload / download 的公开事件叙述 | 无逐对象完整证据 | YES | YES |
| E2 | Parallax | 2026-11-25 | 2026-11-27 | [同期 Daily](../../records/2026-11/2026-11-25.md) | 本仓同期研究背景 | 不证明现实事件且非独立来源 | NO | NO |

## Identity boundary

LFS object identity / client retry / Git pointer 必须分离，包含对象范围、来源身份、实际事件时间、当前读取时间与结算对象

## 控制条件

固定 LFS object OID 与 pointer commit，分别观察传输响应、对象读取与普通 Git

## 实验设计

NO_DIRECT_EXPERIMENT. 对公开报告的直接读取执行 bounded evidence comparison，不运行受控 Trial，不产生新 CASE support
对照 A 保持事件及 publisher，读取直接支持的状态命题；对照 B 改变 proposition 为个体完成或权限，检验是否存在额外证据

## 原始观测

- 11月25日21:30 UTC至26日00:28 UTC，LFS 操作降级，部分失败请求经客户端重试成功；流量迁移后错误率恢复，其他 Git 操作未受影响
- 其他 Git 操作未受影响，而 LFS 请求存在失败和重试，两个存储路径不等价
- 未获 逐对象上传提交、内容 digest、指针可达性及后续读取

## 试验比较

| 对照 | 判断 | 证据 | 结论边界 |
| --- | --- | --- | --- |
| A | 事件级范围和时间 | E1 | 仅直接支持公开命题 |
| B | 个体完成及持续状态 | E1 | 缺少绑定回执，UNKNOWN |

## 历史比较

P-04 time replacement 只允许 later evidence 更新直接覆盖命题；本次报告为新对象，不追溯改变同期 Daily

## 指标结果

平均2%、峰值4%为 LFS 请求失败率；不能推导对象丢失率，影响区间178分钟

## 反例检查

其他 Git 操作未受影响，而 LFS 请求存在失败和重试，两个存储路径不等价
强反例要求 LFS object store、OID digest、Git pointer 与客户端回执 的对象级记录与当前命题绑定，不能仅增加 URL

## 暂时结论

PARTIAL. 逐对象上传提交、内容 digest、指针可达性及后续读取 保持 UNKNOWN，公开报告可支持事件层但不能给出独立 runtime 或 evaluator 证明

## 与 Daily 的关系

[同期 Daily](../../records/2026-11/2026-11-25.md) 为时间锚点；不声称该 Daily 实验由本事件触发或测试了本事件

## AGI-scale relevance boundary

长时自主 Agent 的证据传递需保存 LFS object identity / client retry / Git pointer 的独立身份，不能把同一 recovery label 广播为全部任务终态；不构成 AGI capability claim

## 历史关系

事件日期 2026-11-25，本次实际核验日期 2026-11-27，与当日已有 Daily 共享执行窗口；新增一个 Special batch，新增全局独立窗口、Trial、CASE、NOTES 均为 0

## 复验条件

模拟上传提交后响应丢失及 pointer 已提交但对象缺失，读取并校验 exact OID 后再结算
只有 LFS object store、OID digest、Git pointer 与客户端回执 能够提供对应对象证据时才扩大命题

## 验证结果

EXECUTED: official public report source read and bounded proposition comparison 2026-11-27
NOT_EXECUTED: production replay, independent second publisher, native full checker. No new finding
