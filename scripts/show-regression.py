#!/usr/bin/env python3
"""Render one workflow regression fixture as a human/agent evaluation checklist."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGRESSIONS = ROOT / "regressions"


def bullets(values: list[str]) -> str:
    return "\n".join(f"- {value}" for value in values)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", help="Fixture id, e.g. engineering-grill-to-spec")
    args = parser.parse_args()

    path = REGRESSIONS / args.fixture / "fixture.json"
    if not path.exists():
        known = ", ".join(sorted(p.parent.name for p in REGRESSIONS.glob("*/fixture.json")))
        parser.error(f"unknown fixture '{args.fixture}'. Known: {known}")

    data = json.loads(path.read_text(encoding="utf-8"))
    scenario = data["scenario"]
    expected = data["expected"]

    print(f"# Regression: {data['id']}")
    print(f"\nDomain: {data['domain']} | Status: {data['status']}")
    print("\n## Workflow\n")
    print(" -> ".join(data["workflow"]))
    print("\n## Scenario\n")
    print(scenario["prompt"])
    if scenario.get("context"):
        print("\n### Context\n")
        print(bullets(scenario["context"]))
    print("\n## Expected artifacts\n")
    print(bullets(expected["artifacts"]))
    print("\n## Required behaviors\n")
    print(bullets(expected["required_behaviors"]))
    print("\n## Forbidden behaviors\n")
    print(bullets(expected["forbidden_behaviors"]))
    print("\n## Completion criteria\n")
    print(bullets(expected["completion_criteria"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
