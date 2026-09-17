# 特殊专题

特殊专题记录具有独立公共价值的事件核验.

它们不替代 Daily, 不增加 assigned-date continuity, 也不因为事件重要或页面数量多就自动增加 CASE support 或 NOTES finding.

Special 的作用是把真实公共事件映射成可证伪研究问题, 并保留 event time, observation time, current state, publisher identity 与 evidence limitation.

## 当前计数

- 特殊专题: 13
- 当前最新特殊专题事件日期: 2026-08-28
- 2026-09-01 至 2026-09-17: 0 个新 Special
- 9 月研究生产全部由 Daily 完成, Special 不承担 Daily continuity

## 专题索引

| 事件日期 | 记录 ID | CASE | 实际核验日期 | 当前研究关系 | 专题 |
| --- | --- | --- | --- | --- | --- |
| 2026-07-21 | PX-S-20260721-P04 | P-04 | 2026-07-31 | security-event attribution 与 later final report relation | [OpenAI 与 Hugging Face 安全事件归因更新](2026-07/2026-07-21-openai-hugging-face-security-incident.md) |
| 2026-07-25 | PX-S-20260725-P03 | P-03 | 2026-07-26 | impact scope 与 missing denominator | [OpenAI 错误率事件范围](2026-07/2026-07-25-openai-service-events.md) |
| 2026-07-27 | PX-S-20260727-P03 | P-03 | 2026-07-29 | maintenance state 与 unverified user write action | [OpenAI 开发者社区受限维护](2026-07/2026-07-27-openai-developer-community-maintenance.md) |
| 2026-07-30 | PX-S-20260730-P03 | P-03 | 2026-07-31 | multi-incident scope separation | [OpenAI 近期四场服务事件](2026-07/2026-07-30-openai-recent-service-events.md) |
| 2026-07-31 | PX-S-20260731-P03 | P-03 | 2026-08-01 | partial-user impact 与 missing denominator | [OpenAI 企业与教育对话错误事件](2026-07/2026-07-31-openai-enterprise-education-chat-errors.md) |
| 2026-08-04 | PX-S-20260804-P03 | P-03 | 2026-08-05 | current incident state 与 affected-scope identity | [OpenAI ChatGPT 对话错误事件](2026-08/2026-08-04-openai-chatgpt-conversation-errors.md) |
| 2026-08-04 | PX-S-20260804-P05 | P-05 | 2026-08-05 | developer claim 与 independent evaluator evidence | [OpenAI 第三方网络安全评估事件](2026-08/2026-08-04-openai-third-party-cyber-evaluations.md) |
| 2026-08-05 | PX-S-20260805-P03 | P-03 | 2026-08-06 | separate incidents and component scope | [OpenAI 三项服务事件](2026-08/2026-08-05-openai-service-events.md) |
| 2026-08-13 | PX-S-20260813-P05 | P-05 | 2026-08-13 | cross-provider evaluation comparability | [OpenAI, Anthropic 与 Google 前沿模型官方评价可比性](2026-08/2026-08-13-frontier-model-evaluation-comparability.md) |
| 2026-08-21 | PX-S-20260821-P05 | P-05 | 2026-08-23 | scientific experiment result-branch and evidence-type identity | [Anthropic CHIVE counterfactual explanations](2026-08/2026-08-21-anthropic-chive-counterfactual-explanations.md) |
| 2026-08-21 | PX-S-20260821-P03 | P-03 | 2026-08-23 | research lifecycle boundary and deployment state | [DeepMind SIMA 与 EVE research lifecycle boundary](2026-08/2026-08-21-deepmind-sima-eve-research-boundary.md) |
| 2026-08-26 | PX-S-20260826-P04 | P-04 | 2026-08-28 | final report and earlier incident-state relation | [OpenAI Hugging Face final incident report](2026-08/2026-08-26-openai-hugging-face-final-incident-report.md) |
| 2026-08-28 | PX-S-20260828-P05 | P-05 | 2026-08-28 | social summary vs primary evidence identity | [X/Twitter AI 社交摘要与一手证据身份边界](2026-08/2026-08-28-x-ai-social-summary-source-boundary.md) |

## Current research role

Special 不再承担维护流水账角色.

动态页面发生变化时, 后续研究应在新的 Daily 或新的 Special 中明确记录 current-state cut 与 relation, 而不是把一串维护日志无限追加在 index 文件里.

历史 Special 正文继续作为 point-in-time evidence. 本索引只维护定位, identity 与当前研究关系.

## 下一阶段适用场景

优先创建 Special 的情况包括.

- 突发公开 incident 暴露新的 evidence identity 或 current-state ambiguity
- benchmark/evaluator 出现独立 correction, adjudication 或 version transition
- provider 与 independent evaluator 对同一对象形成可定位冲突
- aggregate recovery 与 per-object completion 出现可公开验证差异
- multi-agent, tool or retrieval chain 出现公开 provenance failure

如果事件只是在已有 Daily 问题上提供一条补充来源, 不需要为了数量新建 Special.

## 计数与 promotion 边界

- 一个完整 Special 可以是一个 research batch
- 同一 actual execution date 的多个 Daily/Special 共享 execution window
- Special 不增加 Daily continuity
- Special 不自动构成 independent publisher
- Special 不自动升级 observation -> candidate -> finding
- Special maintenance text 不计新的 batch 或 Trial

长期 promotion 仍完全服从 `METHOD.md` 和 `CASES.md` 的真实证据门槛.
