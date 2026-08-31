---
name: presentation-architect
description: Design the storyline, slide sequence, evidence placement, visual roles, and delivery structure of a scientific, technical, or business presentation before choosing Slidev, PowerPoint, or another renderer.
disable-model-invocation: true
---

# Presentation Architect

## Mission

Turn source material and a presentation goal into a coherent slide-level argument before implementation in any presentation technology.

This skill owns **presentation structure**, not rendering.

```text
audience + goal + source material
        ↓
one-sentence takeaway
        ↓
storyline
        ↓
slide sequence
        ↓
claim/evidence/visual contract per slide
        ↓
renderer choice
```

## 1. Establish the presentation contract

Determine from available context:

- audience and their expected background;
- presentation purpose: inform, review, decide, teach, defend, or persuade;
- time budget if known;
- source of truth: paper, codebase, experiment results, project review, proposal, etc.;
- one sentence the audience should remember afterward.

Ask the user only for decisions that materially change the deck and cannot be inferred from supplied context.

## 2. Build the storyline

Do not mirror a source document section-by-section. Presentation structure should follow the audience's understanding path.

For scientific/technical work, a useful default is:

```text
problem
→ why it matters
→ current limitation
→ key insight
→ proposed mechanism/formulation
→ evidence
→ limitations/tradeoffs
→ takeaway
```

For internal/business reviews, a useful default is:

```text
context
→ current state
→ key findings
→ implications
→ options/decision
→ next actions
```

Use only the structure needed by the actual goal.

## 3. One slide, one job

For every slide define:

```text
Slide ID:
Question answered:
Title / claim:
Evidence or content:
Primary visual:
What the speaker says that is not on the slide:
Transition to next slide:
```

If a slide has multiple unrelated jobs, split it. If two slides answer the same question, merge or differentiate them.

## 4. Choose representation intentionally

Prefer:

- conceptual diagram for architecture/mechanism;
- equation for a precise relationship;
- quantitative figure for evidence/trend;
- table for exact structured comparison;
- animation/video for temporal behavior;
- short text for framing/interpretation.

Do not add visuals as decoration. Every visual should answer a reader/audience question.

## 5. Evidence discipline

Never invent experimental results, citations, project status, dates, or implementation claims. For result slides, state what evidence supports the title. If evidence is missing, mark the slide as requiring evidence rather than writing a stronger title.

## 6. Renderer selection

After the architecture is stable:

- mathematical/scientific, version-controlled, dynamic presentation → `slidev-scientific-presentation`;
- editable corporate `.pptx` → a PowerPoint/PPTX renderer skill when installed;
- conceptual scientific figure needed → `scientific-figure` from the research pack;
- quantitative result figure needed → `result-figure` from the research pack.

Do not let renderer constraints determine the scientific or business story too early.

## Required output

For substantial work, produce:

1. presentation contract;
2. storyline in 5–10 beats;
3. slide map;
4. figure/evidence requirements;
5. backup-slide candidates;
6. recommended renderer and rationale.

## Completion criterion

The architecture is ready when each slide has one purpose, every central claim has support, the sequence has a clear dependency/order, and the deck can be implemented without inventing missing content.
