---
name: skill-audit
description: Audit this or another skill repository for overlap, routing ambiguity, broken references, oversized skills, missing review gates, weak invocation policies, and pack/installability problems. Experimental repository-maintenance skill.
---

# Skill Audit

## Mission

Keep a skill collection coherent as it grows. Prefer deleting, merging, or sharpening skills over increasing the count without a clear behavioral boundary.

## Audit dimensions

### Boundary

- Does each skill own one clear behavior or domain workflow?
- Are two skills competing for the same trigger?
- Is an orchestrator silently duplicating primitive logic?

### Invocation

- Should the skill be user-invoked, model-invoked, or domain context?
- Could implicit invocation trigger an expensive workflow unexpectedly?
- Are descriptions discriminative enough for routing?

### Self-containment

- Do referenced `references/`, `templates/`, and `scripts/` exist locally?
- Does individual installation break cross-directory assumptions?

### Progressive disclosure

- Is `SKILL.md` carrying branch-specific detail that belongs in references?
- Are important completion criteria buried too deeply?

### Workflow topology

- Is there a clear handoff into and out of the skill?
- Are review/verification gates missing?
- Does the catalog/packs/router reflect reality?

### Repository distribution

- unique skill names;
- valid pack references;
- installer behavior;
- provenance/license records;
- regression fixtures for high-risk workflows.

## Output

Produce:

1. duplicate/overlap candidates;
2. routing ambiguities;
3. broken/self-containment risks;
4. skills that should split or deepen;
5. missing workflow gates;
6. prioritized maintenance actions.

Classify actions as `merge`, `split`, `rename`, `rewrite`, `move`, `add test`, `add reference`, `add metadata`, or `no change`.
