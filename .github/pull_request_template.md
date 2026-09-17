## Outcome and exact scope
What changed, why, and what is explicitly out of scope?

- Base `main` SHA:
- Head SHA:
- Owning surface / logical period:
- Overlapping PR/branch check:

## Change classification
- [ ] implementation repair
- [ ] maintenance / governance repair
- [ ] Horizon evidence/policy correction
- [ ] Parallax maintenance/correction surface change
- [ ] other bounded repository change

## Evidence boundary
- [ ] Repository observations are distinguished from inference or proposal
- [ ] Horizon and Parallax producer identity is preserved
- [ ] External claims, if any, identify source and observation date
- [ ] Runner/checker evidence is revision-bound
- [ ] Unknown, missing, blocked, partial, unverified, or no-conclusion state remains explicit

## Changed and deliberately unchanged boundaries

## Verification actually executed
List exact checks, including `horizon-cortex/check.py`, `parallax/tools/check.py`, workflows, or other commands only when they were actually run, with observed results.

## Verification not executed
Use `NOT_EXECUTED` for relevant checks that were not run. Contract inspection is not checker execution.

## History, producer identity, and provenance
- [ ] Historical artifacts were not silently rewritten to make later knowledge appear earlier
- [ ] Current path presence was not presented as earlier execution evidence
- [ ] Parallax research production was not collapsed into repository maintenance state
- [ ] Private Jules prompts / repository memory / hidden reasoning / credentials were not exposed

## Concurrency and delivery
- [ ] Fresh `main` and live PR/branch ownership were rechecked before delivery
- [ ] Aggregate `main...branch` diff was reviewed
- [ ] No activity-only change was created where `NO_CHANGE_REQUIRED` was appropriate
- [ ] No direct `main` write, force-push, or auto-merge is requested by this PR

## Security and privacy
State impact on credentials, permissions, private data, generated artifacts, or public exposure. Follow `SECURITY.md` for sensitive details.

## Rollback
Describe the smallest safe rollback.

## Final review
- [ ] Change is focused and reviewable
- [ ] Required repository-facing surfaces remain synchronized
- [ ] Checks not run are explicit

Final doctrine and merge authority remains with the maintainer.
