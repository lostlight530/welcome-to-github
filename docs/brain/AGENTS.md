AGENTS.md
目标

本仓库采用“自动侦察 → 证据提炼 → PR 审核 → 记忆入库”的工程化闭环。
任何 Agent（含 Jules）必须优先保证：可审计、可回滚、低噪音、人在环。

角色分工

Agent：负责检索、提炼、生成候选结论与变更（只提交 PR）

人类：负责最终合并、记忆取舍、方向决策（Human-in-the-loop）

强约束（必须遵守）

禁止直推 main：所有输出必须通过 PR。

Append-only：历史记录不覆盖；错误用“追加更正”修正。

事实/推断分层：

Facts：必须有可核验来源链接支持

Hypothesis：必须标注“推断”，并引用对应 Facts

只做技术文档/官方源头侦察：避免泛新闻与无来源结论。

输出可变长：允许“今日无强信号”；禁止为了凑模板制造噪音。

允许写入的目录（白名单）

docs/daily-briefs/（每日简报）

docs/archaeology/（数字考古与更正记录）

docs/index.md 或 docs/README.md（索引）

除上述目录外，默认不改动代码与依赖；如需改动，必须在 PR 中说明理由与风险，并请求人类确认。

每日简报文件规范

新建：docs/daily-briefs/YYYY-MM-DD.md

追加索引：docs/daily-briefs/README.md（只追加一行链接）

YYYY-MM-DD.md 推荐结构（可缺省）：

今日主题（1–3 条）

Facts（1–7 条：一句话结论 + 为什么重要 + 来源链接）

Hypothesis（可选：推断 + 依据的 Facts 链接）

Risks / Breaking（可选：必须有证据；否则降级为 Attention）

Action（可选：若无强信号则写“无行动项”）

Memory Candidates（<=5 条：候选，不做最终记忆决策）

变更审计要求（PR 描述必须包含）

变更范围（写入了哪些文件）

今日最高信号（1–2 条）

主要来源列表（官方文档/发布说明/仓库链接）

关于 Jules 的约定提示

Jules 会读取本 AGENTS.md 以生成更贴合的计划与输出。

Jules Web Search 仅用于技术文档/代码片段检索，不做泛新闻。

Scheduled Tasks 可用于每日/每周自动运行；如 UI/文档描述冲突，以 Jules Changelog 为准。
