---
name: grilling
description: Clarify a design or plan by resolving the current frontier of decisions in focused rounds. Use when important choices are unresolved and later choices depend on them. Investigate facts with available tools instead of asking the user to supply inspectable facts.
---

# Grilling

## Mission

Turn an ambiguous design space into an explicit decision tree and resolve it in dependency order.

This skill is adapted from the grilling/frontier pattern in `mattpocock/skills`; see `THIRD_PARTY_NOTICES.md`.

## Core concepts

- **decision tree**: unresolved choices and their dependencies;
- **frontier**: choices whose prerequisites are already settled;
- **round**: the current frontier presented together so the user can make coherent decisions.

## Workflow

1. Reconstruct the goal, known constraints, settled decisions, and unresolved choices.
2. Separate facts from decisions.
3. Investigate facts using files, tools, source code, documentation, or public sources whenever possible.
4. Build the decision tree and select the current frontier.
5. Ask only the frontier questions. Number them and include a concise recommendation when useful.
6. Incorporate the answers, recompute the frontier, and continue.
7. Persist important decisions in the domain's normal artifact when the parent workflow requires it.

## Rules

- Do not ask the user for facts the agent can reasonably establish itself.
- Do not ask dependent questions before their prerequisites are resolved.
- Do not silently choose a material product, research, architecture, presentation, or legal-strategy decision for the user.
- Do not keep interviewing after the decision frontier is empty.

## Completion

The grilling pass is complete when no material decision remains silently assumed and downstream work can start from shared, explicit constraints.
