# Contributing

> **Current bilingual reading guide / 当前双语阅读指引（2026-11-13）**  
> **中文**：分别核对公共入口、记忆与编排实现、Yearbook 展示和研究证据，避免混合权威；这是一项根目录说明校准，不代表执行新任务或更改私有生产者 SOP  
> **English**: Review portal, memory/orchestration implementation, Yearbook presentation, and research evidence as separate authority surfaces. This root-document calibration does not execute a new task or publish private producer SOPs


## Open research contributions

For research-method contributions, start with [`OPEN_RESEARCH.md`](./OPEN_RESEARCH.md). For new bounded research records, use [`RESEARCH_TEMPLATE.md`](./RESEARCH_TEMPLATE.md). Repository-native implementation, methodology, evidence, and historical contracts remain authoritative for their own surfaces.

Contributions are welcome when they improve the public portal, repository-owned implementation, research documentation, evidence surfaces, metadata, or developer experience without blurring the boundary between observed evidence and interpretation.

## Choose the owning surface first

This repository contains several distinct public surfaces. Keep a change with the surface that owns it:

- root documentation and the GitHub Pages portal — public project and portfolio presentation;
- repository-owned Python and lifecycle code — deterministic implementation and state-processing behavior;
- `horizon-cortex/` and `parallax/` — research/evidence surfaces with their own current contracts;
- archaeology and archived material — historical evidence that should remain point-in-time unless a correction is explicitly required;
- `.github/`, citation files, release metadata, security, and contribution documents — repository infrastructure.

A change in one surface does not automatically authorize changes in another.

## Before proposing a change

1. Start from current `main` and identify the current file, implementation, contract, or public surface that owns the behavior you want to change.
2. Separate current implementation, observed execution, external source claims, repository analysis, and proposals.
3. For code changes, define the input/output or state-transition behavior and add or update proportionate regression coverage.
4. For research or evidence changes, identify the exact source, date/version, supported proposition, uncertainty, and local applicability.
5. Preserve historical records when a forward correction or current-document update is sufficient.
6. Keep the change bounded and reviewable; avoid unrelated cleanup in the same pull request.

### Stage and citation review / 阶段与引用审阅

更改公开入口、项目地图或长期指标时，必须先辨认原始十仓、独立控制仓和生科仓，列出对应来源路径、Git SHA、观察日期、派生规则与可复核结果；不能把旧 snapshot 数字改写成 live 指标，也不能让 Yearbook、当前主页、自动维护记录和 DOI 相互背书

For portal, portfolio-map or longitudinal-metric changes, identify the original ten, the independent control repository and the separate life-science repository; cite source path, Git SHA, observation date, derivation and verification result. Do not relabel a frozen snapshot as a live metric or let the Yearbook, current landing page, automation history and DOI validate one another

## Evidence and documentation

Public prose should describe only what the linked implementation, source, artifact, or retained observation supports.

Keep these distinctions explicit when material:

```text
source exists != claim is true
file exists != task executed
checker passes != scientific validation
hash identity != semantic equivalence
current repository state != historical observation
archived publication != later main revision
```

When a source or result is uncertain, retain that uncertainty rather than strengthening the wording for readability.

## Implementation and dependencies

Follow existing repository conventions and prefer the smallest dependency surface that solves the problem. New runtime dependencies, external services, public network exposure, or authority-bearing mechanisms require a clear justification, failure model, and rollback path.

Do not bundle generated artifacts, caches, credentials, private data, or unrelated local state into a contribution.

## Verification

Run checks that are relevant to the changed surface and supported by the repository. In the pull request, list the commands or review steps actually performed and their observed results.

Do not describe a check as passed when it was not run. If a relevant check could not be executed, state that limitation directly.

For evidence/document changes, verification may include source inspection, link/version checks, schema/format validation, and comparison against the current owning implementation or contract. Documentary review is not a substitute for runtime execution when runtime behavior is being claimed.

## Pull requests

Use the repository pull-request template and include:

- a concise explanation of the problem and change;
- the affected repository surfaces;
- implementation, evidence, compatibility, or metadata impact as applicable;
- verification actually performed;
- known limitations or checks not performed;
- security/privacy impact when relevant;
- the smallest practical rollback.

Keep historical or externally sourced material attributable. Do not silently rewrite point-in-time evidence to make it match later knowledge.

## Security and privacy

Follow [SECURITY.md](./SECURITY.md) for sensitive security reports. Do not publish credentials, private data, exploit details that require coordinated disclosure, or non-public source material in issues or pull requests.

## Conduct, license, and attribution

Keep discussion technical, specific, and respectful. Contributions to repository-owned work are submitted under the current `LICENSE`. Third-party material retains its own attribution and licensing, and Git/PR history remains the source of contribution attribution.
