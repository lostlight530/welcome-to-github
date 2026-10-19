"""Deterministic, researcher-defined MCP sampling evidence-gate fixture

This is NOT a protocol conformance suite or an MCP SDK runtime test
Sources: MCP sampling specifications 2025-11-25 and 2026-07-28,
MCP Python SDK v2 and PHP SDK living documentation, accessed 2026-10-20
"""
from dataclasses import dataclass, replace

OLD = "2025-11-25"
NEW = "2026-07-28"


@dataclass(frozen=True)
class Snapshot:
    sdk: str = "python_resolver"
    version: str = NEW
    sampling: bool = True
    sampling_tools: bool = True
    requests_tools: bool = True
    route: str = "input_required"
    tool_use_ids: tuple[str, ...] = ("call_a", "call_b")
    tool_result_ids: tuple[str, ...] = ("call_a", "call_b")
    mixed_result_content: bool = False


def documented_eligible(x: Snapshot) -> bool:
    if not x.sampling or (x.requests_tools and not x.sampling_tools):
        return False
    if x.version == OLD:
        return x.route == "standalone" and x.sdk in {"python_resolver", "php_gateway"}
    if x.version == NEW:
        return x.route == "input_required" and x.sdk == "python_resolver"
    return False


def tool_loop_balanced(x: Snapshot) -> bool:
    if not x.requests_tools:
        return True
    a, b = x.tool_use_ids, x.tool_result_ids
    return (
        bool(a)
        and len(a) == len(set(a))
        and len(b) == len(set(b))
        and set(a) == set(b)
        and not x.mixed_result_content
    )


base = Snapshot()
cases: list[tuple[str, Snapshot, tuple[bool, bool, bool]]] = [
    ("new_python_mrr_baseline", base, (True, True, True)),
    ("new_php_gateway", replace(base, sdk="php_gateway"), (False, True, False)),
    ("new_missing_sampling_cap", replace(base, sampling=False), (False, True, False)),
    ("new_missing_tools_cap", replace(base, sampling_tools=False), (False, True, False)),
    ("new_standalone_route", replace(base, route="standalone"), (False, True, False)),
    ("new_missing_result", replace(base, tool_result_ids=("call_a",)), (True, False, False)),
    ("new_extra_result", replace(base, tool_result_ids=("call_a", "call_b", "call_c")), (True, False, False)),
    ("new_mixed_result", replace(base, mixed_result_content=True), (True, False, False)),
    ("new_duplicate_use", replace(base, tool_use_ids=("call_a", "call_a")), (True, False, False)),
    ("new_wrong_result", replace(base, tool_result_ids=("call_a", "call_z")), (True, False, False)),
    ("old_python_standalone", replace(base, version=OLD, route="standalone"), (True, True, True)),
    ("old_php_standalone", replace(base, version=OLD, route="standalone", sdk="php_gateway"), (True, True, True)),
    ("old_python_mrr_wrong_route", replace(base, version=OLD), (False, True, False)),
    ("old_php_missing_sampling_cap", replace(base, version=OLD, route="standalone", sdk="php_gateway", sampling=False), (False, True, False)),
]

assertions = 0
for name, case, expected in cases:
    actual = (documented_eligible(case), tool_loop_balanced(case))
    actual = (*actual, all(actual))
    for got, want in zip(actual, expected):
        assert got == want, (name, got, want)
        assertions += 1

assert all(not documented_eligible(x) for _, x, _ in cases if x.version == NEW and x.sdk == "php_gateway")
assert documented_eligible(base)
assert not tool_loop_balanced(replace(base, tool_result_ids=("call_a",)))
assert not documented_eligible(replace(base, sampling=False))
assertions += 4
print(
    f"cases={len(cases)} assertions={assertions} "
    f"eligible={sum(documented_eligible(x) for _, x, _ in cases)} "
    f"balanced={sum(tool_loop_balanced(x) for _, x, _ in cases)} "
    f"eligible_balanced={sum(documented_eligible(x) and tool_loop_balanced(x) for _, x, _ in cases)} "
    f"new_php_eligible={sum(documented_eligible(x) for _, x, _ in cases if x.version == NEW and x.sdk == 'php_gateway')}"
)
