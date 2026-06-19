# 🎯 监控目标 (Target)
Google Edge AI 与 GenAI 生态核心库 googleapis/python-genai

# 🚀 新版本发布 (New Release)
本次 v2.9.0-rc1 候选版本带来了多项激动人心的新特性
首先在语音活动识别中新增了 audioOffset 支持
同时为实时服务端内容增加了 interimInputTranscription 字段
在音频转录配置方面 引入了 LanguageAuto、LanguageHints 以及 adaptationPhrases 等关键配置项
此外 本地分词器映射现已支持 gemini-3-flash-preview 模型
系统还放宽了发布者模型路径的检查机制 以兼容所有的发布者环境

# 💡 架构洞察 (Architectural Insight)
此次更新全面强化了音频处理与语音活动的实时交互能力
新增的转录与语言配置项将极大提升多语言场景下的自适应表现
对 gemini-3-flash-preview 的支持表明 Google 正在加速下一代轻量级模型的生态布局
放宽发布者路径限制则体现了架构向更开放、更兼容的多模型环境演进的趋势
建议开发者重点关注音频流式处理与实时交互界面的集成方案