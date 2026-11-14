"""Fail-closed checkout-only mitigation for indexed raw CRLF blobs.

Some historical tracked blobs contain CRLF despite the repository's later
.gitattributes LF policy. Git can report those bytes as modified even in a
fresh checkout. This helper compares index and worktree bytes *before* any
lifecycle action and exempts only proven identical raw blobs in this runner's
untracked .git/info/attributes. It never changes tracked files or Git index.

Real content changes after the bootstrap still surface in git diff/status.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


class CheckoutIntegrityError(RuntimeError):
    """Baseline has an actual change or cannot be proven byte-identical."""


def _git(root: Path, *args: str) -> bytes:
    command = subprocess.run(
        ["git", *args], cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=False,
    )
    if command.returncode:
        raise CheckoutIntegrityError(
            f"git {args[0]} exited {command.returncode}: "
            + command.stderr.decode("utf-8", errors="replace")[:2000]
        )
    return command.stdout


def _paths(payload: bytes) -> list[str]:
    return [part.decode("utf-8") for part in payload.split(b"\0") if part]


def _pattern(path: str) -> str:
    # No ambiguous Git attribute globs or path quoting; fail closed instead.
    if not path or any(char in path for char in " \t\r\n\\*?[]") or path.startswith("/"):
        raise CheckoutIntegrityError(f"cannot safely scope the EOL exception: {path!r}")
    return "/" + path + " -text\n"


def stabilize_checkout(root: Path = Path(".")) -> dict[str, object]:
    root = root.resolve()
    if _paths(_git(root, "diff", "--cached", "--name-only", "-z")):
        raise CheckoutIntegrityError("preflight staged changes are not permitted")
    if _paths(_git(root, "ls-files", "--others", "--exclude-standard", "-z")):
        raise CheckoutIntegrityError("preflight untracked worktree files are not permitted")

    dirty = _paths(_git(root, "diff", "--name-only", "-z"))
    exceptions = []
    for path in dirty:
        target = root / path
        if not target.is_file() or target.is_symlink():
            raise CheckoutIntegrityError(f"changed path is not an ordinary file: {path!r}")
        raw = target.read_bytes()
        index = _git(root, "show", ":" + path)
        if raw != index:
            raise CheckoutIntegrityError(f"real baseline byte change: {path!r}")
        if b"\r\n" not in raw:
            raise CheckoutIntegrityError(f"no CRLF evidence for raw/index mismatch: {path!r}")
        eol_attr = _git(root, "check-attr", "eol", "--", path).decode("utf-8", errors="replace")
        if not eol_attr.rstrip().endswith(": lf"):
            raise CheckoutIntegrityError(f"not a forced-LF attribute: {path!r}: {eol_attr!r}")
        exceptions.append(_pattern(path))

    attr_location = _git(root, "rev-parse", "--git-path", "info/attributes").decode().strip()
    attr_path = Path(attr_location)
    if not attr_path.is_absolute():
        attr_path = root / attr_path
    original = attr_path.read_bytes() if attr_path.exists() else None
    if exceptions:
        attr_path.parent.mkdir(parents=True, exist_ok=True)
        sep = b"" if not original or original.endswith(b"\n") else b"\n"
        attr_path.write_bytes((original or b"") + sep + "".join(exceptions).encode())

    try:
        status = _git(root, "status", "--porcelain", "-z")
        if status or _git(root, "diff", "--name-only", "-z"):
            raise CheckoutIntegrityError("checkout remains dirty after exact-blob EOL exceptions")
    except Exception:
        # Restore local metadata on failure; tracked files have never been touched.
        if exceptions:
            if original is None:
                attr_path.unlink(missing_ok=True)
            else:
                attr_path.write_bytes(original)
        raise
    return {
        "status": "CLEAN_EXACT_RAW_INDEX_BASELINE",
        "raw_blob_eol_exceptions": len(exceptions),
        "tracked_files_modified": 0,
        "index_modified": False,
    }


def main() -> int:
    try:
        print(json.dumps(stabilize_checkout(), sort_keys=True))
        return 0
    except (CheckoutIntegrityError, OSError, UnicodeError) as exc:
        print(f"CHECKOUT_BASELINE_REJECTED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
