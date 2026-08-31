#!/usr/bin/env python3
"""Validate structural and pack contracts for skills in this repository."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
PACKS = ROOT / "packs"
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
        data[key.strip()] = value.strip().strip('"')
    return data


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


def parse_simple_yaml_scalar(text: str, key: str) -> str | None:
    for raw in text.splitlines():
        if raw.startswith(f"{key}:"):
            return raw.split(":", 1)[1].strip().strip('"')
    return None


def find_pack_cycles(pack_includes: dict[str, list[str]]) -> list[str]:
    errors: list[str] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(name: str, path: tuple[str, ...]) -> None:
        if name in visiting:
            cycle = " -> ".join((*path, name))
            errors.append(f"pack include cycle: {cycle}")
            return
        if name in visited:
            return
        visiting.add(name)
        for child in pack_includes.get(name, []):
            if child in pack_includes:
                visit(child, (*path, name))
        visiting.remove(name)
        visited.add(name)

    for pack in pack_includes:
        visit(pack, ())
    return errors


def main() -> int:
    errors: list[str] = []
    skill_names: set[str] = set()

    if not SKILLS.exists():
        errors.append("skills/ directory is missing")
    else:
        for skill_md in sorted(SKILLS.glob("*/*/SKILL.md")):
            skill_dir = skill_md.parent
            name = skill_dir.name
            if not KEBAB.fullmatch(name):
                errors.append(f"{skill_dir}: directory name is not lowercase kebab-case")
            if name in skill_names:
                errors.append(f"duplicate skill name across domains: {name}")
            skill_names.add(name)

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
            errors.extend(
                f"{p}: skills must be exactly skills/<domain>/<name>/SKILL.md"
                for p in nested
            )

    pack_names = {p.stem for p in PACKS.glob("*.yaml")} if PACKS.exists() else set()
    pack_includes: dict[str, list[str]] = {}
    if not PACKS.exists():
        errors.append("packs/ directory is missing")
    else:
        for pack in sorted(PACKS.glob("*.yaml")):
            text = pack.read_text(encoding="utf-8")
            manifest_name = parse_simple_yaml_scalar(text, "name")
            if manifest_name != pack.stem:
                errors.append(f"{pack}: name must equal '{pack.stem}'")
            if not parse_simple_yaml_scalar(text, "description"):
                errors.append(f"{pack}: description is required")

            for skill in parse_simple_yaml_list(text, "skills"):
                if skill not in skill_names:
                    errors.append(f"{pack}: references missing skill '{skill}'")

            includes = parse_simple_yaml_list(text, "includes")
            pack_includes[pack.stem] = includes
            for included in includes:
                if included not in pack_names:
                    errors.append(f"{pack}: includes missing pack '{included}'")
                if included == pack.stem:
                    errors.append(f"{pack}: pack may not include itself")

        errors.extend(find_pack_cycles(pack_includes))

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill validation passed ({len(skill_names)} skills, {len(pack_names)} packs).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
