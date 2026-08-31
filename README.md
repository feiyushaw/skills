# Feiyu Skills

Composable skills for Codex, Claude Code, and other coding/research agents.

This repository is the canonical home for reusable workflows across software engineering, research, presentations, patents, and productivity. Domain skills own domain reasoning; reusable interaction disciplines live in `core`; packs provide installation views.

> 中文说明: [README.zh-CN.md](README.zh-CN.md)

## Work domains

| Domain | Purpose | V1 status |
|---|---|---|
| `core` | Shared primitives: routing, grilling, handoff, agent-document discipline | stable |
| `engineering` | Spec, tickets, architecture, implementation, TDD, debugging, review, long-work planning | stable core set |
| `research` | Literature, idea refinement, experiments, evidence, figures, paper architecture/writing/review | migrated |
| `presentation` | Tool-independent presentation architecture + Slidev scientific renderer | migrated / expanding |
| `patent` | Provenance-aware Chinese invention mining, prior art, drafting, review | migrated |
| `productivity` | GrillMe, teaching workspace, questionnaires, re-pitching, handoff | stable core set |
| `experimental` | Unstable skills under evaluation | reserved |

## Current stack

```text
core
├── workflow-router
├── grilling
├── handoff
└── writing-for-agents

engineering
├── domain-modeling       ├── codebase-design
├── to-spec               ├── to-tickets
├── prototype             ├── implement
├── tdd                   ├── diagnosing-bugs
├── code-review           ├── resolving-merge-conflicts
└── wayfinder

research
├── literature-research   ├── literature-scout
├── research-idea-refiner ├── research-critic
├── experiment-designer   ├── engineering-research
├── result-harvester      ├── scientific-figure / method-figure / result-figure
├── paper-architect       ├── academic-writer
├── faithful-paper-translation / chinese-to-academic-english
└── manuscript-review

presentation
├── presentation-architect
└── slidev-scientific-presentation

patent
codebase-patent-diff → cn-patent-invention-mining → cn-patent-prior-art
→ cn-patent-drafting → cn-patent-review
+ autonomous-driving-patent domain guidance

productivity
├── grill-me
├── teach
├── to-questionnaire
└── wait-what
```

## Design principles

1. **Small, composable behavior.** Avoid one giant agent workflow that owns every task.
2. **Facts are agent work; decisions are human work.** Inspect files/tools/sources instead of asking users for facts the agent can obtain.
3. **Persist important state.** Specs, tickets, CONTEXT.md, ADRs, research maps, claim-evidence tables, patent candidate IDs, and handoffs survive context windows.
4. **Keep domain reasoning in domain skills.** Engineering discipline does not rewrite research methodology; writing does not silently change scientific claims.
5. **Progressive disclosure.** Universal behavior stays in `SKILL.md`; branch-specific guidance belongs in local `references/`, `templates/`, or `scripts/`.
6. **Self-contained installation.** A skill should work when installed individually; avoid fragile cross-directory file references.
7. **Explicit invocation policy.** Large orchestrators normally disable implicit invocation; reusable disciplines can be model-invoked.
8. **Preserve provenance.** Migrated and third-party-derived material records its source and license.

## Packs

`packs/` groups existing skills by job type:

- `engineering.yaml`
- `research.yaml`
- `presentation.yaml`
- `patent.yaml`
- `productivity.yaml`
- `full.yaml`

Packs do not contain workflow logic.

## Repository layout

```text
skills/<domain>/<skill-name>/
  SKILL.md
  agents/openai.yaml      # optional Codex invocation metadata
  references/             # optional, local to this skill
  templates/              # optional
  scripts/                # optional

packs/
docs/
scripts/
.github/workflows/
```

## Source migrations

The initial domain stack was consolidated from:

- `feiyushaw/academic_skills` → `skills/research/`
- `feiyushaw/patent_skills` → `skills/patent/`
- `feiyushaw/presentation_skill` → `skills/presentation/`
- selected/adapted workflows from `mattpocock/skills` → `core`, `engineering`, and `productivity`

See [docs/provenance.md](docs/provenance.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Development

```bash
python3 scripts/validate-skills.py
```

The same structural check runs in GitHub Actions.

## Next extensions

High-value follow-ups are a true PowerPoint/PPTX renderer, presentation review skill, pack installer/catalog generation, and workflow regression tests. The old source repositories remain historical sources until the monorepo has been used long enough to retire them safely.
