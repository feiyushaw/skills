---
name: workflow-router
description: Route a user's work request to the smallest suitable skill or skill sequence in this repository. Use when the user asks which workflow to use, invokes a general work request without a clear skill, or wants to discover available capabilities. Do not perform the full downstream workflow unless explicitly asked.
---

# Workflow Router

## Mission

Identify the current work product and stage, then select the smallest useful skill or short sequence. This is a router, not a super-agent.

## Routing process

1. Identify the primary work product: code, research artifact, presentation, patent artifact, productivity task, or repository-maintenance experiment.
2. Identify the current stage. Do not restart a lifecycle when the user is already downstream.
3. Prefer one primary skill. Add a short sequence only when the handoff is already clear.
4. State the expected artifact/output.
5. Do not route to `experimental` implicitly unless the user explicitly asks for an experimental/maintenance workflow.

## Common routes

```text
unclear engineering design
  → grill-with-docs

incoming issue / external PR
  → triage

architecture pain / refactor strategy
  → improve-codebase-architecture

settled feature context
  → to-spec → to-tickets → implement → code-review

large multi-session decision space
  → wayfinder

broad research landscape
  → literature-research

research idea / novelty
  → research-idea-refiner (+ literature-scout / research-critic)

experiment evidence
  → experiment-designer / engineering-research → result-harvester

paper structure / writing
  → paper-architect → academic-writer

reviewer comments
  → reviewer-response

presentation story
  → presentation-architect

Slidev deck
  → slidev-scientific-presentation

PowerPoint/PPTX deck
  → powerpoint-presentation

final deck audit
  → presentation-review

patent candidate mining
  → codebase-patent-diff → cn-patent-invention-mining

multiple patent candidates
  → patent-portfolio-planner

patent search / drafting / review
  → cn-patent-prior-art → cn-patent-drafting → cn-patent-review
```

## Constraints

- do not pretend an unavailable skill exists;
- do not launch several expensive workflows just because they may eventually be useful;
- domain-specific judgment stays in domain skills;
- when the user already names the correct skill, route directly to it;
- experimental skills require explicit opt-in.

## Completion

Stop when the user has a concrete next skill or short workflow and understands the expected output.
