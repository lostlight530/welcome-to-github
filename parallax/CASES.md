# 控制案例

## P-01 重复观察

- 输入: 同一组固定证据与同一问题
- 变化: 在不同时间重新执行
- 检查: 事实, 证据等级, 判断边界与置信度是否无理由变化
- 最近实际执行日期: 2026-08-16
- 累计研究批次: 5
- 独立执行窗口: 5
- 已覆盖实验类型: 跨时重复判断, 来源顺序交换, 关键证据缺失, 误导摘要位置交换, 冻结证据包, 可重复文本检查, 冲突访问状态, 当前访问恢复, 检查器行为测试, 结构错误注入, 语义反例, 外部框架测试契约, 文档删除, 测试删除, 冲突摘要, 主动反例
- 当前状态: 发现
- 已知反例: 官方文档可能落后于实现, 技术文档与维护规则不能证明稳定运行, 文本标记命中不能证明框架行为, 检查器通过不能证明事实正确, 追踪可以禁用且可能含敏感数据, 并行护栏失败前运行可能已经开始, 新会话具有输入与终态约束, 同一官网在不同客户端可以同时返回 HTTP 200 与 418, 官方测试源码契约不能替代本轮未执行的测试结果, 阻塞护栏测试不能推广为并行模式
- 下一复验条件: 在新的执行窗口安全运行固定版本的 OpenAI Agents SDK input guardrail 最小复现或官方可重放测试, 取得实际运行结果后构造与文档冲突, 分别删除运行结果与文档正文, 另行复验合法结构中的语义冲突
- 关联记录: [2026-07-20 历史批次](records/2026-07.md#2026-07-20), [2026-08-01 每日专题](records/2026-08/2026-08-01.md), [2026-08-02 每日专题](records/2026-08/2026-08-02.md), [2026-08-03 每日专题](records/2026-08/2026-08-03.md), [2026-08-16 每日专题](records/2026-08/2026-08-16.md)

## P-02 冲突来源

- 输入: 两个结论冲突且证据强度不同的来源
- 变化: 调换来源顺序
- 检查: 结论是否由证据强度决定, 而不是由出现顺序决定
- 最近实际执行日期: 2026-08-08
- 累计研究批次: 7
- 独立执行窗口: 7
- 已覆盖实验类型: 顺序交换, 关键条件缺失, 误导摘要, 实时证据更新, 404 反例, 跨发布者冲突, 隐藏评价字段, 非 GitHub API, HTTP 400, HTTP 401, HTTP 503, HTTP 429, 响应正文有无对照, 缺失认证, 无效凭据, 同状态异因反例, 请求路径有无对照, 受控状态生成, 空正文, 误导认证与额度摘要, 误导过载与恢复摘要, 真实生产 API 契约, Retry-After 有无对照, 限流范围
- 当前状态: 发现
- 已知反例: 仅有 HTTP 400, 401, 429 或 503 不能识别当前具体原因, 请求条件与正式文档可以证明违反公开契约或识别测试端点, 响应正文可以进一步识别本次原因, OpenAI 同一端点的缺失 Bearer 与无效 Bearer 均返回 401 但正文诊断不同, httpbin 状态端点可以按请求路径生成 503, RFC 9110 同时允许临时过载与计划维护, 空正文不能补出故障原因或恢复时间, RFC 6585 不定义用户识别和请求计数方式, Cloudflare 同时存在令牌, IP, GraphQL 与端点级限制, 正式 retry-after 规则不能替代本轮未取得的实际响应值
- 下一复验条件: 在新的日期窗口安全取得真实生产 429 响应样本并核对请求对象, 响应正文, Ratelimit, Ratelimit-Policy 与 Retry-After 实值, 或改用具有正式事件说明或明确重试字段的生产 503
- 关联记录: [2026-07-21](records/2026-07/2026-07-21.md), [2026-07-23](records/2026-07/2026-07-23.md), [2026-07-24](records/2026-07/2026-07-24.md), [2026-08-04](records/2026-08/2026-08-04.md), [2026-08-05](records/2026-08/2026-08-05.md), [2026-08-07](records/2026-08/2026-08-07.md), [2026-08-08](records/2026-08/2026-08-08.md)

## P-03 关键缺失

- 输入: 移除形成结论所需的关键条件
- 变化: 保留足以诱导猜测的背景信息
- 检查: 是否明确记录未知并拒绝补全
- 最近实际执行日期: 2026-08-23
- 累计研究批次: 15
- 独立执行窗口: 13
- 已覆盖实验类型: 历史证据缺失, 范围核验, 请求分母缺失, 维护提示核验, 发布者身份核对, 当前浏览复验, 时间条件缺失, 对象边界反例, 顺序交换, 误导摘要, 测试误发反例, 多事件身份隔离, 相似标题合并反例, 当前状态反例, 结构化字段与正文粒度冲突, 更新逆序, 事件身份缺失, 计划范围缺失, 产品范围缺失, 用户量词缺失, 全称摘要, 全日范围反例, impact 字段定义, impact 与正文冲突, 关键定义缺失, 公开失败率, 近似失败请求数, 比例删除, 计数删除, 对象身份删除, 精确分母冲突摘要, 直接请求总分母, 分母删除, 阶段身份删除, 冲突摘要, 第二发布者复验, 分母身份删除, 聚合对象冲突, 数值请求总分母, 请求级比例, source 级反例, 统计单位删除, 机械反推冲突, 能力阈值限定, preliminary evidence 删除, upcoming 生命周期删除, framework threshold 恢复, AI agent lifecycle, offline environment 删除, product identity 删除, future modal 删除, live deployment 冲突摘要, 主动反例
- 当前状态: 发现
- 已知反例: 远端记录缺失不能证明没有离线工作, 受影响组件与事件对象不能证明全部请求失败, 测试误发事件不能证明客户影响, 社区恢复公告确认论坛重新可用但不能证明普通账户每项写操作已经成功, 社区维护不能证明文档站或 API 不可用, 动态事件列表的部分核验不能证明全日只有已选事件, 相邻日期的相似标题不能证明连续故障, 当前全部 operational 或 resolved 不能否定已解决的历史事件, impact 字段与组件标记不能删除同一事件正文中的部分用户错误, 计划名称不能替代用户或请求分母, 三个同日事件不能证明全部服务或全部用户受影响, 一个事件的 resolved 不能替代另两个事件的 monitoring, Statuspage incident impact 是基于组件状态的严重度字段并允许人工覆盖, OpenAI 同一事件的 impact none 可以与部分 Business 和 Education 用户错误正文并存, impact none 不能替代用户数量或请求分母, 平均错误率与近似失败请求数不能反推官方发布的精确总请求分母, GitHub Pages 请求统计不能扩大为全部 GitHub 流量或用户数量, 直接总分母出现后应允许有边界更新而不是固定拒绝量化, 230 个错误送达请求不能解释为该窗口全部失败请求, 1700 万减 230 不能解释为成功请求数, 删除处理阶段身份后不能跨层级相减得到精确失败量, 四舍五入比例不能替代删除后的直接精确分母, 28% applications 不能替代 28% of all HTTP traffic served by Cloudflare, 相同百分比不能证明两个聚合总体一一对应, Cloudflare 公开比例与总体身份不能补出未公开的精确请求总计数, 400 million requests 与 270000 sources 不能跨单位合并, 3 false-negative sources 不能改写为 3 false-negative requests, 0.003% of requests 不能在缺少直接 numerator 与底层精度时改写为官方精确 12000 个错误请求, OpenAI 对 Astra 的 preliminary evidence 与 cannot rule out 不能改写为 confirmed Critical capability, upcoming model 不能改写为 public deployment, strict safeguards 与 training pause 不能单独证明模型已经公开上线, Aura Guidance 当前玩家功能不能自动归因为 SIMA live agent, offline EVE local-server research 不能改写为 live-player deployment, would consider when mature 不能改写为已经部署
- 下一复验条件: 分母方向中第二个独立发布者, 数值 request 总分母与 request-level 公开比例均已满足, 后续优先寻找同一统计对象与窗口直接同时发布数值 total requests 与 exact failed or successful requests 的独立发布者, AI capability 与 agent lifecycle 方向只在正式 capability report, system card, 独立复测或明确 live deployment state 出现实质变化时继续, 若只有显示比例必须保留公开精度并拒绝把机械反推结果改写为原始精确计数, 普通账户社区回复与点赞仍保留为安全复验路径
- 关联记录: [2026-07-22 每日专题](records/2026-07/2026-07-22.md), [2026-07-25 特殊专题](specials/2026-07/2026-07-25-openai-service-events.md), [2026-07-27 每日专题](records/2026-07/2026-07-27.md), [2026-07-27 社区维护专题](specials/2026-07/2026-07-27-openai-developer-community-maintenance.md), [2026-07-30 近期服务事件专题](specials/2026-07/2026-07-30-openai-recent-service-events.md), [2026-07-31 企业与教育事件专题](specials/2026-07/2026-07-31-openai-enterprise-education-chat-errors.md), [2026-08-04 ChatGPT 对话错误专题](specials/2026-08/2026-08-04-openai-chatgpt-conversation-errors.md), [2026-08-05 三项服务事件专题](specials/2026-08/2026-08-05-openai-service-events.md), [2026-08-09 每日专题](records/2026-08/2026-08-09.md), [2026-08-15 每日专题](records/2026-08/2026-08-15.md), [2026-08-18 每日专题](records/2026-08/2026-08-18.md), [2026-08-19 每日专题](records/2026-08/2026-08-19.md), [2026-08-22 每日专题](records/2026-08/2026-08-22.md), [2026-08-23 每日专题](records/2026-08/2026-08-23.md), [2026-08-21 DeepMind SIMA 与 EVE 专题](specials/2026-08/2026-08-21-deepmind-sima-eve-research-boundary.md)

## P-04 时间替换

- 输入: 旧契约与更新后的官方契约
- 变化: 明确两者生效时间
- 检查: 是否更新当前判断, 同时保留历史原因
- 最近实际执行日期: 2026-08-22
- 最近关联观察日期: 2026-08-10
- 累计研究批次: 9
- 独立执行窗口: 9
- 已覆盖实验类型: 状态更新, 明确纠正, resolved 后 monitoring, 顺序交换, 关键状态缺失, 时间戳缺失, 事件身份缺失, 同日事件隔离, 事件重排, 冲突摘要, 跨事件反例, 跨发布者更新, 初始未知与后续归因, 初步结论边界, 历史纠错, 非状态页契约, deprecated API, deprecated module, removal 边界, 版本生效时间, 时间删除, 对象身份删除, 第三方兼容实现冲突, 模型部署 rollback, full rollback, previous version 恢复, 多阶段替代契约, deprecation pause, deadline removal, 当前文档恢复
- 当前状态: 发现
- 已知反例: 同日事件可以具有不同当前状态, 一个事件的 resolved 不能复制给相邻 monitoring 事件, 通用 resolved 模板不能证明真实事故, 首次 resolved 后仍可能出现 monitoring, 线性恢复事件不能代表所有更新路径, 动态页面快照不能代表后续状态, 后续归因可以更新当前判断但不能把初始未知改写为当时已知, 初步调查结论不能冒充最终报告, 当前动态事件页已经出现 write-up 发布标记时不能冒充真实的 write-up 发布前历史快照, 没有明确旧新契约生效时间时不能把正式事故复盘恢复计为 P-04 核心变化, Kubernetes v1.26 的 v1beta2 迁移目标不能证明 v1beta2 在 v1.29 后仍继续提供, 持久对象可通过新 API 访问不能证明旧 API 版本继续服务, 删除版本时间后不能仅凭迁移文本确定当前较新契约, 删除稳定资源身份后不能把相似 deprecated 说明拼成同一对象链, Python 3.10 的 deprecated 状态不能证明 distutils 在所有历史版本中都已移除, setuptools 第三方兼容提供不能证明 Python 3.12 标准库仍包含 distutils, 删除发布时间锚点后不能补出具体 Python 发布边界, GPT-4o full rollback 不能证明 4 月 25 日更新从未部署, system prompt 临时缓解不能替代 full rollback, previous version 不能补出公开 snapshot ID, 删除 GPT-4o 与 ChatGPT 对象身份后不能把相似 rollback 文本拼成同一部署链, Atlassian 2022-04-20 deadline removal 不能证明此前迁移要求从未存在, 当前 Jira Cloud platform 的 classic scope recommendation 不能扩大为全部 Atlassian 产品禁止 granular scopes
- 下一复验条件: 多阶段 replacement, 新独立发布体系, 稳定对象身份与可排序时间均已满足, 后续不优先重复一般 deprecation, 单次 rollback 或相同 scope 迁移主题, 若继续 P-04 优先寻找明确 superseded 后恢复或真正双向切换且具有当前可验证终态的第四独立发布体系, 缺少高质量对象时返回其他已达到复验条件或近期覆盖不足的 CASE
- 关联记录: [2026-07-26 每日专题](records/2026-07/2026-07-26.md), [2026-07-28 每日专题](records/2026-07/2026-07-28.md), [2026-07-29 每日专题](records/2026-07/2026-07-29.md), [2026-07-21 安全事件专题](specials/2026-07/2026-07-21-openai-hugging-face-security-incident.md), [2026-08-06 每日专题](records/2026-08/2026-08-06.md), [2026-08-10 关联观察, 不计数](records/2026-08/2026-08-10.md), [2026-08-11 每日专题](records/2026-08/2026-08-11.md), [2026-08-12 每日专题](records/2026-08/2026-08-12.md), [2026-08-14 每日专题](records/2026-08/2026-08-14.md), [2026-08-21 每日专题](records/2026-08/2026-08-21.md)

## P-05 上下文干扰

- 输入: 固定问题, 核心约束与大量相关或无关材料
- 变化: 增加噪声, 误导摘要或删除关键支持记录
- 检查: 核心约束, 证据计数与结论门槛是否保持
- 最近实际执行日期: 2026-08-23
- 累计研究批次: 9
- 独立执行窗口: 8
- 已覆盖实验类型: 长上下文干扰, 外部权威长文, 跨发布者复验, 外部行为结果, 单变量删除, 错误摘要位置交换, 冲突表格位置交换, 关键条款缺失, 关键要求缺失, 运行配置缺失, 数量归属缺失, 对象身份缺失, 冲突证据, 主动反例, 原始报告恢复, 多发布者长上下文, 模型归属删除, 三发布者评价材料, 跨厂商 benchmark, 方法字段删除, 时间快照删除, 风险框架冲突摘要, 事件关系删除, 关系恢复, 新发布者直接复盘, 数量层级删除, 非受控比较反例, 科研长上下文, 结果支路分离, result branch identity 删除, explanation ground truth 删除, measured outcome identity, evaluation 与 training 混并反例
- 当前状态: 发现
- 已知反例: 首次输入只来自 Parallax, 第二次只使用一份 RFC 的三个官方表示, 第三次的三个页面均来自 W3C 体系, 同一研究体系的三个批次不能代表不同执行主体或环境, 404 的多义性不能证明具体响应原因, WCAG 阈值不能证明具体页面已经合规, AISI 的 19 项越界动作只有 2 项涉及 GPT-5.6 Sol, 互联网启用与分类器关闭不代表普通部署, 未发现现实损害不等于证明没有风险, Irregular 的 19/197 FrontierCyber 结果不能扩大为全部挑战成功, 7/11 至少一次解题不能与 28% 平均成功率混为同一统计量, capability-elicitation 设置不能代表带部署缓解措施的现实滥用画像, OpenAI System Card 中相邻的 AISI 数量不能并入 Irregular 结果, 同一 benchmark 名称不能证明 token budget, tools, harness, grader 或 scaffold 相同, Anthropic 对 BrowseComp 的方法修正说明公开分数可以随评价方法变化, Google 跨厂商表中的非 Gemini 数字多数来自提供方自报且部分 coding 评价使用不同 scaffold 与 infrastructure, OpenAI reasoning effort 曲线不能压缩为一个固定能力点, 不同厂商安全框架没有本轮可核验的一一换算关系, 相同模型名称与相邻章节不能证明 Irregular 与 UK AISI 属于同一次联合评估, 删除明确合作与归属关系后不能自动补出评估事件关系, Anthropic 141006 次回顾运行不能改写为事故数量, 3 起事故与 6 次相关运行不能互换, isolated incidents 不能升级为受控模型排名, CHIVE evaluation no uplift 不能扩大为所有 applied interpretability tools 完全无用, CHIVE training-data generalization 不能改写为 activation-reading tools 在该 evaluation 上产生 uplift, LLM-generated explanation 不能因为语言流畅而升级为 ground truth, research code 公开不能冒充本轮完整复现
- 下一复验条件: Irregular 自身正式报告, 运行配置删除, 模型归属删除, 事件关系删除, Anthropic incident direct retrospective 与 CHIVE 科研结果支路分离均已完成, AISI 与 METR 的独立第三方复核, OpenAI 后续明确纠正与 CHIVE 独立外部复现仍未完成核验, 跨厂商评价方向只在取得同 benchmark, 同版本数据集, 统一公开 harness 与尽可能一致推理预算的可重复结果时继续, 不重复采样同一事故或论文页面制造新批次
- 关联记录: [2026-07-25 每日专题](records/2026-07/2026-07-25.md), [2026-07-30 每日专题](records/2026-07/2026-07-30.md), [2026-07-31 每日专题](records/2026-07/2026-07-31.md), [2026-08-04 第三方网络安全评估专题](specials/2026-08/2026-08-04-openai-third-party-cyber-evaluations.md), [2026-08-13 每日专题](records/2026-08/2026-08-13.md), [2026-08-13 前沿模型评价专题](specials/2026-08/2026-08-13-frontier-model-evaluation-comparability.md), [2026-08-17 每日专题](records/2026-08/2026-08-17.md), [2026-08-20 每日专题](records/2026-08/2026-08-20.md), [2026-08-21 Anthropic CHIVE 专题](specials/2026-08/2026-08-21-anthropic-chive-counterfactual-explanations.md)

## 扩展规则

新案例必须来自真实实现中出现过的机制或失败模式, 并包含可复验条件

单纯改写已有问题不构成新案例
