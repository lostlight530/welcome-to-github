# 🎯 监控目标 (Target)
追踪 Model Context Protocol (MCP) 官方 Python SDK 核心协议演进

# 🚀 新版本发布 (New Release)
MCP Python SDK 迎来了 v2 架构的第三个 Alpha 预览版 (v2.0.0a3)，正式将无状态协议 (stateless protocol) 协商落地：

- 无状态协议端到端打通：基于 2026-07-28 规范，流式 HTTP 模式废弃了握手初始化，服务器将各 POST 请求视为携带协议版本和客户端参数的独立实体；ServerRunner 被重构为纯处理内核，由三种驱动混合组成；而客户端 ClientSession 引入了 discover 和 adopt 方法来实现无阻力版本协商
- 协议类型解耦拆分：所有的底层协议数据类型和版本常量被拆分至独立包 mcp-types，轻量级客户端只需依赖 pydantic 即可实现 MCP 流量验证，大幅减轻 httpx 或 starlette 依赖
- 多轮工具调用与中间件升级：两端彻底接入了 InputRequiredResult 机制，实现了更为复杂的多轮工具调用状态恢复；ServerMiddleware 变更为只接收上下文与 call_next 参数的新模型，并且引入了 OpenTelemetryMiddleware 以支持 GenAI 语义追踪
- 权限严苛性增强：OAuth 客户端合规性全面增强，引入对 SEP 系列提案的支持，解决跨域绑定、刷新令牌驻留等边缘安全问题

# 💡 架构洞察 (Architectural Insight)
向无状态 HTTP 的全面跃迁标志着 MCP 架构从传统长链接 RPC 走向 Serverless 友好的现代微服务范式；将 mcp-types 单独剥离更是典型的核心极简主义设计，这不仅降低了边缘设备的集成门槛，还展现了协议在迈向生产级标准时的去中心化架构思维
