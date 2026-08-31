---
name: scientific-figure
description: Design conceptual scientific figures that explain a paper's method, mechanism, formulation, architecture, workflow, or central insight. Use when the paper needs a visual explanation rather than a quantitative result plot.
---

# Scientific Figure

## Mission

Design figures that make the reader **understand the scientific idea**.

This skill owns conceptual/method figures such as Figure 1, mechanism diagrams, workflow/architecture figures, formulation comparisons, training-vs-inference diagrams, algorithm schematics, and graphical abstracts. Quantitative evidence plots belong to `result-figure`.

## First principle

Do not start with boxes and arrows. Start with the sentence:

> After seeing this figure, the reader should understand that ______.

If that sentence is unclear, the figure is not ready to design.

## Canonical workflow

```text
Contribution / Insight
        ↓
Scientific message
        ↓
Reader question
        ↓
Visual argument
        ↓
Panel structure
        ↓
Objects / relations / annotations
        ↓
Editable master
        ↓
Caption + paper placement
```

## Figure contract

For every major conceptual figure define:

- figure ID / working title;
- scientific message;
- contribution / claim served;
- reader question answered;
- first section where introduced;
- reading order;
- panels and purpose of each panel;
- semantic objects;
- relationships / arrows / feedback;
- equations or symbols that truly help;
- what must remain editable;
- caption logic.

## Common figure grammars

- **Problem → limitation → proposed idea** comparison.
- **Pipeline** for sequential transformation.
- **Closed loop** for feedback/control/interaction.
- **Offline ↔ online** or **training ↔ inference** split.
- **Baseline vs proposed mechanism** side-by-side comparison.
- **Hierarchy** for system/subsystem relationships.
- **Optimization loop** for propose → evaluate → update.
- **Mechanism chain** for cause → operation → effect.
- **Conceptual landscape** when positioning formulations/paradigms.

## Panel discipline

Each panel should have one job. A useful multi-panel conceptual figure often follows:

```text
(a) Problem / limitation
(b) Key insight
(c) Proposed mechanism / system
(d) Optional detailed operation or consequence
```

Do not split panels merely to fill a page.

## Scientific semantics

Use visual encoding consistently:

- learned/trainable vs fixed components must be explicitly labeled;
- data flow, control flow, supervision, and feedback should be distinguishable;
- optional paths should not look mandatory;
- repeated operations should visibly form a loop;
- essential meaning must not depend only on color;
- equations should expose an interface or novelty, not decorate the figure.

## Figure-to-paper callbacks

A central figure may recur at increasing depth:

```text
Introduction → state the insight
Figure → show the visual argument
Method overview → walk through the figure
Method detail → formalize selected parts
Experiments → test the mechanism shown
Discussion → interpret the broader meaning
```

## Output preference

Prefer editable sources when practical:

- SVG;
- Draw.io;
- PPTX;

Raster PNG/JPEG should normally be a preview/export, not the only master.

## Handoff

- Need paper role / section placement → `paper-architect`.
- Need quantitative experimental evidence plot → `result-figure`.
- Need novelty/claim refinement → `research-idea-refiner`.

## Quality audit

Before accepting a figure ask:

- Can a reader state the main message in one sentence?
- Does every block/panel support that message?
- Is the proposed novelty visually distinguishable from the baseline?
- Are arrows semantically meaningful?
- Could the figure be simplified without losing the argument?
- Is the figure consistent with the paper terminology and equations?
- Does the caption explain semantics rather than repeat labels?
