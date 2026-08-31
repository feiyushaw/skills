#!/usr/bin/env python3
"""List skills in the monorepo with domain and frontmatter description."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"


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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain", help="Only show one domain")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    rows: list[dict[str, str]] = []
    for skill_md in sorted(SKILLS_ROOT.glob("*/*/SKILL.md")):
        domain = skill_md.parent.parent.name
        if args.domain and domain != args.domain:
            continue
        meta = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        rows.append(
            {
                "domain": domain,
                "name": skill_md.parent.name,
                "description": meta.get("description", ""),
            }
        )

    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0

    width_domain = max([len(r["domain"]) for r in rows] + [6])
    width_name = max([len(r["name"]) for r in rows] + [4])
    for row in rows:
        print(f"{row['domain']:<{width_domain}}  {row['name']:<{width_name}}  {row['description']}")
    print(f"\n{len(rows)} skill(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
