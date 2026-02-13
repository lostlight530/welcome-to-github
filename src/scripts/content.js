export const translations = {
  zh: {
    brand: "LOSTLIGHT",
    status: "系统就绪",
    nav: ["首页", "核心能力", "项目矩阵", "工程哲学"],
    hero: {
      title: "端侧 AI 开发者",
      subtitle: "低调务实 / 追求极致 / 稳健交付",
      desc: "专注 Python 与端侧 AI 生态集成，致力于在资源受限环境下实现高效、可扩展的工程解。深耕 Google MediaPipe 与华为昇腾生态。"
    },
    stats: [
      { label: "开发者勋章", value: "13+", unit: "Google" },
      { label: "全国性奖项", value: "4", unit: "Awards" },
      { label: "工程项目", value: "20+", unit: "Repos" }
    ],
    engines: {
      title: "双引擎技术栈",
      google: {
        name: "Google Ecosystem",
        tags: ["MediaPipe", "Vertex AI", "Gemini API", "Firebase"]
      },
      domestic: {
        name: "华为/国内生态",
        tags: ["Ascend 昇腾", "MindSpore 昇思", "HarmonyOS", "DeepSeek"]
      }
    },
    projects: {
      title: "核心项目矩阵",
      items: [
        { name: "MediaPipe Tasks AI", tech: "Android / Kotlin", desc: "端侧实时姿态纠错算法，实现亚秒级动作逻辑判断与反馈。" },
        { name: "消防面板视觉识别", tech: "OpenCV / RANSAC", desc: "复杂环境下 128 键位面板精准检测，解决畸变与强光干扰。" },
        { name: "ClassVision 系统", tech: "FastAPI / Docker", desc: "分布式课堂诊断平台，支持容器化大规模部署与日志审计。" },
        { name: "端侧 LLM 推理优化", tech: "TensorFlow Lite", desc: "轻量化模型压缩与量化实践，提升移动端生成式 AI 响应速度。" },
        { name: "自动化验证流水线", tech: "GitHub Actions", desc: "自研工程级 CI/CD 逻辑，确保代码变更的 100% 结构合规性。" },
        { name: "鸿蒙原生 AI 集成", tech: "ArkTS / HarmonyOS", desc: "基于 HarmonyOS Next 的端侧视觉感知模块开发与调优。" }
      ]
    },
    philosophy: {
      title: "工程哲学",
      content: "“小而稳”高于“大而乱”。每一行代码都应具备可测试性，每一个架构决策都应面向长期维护。拒绝追逐短期炒作，坚持技术深耕。"
    },
    footer: "© 2026 LOSTLIGHT | 数字考古记录于 docs/archaeology"
  },
  en: {
    brand: "LOSTLIGHT",
    status: "SYSTEM READY",
    nav: ["HOME", "CAPABILITY", "MATRIX", "PHILOSOPHY"],
    hero: {
      title: "Edge AI Developer",
      subtitle: "Quiet / Pragmatic / Stable Delivery",
      desc: "Specializing in Python & Edge AI ecosystem integration. Delivering high-performance, scalable solutions in resource-constrained environments."
    },
    stats: [
      { label: "Badges", value: "13+", unit: "Google" },
      { label: "National", value: "4", unit: "Awards" },
      { label: "Engineering", value: "20+", unit: "Repos" }
    ],
    engines: {
      title: "Dual-Engine Foundations",
      google: {
        name: "Google Ecosystem",
        tags: ["MediaPipe", "Vertex AI", "Gemini API", "Firebase"]
      },
      domestic: {
        name: "Huawei/Domestic",
        tags: ["Ascend", "MindSpore", "HarmonyOS", "DeepSeek"]
      }
    },
    projects: {
      title: "Project Matrix",
      items: [
        { name: "MediaPipe Tasks AI", tech: "Android / Kotlin", desc: "Real-time edge-based pose correction with sub-second logic validation." },
        { name: "Fire Panel Vision", tech: "OpenCV / RANSAC", desc: "Precise 128-key detection under extreme distortion and glare." },
        { name: "ClassVision System", tech: "FastAPI / Docker", desc: "Distributed diagnostic platform with containerization and audit logging." },
        { name: "Edge LLM Optimization", tech: "TensorFlow Lite", desc: "Model compression and quantization for high-speed mobile GenAI." },
        { name: "Auto Verification CI", tech: "GitHub Actions", desc: "Custom CI/CD logic ensuring 100% structural compliance of code." },
        { name: "HarmonyOS AI Native", tech: "ArkTS / HarmonyOS", desc: "Vision perception module development and tuning on HarmonyOS Next." }
      ]
    },
    philosophy: {
      title: "Philosophy",
      content: "'Small and Stable' over 'Large and Messy'. Every line must be testable. Every decision must be maintainable. Depth over Hype."
    },
    footer: "© 2026 LOSTLIGHT | Archaeology archived in docs/archaeology"
  }
};
