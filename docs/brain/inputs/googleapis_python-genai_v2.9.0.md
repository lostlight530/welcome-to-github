# 🎯 监控目标 (Target)
Google Python GenAI 官方 SDK

# 🚀 新版本发布 (New Release)
本次发布的 v290 版本包含了重大更新与多项新特性
核心交互实现 interactions 被完全替换，但公共 API 层面保持了向后兼容
在模型支持方面，本地分词器映射新增了 gemini-3-flash-preview 的支持，同时加入了对 Gemma 4 的本地分词器支持
针对多模态与语音能力，VoiceActivity 增加了 audioOffset 属性，LiveServerContent 新增 interimInputTranscription 支持
音频转录配置也加入了 LanguageAuto 提示 LanguageHints 及 adaptationPhrases 等多项参数
此外，新版本暴露了 Computer Use API 字段，放宽了发布者模型路径的检查以支持所有发布者，并在 UsageMetadata 中加入了 ServiceTier
交互 API 方面也有所完善，modelsProto 中引入了 presence_penalty 及 frequency_penalty 字段，StreamMetadata 中的 usage 也被重命名为 total_usage

# 💡 架构洞察 (Architectural Insight)
核心交互实现的完全重构表明底层通信或会话管理机制经历了重大升级，可能旨在提升性能或扩展灵活性，同时保持公共 API 不变体现了良好的工程约束和向后兼容性保证
暴露 Computer Use API 和强化各类多模态参数支持，反映出该 SDK 正在加速适配更复杂的智能体与多模态交互场景，特别是语音流与跨模型本地化的增强，为开发者构建下一代边缘与端侧 AI 提供了更完善的工具链支持
