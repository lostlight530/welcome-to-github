# H1 Daily Signal Observe — 2026-11-19 / MCP memory lock hand-off ownership

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H1
Canonical Identity: welcome/horizon/H1
Cadence: Daily
Loop Stage: Observe
Logical Date: 2026-11-19
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: c403ea0079d4121ba06407aa2a8c63cdb4750f94
Run Identity: welcome-to-github/horizon/H1/2026-11-19/GPT_NATIVE/c403ea0/mcp-memory-lock-handoff-01
Source Identity: modelcontextprotocol/servers PR #5623 head ec42f5bbb6a72ad212b827cf27354e25066c1086
Source Authority For Claim: FIRST_PARTY_PINNED_IMPLEMENTATION_PATCH_AND_AUTHOR_TEST_FIXTURES
Independent Verification: ISSUE_PR_AND_EXACT_FILE_PATCH_READ / AUTHOR_TEST_OUTCOMES_NOT_INDEPENDENTLY_REPRODUCED
Host Applicability: UNKNOWN / NEXUS_OR_WELCOME_MCP_MEMORY_SERVER_DEPLOYMENT_NOT_OBSERVED
Evidence Upgrade Basis: VERSIONED_NEW_LOCK_OWNERSHIP_TRANSITION_AND_EXPLICIT_RESIDUAL_COUNTEREXAMPLE
Original Execution Status: REMOTE_GITHUB_PATCH_INSPECTION_PERFORMED / UPSTREAM_TESTS_AND_LOCAL_RUNTIME_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_EXTERNAL_SOURCE_OBSERVATION / NO_HOST_ADOPTION
Write Scope: horizon-cortex/2026-11-19-H1-signal-observe.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Fresh merged main and complete non-truncated repository Git tree inspected; no Open PR or matching 2026-11-19 branch at preflight. H1/H2 last retained daily on main: 2026-11-18; W46 H3/H4 retained.
- Current governing surfaces: `horizon-cortex/README.md` blob `fb6a2d828764571af66caf94259f67f16b1a8b0d`; `EVIDENCE_POLICY.md` blob `060eaff65437bda48718a9703477815c574a9846`; `check.py` blob `5736c90f56a59728db380180557256a151b1ea83`.
- 2026-11-18 H1/H2 studied ADK MCP prompt argument authority. This observation instead concerns cross-process ownership of a memory server's lock file; neither shared protocol keywords nor one ecosystem implies independent corroboration.
- Source PR #5623 was created 2026-11-18T18:55:37Z and GitHub reports it merged into upstream `v2/main`. Source event, current observation, logical date and eventual Welcome PR merge are distinct timestamps.
- The source patch and public issue/PR discussion were opened via the GitHub connector. No upstream package was installed, no server launched and no Welcome/NEXUS host code changed.
- Independent local Git bootstrap diagnostic: `git ls-remote https://github.com/lostlight530/welcome-to-github.git refs/heads/main`; UTC 2026-11-19T05:35:52.633349050Z–05:35:52.661148156Z; Git 2.47.3; exit 128; stdout empty; stderr `Could not resolve host: github.com`. This is NOT an H1 external-runtime test.

## EXTERNAL_SOURCE_RECORDS
Source ID: SRC-20261119-H01
Title: fix(memory): order every lock hand-off by the breaking guard
Publisher: modelcontextprotocol/servers maintainers and PR author
Canonical Source Identity: modelcontextprotocol/servers PR #5623 head ec42f5bbb6a72ad212b827cf27354e25066c1086
URL: https://github.com/modelcontextprotocol/servers/pull/5623
Underlying issue: https://github.com/modelcontextprotocol/servers/issues/5565
Changed implementation: https://github.com/modelcontextprotocol/servers/blob/ec42f5bbb6a72ad212b827cf27354e25066c1086/src/memory/index.ts
Authored deterministic tests: https://github.com/modelcontextprotocol/servers/blob/ec42f5bbb6a72ad212b827cf27354e25066c1086/src/memory/__tests__/file-lock.test.ts
Residual counterexample issue: https://github.com/modelcontextprotocol/servers/issues/5624
Source Version: PINNED_PR_HEAD / MERGED_UPSTREAM / RELEASE_PACKAGE_COVERAGE_NOT_VERIFIED
Source Publication: PR opened 2026-11-18T18:55:37Z (2026-11-19 Asia/Shanghai)
Source Access: FIRST_PARTY_ISSUE_PR_PATCH / NOT_AUTHOR_TEST_EXECUTION

## RAW_SIGNAL_LOG
Signal ID: SIG-20261119-H01
- The memory server uses an exclusive-create `<memory file>.lock` and a `.lock.break` guard. Before this patch, the guard serialized stale-lock breakers but did not fully serialize release or a just-created writer's confirmation.
- The first patch-level mechanism places release-side compare-then-unlink inside the guard, avoiding a breaker replacing the lock between token comparison and path deletion.
- The second mechanism requires a newly creating writer to wait for guard absence and re-check ownership token before entering its critical section, preventing it from running with a lock overwritten during restore.
- The author's deterministic fixtures control file-system interleavings rather than hoping for a scheduling race. The PR reports 54 file-lock tests and 316 memory tests passing; **these are upstream author claims**, not tests executed here.
- The PR additionally reports mixed old/new process checks. The patch itself states older servers do not take the new guard on release or verify it on acquisition, so mixing versions does not erase every old-process race.
- Most importantly the same source patch explicitly documents a remaining guard-cleanup race: two processes judging a crash-left guard stale may delete another process's newly acquired guard by path. Upstream issue #5624 is still open at inspection. Thus `FIX_MERGED != ALL_LOCK_RACES_ELIMINATED`.
- Threat scope is correctness and write serialization among same-user processes with a shared file, NOT a proven security authorization boundary, not global distributed consensus, and not a Welcome incident.
- Proposed positive control: create three processes sharing a named memory JSONL, inject the exact acquire/release/break interleavings with immutable source revision and record critical-section overlap plus final persisted graph state.
- Proposed negative control A: run only one writer, which should not be counted as evidence for multi-process mutual exclusion.
- Proposed negative control B: run one old writer and one patched writer; tag each acquisition/release by installed version and check whether the old participant retains its pre-patch gap.
- Proposed negative control C: reproduce #5624 with two simultaneous crash-left-guard clearers and a third new guard holder; the new guard must survive before a universal safety claim can be considered.
- Deduplication: code patch, authored tests and issue discussion belong to one upstream project lineage; quoting three URLs is not three independent experiments.
Disposition: WATCH / COUNTEREVIDENCE_RETAINED / NO_HOST_CHANGE / NO_DOCTRINE_PROMOTION.

## EVIDENCE_DELTA
- NEW_EVIDENCE: exact lock-ownership hand-off changes, deterministic test source, and public residual race with separate issue identity.
- CORRECTED_INTERPRETATION: lock-file token equality and conflict-free GitHub merge are not guarantees of serialized execution; the newly guarded path improves a bounded set of interleavings.
- UNCHANGED_BOUNDARY: EXTERNAL_PATCH != RELEASED_SERVER != LOCAL_DEPLOYMENT != INDEPENDENTLY_VERIFIED_DURABILITY.
- NEW_COUNTEREVIDENCE: upstream #5624 and mixed-version behavior explicitly bound the fix.
- UNKNOWN_RETAINED: actual shipped package, Welcome dependency, real effects, process crashes on local FS, remote persistence, author test reproducibility.
- NEXT_RETEST_CONDITION: pin upstream pre/post revisions and package versions, run deterministic 3-process interleaving tests including #5624, inspect exact file/inode/store and independent final readback.

## NEXT_HANDOFF
- Same-date `welcome/horizon/H2` is BLOCKED_DEPENDENCY until this original H1 Draft is merged by Human Maintainer and the exact H1 blob plus merged-main SHA are freshly reread. No speculative H2 completion or successor PR.
- Open `2026-W47` H3/H4 NOT_DUE under closed-week contract; November H5/H6 NOT_DUE until natural month closure.
- This does not create Parallax, Native H2, Independent A1/A2, audit, NEXUS runtime or Host Memory execution credit.

## BOUNDARY_CHECK
- Remote upstream implementation and test text: INSPECTED, NOT_EXECUTED.
- Native Horizon structural `check.py`: NOT_EXECUTED (full worktree DNS acquisition failed).
- External source claim: PATCH_SUPPORTED with explicitly preserved residual race; runtime correctness and host applicability remain UNKNOWN.
- No private scheduler prompt, credentials, personal memory, host data, security exploit material, Jules history or protected runtime surface written.
- Delivery at authoring: DRAFT_PROPOSED / MERGE_NOT_AUTHORIZED / HUMAN_REVIEW_PENDING.
