# Repository instructions for agents

This repository contains reusable agent skills. Treat skill behavior, invocation metadata, references, and provenance as product code.

## Architecture

- `skills/core/`: domain-independent behavior primitives and routers.
- `skills/<domain>/`: work-domain skills.
- `packs/`: declarative groupings only; do not put workflow rules here.
- `docs/`: human/agent design documentation; docs are not registered skills.
- `scripts/`: repository validation and maintenance utilities.

## Editing rules

1. Keep skills independently installable. A skill may invoke another named skill, but its own references/templates/scripts must live inside its directory.
2. Keep `SKILL.md` focused on behavior that affects execution. Move optional deep reference material under the skill's `references/` directory.
3. Use standard terminology. Do not invent synonyms for established domain concepts merely for style.
4. Do not turn domain uncertainty into confident prose. Preserve claim strength, scope, evidence status, terminology, notation, provenance, and legal/research caveats.
5. Prefer positive operational instructions with observable completion criteria.
6. User-invoked orchestrators should set `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
7. Model-invoked primitives should remain small enough to compose into domain workflows.
8. Do not copy content from private source repositories into this public repository unless the migration plan explicitly marks that source as approved for publication.
9. Record adapted third-party material in `THIRD_PARTY_NOTICES.md` and preserve required license notices.
10. Run `python3 scripts/validate-skills.py` after structural changes.

## Naming

- Skill directory names: lowercase kebab-case.
- Frontmatter `name` must equal the skill directory name.
- Prefer task-oriented names such as `research-idea-refiner`, `code-review`, or `presentation-architect`.

## Dependency direction

`core -> no domain dependencies`

`domain skill -> core allowed`

`pack -> references skills only`

Avoid cyclic skill dependencies and hidden cross-domain coupling.
