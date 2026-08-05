# Security Policy

## Supported State

Security fixes apply to the latest commit on `main`.

Feature branches, pull requests, generated reports, and historical snapshots are not maintained as independent release lines.

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
