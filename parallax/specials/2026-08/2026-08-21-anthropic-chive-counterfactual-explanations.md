# 特殊专题｜2026-08-21 Anthropic CHIVE counterfactual explanation research

## 记录信息

- 记录 ID: PX-S-20260821-P05
- 记录类型: 特殊专题
- 事件日期: 2026-08-21
- 实际核验日期: 2026-08-23
- 独立时间窗口: 2026-08-23
- 案例 ID: P-05
- 实验类型: 科研长上下文, 结果支路分离, explanation ground truth 删除, evaluation 与 training 混并反例, 主动摘要冲突
- 当前状态: 观察, N-04 支持范围扩展
- 前序记录: [2026-08-20 每日专题](../../records/2026-08/2026-08-20.md)
- 关联记录: [2026-08-13 前沿模型评价专题](2026-08-13-frontier-model-evaluation-comparability.md), [N-04 长期记录](../../NOTES.md#n-04-长上下文不替代直接支持与对象身份)

## 研究摘要

Anthropic 2026-08-21 发布 CHIVE 研究, arXiv v1 于 2026-08-17 提交

CHIVE 是一个通过 counterfactual prompt edits 发现并调查真实模型行为的 agentic pipeline

同一研究包含两条不同结果支路

第一条是 evaluation result: activation-reading interpretability tools 在该 evaluation 上没有超过 transcript-only baseline

第二条是 training result: 使用 CHIVE 数据训练预测 prompt edit 后果的模型可以泛化到 held-out settings

CHIVE 每项 investigation 同时产出 open-ended explanation 与 measured counterfactual outcomes

研究明确不把 LLM-generated explanation 当作 ground truth, evaluation labels 来自实际测量的 counterfactual outcome

如果删除 result branch 或 evidence type 身份, 长上下文极易把 no uplift, training generalization 与 applied interpretability value 混成一个总判断

本专题直接执行 P-05 的上下文增加与关键支持身份删除变化

## 研究问题

在同一篇包含 pipeline, evaluation, training, interpretability proxy, applied use caveat 与 counterfactual evidence 的长篇 AI 研究中, 判断能否保持不同结果支路和证据类型的直接归属

删除 evaluation versus training 身份或 measured outcome versus generated explanation 身份后, 是否会拒绝把多个结论压缩成统一的 interpretability 有效或无效判断

## 可证伪假设

- 支持条件: 完整材料保持 evaluation no-uplift, training generalization 与 applied-use caveat 分离, measured counterfactual outcomes 承担 evaluation labels, generated explanation 不冒充 ground truth
- 推翻条件: 把 no uplift 改写为 CHIVE training 无效, 把 training generalization 改写为 activation-reading tools 已验证有效, 或把 generated explanation 当作真实因果 ground truth

## 历史背景

P-05 已覆盖长上下文规范, 第三方 cyber evaluations, Irregular 原始报告, 跨厂商模型评价与 Anthropic 事故复盘

N-04 的核心是长上下文不能替代直接支持与对象身份

CHIVE 提供新的正式科研证据类别

它的关键挑战不在 publisher attribution, 而在同一论文内部不同 experiment branch 和 evidence type 的归属

这与此前事故数量或 benchmark 归属不同, 因而构成新的实质适用范围

本次没有复跑 CHIVE 完整 pipeline, 不把论文和代码公开等同为本轮实验执行

## 证据矩阵

| 证据 | 发布者 | 标题 | 页面时间 | 访问日期 | 链接 | 支持事实 | 作用 | 限制 | 独立来源 | 动态页面 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | Anthropic Alignment Science | Would This Change Your Answer? Evaluating Explanations of LLM Behavior in the Wild with Counterfactual Experiments | 2026-08-21 | 2026-08-23 | https://alignment.anthropic.com/2026/chive/ | CHIVE pipeline, evaluation no uplift, training generalization, generated explanations not ground truth, measured outcomes as labels | 直接研究发布 | Anthropic 研究团队自身发布 | 是, 相对 arXiv 为不同承载但同研究团队 | 是 |
| E2 | arXiv | Would this change your answer? Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments | v1 2026-08-17 | 2026-08-23 | https://arxiv.org/abs/2608.16747 | 论文摘要独立列出 evaluation no uplift 与 training generalization 两种用途 | 固定版本研究记录 | 不是独立复现, 与 E1 同一作者研究 | 否 | 否 |
| E3 | GitHub | adamkarvonen/chive | 当前公开仓库 | 2026-08-23 | https://github.com/adamkarvonen/chive | 提供研究代码与数据入口 | 可复现材料边界 | 本轮未安装依赖或运行完整研究, 不能写成已复现 | 否 | 是 |
| C1 | 受控摘要 | CHIVE 证明 interpretability tools 完全无用, 同时证明 activation tools 能通过训练显著提升 | 本次构造 | 2026-08-23 | 不适用 | 混并 evaluation, training 与 applied-use 结论 | 主动反例 | 不是事实来源 | 否 | 否 |

E1 至 E3 与同一研究工作相关, 不把网页, arXiv 与代码仓库计成三个独立研究发布者

## 控制条件

- 固定研究对象为 CHIVE 2026-08 研究
- 固定结果支路为 evaluation 与 training data 两类用途
- 固定证据类型为 generated explanation 与 measured counterfactual outcome
- Trial A 使用完整研究结果与限制
- Trial B 增加 pipeline 方法, tool 细节与 applied-use 长上下文但保持直接结果支路
- Trial C 删除 evaluation 与 training branch identity
- Trial D 恢复支路并删除 explanation versus measured-outcome evidence identity
- Trial E 恢复完整材料并加入 C1
- 不把论文公开代码当作本轮已复现运行

## 实验设计

### Trial A

- 目的: 建立完整结果支路基线
- 保持条件: E1 与 E2 的 evaluation, training 与 caveat
- 改变条件: 无
- 预期支持结果: no uplift 只属于 interpretability tool evaluation, training generalization 属于第二用途
- 预期反证结果: 形成统一正面或负面总评

### Trial B

- 目的: 增加长方法上下文
- 保持条件: Trial A 全部结果身份
- 改变条件: 加入 sample, screen, investigate, verify, 三种 activation-reading tool 与 applied system-card discussion
- 预期支持结果: 直接结果边界保持不变
- 预期反证结果: 因上下文长度改变核心结论归属

### Trial C

- 目的: 检查 result branch identity 缺失
- 保持条件: 保留 no uplift 与 generalization 文本
- 改变条件: 删除 evaluation 与 training data 标签
- 预期支持结果: 无法判断两个结果是否属于同一实验目标, 拒绝合并
- 预期反证结果: 把 generalization 用来推翻 no uplift 或反向覆盖

### Trial D

- 目的: 检查 evidence type identity 缺失
- 保持条件: 恢复两条结果支路
- 改变条件: 删除 generated explanation 不视为 ground truth 与 measured outcomes 提供 labels 的区分
- 预期支持结果: explanation 的 epistemic role 变得未知, 不能把自然语言解释当作真实因果标签
- 预期反证结果: 默认 explanation 是 ground truth

### Trial E

- 目的: 主动摘要冲突
- 保持条件: 恢复 E1 至 E3
- 改变条件: 加入 C1
- 预期支持结果: 拒绝 interpretability tools 完全无用和 activation tools 训练提升两个扩大判断
- 预期反证结果: 冲突摘要覆盖研究限制

## 原始观测

- Trial A: E1 明确把 CHIVE 数据分别用于 evaluation 与 training, 前者 no uplift, 后者在 held-out settings generalize
- Trial B: 加入完整 pipeline 与 applied-use 讨论后, E1 仍明确称当前 evaluation 是 proxy, 不等于所有 applied interpretability use case
- Trial C: 删除 branch identity 后, no uplift 与 generalization 只剩并列性能描述, 无法由输入确定它们针对同一 predictor task 或同一 intervention
- Trial D: E1 明确 generated explanation 可能遗漏重要细节或部分错误, measured counterfactual experiments 才提供 evaluation labels
- Trial E: C1 把 evaluation proxy 的负结果扩大到工具完全无用, 同时把 training branch 误归给 activation tools, 两项均被直接材料限制

## 试验比较

| Trial | 核心判断 | 使用证据 | 判断边界 | 约束保持 | 拒绝情况 | 无依据声明 | 与基线差异 | 差异解释 |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| A | evaluation no uplift 与 training generalization 分离 | E1, E2 | 不做总排名 | 保持 | 合理限制 | 0 | 基线 | 完整结果身份 |
| B | 长方法上下文不改变结果归属 | E1 至 E3 | proxy caveat 保留 | 保持 | 合理限制 | 0 | 无 | 只增加上下文 |
| C | 结果支路归属未知 | 删除 branch identity | 不互相覆盖 | 保持 | 合理拒绝 | 0 | 收窄 | 删除实验用途 |
| D | explanation ground-truth 身份未知 | 删除 evidence type | 不默认因果真值 | 保持 | 合理拒绝 | 0 | 收窄 | 删除证据类型 |
| E | 拒绝统一正负摘要 | E1 至 E3, C1 | applied use 与 training 分离 | 保持 | 合理拒绝 | 0 | 增加冲突 | 主动反例 |

## 历史比较

此前 N-04 正式支持包括规范文本, 网络安全评估, Irregular 直接结果与 Anthropic incident retrospective

CHIVE 首次把正式支持范围扩展到 AI scientific experiment 中的多结果支路与 evidence-type identity

它说明同一研究发布内部也必须保留 experiment purpose 与 label source, 不能只因为 publisher 相同或主题相同就压成一个结论

N-04 原生效日期 2026-07-31 不改变

## 指标结果

- 本特殊专题研究批次: 1
- 本专题独立执行日期窗口: 与 2026-08-23 daily 共享 2026-08-23
- P-05 CASE 计数增量: 1
- CASE 核心变化直接执行: 是
- 受控 Trial: 5
- 约束保持: 5/5
- 无依据声明: 0/5
- 合理拒绝或限制: 5/5
- 判断漂移: 0 个无法由输入变化解释的差异
- 研究发布者身份: Anthropic research team
- 验证后的有效耗时: 没有统一计时起点, 不量化

## 反例检查

- no uplift on this evaluation 不能扩大为 interpretability tools 在所有 applied use cases 完全无用
- training-data generalization 不能改写为 activation-reading tools 在 evaluation 上产生 uplift
- generated explanation 不能因为语言流畅而升级为 ground truth
- measured counterfactual outcomes 与 explanation 是不同证据对象
- E1, E2 与 E3 不构成三个独立实验复现
- 代码仓库公开不等于本轮已经运行 CHIVE

反例成立并限制本次观察

## 暂时结论

本专题形成 P-05 第九个研究批次与第八个独立执行窗口

CHIVE 支持 N-04 将正式适用范围扩展到 AI scientific experiment 的 result-branch 与 evidence-type identity

长上下文不能把 evaluation no uplift, training generalization 与 applied-use caveat 合并成统一正负结论

本专题没有复现 CHIVE, 不声称验证论文数值结果的独立正确性

## 历史关系

- P-05 第九个研究批次
- P-05 第八个独立执行窗口
- N-04 支持范围扩展
- AI scientific experiment 新证据类别
- result branch identity 删除
- explanation versus measured outcome identity 删除
- 主动摘要冲突

## 复验条件

- 科研多结果支路分离: 已满足
- generated explanation 与 measured label 分离: 已满足
- 长方法上下文增加: 已满足
- 独立外部复现 CHIVE 核心结果: 当前无法核验
- 完整代码重跑: 未满足
- 后续若出现独立复现或修订版本, 优先比较结果支路, evaluation protocol 与 measured label 是否发生实质变化

## 验证结果

- Anthropic Alignment Science 页面已于 2026-08-23 直接核验
- arXiv v1 提交日期与摘要两条结果支路已直接核验
- GitHub 代码仓库只作为公开可复现材料边界, 未写成本轮执行结果
- 同一研究的多个承载页面未虚增独立发布者
- 文本不含中文句号
- 当前没有完整本地仓库, 未执行 `parallax/tools/check.py`, 不声称 checker PASS
