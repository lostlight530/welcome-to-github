# H2 Daily Horizon Orient — 2026-11-26 / cache and restore boundaries

## CORTEX_RUN_HEADER
Cortex: horizon-cortex
Host Repository: welcome-to-github
Task ID: H2
Canonical Identity: welcome/horizon/H2
Cadence: Daily
Loop Stage: Orient
Logical Date: 2026-11-26
Logical Timezone: Asia/Shanghai
Agent: GPT-6.2 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
Record Provenance: HUMAN_AUTHORIZED_SUBSTITUTE
Base Main SHA: 0b368598d6138fa3fedc38315458ad22b7d94933
Run Identity: welcome-to-github/horizon/H2/2026-11-26/GPT_NATIVE/0b368598d613/cache-boundary-01
Source Identity: openai/openai-agents-python PR #6221 / merge 7acce4fbecdf4b272c75cd53d875b91e1910b43a
Source Authority For Claim: FIRST_PARTY_MERGED_SOURCE_AND_AUTHOR_FIXTURES
Independent Verification: MERGED_H1_READBACK / EXACT_MERGED_SOURCE / STANDALONE_CONTROL_EXECUTED / SDK_NOT_EXECUTED
Host Applicability: UNKNOWN / NEXUS_DEPENDENCY_UNVERIFIED
Evidence Upgrade Basis: ADDITIONAL_MERGED_SOURCE_INSPECTION_AND_BOUNDED_LOCAL_CONTROL
Original Execution Status: SOURCE_REVIEW_AND_STANDALONE_CONTROL_EXECUTED / FULL_CHECKER_AND_SDK_NOT_EXECUTED
Current Path Status: PROPOSED_DRAFT_PR / NOT_MERGED_AT_AUTHORING
Task Status: BOUNDED_SOURCE_ORIENTATION / NO_HOST_DECISION
Write Scope: horizon-cortex/2026-11-26-H2-horizon-orient.md
Host Repository Change: NO
Boundary Violation: NO

## INPUT_RECORD
- Original same-day horizon-cortex/2026-11-26-H1-signal-observe.md merged via #1063; merge 0b368598d6138fa3fedc38315458ad22b7d94933; exact H1 blob 1567f9d1dff679f3a6b24cbbaa8c94247b359c56 reread from main. H1 historical proposal-time status retained.
- Policy blob 060eaff65437bda48718a9703477815c574a9846; checker blob 5736c90f56a59728db380180557256a151b1ea83; prior H2 blob 3520c140e71b17288aa70155b93f96a58ada44d9.
- Upstream https://github.com/openai/openai-agents-python/pull/6221 metadata rechecked merged, exact run_state.py blob 2c2f1dc3935b6cb90462ff52c52c9d9aa7db4a7c at merge revision, lines 350–375 and 5375–5415 read. W47 retained; W48 and November close NOT_DUE.

## SIGNAL_CLASSIFICATION
- The merged implementation uses functools.cache around a zero-argument TypeAdapter factory, not a cache of run data or authorization receipts.
- The two restore branches call the factory and validate_python, but catch ValidationError and retain normalized raw item. Consequently the existence of a validator or a restored item does not establish that every restored item passed that validator.
- The author local-tool benchmark and MCP-import-path control are one source lineage, not independently reproduced measurements. Release, real concurrency and deployment applicability remain unknown.

## ORIENTATION_NOTES
- Standalone diagnostic H2-20261126-CACHE-CONCURRENT-FIRST-01, Python 3.13.5, actual 2026-11-26T07:03:25Z (approximate completion), command python /tmp/h2_20261126.py, exit 0, stderr empty, script SHA256 6a223bc7dfff83d12a38b76a139efb9d766376f09ba74cade3389f48bde721b2.
- Exact script:
```python
from functools import cache
from threading import Barrier, Thread
barrier=Barrier(2)
builds=[]; results=[]
@cache
def factory():
    token=object(); builds.append(token); barrier.wait(timeout=5); return token
threads=[Thread(target=lambda:results.append(factory())) for _ in range(2)]
for t in threads:t.start()
for t in threads:t.join()
assert len(builds)==2 and len(results)==2 and results[0] is not results[1]
print('concurrent_first_calls',len(results),'factory_builds',len(builds),'same_object',results[0] is results[1])
print('warm_call_reuses_cached_object',factory() is factory())
```
- Actual stdout:
```text
concurrent_first_calls 2 factory_builds 2 same_object False
warm_call_reuses_cached_object True
```
- Forced concurrent first entry shows memoization is not single-flight initialization; warm calls reuse cached object in this fixture. This deliberately synchronized standalone control does not import SDK or construct a real TypeAdapter and is not an SDK defect, latency estimate, or provider experiment.
- Retest actual merged SDK with first local tool, first MCP call, concurrent first restore, warm restore, malformed restored payload and authorization/receipt controls; separately count adapter construction, schema validation, fallback and external effects.

## NO_DECISION_SECTION
NO_DECISION / NO_HOST_PROMOTION. Same upstream lineage plus one local control; no independent SDK reproduction or host adoption claim.

## EVIDENCE_DELTA
- NEW_EVIDENCE: exact merged restore fallback branches and actual concurrent cache control.
- CORRECTED_INTERPRETATION: cached factory != exactly-once initialization; restored item != all validations passed.
- UNCHANGED_BOUNDARY: SOURCE_CHANGE != RELEASE != HOST_ADOPTED; validator cache != run state.
- NEW_COUNTEREVIDENCE: overlapping first calls create two objects; warm calls reuse one; validation-error fallback exists.
- UNKNOWN_RETAINED: production concurrency cost, SDK correctness under concurrent restore, NEXUS applicability.
- NEXT_RETEST_CONDITION: exact installed SDK, first/warm/concurrent restore with validation and fallback observability.

## NEXT_HANDOFF
Retain H1/H2 for next eligible closed week; no host change or premature month close.

## BOUNDARY_CHECK
Original H1 merge and main readback, exact source review and standalone control executed. Full checker, SDK tests, benchmark and host runtime NOT_EXECUTED. Human-authorized merge distinct from independent human review.
