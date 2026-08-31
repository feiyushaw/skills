#!/usr/bin/env python3
"""Install one skills pack into an agent-specific target directory.

The repository intentionally does not guess where a given agent stores skills.
Pass --target explicitly, for example a project-local or user-level skill folder.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
PACKS_ROOT = ROOT / "packs"


def parse_simple_yaml_list(text: str, key: str) -> list[str]:
    values: list[str] = []
    active = False
    for raw in text.splitlines():
        line = raw.rstrip()
        if line == f"{key}:":
            active = True
            continue
        if active:
            stripped = line.strip()
            if stripped.startswith("- "):
                values.append(stripped[2:].strip())
                continue
            if stripped and not line.startswith(" "):
                break
    return values


def discover_skills() -> dict[str, Path]:
    found: dict[str, Path] = {}
    for skill_md in sorted(SKILLS_ROOT.glob("*/*/SKILL.md")):
        name = skill_md.parent.name
        if name in found:
            raise RuntimeError(f"duplicate skill name: {name}")
        found[name] = skill_md.parent
    return found


def read_pack(name: str) -> tuple[list[str], list[str]]:
    path = PACKS_ROOT / f"{name}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"unknown pack '{name}' ({path})")
    text = path.read_text(encoding="utf-8")
    return parse_simple_yaml_list(text, "skills"), parse_simple_yaml_list(text, "includes")


def expand_pack(name: str, stack: tuple[str, ...] = ()) -> list[str]:
    if name in stack:
        cycle = " -> ".join((*stack, name))
        raise RuntimeError(f"pack include cycle: {cycle}")

    skills, includes = read_pack(name)
    ordered: list[str] = []
    for included in includes:
        ordered.extend(expand_pack(included, (*stack, name)))
    ordered.extend(skills)

    deduped: list[str] = []
    seen: set[str] = set()
    for skill in ordered:
        if skill not in seen:
            seen.add(skill)
            deduped.append(skill)
    return deduped


def remove_existing(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pack", help="Pack name, e.g. engineering, research, full")
    parser.add_argument("--target", required=True, type=Path, help="Agent skill directory")
    parser.add_argument("--mode", choices=("copy", "symlink"), default="copy")
    parser.add_argument("--force", action="store_true", help="Replace existing installed skills")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing")
    args = parser.parse_args()

    available = discover_skills()
    requested = expand_pack(args.pack)
    missing = [name for name in requested if name not in available]
    if missing:
        print(f"Pack '{args.pack}' references missing skills: {', '.join(missing)}", file=sys.stderr)
        return 2

    target = args.target.expanduser().resolve()
    if not args.dry_run:
        target.mkdir(parents=True, exist_ok=True)

    for name in requested:
        source = available[name].resolve()
        destination = target / name
        action = f"{args.mode}: {name} -> {destination}"

        if destination.exists() or destination.is_symlink():
            if not args.force:
                print(f"skip existing: {destination}")
                continue
            action = f"replace + {action}"
            if not args.dry_run:
                remove_existing(destination)

        print(action)
        if args.dry_run:
            continue
        if args.mode == "copy":
            shutil.copytree(source, destination)
        else:
            destination.symlink_to(source, target_is_directory=True)

    print(f"Resolved {len(requested)} skills from pack '{args.pack}'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
