# 🎯 监控目标 (Target)
监控 Google 的 python-genai 仓库最新发布动态，提取新特性和文档更新

# 🚀 新版本发布 (New Release)
Google GenAI 官方 Python SDK (python-genai) 发布了 v2.10.0 版本，带来了多项新功能：

- 平台核心增强：支持 Agent Platform MCP 的异步流式内容生成 (async generate_content_stream)
- 交互与模型扩展：在 ComputerUse 模块中添加了 disabled_safety_policies 选项，同时加入了针对步骤 (steps) 的用量字段
- 媒体与输出配置：新增了视频生成功能和响应格式参数设定
- 文档质量优化：修复了代码文档字符串 (docstrings) 中的各类拼写错误

# 💡 架构洞察 (Architectural Insight)
本次更新深化了 SDK 与大模型 Agent 生态的结合，MCP 的支持为跨工具上下文协议交互提供了标准流式基座；禁用安全策略的选项则赋予了高阶开发者更多的调用灵活性，进一步提升了该框架作为智能体开发基础设施的成熟度
