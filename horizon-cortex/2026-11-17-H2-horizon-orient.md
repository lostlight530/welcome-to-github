# H2 Daily Horizon Orient — 2026-11-17 / A2A artifact boundary and false-completion controls

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-17
Logical Timezone: Asia/Shanghai
Agent: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: f89e5128bd9a921eba82d72f034b8eb2109da06c
Run Identity: welcome-to-github/horizon/H2/2026-11-17/GPT_NATIVE/f89e5128bd9a921eba82d72f034b8eb2109da06c/a2a-artifact-completeness-countercontrols-01
Source Identity: google/adk-python@dbae28d3ccd0958d202a85e2c39cdf249ae2c7f2
Source Authority For Claim: EXACT_FIRST_PARTY_PATCH / SAME_ISSUER_AS_H1
Independent Verification: FRESH_COMMIT_DIFF_REREAD_AND_BRANCH_CONDITION_CROSSCHECK / TESTS_NOT_EXECUTED
Host Applicability: UNKNOWN / NO_WELCOME_A2A_CLIENT_RUNTIME_VERIFIED
Evidence Upgrade Basis: DEEPER_BOUNDARY_FINALIZATION_AND_SUPERSESSION_CONDITION_CHECK / NO_SECOND_INDEPENDENT_SOURCE
Original Execution Status: GPT_NATIVE_BOUNDED_H2_SOURCE_ORIENTATION / NO_SDK_OR_HOST_RUN
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: SOURCE_BOUNDED_ORIENTATION / NO_HOST_ADOPTION_DECISION
Write Scope: horizon-cortex/2026-11-17-H2-horizon-orient.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Exact same-day H1 is now main-retained: `horizon-cortex/2026-11-17-H1-signal-observe.md` @ Git blob `c8c5044bd09b594d3d88b9aa4f9e81c2ff33d482`, original merged [PR #1005](https://github.com/lostlight530/welcome-to-github/pull/1005), merge/main SHA `f89e5128bd9a921eba82d72f034b8eb2109da06c`. This H2 reads the post-merge source, not an H1 Draft.
- Reread current Horizon `README.md`, `EVIDENCE_POLICY.md`, `check.py`, previous 2026-11-16 H2 and closed W46 H3/H4. November H5/H6 remain NOT_DUE.
- Reopened exact first-party commit [dbae28d3ccd0958d202a85e2c39cdf249ae2c7f2](https://github.com/google/adk-python/commit/dbae28d3ccd0958d202a85e2c39cdf249ae2c7f2); specifically checked `_StreamingArtifactAggregator`, `finalize_at_boundary`, `discard_task_artifacts`, `_is_boundary_response` in changed implementation, and the associated authored tests file.
- H1 and H2 share ONE original upstream issuer. A different review depth is not an independent publisher/test execution or a second deployed-system observation.

## SIGNAL_CLASSIFICATION
Signal ID: SIG-20261117-H01
External fact: The pinned patch changes RemoteA2aAgent's handling of streamed A2A artifact parts, including incomplete chunks where `last_chunk` is not explicitly true before a terminal task status.
Source evidence: EXACT_VERSION_SCOPED_IMPLEMENTATION_DIFF / FIRST_PARTY_COMMIT
Technical layer: client integration materialization and event semantics, not a newly published A2A protocol version, end-to-end effect ledger, or an authorized host requirement.
Potential failure class: ARTIFACT_FINALIZATION_FALSE_NEGATIVE / INCOMPLETE_STREAM_CARRY_FORWARD.
H2 bounded disposition: KEEP_WATCHLIST / NO_HOST_MIGRATION / NO_DECISION.
Promotion denied: NO_RELEASE_PACKAGE_VERIFIED, NO_REAL_REMOTE_SERVER_FIXTURE, NO_SESSION_PERSISTENCE_RECEIPT, NO_WELCOME_HOST_USAGE.
Independent evidence added: NONE / SAME_UPSTREAM_LINEAGE; H2 introduces new conditional counterchecks, not a new independent source.
Temporal identity: upstream UTC 2026-11-16T22:24:34Z, observed under 2026-11-17 Shanghai; merge time of H1 separate.

## ORIENTATION_NOTES
- `last_chunk` alone is insufficient as a universal completeness predicate when remote server status/task boundaries can close a turn. This is a specific ADK integration scenario under the inspected code path, not a proof about all A2A clients.
- Positive control: `artifact_id = a`, an append stream of partial text, last_chunk False, then a terminal task status; expected event materialization must preserve exact accumulated content, identity, one final non-partial event, and a named session-store readback, tested on before/after pinned revisions.
- Negative control 1: full task snapshot already contains artifact `a`. New code's `discard_task_artifacts` is a source-level deduplication intent; only an actual test can establish no duplicate final event in a particular converter/interceptor flow.
- Negative control 2: an explicit full replacement with `append` unset and `last_chunk=True` supersedes prior fragments; applying unconditional flush may incorrectly retain stale content. The patch routes this as a distinct branch.
- Negative control 3: an empty final marker with no buffered content should not manufacture an artifact. A source path rejecting or dropping an intercepted event must preserve failure accounting rather than pretend it was persisted.
- Negative control 4: no terminal status arrives due to network/cancellation, or the stream is interrupted after a partial chunk. Materialization still cannot be assumed; the code's flush semantics need a named boundary and downstream commit receipt.
- Provenance boundary: `A2ATask.id`, `artifact_id`, conversion `Event.id`, session-store revision and external effect ID are not automatically one identity; source role/author is not authenticated by a transport label.
- Status boundary: A2A task terminal state, ADK event emission, durable session readback and actual external effect settlement are different milestones and have different evidence obligations.
- Host applicability: No evidence in this H2 that Welcome uses this exact ADK revision, protocol client, event converter, interceptor or session store. Source portability remains UNKNOWN.
- Source dependence: authored tests are a first-party design oracle, not this producer's `pytest` receipt, independent compatibility test or production regression result.

## NO_DECISION_SECTION
Decision: NO_DECISION
Decision Basis: Source-level patch and a falsifiable negative-control matrix are supported, but effect identity, event cardinality, versioned installed client and host runtime evidence are not observed.
Host Change: NONE / NO_ADOPTION / NO_RUNTIME_MIGRATION
Claim Promotion: NO / COUNTEREVIDENCE_GATE_NOT_MET
Watchlist: Remote A2A partial-artifact boundary, replacement-vs-append deduplication, session-store persistence and cancellation/stream end provenance
Retest: Paired pinned source revisions, scripted fake A2A stream with partial/terminal controls, exact emitted event IDs, session readback and stdout/stderr/exit; add a non-ADK integration to test portability separately.

## EVIDENCE_DELTA
- NEW_EVIDENCE: exact changed branches for terminal-boundary materialization, superseding snapshots and replacement/delta closure checked after H1 merge
- CORRECTED_INTERPRETATION: status boundary != artifact transport close marker != persisted event != external authoritative effect
- UNCHANGED_BOUNDARY: external client fix is not protocol-wide conformance, host deployment or automatic durable task success
- NEW_COUNTEREVIDENCE: pre-materialized snapshots, full replacements, empty marker, missing terminal status and intercepted event rejection require separate no-duplicate/unknown controls
- UNKNOWN_RETAINED: released SDK version, actual tests, downstream session store, at-least-once replay, event cardinality, Welcome applicability, effect settlement
- NEXT_RETEST_CONDITION: execute revisions and controls with source/attempt/store identities and authoritative readback; capture full stdout/stderr/exit and failed event state

## NEXT_HANDOFF
- 2026-W46 has closed and its H3/H4 records are already main-visible; 2026-11-17 H2 belongs W47 and cannot retroactively alter W46
- Current November Monthly H5/H6 NOT_DUE; H2 creates no Horizon Memory promotion or NEXUS host instruction
- Distinct Independent A1/A2 maintenance may now review H1/H2 only under its own dated cutoff and fresh merged PR dependencies

## BOUNDARY_CHECK
- Only new same-day H2 file; original H1 file and blob untouched, no Jules history, Parallax, NEXUS, workflows or independent audit changed
- Executed: latest H1 merge/main/blob read and first-party pinned ADK patch review; not executed: full Horizon checker, ADK tests, A2A transport, real client or host runtime
- One Draft PR for Human Maintainer with explicit request for merge, no auto-merge or claims of external independent reproduction
