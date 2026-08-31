# Skill Monorepo Architecture

## Goal

Provide one long-lived skill library organized by work category while avoiding duplicated workflow logic and monolithic super-agents.

## Layers

### 1. Core primitives

`skills/core/` contains behavior that is useful across multiple domains:

- decision clarification and grilling;
- context handoff;
- workflow discovery/routing;
- authoring rules for agent-consumed documents.

A core primitive must remain domain-independent.

### 2. Work domains

Domain folders own specialized reasoning and output contracts:

- `engineering`: software design and delivery;
- `research`: scientific reasoning and academic communication;
- `presentation`: presentation narrative and rendering workflows;
- `patent`: patent provenance, invention mining, search, drafting, review;
- `productivity`: general-purpose work utilities.

### 3. Packs

A pack is an installable view over existing skills. It may declare recommended skills and dependencies, but must not contain duplicate workflow instructions.

## Invocation axis

Every skill should be intentionally classified:

### User-invoked workflow/router

Use when starting the skill changes the shape of the session or launches a substantial workflow. Set:

```yaml
policy:
  allow_implicit_invocation: false
```

Examples: `workflow-router`, `to-spec`, `to-tickets`, `presentation-architect`.

### Model-invoked primitive

Reusable discipline that can be invoked by a user or another skill. No implicit-invocation prohibition is needed unless the behavior is expensive or disruptive.

Examples: `grilling`, `tdd`, `code-review`, `research-critic`.

### Domain context

Provides vocabulary, constraints, prior-art baselines, or domain-specific review criteria. It can be loaded alongside a workflow without becoming the workflow itself.

Example: `autonomous-driving-patent`.

## Persistent artifacts

Long workflows should persist decisions and evidence in artifacts rather than depending on conversation memory alone. Typical artifacts include:

- engineering: `CONTEXT.md`, ADRs, specs, tickets;
- research: research maps, idea canvases, claim-evidence maps, experiment plans;
- presentation: storyline, slide plan, asset manifest;
- patent: provenance matrix, invention candidate cards, prior-art matrix, claim versions.

## Dependency rules

1. Core cannot import domain reasoning.
2. Domains may invoke core primitives.
3. Cross-domain calls must be explicit and justified.
4. Packs cannot create hidden dependencies.
5. No skill should require repository-global relative reference files to execute after individual installation.

## Progressive disclosure

Keep execution-critical universal instructions in `SKILL.md`. Move detailed branch-specific material into local `references/`. A reference must be discoverable from the step that needs it.

## What this architecture intentionally avoids

- one super-skill that owns every workflow;
- duplicated `handoff`, `review`, or interview logic in every domain;
- installation that only works when the whole repository is copied;
- automatic invocation of expensive orchestrators;
- silent publication of content from private legacy repositories.
