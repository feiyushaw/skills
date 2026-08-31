#!/usr/bin/env python3
"""Validate the structural contract of skills in this repository."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    data: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def main() -> int:
    errors: list[str] = []
    if not SKILLS.exists():
        errors.append("skills/ directory is missing")
    else:
        for skill_md in sorted(SKILLS.glob("*/*/SKILL.md")):
            skill_dir = skill_md.parent
            name = skill_dir.name
            if not KEBAB.fullmatch(name):
                errors.append(f"{skill_dir}: directory name is not lowercase kebab-case")
            text = skill_md.read_text(encoding="utf-8")
            meta = parse_frontmatter(text)
            if not meta:
                errors.append(f"{skill_md}: missing valid frontmatter")
                continue
            if meta.get("name") != name:
                errors.append(f"{skill_md}: frontmatter name must equal '{name}'")
            if not meta.get("description"):
                errors.append(f"{skill_md}: description is required")

        nested = list(SKILLS.glob("*/*/*/SKILL.md"))
        if nested:
            errors.extend(f"{p}: skills must be exactly skills/<domain>/<name>/SKILL.md" for p in nested)

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    count = len(list(SKILLS.glob("*/*/SKILL.md"))) if SKILLS.exists() else 0
    print(f"Skill validation passed ({count} skills).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
