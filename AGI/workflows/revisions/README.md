# Named Workflow Revision Inventory

This inventory records every main-lineage change to `.github/workflows/brain_evolution.yml` and `.github/workflows/nexus-life-cycle.yml`, including repairs and the registered Brain Evolution precursor's retirement event
It is intentionally more granular than the selected architecture generations in `AGI/workflows/README.md`
The source Git commit remains the historical authority; each YAML backup uses the exact source Git blob

## Verification boundary

- Every executable entry was fetched at its exact source commit and its Git blob matched that commit's workflow file
- SHA-256 was computed over the fetched UTF-8 content
- Static syntax parsing used PyYAML 6.0.3 and does not prove GitHub Actions semantics, present-day dependency compatibility or safe execution
- A linked run is a successful workflow run for the exact head SHA; an empty cell means no qualifying run was found in the current query, not that no run ever existed
- Historical files are inert under AGI; active Actions are discovered only from `.github/workflows`

## Revision events

| # | UTC date | Workflow | Git commit | Change recorded in Git | Syntax | Backup | Exact-commit run |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-02-15 | Brain Evolution | [`a01c6e8df1f5`](https://github.com/lostlight530/welcome-to-github/commit/a01c6e8df1f5e8ba80726ede6cbdb5de692e8741) | feat(brain): Upgrade harvester to Official Source Radar & Ecosystem Consensus | PASS | [YAML](../backups/brain-evolution/recovered-2026-02-15/brain_evolution.yml) | — |
| 2 | 2026-02-16 | Brain Evolution | [`90471216fda8`](https://github.com/lostlight530/welcome-to-github/commit/90471216fda860eb209f188f30aa3b3bb5a383c3) | feat(brain): implement daily contemplation protocol with optimized learner | PASS | [YAML](./snapshots/brain-evolution/2026-02-16-90471216fda8/brain_evolution.yml) | — |
| 3 | 2026-02-16 | Brain Evolution | [`98b3470ef42d`](https://github.com/lostlight530/welcome-to-github/commit/98b3470ef42d25b431b69c654573c7ef735b6f8a) | refactor(brain): adopt static contemplation paradigm | PASS | [YAML](./snapshots/brain-evolution/2026-02-16-98b3470ef42d/brain_evolution.yml) | — |
| 4 | 2026-02-17 | Brain Evolution | [`789878f9cc16`](https://github.com/lostlight530/welcome-to-github/commit/789878f9cc1692e383c8aa2046483e8c13b92267) | Update brain_evolution.yml | PASS | [YAML](./snapshots/brain-evolution/2026-02-17-789878f9cc16/brain_evolution.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/22290484424) |
| 5 | 2026-03-09 | Brain Evolution | [`51df7db5a813`](https://github.com/lostlight530/welcome-to-github/commit/51df7db5a81324c7bed52cb098c249dc45685686) | refactor(brain): install Omniscience & Cognition modules, unify lifecycle workflow | NOT_APPLICABLE | removed | — |
| 6 | 2026-03-09 | NEXUS CORTEX | [`51df7db5a813`](https://github.com/lostlight530/welcome-to-github/commit/51df7db5a81324c7bed52cb098c249dc45685686) | refactor(brain): install Omniscience & Cognition modules, unify lifecycle workflow | PASS | [YAML](../backups/nexus-life-cycle/recovered-2026-03-09/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/22840143668) |
| 7 | 2026-03-15 | NEXUS CORTEX | [`d9fa76931a22`](https://github.com/lostlight530/welcome-to-github/commit/d9fa76931a223e96a8bc659a29ff16c422434559) | chore(cortex): connect superficial frontend identities to architectural worldview | PASS | [YAML](./snapshots/nexus-life-cycle/2026-03-15-d9fa76931a22/nexus-life-cycle.yml) | — |
| 8 | 2026-03-15 | NEXUS CORTEX | [`2ca3388578cc`](https://github.com/lostlight530/welcome-to-github/commit/2ca3388578ccb1ddffdfc2b7d869cc1dc4ad493c) | feat(cortex): ultimate self-awareness closure, ouroboros immunity, and structural optimization | PASS | [YAML](./snapshots/nexus-life-cycle/2026-03-15-2ca3388578cc/nexus-life-cycle.yml) | — |
| 9 | 2026-03-15 | NEXUS CORTEX | [`c0fcf1f0d180`](https://github.com/lostlight530/welcome-to-github/commit/c0fcf1f0d1800dd334a59629edb801e1eced6c37) | fix: automated stash conflict resolution in CI workflow | PASS | [YAML](./snapshots/nexus-life-cycle/2026-03-15-c0fcf1f0d180/nexus-life-cycle.yml) | — |
| 10 | 2026-03-15 | NEXUS CORTEX | [`d8222a0e910d`](https://github.com/lostlight530/welcome-to-github/commit/d8222a0e910d479ddf7c6576ff6662a1c5034c3d) | fix: resolve detached HEAD error during auto commit | PASS | [YAML](../backups/nexus-life-cycle/recovered-2026-03-15/nexus-life-cycle.yml) | — |
| 11 | 2026-03-31 | NEXUS CORTEX | [`a051eb390942`](https://github.com/lostlight530/welcome-to-github/commit/a051eb390942fd270548166e5f32142f0e1d9aef) | docs(archaeology): Enshrine Phase V Omniscient Protocol Dictator manifesto | PASS | [YAML](../backups/nexus-life-cycle/recovered-2026-03-31/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/23798525410) |
| 12 | 2026-03-31 | NEXUS CORTEX | [`a48b972ac25a`](https://github.com/lostlight530/welcome-to-github/commit/a48b972ac25a34b3f880c7b7ae5944bb640a1528) | I have disabled the GitHub dependency graph feature in the CI. | PASS | [YAML](./snapshots/nexus-life-cycle/2026-03-31-a48b972ac25a/nexus-life-cycle.yml) | — |
| 13 | 2026-04-07 | NEXUS CORTEX | [`c00906c255f9`](https://github.com/lostlight530/welcome-to-github/commit/c00906c255f96c060977f0d770a55979aed4892d) | fix: Systemic error correction and CI pipeline optimization | PASS | [YAML](./snapshots/nexus-life-cycle/2026-04-07-c00906c255f9/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/24079291833) |
| 14 | 2026-04-24 | NEXUS CORTEX | [`e66495bf897b`](https://github.com/lostlight530/welcome-to-github/commit/e66495bf897b1a78cec564611a8c96b3f99e2af7) | feat(arch): implement deterministic SOP automation and suppress Node.js 20 warnings | PASS | [YAML](./snapshots/nexus-life-cycle/2026-04-24-e66495bf897b/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/24866092018) |
| 15 | 2026-04-27 | NEXUS CORTEX | [`6015f37bd50d`](https://github.com/lostlight530/welcome-to-github/commit/6015f37bd50da491d55af79ebdbdf6456559a56b) | fix: establish pure deterministic heartbeat to fix missing scheduled outputs | PASS | [YAML](./snapshots/nexus-life-cycle/2026-04-27-6015f37bd50d/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/25025170613) |
| 16 | 2026-05-28 | NEXUS CORTEX | [`f8a9c5f26d02`](https://github.com/lostlight530/welcome-to-github/commit/f8a9c5f26d02a3f08f7aafffdeea77696fed07f5) | chore: full matrix structural review and task mechanic completion | FAIL | [YAML](./snapshots/nexus-life-cycle/2026-05-28-f8a9c5f26d02/nexus-life-cycle.yml) | — |
| 17 | 2026-05-28 | NEXUS CORTEX | [`7c74038d3572`](https://github.com/lostlight530/welcome-to-github/commit/7c74038d3572a62fea4a24e381905fdde40deb52) | ci: fix github actions yaml syntax errors and concurrency issues | PASS | [YAML](./snapshots/nexus-life-cycle/2026-05-28-7c74038d3572/nexus-life-cycle.yml) | — |
| 18 | 2026-07-04 | NEXUS CORTEX | [`ea6d8d201738`](https://github.com/lostlight530/welcome-to-github/commit/ea6d8d2017388a4ce4983056ea3ee484d0868afe) | fix: remove FORCE_JAVASCRIPT_ACTIONS_TO_NODE24 and trigger empty commit to clear ci artifact state | PASS | [YAML](./snapshots/nexus-life-cycle/2026-07-04-ea6d8d201738/nexus-life-cycle.yml) | — |
| 19 | 2026-07-11 | NEXUS CORTEX | [`6743ccbefb8c`](https://github.com/lostlight530/welcome-to-github/commit/6743ccbefb8cae9d7d7ff9b00e822f23900c2470) | archive legacy inputs and add profile-driven harvester | PASS | [YAML](../backups/nexus-life-cycle/recovered-2026-07-11/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/29142338521) |
| 20 | 2026-07-11 | NEXUS CORTEX | [`89d43dc2c04f`](https://github.com/lostlight530/welcome-to-github/commit/89d43dc2c04fdbba549c19de2ee9cca43a33a827) | harden bot maintenance boundaries | PASS | [YAML](./snapshots/nexus-life-cycle/2026-07-11-89d43dc2c04f/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/29142550213) |
| 21 | 2026-07-11 | NEXUS CORTEX | [`75ee2fe775c7`](https://github.com/lostlight530/welcome-to-github/commit/75ee2fe775c716c942cd09ca73236565c2cc5a29) | 完善可读摄取与确定性记忆闭环 | PASS | [YAML](./snapshots/nexus-life-cycle/2026-07-11-75ee2fe775c7/nexus-life-cycle.yml) | — |
| 22 | 2026-07-11 | NEXUS CORTEX | [`9da8329dbe7b`](https://github.com/lostlight530/welcome-to-github/commit/9da8329dbe7bcaf99e89e25464b35e4eafa93744) | fix: safely sync generated lifecycle changes | PASS | [YAML](./snapshots/nexus-life-cycle/2026-07-11-9da8329dbe7b/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/29151047545) |
| 23 | 2026-07-13 | NEXUS CORTEX | [`826ebc4c2231`](https://github.com/lostlight530/welcome-to-github/commit/826ebc4c2231e4b98ee6946731c5d03005a3ae00) | fix: canonicalize active knowledge ledger | PASS | [YAML](./snapshots/nexus-life-cycle/2026-07-13-826ebc4c2231/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/29270004950) |
| 24 | 2026-07-13 | NEXUS CORTEX | [`5d83d7968eb4`](https://github.com/lostlight530/welcome-to-github/commit/5d83d7968eb40b24c52d12115ff08ee53c49e608) | fix: validate canonical ledger after repair | PASS | [YAML](./snapshots/nexus-life-cycle/2026-07-13-5d83d7968eb4/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/29270492461) |
| 25 | 2026-07-17 | NEXUS CORTEX | [`8240a2b842f9`](https://github.com/lostlight530/welcome-to-github/commit/8240a2b842f903737976ab6c5190196e2ee99ef8) | fix lifecycle retry and preflight | PASS | [YAML](./snapshots/nexus-life-cycle/2026-07-17-8240a2b842f9/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/29584779584) |
| 26 | 2026-07-21 | NEXUS CORTEX | [`bc035cbf257f`](https://github.com/lostlight530/welcome-to-github/commit/bc035cbf257f72da90277d8bed0eaea3c6d961b9) | fix lifecycle ledger invariants [skip ci] | PASS | [YAML](./snapshots/nexus-life-cycle/2026-07-21-bc035cbf257f/nexus-life-cycle.yml) | — |
| 27 | 2026-07-23 | NEXUS CORTEX | [`cf4e61603c76`](https://github.com/lostlight530/welcome-to-github/commit/cf4e61603c76b64214668712162759aeb6db879e) | Harden active-memory lifecycle invariants | PASS | [YAML](./snapshots/nexus-life-cycle/2026-07-23-cf4e61603c76/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/29985566906) |
| 28 | 2026-07-23 | NEXUS CORTEX | [`b0063831d260`](https://github.com/lostlight530/welcome-to-github/commit/b0063831d26045be706a16cf286f5c8e0c60de45) | Fix post-merge lifecycle path handling | PASS | [YAML](./snapshots/nexus-life-cycle/2026-07-23-b0063831d260/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/29989663393) |
| 29 | 2026-07-23 | NEXUS CORTEX | [`165820f07510`](https://github.com/lostlight530/welcome-to-github/commit/165820f07510257e2c89af29b369e3312bc6f788) | Fix MCP sandbox root contract | PASS | [YAML](./snapshots/nexus-life-cycle/2026-07-23-165820f07510/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/29991291364) |
| 30 | 2026-08-05 | NEXUS CORTEX | [`b78a2f4722d7`](https://github.com/lostlight530/welcome-to-github/commit/b78a2f4722d766f6fdfc956da852b671db354d9d) | Add deterministic observation boundary and align security controls | PASS | [YAML](./snapshots/nexus-life-cycle/2026-08-05-b78a2f4722d7/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/30981760171) |
| 31 | 2026-08-31 | NEXUS CORTEX | [`d607cc3e1608`](https://github.com/lostlight530/welcome-to-github/commit/d607cc3e1608a34eaf81d2040ccfa64382f02c12) | actions: make lifecycle deterministic and conflict-safe | PASS | [YAML](./snapshots/nexus-life-cycle/2026-08-31-d607cc3e1608/nexus-life-cycle.yml) | [run](https://github.com/lostlight530/welcome-to-github/actions/runs/33388340594) |
| 32 | 2026-08-31 | NEXUS CORTEX | [`3c7ebfb49f69`](https://github.com/lostlight530/welcome-to-github/commit/3c7ebfb49f69f0f015075a98b869437265651001) | ci(lifecycle): publish layered human receipt | PASS | [YAML](./snapshots/nexus-life-cycle/2026-08-31-3c7ebfb49f69/nexus-life-cycle.yml) | — |

## Interpretation

The registered `brain_evolution.yml` precursor has four executable YAML revisions and one removal event on 2026-03-09, when the NEXUS CORTEX workflow path was introduced
The separate `brain-evolution.yml` and `brain-integrity.yml` files are historical companions, not extra versions of that registered precursor or of NEXUS CORTEX; none is reactivated here
The selected 2026-10-07 AGI original baseline is a later capture of the final 2026-08-31 workflow blob, not another workflow-file modification
WorkflowHub registration order is not the historical Git order, and a registry revision comment does not replace a pinned source file
The selected generation records provide architecture descriptions; this inventory preserves every intervening file revision without promoting each repair to a new architecture generation

### Known invalid historical syntax

The 2026-05-28 revision `f8a9c5f26d02a3f08f7aafffdeea77696fed07f5` is preserved exactly but fails static YAML parsing near line 37
The following workflow commit `7c74038d3572a62fea4a24e381905fdde40deb52` parses successfully
Do not run or silently repair the invalid historical backup; its failure is part of the evidence chain


## Safe use

These backups do not change the current workflow, Jules tasks, Codex maintenance or archived task records
Treat any experiment or replay as a separate candidate and validate its write boundary before execution
