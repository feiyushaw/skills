#!/usr/bin/env python3
"""Validate semantic regression-fixture contracts and referenced skill names."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REGRESSIONS = ROOT / "regressions"
REQUIRED_DOMAINS = {"engineering", "research", "presentation", "patent"}
ALLOWED_STATUS = {"stable", "experimental"}


def nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def nonempty_string_list(value: object) -> bool:
    return isinstance(value, list) and bool(value) and all(nonempty_string(item) for item in value)


def main() -> int:
    errors: list[str] = []
    skill_names = {p.parent.name for p in SKILLS.glob("*/*/SKILL.md")}
    domains = {p.name for p in SKILLS.iterdir() if p.is_dir()} if SKILLS.exists() else set()

    fixture_paths = sorted(REGRESSIONS.glob("*/fixture.json")) if REGRESSIONS.exists() else []
    if not fixture_paths:
        errors.append("no regression fixtures found")

    seen_ids: set[str] = set()
    covered_domains: set[str] = set()

    for path in fixture_paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: cannot parse JSON: {exc}")
            continue

        fixture_id = data.get("id")
        if not nonempty_string(fixture_id):
            errors.append(f"{path}: id is required")
        elif fixture_id != path.parent.name:
            errors.append(f"{path}: id must equal directory name '{path.parent.name}'")
        elif fixture_id in seen_ids:
            errors.append(f"{path}: duplicate fixture id '{fixture_id}'")
        else:
            seen_ids.add(fixture_id)

        domain = data.get("domain")
        if domain not in domains:
            errors.append(f"{path}: unknown domain '{domain}'")
        else:
            covered_domains.add(domain)

        if data.get("status") not in ALLOWED_STATUS:
            errors.append(f"{path}: status must be one of {sorted(ALLOWED_STATUS)}")

        workflow = data.get("workflow")
        if not nonempty_string_list(workflow):
            errors.append(f"{path}: workflow must be a non-empty list of skill names")
        else:
            missing = [name for name in workflow if name not in skill_names]
            if missing:
                errors.append(f"{path}: workflow references missing skills: {', '.join(missing)}")

        scenario = data.get("scenario")
        if not isinstance(scenario, dict) or not nonempty_string(scenario.get("prompt")):
            errors.append(f"{path}: scenario.prompt is required")
        elif "context" in scenario and not nonempty_string_list(scenario.get("context")):
            errors.append(f"{path}: scenario.context must be a non-empty string list when present")

        expected = data.get("expected")
        if not isinstance(expected, dict):
            errors.append(f"{path}: expected object is required")
            continue
        for key in ("artifacts", "required_behaviors", "forbidden_behaviors", "completion_criteria"):
            if not nonempty_string_list(expected.get(key)):
                errors.append(f"{path}: expected.{key} must be a non-empty string list")

    missing_domains = REQUIRED_DOMAINS - covered_domains
    if missing_domains:
        errors.append("critical domains without regression coverage: " + ", ".join(sorted(missing_domains)))

    if errors:
        print("Regression validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Regression validation passed ({len(fixture_paths)} fixtures, "
        f"{len(covered_domains)} covered domains)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
