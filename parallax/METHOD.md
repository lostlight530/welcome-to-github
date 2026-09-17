# 方法

## 研究定位

Parallax 是证据稳定性与判断边界研究系统.

目标不是给某个模型做综合排名, 也不是用每日成功率证明系统能力. 目标是测试一个判断在证据身份, 对象身份, 发布者身份, 时间, current state, benchmark, execution, harness, missing fields, source order 与 counterexample 改变后是否仍然成立.

`AGI-scale epistemic integrity` 是下一阶段研究尺度, 不是能力声明. 它表示未来长期自主 Agent 在多来源, 多工具, 多模型, 多 Agent delegation 与动态世界中需要保持可追溯判断, 因而必须把 evidence identity 与 inference boundary 明确建模.

## 每日研究生产合同

每个 Asia/Shanghai 逻辑日期必须形成一个每日研究单元.

每日研究是 mandatory research production, 不是 maintenance/no-change task.

- 一个上海归属日期最多一个每日专题
- 同日再次运行只能补强同一日报, 不创建第二个研究批次
- `failure`, `missing`, `unknown`, `degraded`, `partial`, `unverified`, `evidence insufficient` 与 `no conclusion` 都是合法日报结果
- 没有正面发现不等于没有研究产出
- 不允许为了满足每日产出而制造 CASE, 独立来源, run identity, benchmark comparability 或结论升级
- 如果高价值 CASE 当前无法直接执行, 仍必须选择一个真实可证伪问题并完成 bounded evidence procedure, 同时明确当前能力与证据边界
- 研究完成但 GitHub delivery 受阻时, research state 与 delivery state 分开记录, 不把 delivery failure 改写为没有研究

历史上缺失或未执行的日期保持其真实 provenance. 新的每日强制生产合同不能追溯把 `RECONSTRUCTION`, `NOT_RUN`, `UNVERIFIED` 或其他历史缺口改写为原生运行.

## 记录类型

### 每日专题

- 保存于 `records/YYYY-MM/YYYY-MM-DD.md`
- 文件日期是上海归属日期
- 必须记录实际执行日期与独立执行窗口
- 必须完成固定研究链或明确说明哪一环被事实阻塞
- 后续补录不得伪装成原日期执行
- 同一实际执行日期的多个批次共享一个独立时间窗口

### 特殊专题

- 保存于 `specials/YYYY-MM/YYYY-MM-DD-topic.md`
- 用于具有独立公共价值的事件核验
- 标明事件日期, 实际核验日期与独立时间窗口
- 独立计入研究批次, 不替代每日专题
- 特殊专题存在本身不自动形成 CASE 支持或长期发现

### 周期审计

- 保存于 `audits/YYYY-Www.md`
- 是 derived review, 不是研究批次
- 审计增加 0 research batches, 0 Trials, 0 independent execution windows
- 审计不能降低候选, 发现或失效门槛
- Daily research production 不依赖审计是否存在

## 来源闸门

候选材料进入研究前检查以下条件.

1. 来源能够公开访问并准确定位
2. 能够确定 publisher, object, page or artifact identity
3. 至少具有官方源码, 正式文档, runtime/status record, benchmark material, primary technical report 或可复现实验之一
4. 能够提取具体机制, 状态或可证伪关系, 而不是只有愿景或宣传描述
5. 能够说明限制, failure condition, unknown field 或适用边界
6. 来源独立性按 publisher 与 evidence chain 判断, 不按 URL 数量判断
7. 动态页面记录访问日期, 不把 current snapshot 倒写为过去页面

来源集合保持开放, 不设置厂商, 模型, benchmark 或框架白名单.

## 证据层级

证据强度按 claim-specific authority 判断, 不机械使用单一全局排序.

常见强度从接近运行事实到弱解释包括.

1. 可重复 runtime result, raw trace 或直接 object state
2. benchmark owner / evaluator 的可定位 run-level evidence
3. 当前源码或机器可读合同
4. 官方技术文档, model card, status timeline, changelog 或 release source
5. 官方产品声明
6. 二手解释, search summary, social summary 或转载

同一来源可以对一个 claim 权威, 对另一个 claim 不权威.

弱证据可以产生研究问题, 不能单独产生长期结论.

来源冲突保留冲突. 缺少证据不是反面证据. 来源数量不是来源独立性.

## Epistemic identity tuple

从 2026-09 的连续研究开始, Parallax 对高风险判断至少考虑以下 identity coordinate.

`claim identity`

`object identity`

`publisher identity`

`evidence artifact identity`

`benchmark and dataset identity`

`model/system configuration identity`

`execution identity`

`harness identity`

`evaluation or adjudication identity`

`temporal identity`

`current-state cut`

`correction relation`

不是每个实验都需要全部字段, 但不能在缺少某一关键 identity 时从相邻文字, 同名对象或数值自动补全.

## 永久跨层边界

以下关系默认不等价.

`formal contract != runtime result`

`current docs != historical runtime snapshot`

`source code != executed behavior`

`test source != test execution`

`status resolved != every individual object succeeded`

`completed != semantic success`

`no data lost != every queued item completed processing`

`HTTP success != target semantic success`

`documentation existence != actual field retrieved`

`same publisher multiple pages != independent publishers`

`source count != source independence`

`current state != state transition date`

`evaluation protocol != evaluation result`

`benchmark identity A != benchmark identity B`

`developer summary != independent evaluator result`

`leaderboard display != independent execution`

`shared harness != independent rerun`

`raw submission != final adjudicated result`

`public development set != held-out capability evidence`

`benchmark revision delta != model-only causal improvement`

`aggregate recovery != per-object completion`

`derived arithmetic != publisher direct observation`

Inference 必须保持 inference. Unknown 必须保持 unknown.

## 固定研究链

每个有效研究批次必须完整记录.

`research question -> falsifiable hypothesis -> controls -> Trials or bounded evidence procedure -> raw observations -> counterexample -> provisional conclusion -> retest condition`

事实, 推断与未验证事项分开.

缺少关键证据时允许 `NO_CONCLUSION`.

不得把事后解释写成原始观测.

每个 Trial 明确写出保持条件与改变条件, 避免多个变量一起变化后仍做单因果归因.

## 2026-09-17 四个核心研究面

### Evidence identity and support calculus

同一发布者的多个页面不构成多个独立来源. 同一 benchmark 名称不建立 same-run relation. 直接 evaluator evidence 对 evaluator-specific claim 强于 developer summary. 动态页面只证明访问时点可见状态.

### Temporal and current-state correctness

较新有效证据更新 current judgment, 不删除历史真实状态. correction date, state transition date, access date 与 publication date 分开. terminal update 被删除时不从 mitigation 或其他相邻状态补出 resolved.

### Execution and evaluation provenance

base model, reasoning effort, agent harness, provider route, benchmark version, dataset split, run identity 与 adjudication state分开. 结果显示面不自动证明执行主体. shared harness 不自动证明 independent reproduction.

### Capability, deployment and semantic outcome

capability evidence, deployment availability, intended use, safety classification, execution progress 与 semantic success 分开. 数值字段失去 metric identity 后不能从相邻数字恢复 success/failure category. 算术 residual 不能冒充发布者直接 numerator.

## AGI-scale research frontier

以下是下一阶段优先问题, 在真正 Daily 执行前不计 CASE 支持.

### Delegated evidence chain

研究多个 Agent, tool, retrieval layer 与 summarizer 共同形成一个判断时, primary evidence, delegation identity, attribution 与 source independence 是否仍可恢复.

核心攻击包括 stale subclaim, same-publisher fanout, summary laundering, delegated citation loss 与 conflicting authority.

### World-state drift during deliberation

研究 Agent 在状态 S0 建立计划, 世界在 action 或 conclusion 前进入 S1 时, 哪些事实仍有效, 哪些必须重新读取.

重点区分 historical truth, current truth, decision-time truth 与 execution-time truth.

### System configuration identity

研究同一 base model name 在 reasoning effort, toolset, memory, system prompt surface, harness, sandbox, provider route 或 policy 改变后, 结果还能否归因同一 capability object.

### Per-object completion after aggregate recovery

研究 aggregate status `Resolved`, `Recovered` 或 `No data lost` 后 individual session, queued item, task 或 detection 是否具有 direct terminal evidence.

### Cross-evaluator comparability

研究 provider, benchmark owner, independent evaluator 与 public submission 的结果在什么条件下可以比较, 什么条件下只能并列展示而不能合并为同一 run, correction 或 causal delta.

## 研究批次与时间窗口

- 一个完整每日专题计为一个研究批次
- 一个完整特殊专题计为一个研究批次
- 同一批次多个 Trial 不增加批次数
- 同一实际执行日期多个批次只形成一个执行窗口
- audit 增加 0 batch, 0 Trial, 0 window
- correction, schema repair, source correction, validator repair, preservation correction 与 stale-statement correction 不自动计研究批次
- 历史补录按实际执行日期计算窗口

assigned date 与 actual execution date 不得坍缩.

## 结论状态

- 观察: 只在一个研究批次出现
- 候选: 至少两个独立研究批次, 跨不同日期或实质不同控制条件, 并完成 counterexample check
- 发现: 至少三个独立实验, 跨至少两个实际执行窗口, 并完成 counterexample check
- 失效: 新证据推翻原结论, 保留原记录并写明原因, 日期与影响范围

只有发现进入 `NOTES.md`.

同主题, 相邻证据, 相似状态码, schema repair 或后来重命名 Trial 都不自动增加 CASE 支持.

## 历史保真

Current truth 不删除 old truth.

Later resolved 不删除 earlier degraded.

Later release 不证明 earlier availability.

Later documentation 不证明 earlier runtime behavior.

Later correction 不删除旧值曾经被公开报告的事实.

新方法不追溯使旧研究失效, 除非新证据真正推翻原结论. 若推翻, 保留原记录, invalidation date, replacement evidence 与 impact scope.

## 连续性恢复

- 每次 Daily 检查目标逻辑日期是否已经存在
- 已存在则继续同一文件, 不创建第二个 Daily
- 历史缺口没有可验证原生运行时不得伪造 NATIVE
- 后续真实补录必须记录 actual execution date 与 provenance
- 特殊专题不填补 Daily 连续性
- `RECONSTRUCTION`, `NOT_RUN`, `UNVERIFIED`, `UNKNOWN` 与 `BLOCKED` 都是合法历史状态

## 记录节奏

- `records/YYYY-MM.md` 是月度事实源与当前 research frontier 视图
- `CASES.md` 只保存已建立的控制案例与真实累计支持
- `NOTES.md` 只保存达到发现门槛的长期发现
- `README.md` 保存当前入口, mission 与研究面
- `specials/README.md` 保存特殊专题入口
- Daily 使用 `templates/daily.md`
- Special 使用 `templates/special.md`
- derived audit 使用 `templates/weekly.md`
- 月度研究整理使用 `templates/monthly.md`

模板规定研究结构, 不规定外部 scheduler 实现.

## Provenance 与独立性

- 每份新 Daily 声明 Record Provenance, assigned date, actual execution date 与 execution window
- publisher independence 与 execution independence 分开
- mirrors, same-publisher pages, developer summaries 与 platform-generated summaries 不自动产生 source independence
- benchmark owner display 与 provider self-computed result 可以建立 provenance relation, 但不能自动补 independent rerun
- verifier independence 不仅看实现代码是否不同, 还要看 evidence model, evaluator authority 与语义合同是否独立
- 当前无法取得 primary evidence 时明确拒绝或无结论

## 验证

验证分为至少三个问题.

1. 记录结构是否完整
2. 引用证据是否真的支持声明的 proposition
3. source, execution 与 evaluator independence 是否足以支持当前结论等级

`parallax/tools/check.py` 只能回答其中结构合同的一部分, 不能把 checker PASS 写成 external truth PASS.

## Monthly research synthesis

月度文件首先是 research fact source, 不是 maintenance completion certificate.

至少维护.

- 每日 assigned date coverage 与 actual execution date
- Daily / Special / derived audit 的不同计数
- research batches 与 independent execution windows
- CASE 真实支持变化
- NOTES 真实 promotion 或 no-promotion
- current contradictions and unknowns
- 2026-09-17 之后的 active research frontier

自然月结束前只能做 as-of synthesis, 不能提前把整月写成 sealed final month.

## Separate maintenance and correction surface

Maintenance 与 correction 继续存在, 但不属于 Daily research production gate.

只有真实 defect 需要修正时才进入 maintenance surface. 修正必须保留 original execution facts, real correction time, original identity 与 supporting evidence. 新维护文本不能让 later source 看起来在 earlier run 当时已经可用.

Monthly maintenance ledger 如果存在, 仍使用 `NOT_RUN`, `PARTIAL`, `COMPLETED` 等显式状态, 但这些状态不决定当日研究是否应该产出.

Calendar closure, input delivery, original execution, current content quality 与 maintenance completion 保持分离.
