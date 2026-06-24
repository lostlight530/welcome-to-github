# 🎯 监控目标 (Target)
Google Edge AI 与 GenAI 核心库 googleapis/python-genai 最新动态

# 🚀 新版本发布 (New Release)
v2.10.0 版本带来了多项增强功能
首先，针对异步内容生成流 (async generate_content_stream) 增加了 Agent Platform MCP 支持，提升了平台整合能力
其次，在模型 (Models) 和交互 (Interactions) 层面均添加了 ComputerUse.disabled_safety_policies 配置，增强了策略调控的灵活性
同时，为步骤 (steps) 新增了使用情况统计字段 (usage fields)，便于更好地监控和追踪运行状态
此外，还引入了视频生成和响应格式参数 (video generation and response format parameters)，丰富了媒体处理能力
在文档方面，修复了多处文档字符串 (docstrings) 中的拼写错误，提升了代码库的可读性

# 💡 架构洞察 (Architectural Insight)
本次更新显著强化了在 MCP 环境下的异步流处理能力，表明该库正积极向更复杂的 Agent 架构靠拢
通过增加禁用安全策略的配置项，开发者在受控环境中获得了更大的自由度
同时对运行步骤增加监控指标和扩展视频生成参数，进一步完善了从监控到多媒体处理的全栈功能支持
