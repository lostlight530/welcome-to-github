# 特殊专题｜2026-08-13 前沿模型官方评价的可比性边界

## 记录信息

- 记录 ID: PX-S-20260813-P05
- 记录类型: 特殊专题
- 事件日期: 2026-08-13
- 实际核验日期: 2026-08-13
- 独立时间窗口: 2026-08-13
- 案例 ID: P-05
- 实验类型: 三发布者长上下文, 跨厂商评价表, 方法字段删除, 时间快照删除, 风险框架冲突摘要
- 当前状态: 观察, N-04 复发检查, 长期适用范围不扩大
- 前序记录: [2026-08-13 每日专题](../../records/2026-08/2026-08-13.md)
- 关联记录: [8 月月度索引](../../records/2026-08.md), [N-04 长期记录](../../NOTES.md#n-04-长上下文不替代直接支持与对象身份)

## 研究摘要

本专题联合核验 OpenAI, Anthropic 与 Google DeepMind 三个公开评价体系

选取的公开对象分别为 OpenAI GPT-5.6 System Card, Anthropic Claude Sonnet 5 发布与系统卡入口, Google Gemini 3.1 Pro Model Card 与正式 evaluation methodology

这些材料的发布日期, 模型版本, reasoning 或 effort 设置, 工具访问, harness, scaffold, 数字来源和安全框架均不完全相同

因此本专题不建立跨厂商总分或总排名

五个 Trial 检查完整方法信息, 跨厂商数值表, 方法字段缺失, 发布时点缺失和统一排名冲突摘要出现时, 判断能否保持模型, 发布者, 时间快照与评价方法边界

本专题作为 2026-08-13 第二个 P-05 研究批次, 与同日每日专题共享一个独立执行窗口

## 研究问题

当 OpenAI, Anthropic 与 Google 的官方模型评价材料同时进入长上下文时, 判断能否区分同一 benchmark 名称下不同模型版本, reasoning 或 effort 设置, tool access, token budget, harness, scaffold 与数字来源

在缺少这些方法条件或发布日期时, 是否会错误地把官方跨厂商表压缩为 2026-08-13 的统一总排名

不同公司的安全框架是否会被错误解释为一条共享的高低风险刻度

## 可证伪假设

- 支持条件: 完整材料下只形成 benchmark 与配置限定的比较, 不形成统一总排名
- 方法删除条件: 删除 effort, tools, token budget, harness, scaffold 与数字来源后, 对数值差异的解释必须收窄
- 时间删除条件: 删除发布日期后, 不能把历史模型表解释为 2026-08-13 当前三家模型状态
- 风险框架条件: OpenAI Preparedness, Anthropic RSP 与 Google Frontier Safety Framework 的术语不能直接拼成同一序数尺度
- 推翻条件: 忽略方法与时间差异给出无条件厂商排名, 或把不同安全框架的标签直接排序为同一风险等级

## 历史背景

2026-08-07 至 2026-08-09 的每日专题分别处理 HTTP 状态语义, 生产契约与字段含义, 共同保留对象和证据条件

2026-08-10 的 P-04 研究在同日复核中主动降为关联观察, 因为缺少明确旧新契约生效时间

2026-08-11 与 2026-08-12 分别使用 Kubernetes 与 Python 官方资料完成两个独立发布体系的 P-04 契约替换复验

2026-08-13 每日专题恢复 Irregular 原始报告, 检查开发方二次汇总与第三方原始发布者的归属边界

本专题继续使用 P-05, 但把长上下文从同一网络安全事件扩展到三家前沿模型官方评价材料

这项研究不追溯修改 2026-08-07 至 2026-08-13 已接受日报的有效性

## CASE 对齐门

- P-05 输入, 固定问题与核心约束: 已满足, 五个 Trial 均固定检查跨厂商官方评价的可比性边界
- P-05 核心变化, 增加噪声, 误导摘要或删除关键支持记录: 已满足, Trial B 增加跨厂商数值表, Trial C 删除方法字段, Trial D 删除发布时点, Trial E 增加统一排名冲突摘要
- P-05 检查目标, 核心约束, 证据计数与结论门槛是否保持: 已满足, 每个 Trial 均保留发布者, 模型身份, 方法条件和结论范围的显式判断

本专题计入 P-05 新研究批次

本专题与 2026-08-13 每日专题属于同一个实际执行日期, 因此 P-05 累计研究批次增加 1, 独立执行窗口不增加

## 下一复验条件门

P-05 当前 CASE 下一复验条件仍包含此前网络安全评估的事件关系删除, AISI 后续复核或 OpenAI 后续明确纠正

本专题是用户明确要求的独立公共专题, 不把三厂商评价研究冒充此前事件关系删除复验

- 事件关系删除: 未满足, 本专题研究对象不是 Hugging Face, AISI 与 Irregular 三项事件关系
- AISI 后续独立复核: 当前无法核验为本专题新材料
- OpenAI 对此前第三方评估的明确纠正: 当前无法核验为本专题新材料
- P-05 核心长上下文变化: 已满足
- 方法条件删除: 已满足, Trial C
- 发布时点删除: 已满足, Trial D
- 冲突摘要: 已满足, Trial E

此前未满足条件继续保留, 本专题不将其写成已完成

## 证据矩阵

| 证据 | 发布者 | 标题 | 页面时间 | 访问日期 | 链接 | 支持事实 | 作用 | 限制 | 独立发布者 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| E1 | OpenAI | GPT-5.6 System Card | 2026-07-09 | 2026-08-13 | [System Card](https://deploymentsafety.openai.com/gpt-5-6) | GPT-5.6 评价按 reasoning effort 展示性能曲线, 旧模型比较值使用近期 snapshot 且可能与旧卡数值不同, Preparedness 对 GPT-5.6 使用自身风险分类 | OpenAI 方法与时间边界 | OpenAI 对自身模型和所选对照的发布材料, 不是统一第三方测量 | 1 |
| E2 | OpenAI | Separating signal from noise in coding evaluations | 2026-07-08 | 2026-08-13 | [评价审计](https://openai.com/index/separating-signal-from-noise-coding-evaluations/) | OpenAI 对 SWE-Bench Pro 进行审计并估计约 30% 任务存在问题, 说明 benchmark 本身也可能改变评价可信度 | benchmark 质量反例 | 只覆盖其审计对象, 不能推翻所有 coding benchmark | 0 |
| E3 | Anthropic | Introducing Claude Sonnet 5 | 2026-06-30 | 2026-08-13 | [Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) | Sonnet 5 在 BrowseComp 与 OSWorld-Verified 中按 effort 展示性能, 发布页修正 BrowseComp 图以匹配 10M token budget, compaction 与 programmatic tool calling 的标准方法, 其他分数也有 grader 或运行方法更新 | Anthropic 方法变化反例 | 发布页不是统一第三方 benchmark 平台 | 1 |
| E4 | Anthropic | Model system cards | 当前公开索引 | 2026-08-13 | [System cards](https://www.anthropic.com/system-cards) | Anthropic 将 system card 定义为记录 Claude 能力, 安全评价与负责任部署决策的材料 | 发布者与文档类型身份 | 索引本身不提供本专题所有具体分数 | 0 |
| E5 | Anthropic | Responsible Scaling Policy | 2026-07-08 版本 3.4 | 2026-08-13 | [RSP](https://www.anthropic.com/responsible-scaling-policy) | Anthropic 使用自身 capability thresholds 与 required safeguards 管理前沿风险 | 安全框架身份 | 不能与其他公司的术语按名称直接换算 | 0 |
| E6 | Google DeepMind | Gemini 3.1 Pro Model Card | 2026-02-19 | 2026-08-13 | [Model Card](https://deepmind.google/models/model-cards/gemini-3-1-pro/) | 提供 Gemini 3.1 Pro 与当时 Claude, OpenAI 模型的多项 benchmark 表, 同时说明后续改进的 safety evaluations 与此前卡片结果并非直接可比, Frontier Safety 使用 CCL | Google 模型快照与安全框架 | 表格是 2026-02 快照, 不代表 2026-08 当前三家产品线 | 1 |
| E7 | Google DeepMind | Gemini 3.1 Pro Model Evaluation – Approach, Methodology & Results | 2026-02 | 2026-08-13 | [Methodology](https://deepmind.google/models/evals-methodology/gemini-3-1-pro) | 非 Gemini 数字多数来自各提供方自报, 部分 coding benchmark 使用不同 provider scaffolding 与 infrastructure, Gemini BrowseComp 使用 Deep Research 与 search, Python, browsing | 跨厂商表的来源与 harness 边界 | 同一 Google 发布体系, 不是第二个独立 Google 实现 | 0 |
| C1 | 受控摘要 | 三家公司官方图表已经形成一张统一当前排行榜, benchmark 高分等于整体更强, OpenAI Preparedness, Anthropic RSP 与 Google CCL 是同一风险刻度 | 本次构造 | 2026-08-13 | 不适用 | 合并时间, 方法, 能力维度与安全框架 | 主动反例 | 不是事实来源 | 0 |

E1 至 E7 共覆盖 OpenAI, Anthropic 与 Google DeepMind 三个独立发布者

同一发布者的多个页面只用于补充方法与框架, 不增加独立发布者计数

## 直接观测

E1 明确按不同 reasoning effort 展示 GPT-5.6 性能, 并说明此前模型的比较值来自近期 snapshot, 可能与此前 system card 中公布的数值略有不同

E2 说明 benchmark 数据集本身也可能存在足以影响评价结论的问题

E3 的公开 changelog 明确记录 BrowseComp 图曾因较简单方法而低估 Sonnet 5, 后续改为与 system card 一致的 10M token budget, compaction 与 programmatic tool calling

E3 还记录 Humanity’s Last Exam grader 与 OSWorld-Verified 运行方式更新可以改变此前 Sonnet 4.6 的公开分数

E6 的跨厂商表明确标注具体模型版本和 thinking 设置, 其结果时间为 2026-02

E7 明确说明非 Gemini 模型数字多数来自提供方自报, 并说明 SWE-Bench 使用不同 provider methodology, scaffolding 与 infrastructure

E7 对 BrowseComp 进一步说明 Gemini 使用 Deep Research 与 search, Python, browsing, 其他模型结果来自提供方自报

E5 与 E6 显示 Anthropic RSP 与 Google Frontier Safety Framework 使用不同风险治理术语, E1 的 OpenAI Preparedness 也属于独立框架

## 控制条件

- 固定问题为三家官方评价材料能支持什么层级的跨厂商比较
- 固定对象为 E1 至 E7 中明确命名的模型, benchmark, 方法和风险框架
- 固定评价字段为发布者, 模型版本, 发布时点, benchmark, reasoning 或 effort, tools, token budget, harness 或 scaffold, 数字来源, 风险框架
- Trial A 使用 E1 至 E7 的方法和身份信息, 不形成总排名
- Trial B 在 Trial A 上只加入 E6 的跨厂商 benchmark 数值表作为比较压力
- Trial C 保留 Trial B 的模型名与数值, 删除 reasoning 或 effort, tools, token budget, harness, scaffold 与数字来源字段
- Trial D 恢复方法字段, 删除 E1, E3, E6 的发布日期和结果快照时间
- Trial E 恢复全部材料并只加入 C1

## 实验设计与原始观测

### Trial A｜三发布者完整基线

- 改变条件: 无
- 原始输入: E1 至 E7 的公开方法, 时间与身份信息
- 原始观测: 三家都公开能力或安全评价材料, 但选取模型的发布日期分别位于 2026-07, 2026-06 与 2026-02, 评价设置与风险框架并不统一
- 判断: 可以分别记录三家官方评价如何形成和限定其结论, 不能由这些异步材料形成一个 2026-08-13 全局总排名

### Trial B｜加入跨厂商数值表

- 改变条件: 只加入 E6 中具体 benchmark 数值表
- 保持条件: 模型版本, 2026-02 快照, thinking 设置与 E7 方法说明全部保留
- 原始观测: E6 可以在指定行和指定模型版本上提供数值差异, E7 同时说明部分对照数字来自提供方自报且部分 coding 任务使用不同 scaffold 与 infrastructure
- 判断: 可以描述表内某一 benchmark 在该快照与配置下的相对数值, 不能把一行或多行数值压缩为当前厂商整体排名

### Trial C｜删除方法字段

- 改变条件: 删除 reasoning 或 effort, tool access, token budget, harness, scaffold 与数字来源
- 保持条件: 模型名称与公开分数
- 原始观测: 数字仍存在, 但失去判断是否来自单次运行, 最大 reasoning, provider self-report, Deep Research, 不同 scaffold 或不同 token budget 的条件
- 判断: 数值可以作为未完整标注的方法结果保留, 跨厂商因果解释与高低排序范围明显收窄
- 主动反例: E3 已实际发生因方法更新而修改公开 BrowseComp 图的情况, 因此方法字段不是可安全删除的装饰信息

### Trial D｜删除发布时点

- 改变条件: 删除 E1, E3, E6 的发布日期与结果快照时间
- 保持条件: 模型名称, benchmark 与方法条件
- 原始观测: 可以继续识别 GPT-5.6, Claude Sonnet 5 与 Gemini 3.1 Pro 的指定材料, 但无法仅由本 Trial 输入判断这些材料在 2026-08-13 是否仍代表三家公司当前模型线
- 判断: 保留已命名模型的评价关系, 拒绝补写当前厂商排名或当前旗舰关系

### Trial E｜统一排行榜与风险刻度冲突摘要

- 改变条件: 在完整 E1 至 E7 上只加入 C1
- 原始观测: C1 同时删除 benchmark 维度, 方法差异, 时间快照和安全框架身份
- 原始观测: OpenAI Preparedness, Anthropic RSP 与 Google Frontier Safety Framework 分别由不同发布者定义, 本轮没有取得三者之间的正式换算关系
- 判断: 拒绝 C1, benchmark 只在对应对象与方法范围内解释, 风险标签也只在各自框架内解释

## 试验比较

| Trial | 核心判断 | 判断边界 | 约束保持 | 合理拒绝或限制 | 无依据声明 | 差异解释 |
| --- | --- | --- | --- | --- | ---: | --- |
| A | 三家官方材料可分别核验, 不形成统一总排名 | 发布者, 时间与方法完整 | 保持 | 是 | 0 | 基线 |
| B | 指定 benchmark 行可以有限比较 | 只覆盖表内模型与快照 | 保持 | 是 | 0 | 加入跨厂商数值表 |
| C | 分数存在但可比性显著下降 | 方法字段缺失 | 保持 | 是 | 0 | 删除方法支持 |
| D | 命名模型关系保留, 当前性未知 | 发布时间缺失 | 保持 | 是 | 0 | 删除时间快照 |
| E | 拒绝统一能力排名与统一风险刻度 | 不跨框架归一化 | 保持 | 是 | 0 | 加入冲突摘要 |

## 三家官方评价边界

| 发布体系 | 本专题选取材料 | 可以直接支持 | 不能由本专题直接支持 |
| --- | --- | --- | --- |
| OpenAI | GPT-5.6 System Card, coding eval audit | GPT-5.6 在明确 reasoning effort 与评价条件下的报告结果, Preparedness 自身框架内判断, benchmark 质量审计结论 | 与 2026-02 或 2026-06 他家快照无条件组成当前总排名 |
| Anthropic | Claude Sonnet 5 发布材料, system card 索引, RSP | Sonnet 5 在明确 effort 与方法下的公开评价, 方法修正对分数的影响, Anthropic 自身风险治理框架 | 把 BrowseComp 修正前后数值混成同一方法, 或把 RSP 术语换算为其他公司风险标签 |
| Google DeepMind | Gemini 3.1 Pro Model Card 与 methodology | 2026-02 指定模型与 thinking 设置的表内结果, non-Gemini 数字来源与 scaffold 差异, Google 自身 CCL 判断 | 把 2026-02 表解释成 2026-08-13 当前三家排行榜, 或把 provider self-report 当成统一 harness 重跑 |

这张表只总结证据边界, 不构成能力, 产品或安全总评分

## 反例检查

- Anthropic 已实际修改 Sonnet 5 BrowseComp 图, 原因是较简单方法没有反映其标准 agentic search 方法, 反驳同 benchmark 名称自动代表同方法
- Google 明确说明非 Gemini 结果多数来自提供方自报, 反驳一个厂商模型卡中的跨厂商表必然来自统一测试执行
- Google 明确说明 SWE-Bench provider methodologies 使用不同 scaffolding 与 infrastructure, 反驳同 benchmark 数字天然同条件
- OpenAI 明确按 reasoning effort 展示曲线而非单一分数, 反驳忽略推理预算仍把模型表示为一个固定能力点
- OpenAI 对 SWE-Bench Pro 的审计估计约 30% 任务存在问题, 反驳 benchmark 分数本身不需要数据质量复核
- Google 说明改进后的 safety evaluations 与此前 Gemini model card 结果并非直接可比, 反驳同厂商跨卡片自动可比
- 三家风险治理框架没有本轮可核验的正式一一映射, 反驳按标签词面建立统一风险排序

反例成立并限制本专题观察

## 暂时结论

本专题形成 P-05 第六个研究批次

由于与 2026-08-13 每日专题在同一个实际执行日期完成, P-05 独立执行窗口保持 5, 不增加第六个窗口

三家官方资料能够支持模型, benchmark, 发布时点和方法条件明确时的局部比较

跨厂商官方表仍需要保留数字来源, reasoning 或 effort, tools, token budget, harness, scaffold 与时间快照

删除方法条件后, 公开分数不能继续承担原有可比性强度

删除发布时间后, 已命名模型的历史评价仍可保留, 但不能补成 2026-08-13 当前厂商排行榜

不同公司的安全框架只在各自定义内解释, 本专题不建立跨框架总风险序列

## 历史关系

- P-05 第六个研究批次
- 2026-08-13 第二个研究批次
- 与同日每日专题共享一个独立执行窗口
- 三发布者长上下文
- 跨厂商 benchmark
- 方法字段删除
- 时间快照删除
- 风险框架冲突摘要
- N-04 复发检查

## 长期记录判断

本专题属于 N-04 复发检查

OpenAI, Anthropic 与 Google 的评价材料为新的观察对象, 但本轮不决定把三家跨厂商评价对象正式加入 N-04 支持记录与长期适用范围

N-04 已在今日每日专题中完成 Irregular 原始发布者范围扩展, 本专题不再次扩大正式适用范围

长期适用范围不扩大, `NOTES.md` 不修改

## 7 月 7 日至 8 月 13 日近期段落关系

本专题只复核当前要求的 2026-08-07 至 2026-08-13 连续七日

- 2026-08-07: P-02 把 HTTP 503 通用语义与 httpbin 受控测试端点分开
- 2026-08-08: P-02 把 Cloudflare 429 正式生产契约与本轮未取得的真实响应分开
- 2026-08-09: P-03 把 Statuspage impact 严重度字段与用户或请求覆盖分母分开
- 2026-08-10: P-04 关联观察在复核后拒绝无明确生效时间的 CASE 计数
- 2026-08-11: P-04 使用 Kubernetes 明确版本 removal 契约完成核心变化
- 2026-08-12: P-04 切换到 Python distutils 生命周期完成第二个独立发布体系复验
- 2026-08-13: P-05 每日专题恢复 Irregular 原始发布者, 本特殊专题进一步检查 OpenAI, Anthropic 与 Google 官方评价材料的可比性

七个每日专题保持七个每日研究批次

本特殊专题增加一个独立研究批次, 因而 2026-08-07 至 2026-08-13 当前共形成 8 个研究批次, 仍只覆盖 7 个实际执行日期窗口

这项连续性复核不构成周期审计, 不追溯改变既有记录状态

## 复验条件

下一次同类专题优先满足以下任一条件

- 取得同一 benchmark, 同一版本数据集, 同一公开 harness 与尽可能一致推理预算下的三家当前模型可重复结果
- 取得独立评估发布者对三家同一任务的统一方法结果, 并保留模型快照与执行日期
- 任一厂商正式更正已经用于跨厂商比较的 benchmark 数值或方法, 可执行纠错持续性复验
- 取得各安全框架之间正式定义的映射关系后, 再检验是否允许有限跨框架比较

缺少这些条件时, 不为制造新排名重复选择相同 benchmark 表

## 已验证事实

- OpenAI GPT-5.6 System Card 发布于 2026-07-09, 按 reasoning effort 展示性能曲线, 并说明此前模型比较值来自近期 snapshot
- OpenAI 2026-07-08 coding evaluation 审计报告估计 SWE-Bench Pro 约 30% 任务存在问题
- Anthropic Claude Sonnet 5 发布于 2026-06-30, 公开评价按 effort 展示部分 agentic benchmark
- Anthropic 发布页记录 BrowseComp 图因方法不一致被更正, 更正后采用 10M token budget, compaction 与 programmatic tool calling
- Google Gemini 3.1 Pro Model Card 发布于 2026-02-19
- Google Gemini 3.1 Pro methodology 明确说明非 Gemini 数字多数来自各提供方自报
- Google methodology 明确说明 SWE-Bench 的 provider methodologies 使用不同 scaffolding 与 infrastructure
- Google methodology 明确说明 Gemini BrowseComp 使用 Deep Research 与 search, Python, browsing, 其他模型结果来自提供方自报
- Google Gemini 3.1 Pro Model Card 说明其改进后的 safety evaluations 与此前 model card 结果并非直接可比

## 合理推断

- 官方发布者提供跨厂商数字不等于已经统一执行环境
- 同一 benchmark 名称不足以证明 token budget, tools, harness, grader 与 scaffold 相同
- 公开表可以支持限定条件下的局部数值比较, 但从局部分数到厂商总排名需要额外的统一评价定义
- 2026-02, 2026-06 与 2026-07 的模型快照不能在缺少新执行结果时自动升级为 2026-08-13 当前状态
- 风险框架术语只有在取得正式定义映射后才可能形成有限跨框架比较

## 未验证事项

- 本轮没有调用 GPT-5.6, Claude Sonnet 5 或 Gemini 3.1 Pro 执行统一 benchmark
- 没有复现 BrowseComp, SWE-Bench Pro, OSWorld-Verified 或 Gemini 3.1 Pro 表内任何分数
- 没有取得三家公司在同一执行日期, 同一 harness 与同一推理预算下的统一结果
- 没有验证各厂商所有当前产品线或当前旗舰模型的完整能力排序
- Anthropic Claude Sonnet 5 完整 system card 页面因当前读取路径内容体积过大未完整取得, 本专题只使用可直接核验的 Anthropic 发布页, system card 索引与 RSP
- 没有取得 OpenAI Preparedness, Anthropic RSP 与 Google Frontier Safety Framework 之间的正式风险等级换算关系

## 验证结果

- OpenAI GPT-5.6 System Card 与 coding evaluation 审计完成直接核对
- Anthropic Claude Sonnet 5 发布页, system card 索引与当前 RSP 完成直接核对
- Google Gemini 3.1 Pro Model Card 与三页 evaluation methodology PDF 完成直接核对
- 三个发布者分别计数, 同发布者多个页面没有冒充独立发布者
- Trial A 至 E 均由本轮实际形成的证据增加, 删除或冲突输入构成
- P-05 核心长上下文变化已直接执行
- 本专题不建立跨厂商总分, 总排名或统一安全风险序列
- 本专题不修改 `NOTES.md`, 长期适用范围不扩大
