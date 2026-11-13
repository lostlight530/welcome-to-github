# Welcome Public Pages — Route, Source and UX Reconciliation (2026-11-13)

Status: **proposed correction in Draft PR #976**, not a deployed-main verification.
Repository: `lostlight530/welcome-to-github`
Reviewed baseline: `main@2bd359b9069db3e0304140d40136ad5200aa6c51`
Review branch: `agent/yearbook-mobile-menu-a11y-2026-11-13`
Pages base: `https://lostlight530.github.io/welcome-to-github/`

This is a **new, dated public-surface reconciliation**, not an alteration of the archived yearbook, historical research claims, NEXUS evidence or original project materials.

## Layered verification contract

| Layer | What it proves | Result / caveat |
| --- | --- | --- |
| GitHub source | The files and changes exist at the exact reviewed ref | Checked with GitHub file/PR APIs |
| GitHub upstream | The referenced repositories are public | Checked via GitHub repository API on 2026-11-13 |
| Published artifact contract | Built relative routes and document files resolve under the Pages base | Asserted by `tools/verify-welcome-public-surface.mjs` after the same Vite build **and memorial-copy step** as production |
| External Discussions | The practice-work discussion pages contain their original public records | Checked at GitHub Discussions #824 and #1816 on 2026-11-13; this is not an independent execution test |
| Real public Pages HTTP | A visitor can retrieve and navigate the latest version after deployment | **NOT_VERIFIED**: direct site requests from available clients were inaccessible |
| Browser/a11y behavior | CSS, keyboard focus, responsive menu, screen reader all work on actual devices | **NOT_VERIFIED** pending real browser/device testing |
| Dynamic external availability | Tailwind CDN and Google Fonts remain available | **NOT_VERIFIED**; not implied by a successful Vite build |

An offline build check is **not** proof of successful public HTTP delivery or of every external destination's uptime.

## P1 — Link identity and relative path correctness

### P1-README-YEARBOOK

**Baseline**: two markdown links labeled `Yearbook / 年度回顾` pointed to the *new* primary homepage (`/welcome-to-github/`), not to the archived yearbook.

**Correction**: both labeled yearbook links now target `/welcome-to-github/yearbook/`. A separate, explicitly labeled current research portal link retains `/welcome-to-github/`.

**Evidence**: root `README.md`; HTML source `index.html`; PR #972 (archive route introduction).

### P1-YEARBOOK-MEMORIAL

**Baseline**: the footer of `public/yearbook/index.html` used `./docs/archaeology/legacy_traces/MEMORIAL.md`; from `/welcome-to-github/yearbook/` this resolves under `/yearbook/docs/`, while deployment publishes the file under `/welcome-to-github/docs/`.

**Correction**: `../docs/archaeology/legacy_traces/MEMORIAL.md`.

**Evidence**: `public/yearbook/index.html`, source file `docs/archaeology/legacy_traces/MEMORIAL.md` and `.github/workflows/deploy.yml`, whose post-build `Prepare public memorial` stage copies to `dist/docs/archaeology/legacy_traces/`.

**Important test reconciliation**: the first new CI workflow run (43333543371) failed because the test assembled only Vite's `dist` and omitted the deployment's separate memorial-copy step. Build itself succeeded, route test failed; the test workflow was corrected to mirror deployment. Keep this first failure rather than claiming the original check passed.

## P2 — Navigation and source provenance

### P2-CROSS-NAV

- New portal `index.html`: existing `./yearbook/` link retained
- Archived yearbook: added explicit `../` link back to the current portal, without modifying its existing GitHub, README or Horizon destinations
- Navigation is bilingual; no new translation-module key was added, avoiding recurrence of the PR #974 cached-module mismatch

### P2-EXTERNAL-REPOSITORY-URLS

The following public GitHub repositories were independently located via the repository API:

- `lostlight530/welcome-to-github`
- `lostlight530/agent-foundations`
- `lostlight530/zero-entropy-lab`
- `lostlight530/Axiom-0`
- `lostlight530/reflective-continuum`
- `iflytek/astron-agent`
- `ModelEngine-Group/nexent`
- `bytedance/deer-flow`

The yearbook's five architecture/practice links are sourced from `public/yearbook/src/scripts/translations.js` (five distinct HTTPS URLs, repeated for zh/en).

- `https://github.com/iflytek/astron-agent/discussions/824`: public historical ResumeZhiYoutong discussion, verified at source
- `https://github.com/ModelEngine-Group/nexent/discussions/1816`: public historical RailSmart discussion, verified at source

**Boundary**: source presence does not establish present deployment or runtime validity. The eight historical project cards (MediaPipe Engine AI, Fire Panel Perception, ClassVision Distributed, Tiezhitong Agent, CifarLab Trainer, Persona Chat Studio, spec-X, virtu-tutor-dkt) have no per-item source URLs in the current yearbook data. The repository search in this audit did not establish individual canonical public sources, so **per-project provenance remains UNMAPPED**, rather than inventing a URL or altering their historic content. This user-facing repair does not rewrite practice-work descriptions.

### P2-PLAY-CDN-DEPENDENCY

The legacy page loads Tailwind's Play CDN (`https://cdn.tailwindcss.com`), which Tailwind's own v3 documentation describes as development-oriented rather than production-grade:
`https://v3.tailwindcss.com/docs/installation/play-cdn`

**Mitigation implemented**: an `onerror` fallback state and small local CSS layout rules preserve basic reading/navigation when that CDN script cannot load; the inline `tailwind.config` assignment is guarded so CDN failure does not cause a missing-global exception.

**Residual risk / NOT_FULLY_REMOVED**: normal visual fidelity still depends on the third-party stylesheet generator. A full build-time compiled stylesheet migration requires a separate validated dependency/build migration; this PR does not claim an offline, pixel-equivalent site. External Google Fonts already has `sans-serif` fallbacks but its CDN availability was not tested.

## P3 — Responsive and accessibility navigation

### P3-PORTAL-NARROW-SCREEN

Existing desktop links remain unchanged. A native `<details><summary>` section menu is exposed below 900px. It links to the actual page IDs: `#system`, `#architecture`, `#works`, `#stack` and `#archive`. The native control is focusable and uses language-switchable text; selection and Escape close the menu. Final screen-reader behavior awaits browser testing.

### P3-YEARBOOK-MENU-STATE

The existing yearbook mobile-menu button now has `type="button"`, `aria-controls="mobileMenu"`, and initial `aria-expanded="false"`. Its toggle handler updates the expanded state and its mobile-link handler resets it on close. No project navigation destination was changed.

## Reproducible offline verifier

On this PR's branch, run:

```bash
npm ci
npm run build -- --base=/welcome-to-github/
mkdir -p dist/docs/archaeology/legacy_traces
cp docs/archaeology/legacy_traces/MEMORIAL.md dist/docs/archaeology/legacy_traces/MEMORIAL.md
node tools/verify-welcome-public-surface.mjs
```

The pull-request workflow `.github/workflows/verify-welcome-pages.yml` mirrors these steps. The checker validates built-site links, route scope, anchor IDs, translation assets, memorial presence, README label/URL agreement, and dynamic source URL syntax. Its success result is intentionally `SOURCE_AND_DIST_ROUTE_PASS`, **not** `HTTP_PASS`.

## Non-scope and review gate

- No original `src/**` lifecycle file, `tests/**` or `docs/brain/**` is changed, so this presentation-only work does not enter the NEXUS lifecycle workflow's path filter
- No archived yearbook statements, badges, award totals, project descriptions, or primary-source GitHub Discussions are rewritten
- Open PR #975 is restricted to `parallax/**`; no overlapping file writes
- Current `main` remains the deployed authority until a human review/merge, then deployment checks are required again
- Keep Draft PR #976 open until exact-build CI passes and human maintainer review decides how to handle browser/network verification
