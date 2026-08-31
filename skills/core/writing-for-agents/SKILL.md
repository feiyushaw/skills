---
name: writing-for-agents
description: Design and revise SKILL.md, AGENTS.md, CLAUDE.md, and other agent-consumed instructions for reliable routing and execution. Use when authoring agent documentation, reducing instruction sprawl, improving progressive disclosure, or defining completion criteria.
---

# Writing for Agents

## Mission

Make agent-consumed documentation easy to invoke correctly, cheap to load, and reliable to execute.

This skill is influenced by the agent-document engineering principles in `mattpocock/skills`; see `THIRD_PARTY_NOTICES.md`.

## Principles

### Route with explicit context pointers

Descriptions and top-level instructions should tell the agent what material exists, when it applies, and where to continue.

### Use progressive disclosure

Keep universal execution rules close to the workflow. Move branch-specific tables, examples, and long references behind explicit local pointers.

### Co-locate a concept

Keep a concept's definition, rules, caveats, and completion criteria together instead of scattering them across unrelated files.

### Control context load

Do not make every agent load every rule. Prefer local, task-relevant instructions over repository-wide prose.

### Define completion

Each substantial step needs an observable completion condition. `Review carefully` is weaker than naming the checks or artifact that indicate completion.

### Prefer standard leading terms

Use established terms that already encode useful behavior, such as `red-green-refactor`, `tracer bullet`, `frontier`, `claim-evidence map`, or `provenance matrix`, when those terms accurately match the workflow.

### Prune stale instructions

Configuration, scripts, tests, and current repository structure are often better sources of truth than prose copies. Remove duplicated facts that can drift.

## Review checklist

When reviewing agent documentation, check:

- invocation description;
- behavior boundaries;
- information placement;
- context cost;
- hidden cross-file dependencies;
- contradictory rules;
- stale environment facts;
- completion criteria;
- provenance and license obligations.
