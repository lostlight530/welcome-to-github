# 🎯 监控目标 (Target)
Google Edge AI/GenAI (googleapis/python-genai) 版本 v2.9.0

# 🚀 新版本发布 (New Release)
本次 v2.9.0 版本迎来了重大更新，交互功能的实现已被完全替换，但公共 API 接口保持不变
此外，新版本还引入了多项重要功能：
- 在 VoiceActivity 中新增 audioOffset 功能
- 本地分词器现已支持 gemini-3-flash-preview 模型
- 在 LiveServerContent 中加入 interimInputTranscription
- 在 AudioTranscriptionConfig 中添加 LanguageAuto、LanguageHints 及 adaptationPhrases
- 扩大发布者模型路径的检查范围以支持所有发布者
- 在 UsageMetadata 中新增 ServiceTier 字段
- 开放 Computer Use API 字段
- 增加 Gemma 4 本地分词器支持
- 在 interaction-api 中增加 presence_penalty、frequency_penalty 以及 cached_content 字段
- 将 StreamMetadata 中的 usage 字段重命名为 total_usage

# 💡 架构洞察 (Architectural Insight)
本次更新虽然在底层完全重构了交互功能，但通过保持公共 API 的不变性，有效保障了向下兼容与开发者的平滑过渡
引入多个实验性及早期预览特性，如对 gemini-3-flash-preview 和 Gemma 4 本地分词器的支持，表明系统在快速整合最新 AI 模型能力
同时扩展了音频转录与活跃度检测相关的配置选项，进一步丰富了多模态交互的处理能力
修复了 aiohttp 的兼容性问题以及 WebSocket 安全相关的漏洞，体现了对系统稳定性和安全性持续优化的追求
