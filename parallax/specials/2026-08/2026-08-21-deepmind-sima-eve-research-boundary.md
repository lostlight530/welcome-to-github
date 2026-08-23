# 特殊专题｜2026-08-21 DeepMind SIMA 与 EVE research lifecycle boundary

## 记录信息

- 记录 ID: PX-S-20260821-P03
- 记录类型: 特殊专题
- 事件日期: 2026-08-21
- 实际核验日期: 2026-08-23
- 独立时间窗口: 2026-08-23
- 案例 ID: P-03
- 实验类型: AI agent 产品阶段, offline sandbox 删除, product identity 删除, future modal 删除, live deployment 冲突摘要
- 当前状态: 观察, P-03 AI agent lifecycle 复验
- 前序记录: [2026-08-23 每日专题](../../records/2026-08/2026-08-23.md)
- 关联记录: [P-03 控制案例](../../CASES.md#p-03-关键缺失), [2026-08-21 Anthropic CHIVE 专题](2026-08-21-anthropic-chive-counterfactual-explanations.md)

## 研究摘要

Google DeepMind 2026-08-21 发布其与 Fenris Creations 在 EVE Universe 中推进 AI research 的说明

SIMA 是一个通过屏幕观察, 语言指令与普通键鼠行动的 generalist agent, 不要求游戏 API 或源码访问

当前公开材料同时存在三个不同阶段与对象

Aura Guidance 已经为真实玩家提供价值, 但它使用 Gemini 提供 player-generated knowledge, 不能自动等同为 SIMA agent live deployment

长期研究计划从 EVE Online 的 offline instance 开始, 该环境被明确描述为与 live players 分离的 safe sandbox

后续研究再进入 EVE Frontier

只有在 capabilities mature 时, DeepMind 才表示 would consider 将相关能力带入 EVE Online 与 EVE Vanguard

Fenris Creations 2026-05-06 的独立官方说明也明确 Google DeepMind 会在 local server 上使用 offline EVE Online 版本测试与评估模型

因此删除 offline, product identity 或 future-modal 条件都会显著改变可支持的 deployment 判断

## 研究问题

当同一合作叙述同时包含 current player feature, offline research sandbox, future research environment 与 conditional live deployment roadmap 时, 判断能否保持对象身份和生命周期阶段

删除 offline, separate from live players, Aura Guidance product identity 或 would consider 等关键条件后, 是否会拒绝把研究计划升级为 SIMA 已经在 live EVE Online 自主运行

## 可证伪假设

- 支持条件: Aura Guidance, offline EVE research, EVE Frontier research 与未来 conditional live deployment 分开记录, 删除阶段或对象身份后部署判断收窄
- 推翻条件: 把 Aura Guidance 改写成 SIMA live agent, 把 offline EVE 测试改写成 live-player autonomous deployment, 或把 would consider 改写成已经实施

## 历史背景

P-03 研究关键条件缺失时是否拒绝补全

2026-08-23 daily 已把 P-03 扩展到 Astra capability confidence 与 model lifecycle

本专题进一步使用独立发布体系中的 generalist game agent 与 live-service research partnership

Google DeepMind 与 Fenris Creations 对同一合作分别提供研究方与游戏运营方的一手材料

这使 offline environment 与 live environment 的边界具有跨发布者直接支持

本专题不登录 EVE, 不运行 SIMA, 不验证任何未公开 prototype

## 证据矩阵

| 证据 | 发布者 | 标题 | 页面时间 | 访问日期 | 链接 | 支持事实 | 作用 | 限制 | 独立来源 | 动态页面 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | Google DeepMind | From Atari to EVE Online: Building on 15 Years of AI Research in Games | 2026-08-21 | 2026-08-23 | https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games/ | SIMA agent 交互方式, Aura Guidance 当前价值, offline EVE safe sandbox, EVE Frontier 阶段, mature 后才 consider EVE Online/Vanguard | 研究方主证据 | 合作说明不是本轮 runtime observation | 是 | 是 |
| E2 | Fenris Creations | Studio Behind EVE Online Goes Independent, Rebrands as Fenris Creations, Enters Research Partnership with Google DeepMind | 2026-05-06 | 2026-08-23 | https://fenris.com/news/2026/studio-behind-eve-online-goes-independent-rebrands-as-fenris-creations-enters-research-partnership-with-google-deepmind | Google DeepMind 使用 local server 上的 offline EVE Online 版本测试和评估模型 | 游戏运营方独立确认 | 较早合作说明不覆盖 8 月后续全部 roadmap | 是 | 是 |
| E3 | Fenris Creations | Former Icelandic minister joins Fenris Creations to lead new AI partnerships | 2026-08-07 | 2026-08-23 | https://fenris.com/news/2026/former-icelandic-minister-aslaug-arna-sigurbjoernsdottir-joins-fenris-creations-to-lead-new-ai-partnerships | EVE Frontier AI research initiative 与 DeepMind collaboration active | 当前合作背景 | autonomous systems in EVE Frontier initiative 不等于 SIMA 已在 EVE Online live deployment | 否, 与 E2 同发布者 | 是 |
| C1 | 受控摘要 | SIMA 2 已经作为 autonomous agent 在 live EVE Online 与真实玩家共同运行 | 本次构造 | 2026-08-23 | 不适用 | 删除 product, environment 与 future conditional 边界 | 主动反例 | 不是事实来源 | 否 | 否 |

E1 与 Fenris Creations 构成两个独立发布者

E2 与 E3 同属 Fenris Creations, 不重复计数

## 控制条件

- 固定合作对象为 Google DeepMind 与 Fenris Creations 的 EVE Universe AI research partnership
- 固定四类身份为 Aura Guidance, SIMA research agent, offline EVE Online sandbox, future EVE Online or Vanguard consideration
- Trial A 使用 E1 至 E3 完整阶段基线
- Trial B 删除 offline 与 separate from live players 条件
- Trial C 恢复环境边界并删除 Aura Guidance 与 SIMA 的产品身份差异
- Trial D 恢复对象身份并删除 only when mature 与 would consider 的 future-modal 条件
- Trial E 恢复完整材料并加入 C1
- 不把 research partnership, prototype 或 game environment study 写成 production deployment result

## 实验设计

### Trial A

- 目的: 建立完整 lifecycle 与 product identity 基线
- 保持条件: E1 至 E3 全部阶段字段
- 改变条件: 无
- 预期支持结果: 当前玩家功能, offline research 与未来考虑分离
- 预期反证结果: SIMA live deployment

### Trial B

- 目的: 直接执行 P-03 offline environment 删除
- 保持条件: EVE Online, SIMA research partnership 与测试语义
- 改变条件: 删除 offline, local server, safe sandbox 与 separate from live players
- 预期支持结果: 无法从剩余材料确定是否触达 live players
- 预期反证结果: 默认研究发生在生产世界

### Trial C

- 目的: 检查 product identity 缺失
- 保持条件: 恢复 offline research 与未来 roadmap
- 改变条件: 删除 Aura Guidance 与 SIMA 名称和功能差异
- 预期支持结果: 当前玩家功能的 agent identity 变为未知
- 预期反证结果: 因 Aura Guidance 已上线而推断 SIMA 已上线

### Trial D

- 目的: 检查 future-modal 缺失
- 保持条件: 恢复产品和环境身份
- 改变条件: 删除 only when capabilities are mature, would consider 等条件
- 预期支持结果: 未来 live deployment 仍不能由当前材料确认
- 预期反证结果: 把 conditional roadmap 改写为 current deployment

### Trial E

- 目的: 主动 live deployment 反例
- 保持条件: 恢复 E1 至 E3
- 改变条件: 加入 C1
- 预期支持结果: 由 offline, product identity 与 future modal 三组直接材料拒绝 C1
- 预期反证结果: 冲突摘要覆盖一手阶段说明

## 原始观测

- Trial A: E1 明确区分 Aura Guidance current player value, offline EVE Online research, EVE Frontier progression 与 future conditional EVE Online or Vanguard consideration
- Trial B: 删除 offline 与 live-player separation 后, 研究环境的 production exposure 无法从剩余输入确定
- Trial C: 删除 Aura Guidance 与 SIMA identity 后, 当前已有功能和 research agent 的关系无法可靠归属
- Trial D: 删除 future modal 后只剩产品名称与目标, 不能由输入证明 live deployment 已经发生
- Trial E: E2 独立确认 offline local-server EVE test, E1 又明确 separate from live players, 共同反驳 C1

## 试验比较

| Trial | 核心判断 | 使用证据 | 判断边界 | 约束保持 | 拒绝情况 | 无依据声明 | 与基线差异 | 差异解释 |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| A | current feature, offline research 与 future live consideration 分离 | E1 至 E3 | 不补 SIMA live deployment | 保持 | 合理限制 | 0 | 基线 | 完整阶段身份 |
| B | live exposure 未知 | 删除 offline 条件 | 不默认 production | 保持 | 合理拒绝 | 0 | 收窄 | 删除环境身份 |
| C | 当前玩家功能 agent identity 未知 | 删除 product identity | 不合并 Aura 与 SIMA | 保持 | 合理拒绝 | 0 | 收窄 | 删除对象身份 |
| D | future deployment 未确认 | 删除 future modal | 不把 roadmap 当现状 | 保持 | 合理拒绝 | 0 | 收窄 | 删除条件语气 |
| E | 拒绝 SIMA 已在 live EVE 自主运行 | E1 至 E3, C1 | 直接阶段证据优先 | 保持 | 合理拒绝 | 0 | 增加冲突 | 主动反例 |

## 历史比较

本专题与当日 Astra daily 都执行 P-03 关键条件删除

Astra 删除的是 capability confidence 与 model lifecycle

本专题删除的是 environment stage, product identity 与 future modal

两者在同一 2026-08-23 实际执行日期完成, 因而构成两个实质不同研究批次但共享 P-03 的同一新实际执行窗口

本专题不属于 N-02 的 coverage denominator 正式支持范围, 因而不修改 N-02

## 指标结果

- 本特殊专题研究批次: 1
- 本专题独立执行日期窗口: 与 2026-08-23 daily 共享 2026-08-23
- P-03 CASE 计数增量: 1
- CASE 核心变化直接执行: 是
- 受控 Trial: 5
- 独立发布者: 2 个, Google DeepMind 与 Fenris Creations
- 约束保持: 5/5
- 无依据声明: 0/5
- 合理拒绝或限制: 5/5
- 判断漂移: 0 个无法由输入变化解释的差异
- 验证后的有效耗时: 没有统一计时起点, 不量化

## 反例检查

- research partnership 不等于 production deployment
- offline EVE Online local-server instance 不等于 live EVE Online
- separate from live players 直接限制 live-player exposure
- Aura Guidance 使用 Gemini 提供 player-generated knowledge, 不能仅凭同一合作页面改写为 SIMA live agent
- EVE Frontier research initiative 不等于 SIMA 已在 EVE Online 当前运行
- would consider when mature 不能改写成已经部署
- DeepMind 与 Fenris 的两个发布者都支持 offline research boundary

反例成立并限制本次观察

## 暂时结论

本专题形成 P-03 第十五个研究批次

P-03 独立执行窗口仍为第十三个, 因为当日 daily 与本专题共享 2026-08-23

Google DeepMind 与 Fenris Creations 的当前公开材料支持真实合作和分阶段 AI research, 但不支持 SIMA 2 已经在 live EVE Online 与真实玩家共同自主运行

本专题不改变 N-02 正式适用范围

## 历史关系

- P-03 第十五个研究批次
- P-03 第十三个独立执行窗口
- AI agent lifecycle 新对象
- offline environment 删除
- product identity 删除
- future modal 删除
- 跨发布者 live deployment 反例

## 复验条件

- offline versus live environment 分离: 已满足
- current feature versus research agent identity 分离: 已满足
- conditional future deployment 分离: 已满足
- 两个独立发布者的 offline boundary: 已满足
- SIMA 在 live EVE Online 的未来 deployment status: 当前无法核验为已发生
- 后续只有在 Fenris 或 DeepMind 发布明确 live deployment, runtime evaluation 或产品化说明时再开启新窗口复验

## 验证结果

- Google DeepMind 2026-08-21 官方研究页已于 2026-08-23 直接核验
- Fenris Creations 2026-05-06 与 2026-08-07 官方页面已直接核验
- DeepMind 与 Fenris 独立发布者身份保持分离, Fenris 自身多页面不重复计数
- Aura Guidance, SIMA, offline EVE, EVE Frontier 与 future live deployment 未混并
- 文本不含中文句号
- 当前没有完整本地仓库, 未执行 `parallax/tools/check.py`, 不声称 checker PASS
