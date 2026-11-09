# Independent A2 — welcome-to-github — 2026-11-09 month relations

## Identity and fresh-main gate
- Repository: `lostlight530/welcome-to-github`; task: `independent-maintenance/A2`.
- Logical date: 2026-11-09 Asia/Shanghai; review cut: 2026-11-09 23:20:01 +08:00.
- A1-before-A2 order: satisfied. A1 [PR #944](https://github.com/lostlight530/welcome-to-github/pull/944) is merged.
- Fresh main after A1 merge: `b21cd118a08457b932d7d0ec4cf7401996d53384`.
- Exact merged A1 blob: `95c5a469cabf858a3ab176e3804fbee573a93a89`.
- Prior A2: `historical-audits/2026-11/2026-11-08-a2-month-relations.md` @ `44f4c1cd1d8e84f147d55afa01bbc71a126dbf83`; preserved as the Nov08 source-time relation.

## Nov09 current-main inputs
| Object | Exact blob | Relation |
|---|---|---|
| `horizon-cortex/2026-11-09-H1-signal-observe.md` | `7710ae9a1be335fccf74469990d078e7cde62f8d` | new upstream source observation |
| `horizon-cortex/2026-11-09-H2-horizon-orient.md` | `796b699891f5317d6ee7ef891783fc38aa37e63b` | same-day orientation, exact H1 dependency |
| `parallax/records/2026-11/2026-11-09.md` | `9318ab1eb0fdf5a8cbe942aaf5d793a309c82fe3` | bounded GitHub open/merged-state projection |
| W45 H3/H4 | existing Nov08 owners | W45 FINAL 7/7; not reopened by W46 |

## Month-relation judgments
1. Nov01 is W44 Sunday; Nov02–08 are W45; Nov09 opens W46. The calendar boundary is independent of the time when a weekly PR is merged.
2. W45 is FINAL 7/7. This closes the coverage period, not all H45 hypotheses or every unresolved horizon question.
3. Nov09 H1/H2 are W46 inputs and must not be inserted into W45 H3/H4 evidence.
4. H1/H2 share Google ADK commit `67b217d009cbcdd5827f035e001620dbe08e839b`; one first-party source lineage, not two independent publishers.
5. The upstream change offloads synchronous evaluator callbacks / `evaluate_invocations` work from the orchestration event loop with `asyncio.to_thread`; async callables remain awaited.
6. Worker-thread offload changes scheduling and concurrency boundaries; it does not prove callback thread safety, cancellation of an already-running worker, context propagation or absence of shared-state races.
7. H2's countercases narrow the claim: authored test fixtures model worker-thread, heartbeat and barrier behavior, but the upstream tests were NOT_EXECUTED in this A2.
8. The Welcome host's installed ADK version, runtime configuration and actual callback behavior remain UNKNOWN; no local host applicability is inferred.
9. The Nov09 Parallax record is a bounded early-day read shortly after 04:03 Asia/Shanghai, with exact main `a0c5b428...`, PR #937 merged and zero legacy status contexts.
10. That Parallax snapshot predates later Nov09 H1/H2 and independent A1 merges; its author-time main SHA and empty-open-PR result remain historical, not the current 23:20 main state.
11. Empty current open-PR projection, ordinary branch list containing only main, and zero legacy status contexts do not prove no earlier merge or no Actions execution.
12. Direct PR receipt #937, merge SHA, main SHA, ordinary branch ref and legacy commit-status projection are distinct API objects and were read non-atomically.
13. November remains OPEN; H5/H6 monthly final tasks are NOT_DUE. W46 is OPEN after its first native date; it is not a second November.
14. A1 #944 and this A2 are maintenance records, not extra H1/H2 Daily runs and not additional independent external evidence.
15. No upstream Google ADK test, Welcome local harness, live A2A peer, callback stress test or external side effect was executed by this A2.

## Current calendar and ownership matrix
| Owner | Current state | A2 decision |
|---|---|---|
| November 2026 | OPEN | continue; no natural-month final |
| W44 | FINAL; contains Nov01 | preserve |
| W45 | FINAL 7/7; Nov02–08 | preserve; H45 unresolved questions carry |
| W46 | OPEN 1/7; Nov09 H1/H2/Parallax | APPEND_CURRENT_RELATION |
| H5/H6 monthly | NOT_DUE | no early close |
| Nov10–30 | NOT_DUE | no future-state inference |

- A2 current relation is appended after the merged A1 and fresh main read.
- No native H1/H2/Parallax, weekly or monthly owner is rewritten here.
- Result: `A2_MONTH_RELATION_DELIVERED / NOVEMBER_OPEN / W45_FINAL / W46_OPEN_1_OF_7`.
