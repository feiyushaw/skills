# Provenance

This document records source snapshots and major adaptation waves used by the monorepo.

| Destination domain | Source repository | Source commit | Migration type |
|---|---|---|---|
| `research` | `feiyushaw/academic_skills` | `b03a7651300081b9d292630fe50bb8c4be8d2007` | owner-controlled content migration + self-containment fixes |
| `patent` | `feiyushaw/patent_skills` | `be8f362d72a3f1df4058cccf8b39f3b75ab62b49` | owner-controlled content migration + reference localization |
| `presentation` | `feiyushaw/presentation_skill` | `0bcae01f201c8edac4b9243ffa38534d9b9c7a5d` | owner-controlled content migration + architecture split |
| `core/engineering/productivity` | `mattpocock/skills` | `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76` | selective MIT-licensed adaptation |

## V2 local extensions

New locally-authored workflow closures include:

- `research/reviewer-response`;
- `presentation/powerpoint-presentation`;
- `presentation/presentation-review`;
- `patent/patent-portfolio-planner`;
- `experimental/skill-audit`;
- pack discovery/install tooling.

V2 also adapts additional Matt Pocock patterns into local, environment-decoupled versions:

- `engineering/grill-with-docs`;
- `engineering/triage`;
- `engineering/improve-codebase-architecture`;
- `experimental/retro`.

## Owner-controlled source repos

Research, patent, and presentation sources remain available as historical repositories. The monorepo is the canonical active distribution after migration.

## Third-party adaptation policy

For Matt Pocock-derived work, this repository preserves the upstream MIT license in `licenses/mattpocock-skills-MIT.txt` and records adapted skills in `THIRD_PARTY_NOTICES.md`.

Later rewrites should retain provenance whenever upstream design materially influenced the local skill.
