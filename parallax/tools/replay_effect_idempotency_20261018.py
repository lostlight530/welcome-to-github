"""PX-20261018-REPLAY-EFFECT-IDEMPOTENCY synthetic control only, no live API."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Req:
    key: str | None
    payload: str
    hour: int = 0


class Sink:
    def __init__(self):
        self.cache = {}
        self.effects = []
        self.attempts = self.dedup = self.rejected = 0

    def apply(self, req):
        self.attempts += 1
        old = self.cache.get(req.key) if req.key is not None else None
        if old and req.hour - old[0] < 24:
            if req.payload != old[1]:
                self.rejected += 1
                return "REJECT_PARAMETER_MISMATCH"
            self.dedup += 1
            return old[2]
        receipt = f"synthetic-receipt-{len(self.effects) + 1}"
        self.effects.append(req.payload)
        if req.key is not None:
            self.cache[req.key] = (req.hour, req.payload, receipt)
        return receipt


def run():
    a = Req(None, "send:A")
    k = Req("job-A:tool-1", "send:A")
    cases = [
        ("baseline_once", [a], (1, 1, 0, 0), "single"),
        ("lost_ack_unkeyed", [a, a], (2, 2, 0, 0), "different"),
        ("lost_ack_stable_key", [k, k], (2, 1, 1, 0), "same"),
        ("lost_ack_rotated_key", [Req("attempt-1", "send:A"), Req("attempt-2", "send:A")], (2, 2, 0, 0), "different"),
        ("same_key_changed_payload", [k, Req(k.key, "send:B")], (2, 1, 0, 1), "rejected"),
        ("same_key_expired", [k, Req(k.key, k.payload, 25)], (2, 2, 0, 0), "different"),
        ("cross_workflow_key_collision", [k, k], (2, 1, 1, 0), "same"),
        ("checkpoint_recorded_no_retry", [k], (1, 1, 0, 0), "single"),
    ]
    checks = 0
    totals = [0, 0, 0]
    for name, requests, expected, relation in cases:
        sink = Sink()
        replies = [sink.apply(req) for req in requests]
        actual = (sink.attempts, len(sink.effects), sink.dedup, sink.rejected)
        for got, want in zip(actual, expected):
            assert got == want, (name, got, want)
            checks += 1
        observed = ("single" if len(replies) == 1 else
                    "rejected" if replies[1] == "REJECT_PARAMETER_MISMATCH" else
                    "same" if replies[0] == replies[1] else "different")
        assert observed == relation, (name, observed, relation)
        checks += 1
        for i, value in enumerate(actual[1:]):
            totals[i] += value
        print(f"{name}: attempts={actual[0]} effects={actual[1]} deduplicated={actual[2]} rejected={actual[3]} relation={observed}")
    for got, want in zip((len(cases), *totals), (8, 11, 2, 1)):
        assert got == want, (got, want)
        checks += 1
    print(f"cases={len(cases)} assertions={checks} effects={totals[0]} deduplicated={totals[1]} rejected={totals[2]}")


if __name__ == "__main__":
    run()
