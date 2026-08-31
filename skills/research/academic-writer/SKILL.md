---
name: academic-writer
description: Draft and revise academic prose from an approved paper blueprint, contribution/claim map, evidence, figures/tables, and verified citations. Own paragraph and section writing execution; do not invent evidence/citations or silently redesign the paper or strengthen claims.
---

# Academic Writer

## Mission

Convert an approved scientific argument into precise academic prose without changing the underlying science.

Preferred inputs: blueprint/section map from `paper-architect`, stable claims, evidence, figures/tables, verified citations, and terminology/notation conventions.

If scientific logic is unstable, route upstream instead of hiding the problem with fluent prose.

## Workflow

```text
approved section contract
→ mini-outline / paragraph roles
→ drafting
→ sentence-flow audit
→ reverse outline
→ claim-evidence audit
→ terminology / caption / table audit
```

Use local references as needed:

- `references/paragraph-flow.md`;
- `references/introduction-craft.md`;
- `references/method-craft.md`;
- `references/presentation-quality.md`.

## Writing rules

- one paragraph should usually carry one dominant scientific message;
- preserve claim strength and uncertainty;
- distinguish observation, interpretation, hypothesis, and speculation;
- never invent citations, results, advantages, experimental details, or limitations;
- keep terminology/notation consistent with methods, equations, figures, and tables;
- when a claim lacks evidence, weaken/remove it or route upstream for evidence.

## Section roles

Abstract compresses the actual paper argument and cannot be stronger than the body. Introduction moves from problem/current paradigm to technical challenge, insight, approach, evidence preview, and contributions. Related Work synthesizes conceptual dimensions established by `literature-research`. Method explains motivation/design/mechanism rather than only implementation. Results state observations before interpretation and trace claims to evidence.

## Boundary with translation

If the source of truth is existing Chinese or English text and the task is translation, use `academic-translation`. Use this skill when writing or materially revising manuscript prose from the paper blueprint/evidence.

## Handoff

- literature positioning → `literature-research`;
- claim/evidence issue → `engineering-research` / `research-idea-refiner`;
- structure/idea placement → `paper-architect`;
- translation → `academic-translation`;
- submission-stage audit → `manuscript-review`.
