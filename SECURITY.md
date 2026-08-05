# Security Policy

## Supported Versions

This repository operates under the deterministic autonomy architecture and is governed by Phase VII protocols.

| Version | Supported |
| --- | --- |
| Phase VII (Current) | :white_check_mark: |
| Phase VI | :white_check_mark: |
| Phase V & Below | :x: |

## Reporting a Vulnerability

If you discover a vulnerability or a violation of the Trust Gateway / Zero-Dependency protocols, please submit a detailed report.

The repository runs on GitHub Actions with deterministic cron schedules. The Trust Gateway actively penalizes malformed MCP requests. If a security issue is identified, it will be analyzed within the deterministic pipeline and addressed promptly.

## Scope

- GitHub Actions workflows (`.github/workflows/`)
- Nexus lifecycle automation
- Harvester data pipeline
- Pages deployment (`index.html` via CDN Tailwind)
- `docs/brain/` knowledge graph runtime

Out of scope: archived historical assets under `docs/archaeology/` and `docs/brain/knowledge/archive/`.
