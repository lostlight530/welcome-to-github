# 长期记录

## N-01 多义证据不足以支持单一事实

- 状态: 有效
- 生效日期: 2026-07-24
- 案例: P-02
- 支持记录: [PX-20260721-P02](records/2026-07/2026-07-21.md), [PX-20260723-P02](records/2026-07/2026-07-23.md), [PX-20260724-P02](records/2026-07/2026-07-24.md), [PX-20260804-P02](records/2026-08/2026-08-04.md), [PX-20260805-P02](records/2026-08/2026-08-05.md), [PX-20260807-P02](records/2026-08/2026-08-07.md)
- 时间窗口: 2026-07-21, 2026-07-23, 2026-07-24, 2026-08-04, 2026-08-05, 2026-08-07

### 发现

在已记录的保护机制, HTTP 404, Crossref HTTP 400, OpenAI HTTP 401 与 httpbin HTTP 503 材料中, 当证据允许多个原因时, 判断保持证据适用范围并要求关键条件, 可以避免把错误状态扩大为单一事实

六个日期窗口都保持来源顺序不改变判断边界

第三个窗口换用 IETF 与 GitHub 两个发布者并隐藏显式评价字段, 结果仍保持

第四个窗口换用 Crossref API 与 HTTP 400, 仅有状态时保持具体原因未知, 恢复请求参数与正式文档后确认违反公开范围, 再恢复响应正文后确认本次 rows 校验原因

第五个窗口换用 OpenAI Models API 与 HTTP 401, 缺失 Bearer 与无效 Bearer 返回相同状态但不同正文诊断

第六个窗口换用 httpbin 状态生成端点与 HTTP 503, 恢复请求路径和端点契约后识别受控状态生成, 空正文与误导摘要没有被扩大为真实过载, 维护或恢复时间

### 反例检查

- 实时分支响应返回 protected=true, 直接推翻分支未受保护的解释
- 该字段不能区分经典保护规则与规则集, 因此具体机制仍未知
- GitHub 的权限说明不能证明目标 404 的实际原因就是权限不足
- Crossref 的 HTTP 400 状态本身不能证明本次具体校验字段
- 当前 JSON 响应直接标识 rows 值 1001 不满足不大于 1000 的约束
- Crossref 公开访问说明与当前响应不支持 API key 过期摘要
- OpenAI 同一端点的两项 401 响应分别标识缺失 Bearer 与 invalid_api_key
- OpenAI 错误指南列出多种 401 原因, 反驳 401 必然等于错误密钥
- httpbin 的 `/status/:codes` 可以按请求参数生成指定状态, 反驳每个 503 都代表真实生产事故
- RFC 9110 同时允许临时过载与计划维护, 反驳 503 必然只有一个具体原因
- 没有当前响应字节, Retry-After 或正式事件说明时, 不能补出本次故障原因和恢复时间

### 适用边界

- 仅覆盖支持记录中的 GitHub 保护机制, HTTP 404, Crossref rows=1001 对应 HTTP 400, OpenAI Models API 缺失或无效 Bearer 对应 HTTP 401 与 httpbin 状态端点对应 HTTP 503
- 不推广到其他 HTTP 400, 401 或 503 原因, 其他错误状态, 其他 API 或所有 Agent
- httpbin 观察只覆盖受控状态端点契约, 不证明该服务当前生产运行状态
- 同日多个 Trial 只共同构成一个时间窗口

### 复验与失效条件

在新的日期窗口选择真实生产 API 的 HTTP 429 或 503, 优先取得 Retry-After, 明确错误正文或正式事件说明

如果来源顺序改变判断边界, 或关键条件缺失时出现无条件事实断言, 保留本记录并标记失效日期, 推翻证据和影响范围

## N-02 缺少覆盖分母时不能形成全称事实

- 状态: 有效
- 生效日期: 2026-07-28
- 案例: P-03
- 支持记录: [PX-20260722-P03](records/2026-07/2026-07-22.md), [PX-S-20260725-P03](specials/2026-07/2026-07-25-openai-service-events.md), [PX-20260727-P03](records/2026-07/2026-07-27.md), [PX-20260822-P03](records/2026-08/2026-08-22.md), [PX-20260825-P03](records/2026-08/2026-08-25.md)
- 时间窗口: 2026-07-26, 2026-07-28, 2026-08-22, 2026-08-25

### 发现

在已记录的公开审计轨迹, 官方服务状态, 请求级统计材料与 AWS 受控负载测试中, 判断只使用证据直接覆盖的总体, 时间窗口, 统计单位与公开精度, 不把缺失部分补成全称事实

远端记录缺失只支持没有找到公开产物, 不能证明没有离线活动

受影响组件或事件对象只支持公开事件范围, 没有请求分母时不能证明全部请求失败

直接数值请求分母与公开比例出现后可以形成对应粒度的有边界量化, 但 request 与 source 等不同统计单位仍必须分开, 公开显示比例也不能在缺少 direct numerator 与底层精度时机械反推出发布者未直接给出的精确计数

AWS 2017 Lambda concurrency 受控负载进一步给出同一运行的 direct total 5000 requests, exact 3076 HTTP 502 failures 与 exact 1924 HTTP 200 successes, 完整同单位 denominator 与 numerator 存在时允许在该运行边界内形成精确请求计数判断

删除 exact status counts 后判断重新收窄, 删除 direct total 后状态计数的算术加总只能作为构造值, 不能冒充仍存在的 direct denominator 字段

五个正式支持记录跨四个执行窗口保持该边界

### 反例检查

- 未推送提交与离线活动不会出现在远端时间线
- OpenAI 组件总数反证初始受影响组件等于全部已列组件
- GitHub 测试误发事件具有 incident 对象, 后续却明确为无客户影响
- resolved 与组件字段不能补出事件期间请求总量和失败率
- 400 million requests 与 270000 distinct sources 不是同一统计单位
- 3 false-negative sources 不能改写为 3 false-negative requests
- 0.003% of requests 可以保留为公开比例, 但机械计算 12000 不能改写为 Cloudflare 直接发布的精确错误请求 numerator
- no mitigated sources below threshold 不能证明其余所有 requests 都被正确分类
- AWS 2017 受控运行的 3076 个 HTTP 502 只属于该 API Gateway + Lambda 测试对象与运行, 不能推广为所有 Lambda throttle 的统一响应状态
- AWS 当前 Lambda Function URL 文档说明 concurrency 超限返回 HTTP 429, 直接反驳从历史 API Gateway 示例推出 throttle 一律为 HTTP 502
- 5000, 3076 与 1924 的直接计数不构成 AWS Lambda 全局历史或当前生产失败率

### 适用边界

- 覆盖支持记录中的公开提交轨迹, OpenAI 与 GitHub 状态事件, Cloudflare 400 million request rate limiting analysis, 以及 AWS 2017 API Gateway + Lambda concurrency 受控负载测试
- 只约束从部分记录到全称事实, 从显示比例到精确计数, 跨统计单位换算, 以及 direct field 与构造计算之间的扩大判断
- Cloudflare 范围只覆盖该文章公开的 request 与 source 统计对象, 不推广到其全部生产流量或所有 rate limiting 实现
- AWS 范围只覆盖官方文章中的两个固定 5000-request 受控运行及其直接状态计数, 不推广到当前生产流量, 所有 Lambda invocation surfaces 或一般 HTTP throttle status
- direct denominator 存在时允许使用发布者实际给出的统计粒度, direct exact numerator 同时存在时允许对应运行内精确计数, 但不自动证明未覆盖 category 已穷尽或其他对象具有同样分布
- 不证明未观察部分一定存在活动或成功请求
- 不推广到所有完整分母统计报告, 所有任务或所有 Agent

### 复验与失效条件

同一统计对象与窗口的 direct numeric total requests 与 exact failed or successful requests 已在 AWS 独立发布体系中完成复验

后续统计方向不重复同一 AWS 页面, 优先选择另一个独立实现或正式事件, 检查 direct total 与多个 exact outcome categories 是否覆盖完整且单位一致, 或测试发布者 direct exact numerator 与 derived rate 的精度边界

若只有显示比例, 保留其公开精度并把机械反推计数标为构造计算而不是原始精确观测

普通账户社区回复与点赞仍可作为另一条安全复验路径

如果加入完整同单位分母与 numerator 后判断仍拒绝有边界更新, 或缺少分母, 单位身份与精度时出现无条件全称或精确计数断言, 保留本记录并标记失效日期, 推翻证据和影响范围

## N-03 较新有效证据替换当前判断但不删除历史

- 状态: 有效
- 生效日期: 2026-07-29
- 案例: P-04
- 支持记录: [PX-20260726-P04](records/2026-07/2026-07-26.md), [PX-20260728-P04](records/2026-07/2026-07-28.md), [PX-20260729-P04](records/2026-07/2026-07-29.md), [PX-20260814-P04](records/2026-08/2026-08-14.md), [PX-20260821-P04](records/2026-08/2026-08-21.md), [PX-20260824-P04](records/2026-08/2026-08-24.md)
- 时间窗口: 2026-07-26, 2026-07-28, 2026-07-29, 2026-08-14, 2026-08-22, 2026-08-24

### 发现

在已记录的官方服务状态事件, OpenAI GPT-4o 非状态页模型部署 rollback, Atlassian Jira Cloud platform scopes 时间链与 Google Chrome 第三方 Cookie 多阶段路线中, 具有稳定对象身份与可排序时间时, 当前判断随同一对象的较新有效证据更新, 被替代状态保留为对应时间范围内的历史记录

常规 investigating, monitoring, resolved 更新链保持该边界

明确测试纠正替换初始影响判断, 但初始消息仍保留为曾经发布的历史记录

首次 resolved 后出现更晚 monitoring 时, 当前状态更新为 monitoring, 最终 resolved 再次成为当前状态

OpenAI GPT-4o 2025-04-25 更新完成 rollout 后, 2025-04-28 开始的 full rollback 更新后续部署判断为 previous version, 同时保留 4 月 25 日更新曾真实部署的历史事实

Atlassian scopes 在 2022-02-22 发布迁移要求后, 2022-04-20 明确暂停旧 scopes deprecation 并移除 2022-08-23 迁移 deadline, 当前 Jira Cloud platform 文档又推荐在可用时优先使用 classic scopes, 后续契约更新当前判断但没有删除此前迁移要求曾被发布的历史阶段

Google Chrome 第三方 Cookie 路线从 2021 至 2023 的 phase-out 计划, 更新到 2024-07-22 instead-of-deprecating 的 informed-choice proposal, 再到 2025-04-22 maintain-current-approach 且不推出 new standalone prompt, 当前终态更新判断而没有删除早期计划和中间方案曾真实发布的历史身份

六个正式支持记录跨六个执行窗口保持该边界

### 反例检查

- 同日不同事件可以具有不同当前状态, 不能跨事件复制更新
- GitHub 测试事件的通用 resolved 文本不能证明真实客户事故
- OpenAI 对照事件只经历线性 identified, monitoring, resolved, 反证所有事件都会在 resolved 后重新进入 monitoring
- 删除时间戳后无法确定两次 resolved 与 monitoring 的先后
- 删除事件 ID 后无法把相似更新可靠归属到同一事件
- GPT-4o full rollback 不能证明 4 月 25 日更新从未部署
- system prompt 临时缓解不能替代 full rollback
- previous version 不等于公开给出可核验 snapshot ID
- 删除 GPT-4o, ChatGPT 与 2025-04-25 update 身份后不能把相似 rollback 文本拼成同一部署链
- Atlassian 2022-04-20 deadline removal 不能证明此前迁移要求从未存在
- 当前 Jira Cloud platform 的 classic scope recommendation 不能扩大为全部 Atlassian 产品禁止 granular scopes
- 删除可排序时间后不能根据 migration, pause 与 recommendation 文本强行确定当前先后关系
- 2025 maintain current approach 不能改写为 Google 从未计划淘汰 Chrome 第三方 Cookie
- 2024 proposed informed-choice experience 不能提前等同于 2025 no-standalone-prompt 当前终态
- 删除 Chrome 与 third-party cookies 对象身份后不能把 Privacy Sandbox API 路线与 Cookie 支持状态自动拼成同一对象链

### 适用边界

- 覆盖支持记录中的 OpenAI 与 GitHub 官方服务状态事件, OpenAI GPT-4o 在 ChatGPT 中的 2025-04-25 mainline update rollback, Atlassian Jira Cloud platform Forge 与 OAuth 2.0 3LO scopes 的多阶段迁移时间链, 以及 Google Chrome 第三方 Cookie 2021 至 2025 的公开路线更新
- 依赖稳定对象身份, 可排序时间与可访问的替代关系或更新历史
- GPT-4o 范围只覆盖本次 ChatGPT mainline update, 不自动扩展到 API, Voice, 图像模型或其他 GPT-4o 产品表面
- Atlassian 范围只覆盖本次 Jira Cloud platform 相关 scope 迁移与当前 recommendation, 不自动扩展到 Jira Software, Confluence 或所有 Atlassian 产品
- Chrome 范围只覆盖第三方 Cookie 支持路线与公开 user-choice 状态, 不自动扩展到 Privacy Sandbox 全部 API, Incognito tracking protections 或其他 Chrome 隐私功能
- 正式 rollback, pause, documentation recommendation 或路线公告不等于本轮取得生产请求或 app runtime 样本
- 不证明状态页描述与每个用户的实际体验完全一致
- 不推广到缺少替代关系的普通文档, 所有任务或所有 Agent

### 复验与失效条件

多阶段 replacement, 新独立发布体系, 稳定对象身份, 可排序时间与当前可验证终态已经在 Atlassian 与 Chrome 两条独立时间链中完成复验

若继续 P-04, 优先等待同一高质量对象再次出现明确 current-state 更新, 或选择具有真正双向 on/off 切换且能直接核验当前运行终态的新对象, 不重复一般 deprecation, 单次 rollback, 相同 scope 迁移或同一 Cookie 时间链

如果较新有效证据没有更新当前判断, 被替代状态被物理删除, 当前文档被倒写成历史原始状态, 或缺少身份与时间条件时仍形成确定归属, 保留本记录并标记失效日期, 推翻证据和影响范围

## N-04 长上下文不替代直接支持与对象身份

- 状态: 有效
- 生效日期: 2026-07-31
- 案例: P-05
- 支持记录: [PX-20260725-P05](records/2026-07/2026-07-25.md), [PX-20260730-P05](records/2026-07/2026-07-30.md), [PX-20260731-P05](records/2026-07/2026-07-31.md), [PX-S-20260804-P05](specials/2026-08/2026-08-04-openai-third-party-cyber-evaluations.md), [PX-20260813-P05](records/2026-08/2026-08-13.md), [PX-20260820-P05](records/2026-08/2026-08-20.md), [PX-S-20260821-P05](specials/2026-08/2026-08-21-anthropic-chive-counterfactual-explanations.md)
- 时间窗口: 2026-07-26, 2026-07-30, 2026-07-31, 2026-08-05, 2026-08-13, 2026-08-22, 2026-08-23

### 发现

在已记录的研究门槛, HTTP 语义, 无障碍对比度, 多发布者网络安全评估与 AI scientific experiment 材料中, 增加长上下文或与正文冲突的摘要没有替代可定位的直接支持

删除关键支持时, 判断收窄为未验证

删除适用对象身份时, 判断拒绝从多个允许边界中猜测一个默认类别

Irregular 自身正式报告加入后, 直接评估发布者与开发方二次汇总仍保持事实归属分离, 相邻 UK AISI 结果没有并入 Irregular 数量

Anthropic 自身事故复盘加入后, 141006 次回顾运行, 3 起事故, 6 次相关运行与三个模型身份继续按直接发布者和统计层级分开保存, 相邻 AISI 材料没有改变 Anthropic 事故事实归属, 非受控个案也没有被升级为稳定模型排名

CHIVE 科研专题加入后, evaluation no uplift, training-data generalization 与 applied-use caveat 按 result branch 分开保存, LLM-generated explanation 也没有替代 measured counterfactual outcome 的 evaluation-label 身份

七个实质不同支持记录跨七个执行窗口保持该边界

### 反例检查

- 同一日期的多个 Trial 不能增加独立时间窗口
- RFC 9110 的 404 多义性不能证明具体响应采用隐藏访问限制
- WCAG 2.2 的大号文字与例外类别反驳所有文字统一为 4.5:1
- WCAG 规范阈值不能证明具体页面已经合规
- 三个早期批次仍由同一研究体系执行, 不能代表不同执行主体或环境
- AISI 的 19 项越界动作只有 2 项涉及 GPT-5.6 Sol, 反驳按文章主题默认归因
- 互联网启用与分类器关闭不代表普通公开部署
- 未发现现实损害不等于证明没有风险
- Irregular 的 19/197 FrontierCyber 结果不能扩大为全部挑战成功或可靠端到端攻击
- Irregular 的 capability-elicitation 设置不包含部署网络安全缓解措施, 不能直接代表经过缓解模型的现实滥用画像
- OpenAI System Card 同时列出 Irregular 与 UK AISI 结果, 相邻长上下文不能改变独立评估归属
- Anthropic 141006 次被回顾运行不能改写为事故数量
- 3 起事故与 6 次相关运行不能互换或按三个模型机械平均
- Anthropic 明确说明三个 isolated incidents 不是 controlled experimental comparison, 个案差异不能形成稳定模型安全排名
- AISI 的 122 次运行与 19 项动作属于另一评估对象, 不能加入 Anthropic 的统计分母
- CHIVE no uplift 只属于当前 counterfactual evaluation, 不能扩大为所有 applied interpretability tools 完全无用
- CHIVE training-data generalization 不能改写为 activation-reading tools 在 evaluation 上产生 uplift
- LLM-generated explanation 不能因为语言流畅而升级为 ground truth
- CHIVE 代码公开不能冒充本轮已经完整复现研究结果

### 适用边界

- 仅覆盖支持记录中的 Parallax 门槛材料, RFC 9110, WCAG 2.2, OpenAI 与 AISI 第三方评估材料, Irregular 自身正式评估报告, Anthropic 2026-07-30 官方事故复盘以及 2026-08 CHIVE scientific experiment
- Irregular 范围只覆盖其 GPT-5.6 Sol FrontierCyber, CyScenarioBench 与 Atomic Challenges 报告中的直接结果, 配置与限制
- Anthropic incident 范围只覆盖其复盘中的三起 isolated incidents, 涉及运行与模型身份, 不推广为一般部署事故率或模型总体排名
- CHIVE 范围只覆盖当前论文和官方研究页中的 counterfactual evaluation, training-data result 与 evidence-type identity, 不推广为所有 interpretability 方法的最终有效性判断
- 只描述直接支持, 冲突摘要, 关键缺失, 统计对象, result branch, evidence type 与对象身份之间的判断边界
- 不推广到所有长上下文, 所有规范, 所有任务或所有 Agent
- 不证明长上下文长度本身是判断保持或失败的原因
- 不把 capability-elicitation 或特定评估环境结果推广为普通部署的现实滥用画像

### 复验与失效条件

事件关系删除, Anthropic 新发布者直接事故复盘与 CHIVE 科研结果支路分离已经完成

后续优先等待 CHIVE 独立外部复现, AISI 或 Anthropic 与 METR 的独立第三方复核正式发布, OpenAI 对此前第三方评估的明确纠正, 或取得同 benchmark, 同版本数据集, 统一公开 harness 与尽可能一致推理预算的跨厂商可重复结果

计划中的第三方复核不能写成已完成结果, 公开代码不能写成本轮已复现结果, 不重复采样同一事故或论文页面制造新支持记录

如果冲突摘要改变判断边界, 关键支持缺失时仍形成无条件事实, 对象身份, 统计层级, result branch 或 evidence type 缺失时仍猜测默认类别, 开发方二次汇总覆盖原始评估发布者直接事实归属, 非受控个案被升级为稳定模型排名, 或 generated explanation 被升级为 ground truth, 保留本记录并标记失效日期, 推翻证据和影响范围

## N-05 证据层级不能被顺序与文本命中替代

- 状态: 有效
- 生效日期: 2026-08-02
- 案例: P-01
- 支持记录: [PX-20260720-P01](records/2026-07.md#2026-07-20), [PX-20260801-P01](records/2026-08/2026-08-01.md), [PX-20260802-P01](records/2026-08/2026-08-02.md)
- 时间窗口: 2026-07-20, 2026-08-01, 2026-08-02

### 发现

在已记录的五组 Agent 材料中, 技术文档, 维护规则, 产品声明与可重复文本命中只支持各自证据层级

来源顺序与误导摘要没有把这些材料扩大为稳定运行证明

关键正文或确定性检查结果缺失时, 判断随直接支持收窄, 没有从页面身份, 哈希或其他项目材料补全

三个实质不同批次跨三个执行窗口保持该边界

### 反例检查

- 12/12 个预设标记命中只证明冻结字节中存在文本, 不证明框架行为
- OpenAI 追踪可以禁用并具有数据保留边界
- 并行输入护栏失败前可能已经产生资源消耗或工具副作用
- Hermes 新会话与 unknown 终态说明调度不等于成功完成
- OpenClaw 规则文本不能证明每次执行已经遵守
- openJiuwen 同一地址在 Python 与浏览客户端分别返回 HTTP 200 与 418, 单一访问结果不能扩大为全局状态

### 适用边界

- 仅覆盖支持记录中的 OpenAI Agents SDK, Hermes Agent, OpenClaw 与 openJiuwen 材料
- 可重复结果只覆盖网页字节, 哈希与预设文本标记, 不属于框架行为测试
- 不证明文档与当前实现完全一致
- 不推广到所有证据类型, 所有任务, 所有执行主体或所有 Agent

### 复验与失效条件

2026-08-16 已取得 OpenAI Agents SDK 当前 Guardrails 文档与固定测试源码契约, 但没有安装或运行 SDK 测试套件, 下一窗口优先安全运行固定版本 input guardrail 最小复现或官方可重放测试, 再将实际运行结果与文档和测试源码契约分层比较并构造可定位冲突

如果来源顺序或误导摘要改变证据等级, 关键支持缺失时仍出现无条件事实, 或文本命中被扩大为运行证明, 保留本记录并标记失效日期, 推翻证据和影响范围
