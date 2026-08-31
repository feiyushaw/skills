#!/usr/bin/env python3
"""Offline smoke tests for pack expansion and installation behavior."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install-pack.py"
SKILLS = ROOT / "skills"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(INSTALLER), *args],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )


def installed_names(path: Path) -> set[str]:
    return {p.name for p in path.iterdir() if p.is_dir() or p.is_symlink()}


def main() -> int:
    stable = {
        p.parent.name
        for p in SKILLS.glob("*/*/SKILL.md")
        if p.parent.parent.name != "experimental"
    }
    experimental = {
        p.parent.name
        for p in (SKILLS / "experimental").glob("*/SKILL.md")
    }

    with tempfile.TemporaryDirectory(prefix="skills-distribution-") as tmp:
        root = Path(tmp)

        dry_target = root / "dry-run"
        dry = run("full", "--target", str(dry_target), "--dry-run")
        if dry_target.exists():
            raise AssertionError("dry-run created the target directory")
        if f"Resolved {len(stable)} skills from pack 'full'." not in dry.stdout:
            raise AssertionError("full dry-run resolved an unexpected number of skills")

        full_target = root / "full"
        run("full", "--target", str(full_target), "--mode", "copy")
        full_names = installed_names(full_target)
        if full_names != stable:
            missing = sorted(stable - full_names)
            extra = sorted(full_names - stable)
            raise AssertionError(f"full pack mismatch: missing={missing}, extra={extra}")
        for name in full_names:
            if not (full_target / name / "SKILL.md").exists():
                raise AssertionError(f"installed stable skill lacks SKILL.md: {name}")

        # Installing again without --force is intentionally idempotent-by-skip.
        run("full", "--target", str(full_target), "--mode", "copy")
        if installed_names(full_target) != stable:
            raise AssertionError("second full installation changed the installed set")

        experimental_target = root / "experimental"
        run("experimental", "--target", str(experimental_target), "--mode", "symlink")
        if installed_names(experimental_target) != experimental:
            raise AssertionError("experimental pack does not match experimental domain")
        if any(not (experimental_target / name).is_symlink() for name in experimental):
            raise AssertionError("experimental symlink-mode install did not create symlinks")

    print(
        f"Distribution smoke test passed ({len(stable)} stable + "
        f"{len(experimental)} experimental skills)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
