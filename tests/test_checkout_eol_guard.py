"""Regression checks for fail-closed checkout EOL reconciliation."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "docs" / "brain"))
from checkout_eol_guard import CheckoutIntegrityError, stabilize_checkout


class CheckoutEolGuardTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        self.git("init", "-q")
        self.git("config", "user.name", "CI Fixture")
        self.git("config", "user.email", "ci-fixture@example.invalid")
        (self.root / ".gitattributes").write_text("* text=auto\n*.md text eol=lf\n")
        self.git("add", ".gitattributes")
        self.git("commit", "-qm", "attributes")
        # Store legacy CRLF bytes in index without the normal clean filter.
        (self.root / "legacy.md").write_bytes(b"original\r\nsecond\n")
        raw_sha = self.git("hash-object", "-w", "--no-filters", "legacy.md").strip()
        self.git("update-index", "--add", "--cacheinfo", "100644," + raw_sha + ",legacy.md")
        self.git("commit", "-qm", "legacy raw blob")
        self.original_blob = self.git("show", ":legacy.md")

    def git(self, *arguments):
        return subprocess.check_output(
            ["git", *arguments], cwd=self.root, stderr=subprocess.DEVNULL
        ).decode()

    def test_exact_blob_exception_is_local_and_idempotent(self):
        self.assertIn("legacy.md", self.git("status", "--porcelain"))
        outcome = stabilize_checkout(self.root)
        self.assertEqual(outcome["raw_blob_eol_exceptions"], 1)
        self.assertEqual(self.git("status", "--porcelain"), "")
        self.assertEqual((self.root / "legacy.md").read_bytes(), self.original_blob.encode())
        self.assertIn("/legacy.md -text", (self.root / ".git/info/attributes").read_text())
        self.assertEqual(stabilize_checkout(self.root)["raw_blob_eol_exceptions"], 0)

    def test_actual_post_preflight_change_remains_visible(self):
        stabilize_checkout(self.root)
        (self.root / "legacy.md").write_bytes(b"tampered\r\nsecond\n")
        self.assertIn("legacy.md", self.git("status", "--porcelain"))
        self.assertIn("legacy.md", self.git("diff", "--name-only"))

    def test_real_preflight_change_is_rejected(self):
        (self.root / "legacy.md").write_bytes(b"different\r\nsecond\n")
        with self.assertRaisesRegex(CheckoutIntegrityError, "real baseline byte change"):
            stabilize_checkout(self.root)
        self.assertFalse((self.root / ".git/info/attributes").exists())

    def test_untracked_preflight_change_is_rejected(self):
        (self.root / "extra.txt").write_text("not a checkout file\n")
        with self.assertRaisesRegex(CheckoutIntegrityError, "untracked"):
            stabilize_checkout(self.root)

    def test_staged_preflight_change_is_rejected(self):
        (self.root / "new.md").write_text("already staged\n")
        self.git("add", "new.md")
        with self.assertRaisesRegex(CheckoutIntegrityError, "staged"):
            stabilize_checkout(self.root)


if __name__ == "__main__":
    unittest.main()
