# Feiyu Skills

A composable personal skill monorepo for Codex, Claude Code, and other coding/research agents.

The repository is organized by real work domains. Cross-domain primitives live in `core`; `packs` define installable groups; `experimental` remains opt-in.

> 中文说明: [README.zh-CN.md](README.zh-CN.md)

## Domains

| Domain | Purpose | Status |
|---|---|---|
| `core` | routing, grilling, handoff, agent-document discipline | stable |
| `engineering` | triage, design, specs, tickets, implementation, TDD, debugging, review, long-work planning | stable V2 |
| `research` | literature, idea refinement, evidence, figures, paper architecture/writing/translation/review/response | stable V2, consolidated |
| `presentation` | presentation architecture, Slidev, PPTX, final review | closed-loop core |
| `patent` | CN invention provenance, mining, portfolio planning, prior art, drafting, review | stable V2 |
| `productivity` | GrillMe, teaching, questionnaires, re-pitching | stable |
| `experimental` | session retro and skill-repository audit | opt-in |

The catalog now contains **46 skills**: 44 stable skills in `full` plus 2 experimental skills.

Each domain directory contains a `README.md` explaining its scope, lifecycle, skill selection, and common multi-skill workflows.

## Main workflows

### Engineering

```text
triage
or
grill-with-docs → domain-modeling → to-spec → to-tickets
                                      ↓
                                  implement
                           prototype / tdd / diagnose
                                      ↓
                                  code-review
```

### Research

```text
literature-research
→ research-idea-refiner
→ engineering-research
→ result-harvester
→ method-figure / result-figure
→ paper-architect
→ academic-writer / academic-translation
→ manuscript-review
→ reviewer-response
```

Research uses 11 top-level skills. Targeted novelty scouting, adversarial idea critique, experiment design, and the two translation directions are modes/references inside those primary lifecycle entry points rather than separate competing skills.

### Presentation

```text
presentation-architect
→ slidev-scientific-presentation OR powerpoint-presentation
→ presentation-review
```

### Patent

```text
codebase-patent-diff
→ cn-patent-invention-mining
→ patent-portfolio-planner (when needed)
→ cn-patent-prior-art
→ cn-patent-drafting
→ cn-patent-review
```

## Discover, validate, install

```bash
python3 scripts/list-skills.py
python3 scripts/validate-skills.py
python3 scripts/validate-regressions.py
python3 scripts/smoke-test-distribution.py
python3 scripts/install-pack.py full --target /path/to/agent/skills
```

See [docs/catalog.md](docs/catalog.md), [docs/using-skills.md](docs/using-skills.md), [docs/architecture.md](docs/architecture.md), and [docs/provenance.md](docs/provenance.md).
