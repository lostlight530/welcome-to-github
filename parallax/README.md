# Parallax

Parallax 是面向长期自主系统的证据稳定性研究系统.

它研究同一判断在证据身份, 对象身份, 发布者身份, benchmark 身份, execution/harness 身份, 时间, current state, 缺失字段, 来源顺序与反例变化时是否仍然成立.

Parallax 不把模型名称, 排名, 页面当前内容或单次成功当成事实捷径. 它也不声称已经实现 AGI. `AGI-scale` 在这里表示研究目标开始覆盖未来长期自主 Agent 必须面对的证据委托, 状态漂移, 多工具执行, 动态世界与跨时间判断问题.

## 核心任务

Parallax 的核心问题不是 `今天有没有正面发现`.

核心问题是 `今天能够形成什么可证伪, 可追溯, 有反例边界的研究结果`.

因此每个 Asia/Shanghai 逻辑日期必须形成一个每日研究单元. `failure`, `missing`, `unknown`, `degraded`, `partial`, `unverified` 与 `no conclusion` 都是合法研究结果, 但不能因为没有正面发现而不产出日报.

同一上海日期最多一个每日研究单元. 同日补强继续完善同一日报, 不增加新的研究批次或独立执行窗口.

## 当前入口

- 最新每日归属日期: 2026-09-24
- 最新每日研究: [动态工具清单与执行时 capability identity](records/2026-09/2026-09-24.md)
- 每日专题: 65
- 特殊专题: 17
- 当前专题研究批次: 82
- 当前专题独立执行日期窗口: 60
- 当前观察案例: 0
- 当前候选案例: 0
- 当前长期结论: 5
- 周期审计: 7
- 最新周期审计: [2026-W38](audits/2026-W38.md)
- 当前月度事实源: [2026-09](records/2026-09.md)
- 当前方法: [METHOD.md](METHOD.md)
- 控制案例: [CASES.md](CASES.md)
- 长期发现: [NOTES.md](NOTES.md)
- 当前日记录模板: [templates/daily.md](templates/daily.md)
- 当前周期整理模板: [templates/monthly.md](templates/monthly.md)

截至 2026-09-24, 9 月已有 24 个 assigned-date Daily artifacts, 其中 23 个 primary research units, 1 个 2026-09-23 RECONSTRUCTION / NOT_RUN / UNVERIFIED gap. W38 已自然完成 7/7 并形成 optional derived audit, 该 audit 不增加 research batch, Trial, execution window 或 finding. W39 已由 2026-09-21 Daily 自然开始. 2026-09-22 与 2026-09-24 各增加 1 个 primary research batch, 2026-09-23 reconstruction 增加 0 research batch 与 0 execution-window credit. 当前仍没有新增 NOTES 级长期发现.

> Maintenance annotation — 2026-09-19
>
> 当前入口已推进到 2026-09-21 Daily. 2026-09-01 至 2026-09-18 的 retrospective maintenance second pass 继续作为历史维护窗口保留: 历史 Daily 保留各自当时 schema 与 point-in-time judgment, 不按后续模板追溯补栏. 2026-09-19 至 2026-09-21 属于之后自然产生的 current research state, 不倒写进该 retrospective window.

## 2026-09-17 research surfaces

### 1 Evidence identity and support

同一 URL 数量不等于独立来源数量.

同一 benchmark 名称不等于同一 run.

同一发布者的多个页面不自动增加独立性.

开发者摘要不等于独立 evaluator result.

搜索索引, 社交摘要, living docs 与 primary technical report 必须保持不同证据身份.

### 2 Temporal and current-state correctness

历史状态与 current state 分开记录.

较新有效证据可以替换 current judgment, 但不能删除旧时点真实状态.

当前动态页面只能证明访问时可见状态, 不能自动重建过去页面.

aggregate incident resolved 不等于每个 individual object 已成功完成.

`no data lost` 不等于每个 queued item 已处理完成.

### 3 Execution and evaluation provenance

base model, reasoning effort, agent harness, benchmark version, dataset split, execution identity 与 adjudication state 分开记录.

shared harness 不等于 independent rerun.

leaderboard display 不等于 benchmark owner 独立执行.

raw submission 不等于 final adjudicated result.

benchmark revision 前后的 score delta 不等于 model-only causal improvement.

### 4 Capability and deployment semantics

capability assessment, deployment availability, intended use, production runtime state, safety classification 与 current configuration 分开记录.

provider self-assessment 不等于 independent reproduction.

public development-set evidence 不等于 held-out capability evidence.

execution progress, transport completion 与 semantic success 不得坍缩为一个 `SUCCESS`.

## 下一阶段 AGI research frontier

下一阶段不是给现有模型贴 AGI 标签, 而是把已验证的 evidence discipline 推到更复杂的 autonomous-agent 场景.

优先研究以下问题.

1. Delegated evidence chain: 多 Agent, 多工具和多 summarizer 共同构造一个判断时, primary evidence, delegation identity 与 independence 是否仍可追溯.
2. World-state drift during deliberation: Agent 从状态 S0 开始推理, 在行动前世界已经进入 S1 时, 哪些 evidence 仍然有效.
3. System configuration identity: 同一模型名称在 toolset, memory, reasoning effort, harness, policy 或 runtime 改变后, 是否仍能合法归因同一 capability.
4. Per-object completion after aggregate recovery: aggregate service recovery 后, individual queued item, session 或 task 的 terminal evidence 如何建立.
5. Cross-evaluator comparability: benchmark owner, provider, independent evaluator 与公开 submission 的结果如何在不虚构 same-run relation 的前提下组合.

这些 frontier 在真正执行 Daily 前只是研究问题, 不自动创建新的 CASE, 不增加 CASE 次数, 也不进入 NOTES.

## 固定研究链

每个有效研究批次保持以下链条.

`research question -> falsifiable hypothesis -> controls -> Trials or bounded evidence procedure -> raw observations -> counterexample -> provisional conclusion -> retest condition`

事实, 推断和未验证事项必须分开.

缺少证据不是反面证据.

Inference 必须保持 inference. Unknown 必须保持 unknown.

## 记录类型

- 每日专题是每日强制研究生产单元, 一个上海归属日期最多一个
- 特殊专题围绕独立公共事件或高价值突发对象建立, 不替代每日连续性
- 周期审计是派生复核, 不增加研究批次, Trial 或独立执行窗口
- 实际执行日期决定独立执行窗口, assigned date 与 execution date 分开
- 历史补录必须保存两种日期, 不把 later execution 倒写成 original run

## 结论升级

- 一个研究批次最多形成观察
- 候选至少需要两个独立研究批次, 不同日期或实质不同控制条件, 并完成反例检查
- 发现至少需要三个独立实验, 跨至少两个实际执行窗口, 并完成反例检查
- 只有发现进入 `NOTES.md`

记录数量, Trial 数量, publisher 数量与独立执行窗口必须分别统计.

## 阅读顺序

1. `METHOD.md` 说明研究生产, 证据身份, 时间边界与结论门槛
2. `CASES.md` 保存已经建立的控制案例和真实复验状态
3. `records/YYYY-MM.md` 保存月度事实源, 每日索引与当前 research frontier
4. `records/YYYY-MM/YYYY-MM-DD.md` 保存每日 point-in-time 研究
5. `specials/README.md` 保存特殊专题入口
6. `NOTES.md` 只保存达到长期门槛的发现
7. `audits/` 保留派生复核, 但不是 Daily research production 的前置条件

## 收录边界

- 事实必须能够追溯到公开权威来源或可复现实验
- 动态页面必须记录访问时点和动态属性
- publisher count 与 independent source count 分开
- current content 不自动代表 historical content
- formal contract 不等于 executed behavior
- test source 不等于 test execution
- completed 不等于 semantic success
- 不保存私人信息, 内部提示词, 隐藏推理或其他目录内容

## 本地检查

运行 `python parallax/tools/check.py`.

检查器只验证当前结构合同, 链接与声明一致性, 不证明外部事实真实, 来源独立或研究结论充分.

## 历史与维护边界

历史 Daily 继续作为 point-in-time primary evidence. 新方法不追溯改变旧实验的原始事实.

维护, correction 与 audit 是独立治理 surface, 不是每日研究是否产出的 gate. 当真实修正发生时仍按 `METHOD.md` 的历史保真规则处理, 但 Parallax 的主循环始终是每日研究生产而不是维护活动.


### Current pointer — 2026-09-22

Latest primary Daily: `records/2026-09/2026-09-22.md`.
September primary Daily coverage now runs through 2026-09-22. Derived pointer updates do not create research or audit credit.


### A2 current-state reconciliation — 2026-09-23

At this repository cut, Parallax primary research remains current through the retained 2026-09-22 Daily.

The host repository has newer 2026-09-23 Horizon task artifacts, but Horizon chronology does not advance Parallax research credit.

```text
HOST_REPOSITORY_ADVANCED
!= PARALLAX_DAILY_EXECUTED

HORIZON_CURRENT_PATH
!= PARALLAX_RESEARCH_BATCH

DERIVED_POINTER_REVIEW
!= NEW_RESEARCH_CREDIT
```

Parallax therefore keeps its primary-Daily endpoint at 2026-09-22 until an actual Parallax Daily for a later Shanghai logical date exists.


## Parallax current-state reconciliation — 2026-09-24

Current repository truth now separates three adjacent states.

- 2026-09-22 remains a retained primary Daily and one research batch.
- 2026-09-23 is represented only as RECONSTRUCTION / NOT_RUN / UNVERIFIED. It restores assigned-date continuity and adds zero research batch, Trial, CASE support, NOTES finding or independent execution-window credit.
- 2026-09-24 is one new primary Daily on MCP tool-state freshness and action-time capability identity.

The current counter contract therefore keeps artifact continuity separate from research occurrence.

```text
ASSIGNED_DATE_ARTIFACT
!= NATIVE_RESEARCH_EXECUTION

RECONSTRUCTION
!= RESEARCH_BATCH
!= INDEPENDENT_EXECUTION_WINDOW
```

The 2026-09-22 and 2026-09-23 maintenance annotations above remain historical point-in-time records and are not rewritten by this current reconciliation.
### A2 current-state reconciliation — 2026-09-24

Current Parallax state after the A1 full-period review:

- assigned-date Daily artifacts through 2026-09-24: 24;
- native primary Daily research units in September: 23;
- 2026-09-23 remains `RECONSTRUCTION / NOT_RUN / UNVERIFIED` with zero research/execution-window credit;
- 2026-09-24 is one native primary Daily on dynamic MCP tool inventory and action-time capability identity;
- current research-batch / execution-window accounting remains the repository-recorded bounded accounting;
- no CASE or NOTES promotion is created by this maintenance reconciliation.

```text
ASSIGNED_DATE_COVERAGE
!= NATIVE_RESEARCH_COUNT

RECONSTRUCTION
!= NATIVE_EXECUTION

TOOL_LIST_AT_S0
!= ACTION_TIME_CAPABILITY_AT_S1
```

The A1 full-September-through-2026-09-23 annotations remain historical/current-boundary evidence and are not replaced.
