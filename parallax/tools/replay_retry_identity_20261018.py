"""Synthetic acknowledgement / retry / task evidence gate; not an HTTP or A2A implementation."""
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Snapshot:
    acknowledged: bool = True
    key: str | None = 'retry-A'
    original_key: str = 'retry-A'
    same_parameters: bool = True
    scope_matches: bool = True
    ledger_active: bool = True
    operation_id: str | None = 'op-A'
    task_id: str | None = 'task-A'
    operation_task_bound: bool = True
    task_state: str = 'COMPLETED'
    effect_receipt: bool = True
    client_accepted: bool = True
    prior_execution_conflict: bool = False

def gates(x: Snapshot) -> tuple[bool, bool, bool]:
    shortcut = x.acknowledged
    retry_binding = all((shortcut, x.key is not None, x.key == x.original_key,
                         x.same_parameters, x.scope_matches, x.ledger_active,
                         bool(x.operation_id), bool(x.task_id),
                         x.operation_task_bound, not x.prior_execution_conflict))
    settled = all((retry_binding, x.task_state == 'COMPLETED',
                   x.effect_receipt, x.client_accepted))
    return shortcut, retry_binding, settled

base = Snapshot()
cases = {
    'baseline': (base, (True, True, True)),
    'ack_missing': (replace(base, acknowledged=False), (False, False, False)),
    'key_missing': (replace(base, key=None), (True, False, False)),
    'key_changed': (replace(base, key='retry-B'), (True, False, False)),
    'parameters_changed': (replace(base, same_parameters=False), (True, False, False)),
    'namespace_changed': (replace(base, scope_matches=False), (True, False, False)),
    'ledger_expired': (replace(base, ledger_active=False), (True, False, False)),
    'operation_missing': (replace(base, operation_id=None), (True, False, False)),
    'task_missing': (replace(base, task_id=None), (True, False, False)),
    'task_unbound': (replace(base, operation_task_bound=False), (True, False, False)),
    'task_working': (replace(base, task_state='WORKING'), (True, True, False)),
    'task_failed': (replace(base, task_state='FAILED'), (True, True, False)),
    'effect_unverified': (replace(base, effect_receipt=False), (True, True, False)),
    'client_rejected': (replace(base, client_accepted=False), (True, True, False)),
    'execution_conflict': (replace(base, prior_execution_conflict=True), (True, False, False)),
}
assertions = 0
for name, (snapshot, expected) in cases.items():
    actual = gates(snapshot)
    for step, (got, want) in enumerate(zip(actual, expected)):
        assert got == want, (name, step, got, want)
        assertions += 1
counts = tuple(sum(gates(x)[i] for x, _ in cases.values()) for i in range(3))
for actual, expected in zip(counts, (14, 5, 1)):
    assert actual == expected, (actual, expected)
    assertions += 1
assert counts[0] - counts[2] == 13
assertions += 1
assert counts[1] - counts[2] == 4
assertions += 1
assert all((not gates(x)[2] or gates(x)[1]) for x, _ in cases.values())
assertions += 1
print(f'cases={len(cases)} assertions={assertions} acknowledged={counts[0]} retry_bound={counts[1]} settled={counts[2]} acknowledged_negative={counts[0]-counts[2]} retry_bound_unsettled={counts[1]-counts[2]}')
