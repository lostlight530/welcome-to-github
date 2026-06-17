# 🎯 监控目标 (Target)
Google Edge AI GenAI (python-genai) 最新的发布动态

# 🚀 新版本发布 (New Release)
发布了 v2.9.0-rc0 版本
主要更新包括交互实现被完全替换，公开的 API 表面保持不变
新特性方面，在 UsageMetadata 中添加了 ServiceTier，暴露了 Computer Use API 字段，并且支持了 Gemma 4 本地分词器 此外，交互 API 在 models.proto 中添加了 presence_penalty、frequency_penalty 和 cached_content，并且在 StreamMetadata 中将 usage 重命名为 total_usage
修复了包括为 aiohttp.readline 增加向后兼容性，修复请求头，以及隐藏实时音乐 API keys 避免在 websocket urls 中泄漏等问题
文档方面宣布了自动函数调用 (AFC) 即将发生的破坏性变更，以及澄清了 Live API 的一些默认设置问题

# 💡 架构洞察 (Architectural Insight)
在保持 API 稳定性的同时，底层交互实现的完全替换展示了良好的架构抽象能力
将 transformers 作为可选依赖项，体现了对减少项目冗余依赖和增强本地分词器灵活性的考量
对依赖问题的向后兼容修复，确保了用户体验的平滑过渡
