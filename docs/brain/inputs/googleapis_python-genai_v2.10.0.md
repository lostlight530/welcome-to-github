# 🎯 监控目标 (Target)
Google Edge AI 与 GenAI 核心工具链更新 (googleapis/python-genai)

# 🚀 新版本发布 (New Release)
v2.10.0 版本于 2026 年 06 月 24 日发布，包含以下主要更新内容：
- [特性] 增加了对 Agent Platform MCP 的支持，用于异步 generate_content_stream 方法
- [交互] 添加了 ComputerUse disabled_safety_policies 设置
- [模型] 同样增加了 ComputerUse disabled_safety_policies 选项
- [功能] 针对各步骤 (steps) 补充了使用情况字段 (usage fields)
- [功能] 增加了视频生成 (video generation) 以及响应格式 (response format) 相关参数
- [文档] 修正了多个文档字符串中的错别字

# 💡 架构洞察 (Architectural Insight)
此次更新表明 Google 在 Edge AI 场景中进一步加强了对 MCP 协议的集成，这对于扩展代理能力与异步流处理具有积极意义，并且放宽/精细化了计算机使用场景的安全策略配置，使得本地模型调度更加灵活
