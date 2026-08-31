# Provenance

This document records the source snapshot used for the initial monorepo consolidation.

| Destination domain | Source repository | Source commit | Migration type |
|---|---|---|---|
| `research` | `feiyushaw/academic_skills` | `b03a7651300081b9d292630fe50bb8c4be8d2007` | owner-controlled content migration + self-containment fixes |
| `patent` | `feiyushaw/patent_skills` | `be8f362d72a3f1df4058cccf8b39f3b75ab62b49` | owner-controlled content migration + reference localization |
| `presentation` | `feiyushaw/presentation_skill` | `0bcae01f201c8edac4b9243ffa38534d9b9c7a5d` | owner-controlled content migration + architecture split |
| `core/engineering/productivity` | `mattpocock/skills` | `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76` | selective MIT-licensed adaptation |

## Owner-controlled source repos

Research, patent, and presentation sources are retained as historical repositories. Migration intentionally preserves their conceptual boundaries while adapting paths to the new self-contained skill contract.

## Third-party adaptation policy

For Matt Pocock-derived work, this repository preserves the upstream MIT license in `licenses/mattpocock-skills-MIT.txt` and records adapted skills in `THIRD_PARTY_NOTICES.md`.

Subsequent major rewrites should keep this provenance record when upstream design materially influenced the local skill.
