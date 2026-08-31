# Feiyu Skills

Composable skills for Codex, Claude Code, and other coding/research agents.

This repository is the unified home for reusable agent workflows across software engineering, research, presentations, patents, and productivity. It follows a small-and-composable design: domain skills own domain reasoning; shared interaction patterns live in `core`; packs provide convenient installation groups.

> Chinese documentation: [README.zh-CN.md](README.zh-CN.md)

## Work domains

| Domain | Purpose | Status |
|---|---|---|
| `core` | Shared agent primitives and routing | V1 scaffold |
| `engineering` | Specs, tickets, implementation, testing, debugging, review | planned |
| `research` | Literature, idea refinement, experiments, figures, papers, review | migration planned |
| `presentation` | Presentation architecture, Slidev, PPTX, review | migration planned |
| `patent` | Chinese patent mining, prior art, drafting, review | migration planned |
| `productivity` | Teaching, questionnaires, context handoff, utilities | planned |
| `experimental` | Unstable skills under evaluation | reserved |

## Design model

```text
                         core
              routing / interaction primitives
                           |
        +------------------+------------------+
        |                  |                  |
   engineering          research        presentation
        |                  |                  |
        +------------------+------------------+
                           |
                         patent

packs = installable views over these skills
```

The dependency direction is intentional:

- `core` may not depend on a work domain.
- domain skills may use `core` skills.
- one domain should not silently own another domain's reasoning.
- packs group skills; they do not contain workflow logic.

## Invocation model

Skills are classified by invocation behavior:

- **user-invoked workflow/router**: starts a substantial workflow and normally sets `policy.allow_implicit_invocation: false`.
- **model-invoked primitive**: reusable discipline that an agent may call when useful.
- **domain context**: specialized vocabulary, constraints, and review criteria that can be loaded alongside a workflow.

## Repository layout

```text
skills/
  core/
  engineering/
  research/
  presentation/
  patent/
  productivity/
  experimental/
packs/
docs/
scripts/
.github/workflows/
```

Each skill is self-contained:

```text
skills/<domain>/<skill-name>/
  SKILL.md
  agents/openai.yaml        # when Codex metadata is useful
  references/               # optional
  templates/                # optional
  scripts/                  # optional
```

A skill should not require fragile `../../../shared/...` references to function after individual installation.

## V1 scope

The first milestone establishes the monorepo architecture and migration contract. Existing private repositories are **not copied into this public repository in this bootstrap PR**.

Planned sources:

- `feiyushaw/academic_skills` -> `skills/research/`
- `feiyushaw/patent_skills` -> `skills/patent/`
- `feiyushaw/presentation_skill` -> `skills/presentation/`
- selected, adapted engineering/productivity patterns from `mattpocock/skills`

See [docs/migration.md](docs/migration.md) before moving any private source material.

## Core principles

1. A skill is a behavior primitive or a coherent domain workflow, not a giant prompt bundle.
2. Facts the agent can inspect should be investigated by the agent; user questions should focus on decisions.
3. Persist important state in explicit artifacts rather than relying on an indefinitely growing conversation.
4. Domain claims must remain traceable to evidence; writing layers may not silently change technical meaning.
5. Prefer progressive disclosure: keep universal rules in `SKILL.md`, move branch-specific detail into local references.
6. Keep every skill independently installable and testable.
7. Preserve upstream license and provenance when adapting third-party skills.

## Development

Validate the repository with:

```bash
python3 scripts/validate-skills.py
```

The same check runs in GitHub Actions.

## Third-party provenance

Adapted third-party material must be recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Matt Pocock's `skills` repository is MIT licensed; attribution is retained for adapted material.
