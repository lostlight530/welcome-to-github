const translations = {
    zh: {
        title: "lostlight | 2025-2026 年度回顾",
        nav: {
            home: "首页",
            achievements: "年度成就",
            projects: "核心项目",
            philosophy: "工程哲学"
        },
        hero: {
            role: "端侧 AI 实践者",
            tagline: "低调。务实。<br><span class='gradient-text'>极致工程化。</span>",
            description: "专注 Python + AI，深耕 Google 生态与国产 AI 架构。追求代码的可读性、可测性与可维护性。"
        },
        achievements: {
            title: "2025 荣耀时刻",
            googleBadges: "13 枚 Google 开发者勋章",
            awards: "4 项国家级/省级竞赛奖项",
            awardList: [
                "华为 ICT 大赛中国总决赛二等奖",
                "昇思 MindSpore 创新训练营二等奖",
                "蓝桥杯智能体开发省赛三等奖",
                "金砖国家技能大赛鸿蒙赛道晋级"
            ]
        },
        projects: {
            title: "核心项目矩阵",
            items: [
                {
                    name: "MediaPipe Tasks AI 助手",
                    desc: "基于 Android + MediaPipe 的端侧健身/手指操纠错助手。采用状态机逻辑，实现低延迟、高精度的姿态识别。",
                    tech: "Android / MediaPipe / Kotlin"
                },
                {
                    name: "消防面板视觉检测",
                    desc: "针对 128 键复杂面板的高精度算法。结合仿射变换与 RANSAC，解决极端畸变与光影问题。",
                    tech: "OpenCV / Python / RANSAC"
                },
                {
                    name: "ClassVision 分布式系统",
                    desc: "FastAPI + YOLOv8 驱动的课堂诊断平台。支持 Docker 容器化部署，具备完善的日志与监控逻辑。",
                    tech: "Docker / FastAPI / YOLOv8"
                }
            ]
        },
        philosophy: {
            title: "工程化哲学",
            content: "不追逐短期炒作（Hype），坚持技术深度。推崇 DDD 领域驱动设计、自动化测试与配置隔离。每一个 Commit 都是对“小而稳”承诺的践行。"
        },
        footer: {
            greeting: "新春快乐 | Happy Chinese New Year 2026"
        }
    },
    en: {
        title: "lostlight | 2025-2026 Year in Review",
        nav: {
            home: "Home",
            achievements: "Achievements",
            projects: "Projects",
            philosophy: "Philosophy"
        },
        hero: {
            role: "Edge AI Practitioner",
            tagline: "Quiet. Pragmatic.<br><span class='gradient-text'>Engineering Excellence.</span>",
            description: "Focusing on Python + AI, deeply involved in Google ecosystem and domestic AI architectures. Dedicated to readability, testability, and maintainability."
        },
        achievements: {
            title: "2025 Highlights",
            googleBadges: "13 Google Developer Badges",
            awards: "4 National/Provincial Awards",
            awardList: [
                "2nd Prize, Huawei ICT Competition China Finals",
                "2nd Prize, MindSpore Innovation Bootcamp",
                "3rd Prize, Lanqiao Cup AI Agent Development",
                "Finalist, BRICS Skills HarmonyOS Track"
            ]
        },
        projects: {
            title: "Project Matrix",
            items: [
                {
                    name: "MediaPipe Tasks AI",
                    desc: "Edge-based fitness/hand exercise assistant using Android & MediaPipe. Features state-machine logic for low-latency posture correction.",
                    tech: "Android / MediaPipe / Kotlin"
                },
                {
                    name: "Fire Panel Vision Detection",
                    desc: "High-precision algorithm for 128-key panels. Combines Affine Transform & RANSAC to handle extreme distortion and glare.",
                    tech: "OpenCV / Python / RANSAC"
                },
                {
                    name: "ClassVision Distributed System",
                    desc: "FastAPI + YOLOv8 driven diagnostic platform. Supports Docker orchestration with robust logging and monitoring.",
                    tech: "Docker / FastAPI / YOLOv8"
                }
            ]
        },
        philosophy: {
            title: "Engineering Philosophy",
            content: "Avoiding hype, prioritizing depth. Advocating for DDD, automated testing, and configuration isolation. Every commit is a practice of 'Small and Stable'."
        },
        footer: {
            greeting: "Happy Chinese New Year 2026"
        }
    }
};

export default translations;
