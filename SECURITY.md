# Security Policy


## Supported State

Security fixes apply to the latest commit on `main`.

Feature branches, pull requests, generated reports, and historical snapshots are not maintained as independent release lines.

### 中文安全报告与发布边界 / Private reporting and publication boundary

疑似敏感信息或漏洞应使用下方私密渠道，公开 Issue、PR、Pages 或 DOI 附件不得包含密钥、令牌、私人研究材料及未经修复的可利用细节；代码扫描、哈希与公开归档只证明其自身检查范围，不保证完整安全

Use the private reporting route below for suspected security issues; do not place secrets, tokens, private research information or unpatched exploit details into public issues, PRs, Pages or archive files. A scanner, digest or public archive supports only its tested security scope

## Private Reporting

Report suspected vulnerabilities through [GitHub Private Vulnerability Reporting](https://github.com/lostlight530/welcome-to-github/security/advisories/new).

Do not open a public issue containing:

- credentials, tokens, or private data
- working exploit details
- unpatched workflow or Pages weaknesses
- information that could put another repository or user at risk

A useful report includes the affected path, commit SHA, reproducible steps, expected boundary, observed behavior, and potential impact.

Reports are reviewed on a best-effort basis. No automated system accepts, triages, or resolves security reports without human review.

## Scope

Security-relevant surfaces include:

- GitHub Actions workflows under `.github/workflows/`
- lifecycle and harvesting code under `docs/brain/`
- active knowledge and input processing
- the GitHub Pages presentation layer
- repository permissions and generated-artifact write boundaries

## Security Boundaries

- This repository does not operate a public MCP server or remote Trust Gateway.
- Deterministic validation reduces ambiguity but does not authenticate an external source.
- A SHA-256 digest proves content identity, not author identity or trust.
- Generated knowledge remains untrusted until its provenance and active-ledger constraints are verified.
- GitHub Actions permissions are limited by each workflow and remain subject to human review.

## Historical Material

Historical assets under `docs/archaeology/` and archive directories are preserved as evidence and are not active runtime components.

Incorrect or obsolete historical claims are normally out of scope. Exposed credentials, private data, unsafe executable content, or paths that affect the active runtime remain reportable regardless of location.
