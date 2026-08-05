"""Deterministic observation declarations with no I/O or runtime integration."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
import hashlib
import json
from typing import Any


__all__ = ["DeclarationValidationError", "ObservationDeclaration"]


class DeclarationValidationError(ValueError):
    """Raised when an observation declaration is incomplete or ambiguous."""


def _required_text(field: str, value: object) -> str:
    if not isinstance(value, str):
        raise DeclarationValidationError(f"{field} must be a string")
    if not value.strip():
        raise DeclarationValidationError(f"{field} must not be empty")
    if value != value.strip():
        raise DeclarationValidationError(
            f"{field} must not contain leading or trailing whitespace"
        )
    return value


def _text_tuple(
    field: str,
    value: object,
    *,
    allow_empty: bool,
) -> tuple[str, ...]:
    if isinstance(value, str) or not isinstance(value, Sequence):
        raise DeclarationValidationError(f"{field} must be a sequence of strings")

    items = tuple(
        _required_text(f"{field}[{index}]", item)
        for index, item in enumerate(value)
    )
    if not allow_empty and not items:
        raise DeclarationValidationError(f"{field} must not be empty")
    if len(set(items)) != len(items):
        raise DeclarationValidationError(f"{field} must not contain duplicates")
    return items


@dataclass(frozen=True, slots=True)
class ObservationDeclaration:
    """Declare why an observation may enter a knowledge boundary."""

    identity: str
    source: str
    claim: str
    evidence: tuple[str, ...]
    boundary: tuple[str, ...]
    supersedes: tuple[str, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "identity", _required_text("identity", self.identity))
        object.__setattr__(self, "source", _required_text("source", self.source))
        object.__setattr__(self, "claim", _required_text("claim", self.claim))
        object.__setattr__(
            self,
            "evidence",
            _text_tuple("evidence", self.evidence, allow_empty=False),
        )
        object.__setattr__(
            self,
            "boundary",
            _text_tuple("boundary", self.boundary, allow_empty=False),
        )
        object.__setattr__(
            self,
            "supersedes",
            _text_tuple("supersedes", self.supersedes, allow_empty=True),
        )

    def to_canonical_dict(self) -> dict[str, Any]:
        """Return a JSON-compatible declaration with stable field names."""

        return {
            "identity": self.identity,
            "source": self.source,
            "claim": self.claim,
            "evidence": list(self.evidence),
            "boundary": list(self.boundary),
            "supersedes": list(self.supersedes),
        }

    def to_canonical_json(self) -> str:
        """Serialize without locale, clock, randomness, or platform variance."""

        return json.dumps(
            self.to_canonical_dict(),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )

    def fingerprint(self) -> str:
        """Return the SHA-256 identity of the canonical declaration."""

        return hashlib.sha256(self.to_canonical_json().encode("utf-8")).hexdigest()
