# Welcome public frontends — maintenance boundary

This directory records the source, artifact and historical-release boundaries for the two distinct Welcome surfaces; it is not a parallel project database

## Two public surfaces

| Role | Maintained source | Status |
| --- | --- | --- |
| Current research portal | repository root `index.html`, root `package.json`, `tools/verify-welcome-public-surface.mjs` | Current entry, Vite-built as Pages root |
| Historical Yearbook | `public/yearbook/index.html` and `public/yearbook/src/scripts/translations.js` | Preserved, separately maintained historical reading surface |
| Method / review record | `docs/public-surface/2026-11-13-welcome-navigation-evidence.md` | Audit/decision evidence, not deployment input |

The Yearbook is **not** a disposable transition file; avoid importing its historical presentation into the current research portal or silently rewriting its dated narrative. It remains a distinct published route under `/welcome-to-github/yearbook/`

## Invariants

- Keep each page's Chinese visible text free of the full-stop glyph `U+3002`, without changing numeric decimal points, URLs or archival evidence
- Root navigation and Yearbook links must resolve to exact same-origin Pages routes; no speculative runtime claims or current-statistics conversion
- Deployment builds with `npm ci` and `npm run build -- --base=/welcome-to-github/`; the existing verify workflow checks linked assets, base path and route targets
- Do not delete historical review records, `AGI/**`, `docs/brain/**` or Yearbook assets as though they were intermediate build files
- Older pages remain recoverable through Git history; new visual changes belong in the current source files and reviewed PRs, not a second live homepage copy

Prior frontend update: [PR #976](https://github.com/lostlight530/welcome-to-github/pull/976)
