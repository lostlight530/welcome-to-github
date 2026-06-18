# 🎯 监控目标 (Target)
Google Python GenAI 官方 SDK

# 🚀 新版本发布 (New Release)
发布了 v2.9.0-rc1 版本
新增了针对 VoiceActivity 的 audioOffset 支持
将 gemini-3-flash-preview 加入到了本地的分词器映射中
在 LiveServerContent 中增加了 interimInputTranscription
在 AudioTranscriptionConfig 中加入了 LanguageAuto 以及 LanguageHints 和 adaptationPhrases 支持
扩展了发布者模型路径的检查机制以支持所有发布者

# 💡 架构洞察 (Architectural Insight)
本次更新重点增强了对音频和语音相关的支持，加入了诸如 VoiceActivity 音频偏移量调整以及 AudioTranscriptionConfig 多语言适配的配置机制，为实时多模态交互提供了更多控制参数
同时本地分词器加入了新版本的预览模型支持，显示出官方在快速迭代模型能力并推动边缘计算和本地处理结合的趋势

---