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

选取对象分别为 OpenAI GPT-5.6 System Card, Anthropic Claude Sonnet 5 发布与系统卡入口, Google Gemini 3.1 Pro Model Card 与 evaluation methodology

这些材料的发布日期, 模型版本, reasoning 或 effort 设置, 工具访问, token budget, harness, scaffold, 数字来源和安全框架并不完全相同

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

CASE 对齐结果

- 固定问题与核心约束: 已满足
- 增加噪声, 误导摘要或删除关键支持记录: 已满足
- 核心约束, 证据计数与结论门槛保持: 已满足

下一复验条件结果

- 事件关系删除: 未满足
- AISI 后续独立复核: 当前无法核验
- OpenAI 对此前第三方评估的明确纠正: 当前无法核验
- P-05 核心长上下文变化: 已满足
- 方法条件删除: 已满足
- 发布时点删除: 已满足
- 冲突摘要: 已满足

此前未满足条件继续保留, 本专题不将其写成已完成

## 证据矩阵

| 证据 | 发布者 | 标题 | 页面时间 | 访问日期 | 链接 | 支持事实 | 作用 | 限制 | 独立来源 | 动态页面 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | OpenAI | GPT-5.6 System Card | 2026-07-09 | 2026-08-13 | https://deploymentsafety.openai.com/gpt-5-6 | GPT-5.6 评价按 reasoning effort 展示性能, 旧模型比较值使用近期 snapshot, Preparedness 使用自身风险分类 | OpenAI 方法与时间边界 | OpenAI 自身发布材料, 不是统一第三方测量 | 是 | 否 |
| E2 | OpenAI | Separating signal from noise in coding evaluations | 2026-07-08 | 2026-08-13 | https://openai.com/index/separating-signal-from-noise-coding-evaluations/ | OpenAI 对 SWE-Bench Pro 进行审计并记录任务质量问题 | benchmark 质量反例 | 只覆盖其审计对象 | 否 | 否 |
| E3 | Anthropic | Introducing Claude Sonnet 5 | 2026-06-30 | 2026-08-13 | https://www.anthropic.com/news/claude-sonnet-5 | Sonnet 5 在 BrowseComp 与 OSWorld-Verified 中按 effort 展示性能, 发布页记录 BrowseComp 图因方法变化被更正, 更正后采用 10M token budget, compaction 与 programmatic tool calling | Anthropic 方法变化反例 | 发布页不是统一第三方 benchmark 平台 | 是 | 是 |
| E4 | Anthropic | Model system cards | 当前公开索引 | 2026-08-13 | https://www.anthropic.com/system-cards | system card 索引提供模型评价材料身份 | 发布者与文档类型身份 | 索引本身不提供本专题所有具体分数 | 否 | 是 |
| E5 | Anthropic | Responsible Scaling Policy | 2026-07-08 版本 3.4 | 2026-08-13 | https://www.anthropic.com/responsible-scaling-policy | Anthropic 使用自身 capability thresholds 与 required safeguards 管理前沿风险 | 安全框架身份 | 不能与其他公司的术语按名称直接换算 | 否 | 是 |
| E6 | Google DeepMind | Gemini 3.1 Pro Model Card | 2026-02-19 | 2026-08-13 | https://deepmind.google/models/model-cards/gemini-3-1-pro/ | 提供 Gemini 3.1 Pro 与当时其他模型的 benchmark 表, 并记录 safety evaluation 可比性边界与 Frontier Safety CCL | Google 模型快照与安全框架 | 2026-02 快照不代表 2026-08 当前三家产品线 | 是 | 是 |
| E7 | Google DeepMind | Gemini 3.1 Pro Model Evaluation – Approach, Methodology & Results | 2026-02 | 2026-08-13 | https://deepmind.google/models/evals-methodology/gemini-3-1-pro | 非 Gemini 数字多数来自各提供方自报, 部分 coding benchmark 使用不同 provider scaffolding 与 infrastructure, Gemini BrowseComp 使用自身工具链 | 跨厂商表的来源与 harness 边界 | 同一 Google 发布体系, 不是第二个独立 Google 实现 | 否 | 是 |
| C1 | 受控摘要 | 三家公司官方图表已经形成一张统一当前排行榜, benchmark 高分等于整体更强, 三家安全框架是同一风险刻度 | 本次构造 | 2026-08-13 | 不适用 | 合并时间, 方法, 能力维度与安全框架 | 主动反例 | 不是事实来源 | 否 | 否 |

E1 至 E7 覆盖 OpenAI, Anthropic 与 Google DeepMind 三个独立发布者

同一发布者的多个页面只用于补充方法与框架, 不增加独立发布者计数

## 控制条件

- 固定问题为三家官方评价材料能支持什么层级的跨厂商比较
- 固定对象为 E1 至 E7 中明确命名的模型, benchmark, 方法和风险框架
- 固定评价字段为发布者, 模型版本, 发布时点, benchmark, reasoning 或 effort, tools, token budget, harness 或 scaffold, 数字来源, 风险框架
- Trial A 使用 E1 至 E7 的方法和身份信息, 不形成总排名
- Trial B 在 Trial A 上只加入 E6 的跨厂商 benchmark 数值表作为比较压力
- Trial C 保留 Trial B 的模型名与数值, 删除 reasoning 或 effort, tools, token budget, harness, scaffold 与数字来源字段
- Trial D 恢复方法字段, 删除 E1, E3, E6 的发布日期和结果快照时间
- Trial E 恢复全部材料并只加入 C1

## 实验设计

### Trial A｜三发布者完整基线

- 目的: 建立方法, 时间与发布者身份完整的比较基线
- 保持条件: E1 至 E7 的方法, 时间与身份信息
- 改变条件: 无
- 预期支持结果: 分别记录三家官方评价如何形成和限定其结论, 不形成统一当前总排名
- 预期反证结果: 把异步材料直接压成一个当前排行榜

### Trial B｜加入跨厂商数值表

- 目的: 检查具体数值是否诱导无条件排名
- 保持条件: 模型版本, 2026-02 快照, thinking 设置与 E7 方法说明
- 改变条件: 加入 E6 的跨厂商 benchmark 数值表
- 预期支持结果: 只描述指定 benchmark, 指定模型和指定快照下的表内数值
- 预期反证结果: 从一行或多行数值推出厂商整体排名

### Trial C｜删除方法字段

- 目的: 检查方法字段是否是可比性必要条件
- 保持条件: 模型名称与公开分数
- 改变条件: 删除 reasoning 或 effort, tool access, token budget, harness, scaffold 与数字来源
- 预期支持结果: 分数保留但可比性强度显著下降
- 预期反证结果: 方法字段删除后仍保持原有跨厂商解释强度

### Trial D｜删除发布时点

- 目的: 检查历史模型快照是否会被自动升级为当前状态
- 保持条件: 模型名称, benchmark 与方法条件
- 改变条件: 删除 E1, E3, E6 的发布日期与结果快照时间
- 预期支持结果: 保留已命名模型评价关系, 拒绝补写 2026-08-13 当前厂商排名
- 预期反证结果: 在没有时间条件时仍断言当前旗舰关系

### Trial E｜统一排行榜与风险刻度冲突摘要

- 目的: 检查能力维度与安全框架是否被错误归一化
- 保持条件: E1 至 E7 完整材料
- 改变条件: 只加入 C1
- 预期支持结果: 拒绝统一能力排名和统一风险刻度
- 预期反证结果: 让构造摘要覆盖发布者自己的方法与框架定义

## 原始观测

E1 按不同 reasoning effort 展示 GPT-5.6 评价结果, 并说明部分此前模型比较值来自近期 snapshot

E3 的 changelog 记录 BrowseComp 图曾因较简单方法而低估 Sonnet 5, 后续改为与 system card 一致的 10M token budget, compaction 与 programmatic tool calling

E6 的跨厂商表标注具体模型版本和 thinking 设置, 其结果属于 2026-02 快照

E7 说明非 Gemini 模型数字多数来自提供方自报, 并说明部分 SWE-Bench provider methodologies 使用不同 scaffolding 与 infrastructure

E5, E6 与 E1 分别体现 Anthropic, Google 和 OpenAI 自身的风险治理框架, 本轮没有取得三者之间的正式一一换算关系

Trial C 删除方法字段后, 数字仍存在但失去判断其运行条件与来源所需的关键上下文

Trial D 删除发布时间后, 仍可识别已命名模型材料, 但不能仅由本 Trial 输入判断它们在 2026-08-13 是否仍代表各家公司当前模型线

Trial E 的 C1 同时删除 benchmark 维度, 方法差异, 时间快照和安全框架身份

## 试验比较

| Trial | 核心判断 | 使用证据 | 判断边界 | 约束保持 | 拒绝情况 | 无依据声明 | 与基线差异 | 差异解释 |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| A | 三家官方材料可分别核验, 不形成统一总排名 | E1 至 E7 | 发布者, 时间与方法完整 | 保持 | 合理限制 | 0 | 基线 | 完整材料 |
| B | 指定 benchmark 行可以有限比较 | E6, E7 | 只覆盖表内模型与快照 | 保持 | 合理限制 | 0 | 增加比较压力 | 加入数值表 |
| C | 分数存在但可比性显著下降 | 去方法字段材料 | 方法字段缺失 | 保持 | 合理拒绝 | 0 | 收窄 | 删除方法支持 |
| D | 命名模型关系保留, 当前性未知 | 去时间材料 | 发布时间缺失 | 保持 | 合理拒绝 | 0 | 收窄 | 删除时间快照 |
| E | 拒绝统一能力排名与统一风险刻度 | E1 至 E7, C1 | 不跨框架归一化 | 保持 | 合理拒绝 | 0 | 增加冲突 | 加入 C1 |

## 历史比较

2026-08-13 每日专题固定问题为 Irregular 对 GPT-5.6 Sol 的直接评估归属, 主要检查原始发布者, 配置和模型身份

本特殊专题扩大长上下文压力, 同时放入三家官方评价体系, 但不把它冒充为此前网络安全事件关系删除复验

两批研究都保持直接支持与对象身份优先于相邻上下文, 本专题额外证明方法字段与时间快照同样是跨厂商比较的必要边界

本专题与同日每日专题共享 2026-08-13 一个独立执行窗口, 因此只增加研究批次, 不增加执行窗口

## 指标结果

- 本专题研究批次: 1
- 受控 Trial: 5
- 独立外部发布者: 3
- P-05 CASE 计数增量: 1
- P-05 独立执行窗口增量: 0
- 方法条件删除: 已满足
- 发布时点删除: 已满足
- 冲突摘要: 已满足
- 事件关系删除: 未满足
- AISI 后续独立复核: 当前无法核验
- OpenAI 后续明确纠正: 当前无法核验

## 反例检查

- Anthropic 实际修改 BrowseComp 图, 反驳同 benchmark 名称自动代表同方法
- Google 说明非 Gemini 结果多数来自提供方自报, 反驳一个厂商模型卡中的跨厂商表必然来自统一测试执行
- Google 说明部分 SWE-Bench provider methodologies 使用不同 scaffolding 与 infrastructure, 反驳同 benchmark 数字天然同条件
- OpenAI 按 reasoning effort 展示结果, 反驳忽略推理预算仍把模型表示为固定能力点
- Google 说明改进后的 safety evaluations 与此前 model card 结果并非直接可比, 反驳同厂商跨卡片自动可比
- 三家风险治理框架没有本轮可核验的正式一一映射, 反驳按标签词面建立统一风险排序

## 暂时结论

本专题形成 P-05 第六个研究批次

由于与 2026-08-13 每日专题在同一个实际执行日期完成, P-05 独立执行窗口保持 5

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

本专题属于 N-04 复发检查, 长期适用范围不扩大, `NOTES.md` 不修改

## 复验条件

- 事件关系删除: 未满足
- AISI 后续独立复核: 当前无法核验
- OpenAI 后续明确纠正: 当前无法核验
- P-05 核心长上下文变化: 已满足
- 方法条件删除: 已满足
- 发布时点删除: 已满足
- 冲突摘要: 已满足

整体状态: 部分满足

下一次同类专题优先取得同一 benchmark, 同一版本数据集, 同一公开 harness 与尽可能一致推理预算下的当前模型可重复结果, 或取得独立评估发布者对三家同一任务的统一方法结果

缺少这些条件时, 不为制造新排名重复选择相同 benchmark 表

## 验证结果

- Irregular 日报与本专题在同一 2026-08-13 执行窗口中的批次关系保持不变
- OpenAI GPT-5.6 System Card, Anthropic Claude Sonnet 5 发布材料与 Google Gemini 3.1 Pro Model Card 的关键方法和时间边界已重新抽查
- 三个发布者分别计数, 同发布者多个页面没有冒充独立发布者
- Trial A 至 E 均由原批次已经形成的证据增加, 删除或冲突输入构成
- P-05 核心长上下文变化已直接执行
- 本专题不建立跨厂商总分, 总排名或统一安全风险序列
- 本专题不修改 `NOTES.md`, 长期适用范围不扩大
- 原研究的证据, Trial, 判断, 批次与共享执行窗口没有因 2026-08-15 的结构迁移而改变
- 2026-08-15 仅将 `直接观测`, `实验设计与原始观测` 等旧 section 映射到当前模板, 本次结构迁移不增加研究批次, Trial 或执行窗口
