# H3 Weekly Position Decide

CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H3
Cadence: Weekly
Loop Stage: Decide
Target Week: 2026-W36
Logical Week Basis: Asia/Shanghai
Coverage Window: 2026-08-31 to 2026-09-06
Execution Time Asia/Shanghai: 2026-09-13 14:30:00 CST
Agent: Jules
Input Status: SUCCESS
Network Status: NETWORK_VERIFIED
Task Status: SUCCESS
Repository Inspection: NO
GitHub Actions Inspection: NO
Write Scope: horizon-cortex only
Boundary Violation: NO
Original Execution Status: SUCCESS
Current Path Status: PRESENT
Record Provenance: JULES_NATIVE
Daily Coverage Matrix: 7 H1 + 7 H2 / COMPLETE
Inherited Evidence: W36 Daily H1/H2 signals
Independent Evidence Added: https://docs.aws.amazon.com/connect/latest/adminguide/ai-agent-mcp-tools.html
Missing Inputs Preserved: NONE
Decision Evidence Basis: DEC-2026W36-01 based on AWS MCP support and official MCP docs; DEC-2026W36-02 based on Auth0 and Merge.dev blogs
Historical Execution State: SUCCESS
Current Delivery State: PRESENT

INPUT_RECORD

Target Week: 2026-W36
Week Start: 2026-08-31
Week End: 2026-09-06
Expected H1 Dates: 2026-08-31 to 2026-09-06
Expected H2 Dates: 2026-08-31 to 2026-09-06

Actual H1 Files:
- horizon-cortex/2026-08-31-H1-signal-observe.md
- horizon-cortex/2026-09-01-H1-signal-observe.md
- horizon-cortex/2026-09-02-H1-signal-observe.md
- horizon-cortex/2026-09-03-H1-signal-observe.md
- horizon-cortex/2026-09-04-H1-signal-observe.md
- horizon-cortex/2026-09-05-H1-signal-observe.md
- horizon-cortex/2026-09-06-H1-signal-observe.md

Actual H2 Files:
- horizon-cortex/2026-08-31-H2-horizon-orient.md
- horizon-cortex/2026-09-01-H2-horizon-orient.md
- horizon-cortex/2026-09-02-H2-horizon-orient.md
- horizon-cortex/2026-09-03-H2-horizon-orient.md
- horizon-cortex/2026-09-04-H2-horizon-orient.md
- horizon-cortex/2026-09-05-H2-horizon-orient.md
- horizon-cortex/2026-09-06-H2-horizon-orient.md

Missing Files: NONE
Blocked Files: NONE
Degraded Files: NONE
Coverage Ratio: 100%
Source Independence Notes: AWS Connect 实施方案与 Google Cloud 部署来自不同的云厂商；Auth0 和 Merge.dev 代表独立的身份认证和集成平台视角。

Recent 4 historical H3:
- horizon-cortex/2026-W32-H3-position-decide.md
- horizon-cortex/2026-W33-H3-position-decide.md
- horizon-cortex/2026-W34-H3-position-decide.md
- horizon-cortex/2026-W35-H3-position-decide.md

Recent 4 historical H4:
- horizon-cortex/2026-W32-H4-narrative-act.md
- horizon-cortex/2026-W33-H4-narrative-act.md
- horizon-cortex/2026-W34-H4-narrative-act.md
- horizon-cortex/2026-W35-H4-narrative-act.md

Most recent H6 before Target Week:
- horizon-cortex/2026-08-H6-horizon-memorize.md

External Sources verified:
- https://docs.aws.amazon.com/connect/latest/adminguide/ai-agent-mcp-tools.html
- https://auth0.com/blog/mcp-vs-a2a/

WEEKLY_SIGNAL_SYNTHESIS

重复信号:
- MCP (Model Context Protocol) 转向完全无状态 (Stateless) 模型（移除 Session、依赖 HTTP Header）是 H1 中的高频信号。
- 长期运行代理的持久化执行（Durable Execution）和异步任务 (Tasks) 在多天的信号中重复出现。

新信号:
- 云厂商（如 AWS Connect）在具体企业工作流中正式落地支持 MCP 工具调用，说明 MCP 开始向企业核心业务场景渗透。
- Auth0/Merge.dev 提出并强调 MCP 与 A2A (Agent-to-Agent) 作为互补协议的明确分工：MCP 用于工具，A2A 用于智能体间协同。

独立证据增强的信号:
- MCP 协议的 2026-07-28 无状态基线已经获得了 AWS Connect 实施方案和 Google Cloud 云原生基础设施部署这两个独立的一线云厂商证据增强。

同源重复造成的假增强:
- 连续数日对于 MCP 无状态设计和 2026 路线图的探讨，源自相同的 MCP 官方博客或官方路线图发布，不代表行业存在多个独立标准的共识，而是单一规范演进的重复反馈。

降级信号:
- 原有 MCP 规范中的 Roots, Sampling 和 Logging 等特性已被官方弃用（Deprecated），应从观察雷达中降级或移除。

证伪信号:
- 认为所有 AI 代理间协作和外部工具调用会合并为单一协议的假设被证伪，当前行业更倾向于分离的互补协议组合（如 MCP + A2A）。

过期信号:
- 针对 MCP 旧版基于 Mcp-Session-Id 和强制连接握手的有状态架构探讨已正式过期。

输入缺失影响的信号:
- 无。本周 H1/H2 覆盖率为 100%。

仍不确定信号:
- A2A (Agent-to-Agent) 协作协议的具体实施标准（特别是 Google 等推动的版本）能否在行业内达成最终共识仍不确定。

DECISION_SET

Decision ID: DEC-2026W36-01
Decision: 将 MCP (Model Context Protocol) 2026-07-28 的无状态核心架构及其企业落地支持（如 AWS Connect）设定为本周关于外部工具集成的核心观察方向。
Decision Type: FOCUS
Evidence: 官方规范 (2026-07-28 Specification) 废弃了 Mcp-Session-Id 并转为无状态架构，AWS Connect 提供了官方文档支持 MCP 工具调用以取代定制化集成。
Independent Evidence: AWS Connect 实施指南和 Google Cloud 的大规模部署提供了跨云平台的独立实践证据。
Repository Record Comparison: 之前周次对 MCP 的追踪多停留在规范解读和框架验证阶段，本周 H1/H2 明确捕捉到了云平台直接原生集成的证据。
Counterevidence: 无明显的实现层反证，但部分供应商可能有自己的专有工具调用实现。
Expected Value: 为未来宿主仓库潜在的 AI Agent 工具连接方案提供清晰的无状态参考基准，避免基于已废弃的有状态 MCP 规范进行设计。
Risk: 错误地将特定云厂商（如 AWS, Google）的落地细节等同于 MCP 协议本身的普适性要求。
Why Now: 2026-07-28 规范的无状态更新已经通过多个头部企业实装，架构模式已固化。
Confidence: HIGH
Validity Window: 2026-W37 to 2026-W40
Invalidation Trigger: 行业出现全面取代 MCP 的更优工具调用开放标准。
Host Repository Change: NO

Decision ID: DEC-2026W36-02
Decision: 跟踪 MCP 用于单一 Agent 外部工具访问与 A2A 用于多 Agent 协同的互补架构模式演进。
Decision Type: CONTINUE_WATCH
Evidence: Auth0 和 Merge.dev 等独立厂商在工程博客中详述了这两种协议的明确责任边界及所需的不同身份验证机制。
Independent Evidence: Auth0 (身份认证层) 和 Merge.dev (集成平台层) 作为非 MCP 直接维护方，独立论证了这一互补架构。
Repository Record Comparison: 扩展了上周关于 AI 系统解耦和多智能体无状态网关架构的观察，指出了具体的互补协议方案。
Counterevidence: A2A 标准仍在发展阶段，具体的协议细节存在不确定性。
Expected Value: 提供关于多智能体复杂系统的架构分离视角。
Risk: 早期信号可能不会成为最终的行业统一规范。
Why Now: 业界开始尝试清理并明确不同“Agent 协议”的适用边界。
Confidence: MEDIUM
Validity Window: 2026-W37 to 2026-W42
Invalidation Trigger: A2A 标准化失败或 MCP 官方自身拓展出涵盖多智能体协同功能的成熟扩展。
Host Repository Change: NO

Decision ID: DEC-2026W36-03
Decision: 将针对 AI Agent 的持久化执行（Durable Execution）基建作为基础层设施进行跟踪。
Decision Type: CONTINUE_WATCH
Evidence: 行业工程分析指出，传统短生命周期请求模型无法满足长时间运行的 Agent 需求，因此云托管运行时和框架原生平台均开始强调基于 Checkpoint 的持久化执行。
Independent Evidence: 多种框架和平台（AWS Bedrock AgentCore, LangGraph Platform）独立推进了类似架构。
Repository Record Comparison: 符合本月早期 H6 关于多智能体系统基础设施演进的长期观察基线。
Counterevidence: 许多简单的单轮 Agent 任务并不需要引入复杂的持久化执行引擎。
Expected Value: 当未来宿主仓库遇到长周期 AI 任务时，可提供底层运行时架构参考。
Risk: 持久化框架目前仍处于厂商碎片化阶段，尚未形成单一主导开源标准。
Why Now: 随着 Agent 从简单的对话转向自主完成长周期的复杂任务，底层 Runtime 的持久化需求日益凸显。
Confidence: MEDIUM
Validity Window: 2026-W37 to 2026-W44
Invalidation Trigger: LLM 原生支持更长时间线的状态维持而无需外部复杂的持久化框架。
Host Repository Change: NO

DO_NOT_PURSUE

- 明确不追的方向：不要将云厂商（如 AWS Connect）的 MCP 特定实施方案或配置参数当作 MCP 协议的通用强制要求。
- 原因：特定商业平台的实现细节带有平台强绑定属性（如 IAM 安全配置），不适用于一般性的开源仓库或跨平台系统。
- 重新考虑所需证据：除非该安全配置或落地细节被 MCP 官方重新吸收为开源标准规范（RFC 级别）。

HANDOFF_TO_H4

- 观察重点: MCP 2026-07-28 版本的无状态机制在更多第三方非 AI 工具中的集成反馈；A2A (Agent-to-Agent) 协作协议标准化进展。
- 验证重点: 区分协议层面的更新事实（如 MCP 无状态）与厂商部署层面的实际采纳情况。
- 来源质量要求: 优先获取独立的一线开发者实践或集成平台（如 Auth0, Merge）的工程博客，避免单一依赖官方宣发。
- 叙事边界: 明确 MCP 解决的是外部工具连通性（Tooling），而非多智能体自我协调与发现（Agent Collaboration, A2A）。
- 不确定性提醒: A2A 标准仍在早期，不要过早采信某一特定厂商的独家方案。
- Watchlist 延续: AI Agent Runtime 层的持久化执行 (Durable Execution) 支持情况。
- 主题降级: 放弃跟踪 MCP 规范中已废弃的 Roots、Sampling 和 Logging 功能。

BOUNDARY_CHECK

确认未越界：YES
确认未实施宿主仓库决策：YES
确认未升级长期记忆：YES
