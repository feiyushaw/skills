---
name: workflow-router
description: Route a user's work request to the smallest suitable skill or short skill sequence in this repository. Use when the task is general, the correct workflow is unclear, or the user wants capability discovery. Do not perform the full downstream workflow unless asked.
---

# Workflow Router

## Process

1. Identify the primary work product: code, research artifact, presentation, patent artifact, productivity task, or repository-maintenance experiment.
2. Identify the current lifecycle stage; do not restart upstream work unnecessarily.
3. Prefer one primary skill and add a short sequence only when the handoff is clear.
4. State the expected output.
5. Never route to `experimental` implicitly.

## Common routes

```text
unclear engineering design       → grill-with-docs
incoming issue / external PR     → triage
architecture pain                → improve-codebase-architecture
settled feature                  → to-spec → to-tickets → implement → code-review
multi-session unknown route      → wayfinder

broad literature / closest work  → literature-research
raw research idea                → research-idea-refiner
experiments / claim evidence     → engineering-research → result-harvester
conceptual paper figure          → method-figure
quantitative evidence figure     → result-figure
paper structure                  → paper-architect → academic-writer
academic EN↔ZH translation       → academic-translation
submission readiness             → manuscript-review
reviewer comments                → reviewer-response

presentation story               → presentation-architect
Slidev renderer                  → slidev-scientific-presentation
PowerPoint renderer              → powerpoint-presentation
final deck audit                 → presentation-review

patent source/provenance         → codebase-patent-diff → cn-patent-invention-mining
multiple patent candidates       → patent-portfolio-planner
prior art / drafting / review    → cn-patent-prior-art → cn-patent-drafting → cn-patent-review
```

## Constraints

Use only installed skills; do not launch several expensive workflows just because they may eventually be useful; domain judgment stays in domain skills; experimental skills require explicit opt-in.
