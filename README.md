# Feiyu Skills

A composable personal skill monorepo for Codex, Claude Code, and other coding/research agents.

The repository is organized by real work domains. Cross-domain interaction/context primitives live in `core`; `packs` define installable groups; `experimental` is opt-in until repeated use justifies promotion.

> 中文说明: [README.zh-CN.md](README.zh-CN.md)

## Domains

| Domain | Purpose | Status |
|---|---|---|
| `core` | routing, grilling, handoff, agent-document discipline | stable |
| `engineering` | triage, specs, tickets, architecture, implementation, TDD, debugging, review, long-work planning | stable V2 |
| `research` | literature, idea refinement, experiments, evidence, figures, paper architecture/writing/review/response | stable V2 |
| `presentation` | presentation architecture, Slidev, PPTX, final review | closed-loop core |
| `patent` | CN invention provenance, mining, portfolio planning, prior art, drafting, review | stable V2 |
| `productivity` | GrillMe, teaching, questionnaires, re-pitching | stable |
| `experimental` | session retro and skill-repository audit | opt-in |

The V2 catalog contains **51 skills**. The `full` pack installs the 49 stable skills and intentionally excludes `experimental`.

## Main workflows

### Engineering

```text
triage incoming work
or
grill-with-docs → domain-modeling → to-spec → to-tickets
                                      ↓
                                  implement
                           prototype / tdd / diagnose
                                      ↓
                                  code-review
```

Use `improve-codebase-architecture` for systematic architecture deepening and `wayfinder` for multi-session work whose route is still being discovered.

### Research

```text
Understand → Innovate → Prove → Communicate → Review → Respond
```

The workflow preserves the central chain:

```text
Contribution → Claim → Required Evidence → Experiment / Analysis
→ Figure / Table → Paper Section
```

`reviewer-response` closes the post-review loop and routes substantive requests back to literature, experiments, paper architecture, or writing.

### Presentation

```text
presentation-architect
  → slidev-scientific-presentation OR powerpoint-presentation
  → presentation-review
```

Presentation reasoning is separated from rendering technology and from final quality review.

### Patent

```text
codebase-patent-diff
  → cn-patent-invention-mining
  → patent-portfolio-planner (when multiple candidates exist)
  → cn-patent-prior-art
  → cn-patent-drafting
  → cn-patent-review
```

## Discover, validate, install

```bash
python3 scripts/list-skills.py
python3 scripts/validate-skills.py
python3 scripts/install-pack.py engineering --target /path/to/agent/skills --dry-run
python3 scripts/install-pack.py full --target /path/to/agent/skills
```

The installer deliberately requires an explicit destination instead of hard-coding product-specific paths that may change. See [docs/using-skills.md](docs/using-skills.md).

## Repository rules

- Skills are `skills/<domain>/<name>/SKILL.md` and names are globally unique.
- Skills should remain individually installable and self-contained.
- Large orchestrators should normally disable implicit invocation.
- Packs group skills but do not own workflow logic.
- Experimental skills are not part of `full`.
- Third-party provenance and licenses are preserved.

See [docs/catalog.md](docs/catalog.md), [docs/architecture.md](docs/architecture.md), and [docs/provenance.md](docs/provenance.md).
