---
name: method-figure
description: Design editable academic method, architecture, mechanism, workflow, and graphical-abstract figures for engineering and AI research. Prefer structured SVG or Draw.io sources over raster-only output; use this skill for conceptual/method figures, not quantitative experiment plots.
---

# Method Figure

## Mission

Turn a research method into a clear, editable visual argument. The output should explain the method, not decorate it.

Use this skill for:

- paper Figure 1 / method overview;
- algorithm architecture;
- closed-loop planning or control workflow;
- FEM / numerical method pipeline;
- optimization loop;
- mechanism / causal schematic;
- data flow and training/inference comparison;
- graphical abstract when the content is primarily structured rather than illustrative.

Do **not** use this skill for numerical curves, bar charts, box plots, convergence plots, heatmaps, or statistical figures. Route those to `academic-figure-skill`.

## Default output contract

For each requested figure, define a `figure contract` before drawing:

1. **Scientific claim** — one sentence the figure must communicate.
2. **Audience** — reviewer / domain expert / broad reader.
3. **Reading order** — left-to-right, top-to-bottom, or loop.
4. **Semantic blocks** — only blocks necessary to support the claim.
5. **Data/control arrows** — distinguish data, supervision, feedback, and optional paths.
6. **Editable master** — SVG or Draw.io whenever possible.
7. **Preview** — PNG/PDF only as a derivative artifact.
8. **Caption draft** — explain semantics, abbreviations, and panel relationships.

## Workflow

### 1. Extract the method graph

Map prose/code into:

```text
inputs → transformation → intermediate representation → decision/solver → output
                                ↑                         ↓
                           supervision              feedback/environment
```

Remove implementation details that do not support the paper claim.

### 2. Choose a figure grammar

Prefer one of:

- **Pipeline** — sequential processing.
- **Closed loop** — planning/control/environment interaction.
- **Two-stage** — offline/online, training/inference, coarse/fine.
- **Hierarchical** — system/subsystem decomposition.
- **Comparison** — baseline vs proposed method.
- **Mechanism** — state transition or causal explanation.
- **Optimization loop** — proposal → evaluation → update → convergence.

### 3. Preserve semantics visually

Use shape and grouping consistently:

- process/module: rounded rectangle;
- data/state: rectangle or document-like block;
- solver/optimizer: distinct labeled module, not a generic magic box;
- environment/plant: enclosing external block;
- repeated operation: explicit loop arrow;
- optional path: dashed line;
- learned component: mark as learned/trainable in text rather than relying only on color.

Do not encode essential meaning by color alone.

### 4. Use equations selectively

Include an equation only when it explains the interface or novelty, e.g.:

- `V_θ(s,a)` for an action-conditioned value network;
- `argmin_u J(u)` for an online optimizer;
- `Ku=f` for a FEM solve;
- a recovery/update equation for a numerical post-processor.

Avoid placing a full derivation inside the figure.

### 5. Produce editable source

Preferred order:

1. SVG for deterministic paper-ready diagrams;
2. Draw.io when interactive editing/layout is valuable;
3. PPTX only when the user explicitly prefers slides/editability there;
4. raster generation only for illustrative assets that cannot be represented structurally.

Text, arrows, boxes, and labels should remain editable.

### 6. QA

Check:

- the figure has one dominant message;
- labels match manuscript terminology exactly;
- arrow direction is unambiguous;
- training-only and inference-only paths are distinguishable;
- no hidden dependency is omitted;
- baseline/proposed comparison is fair and symmetric;
- the figure remains understandable in grayscale;
- the smallest text remains readable at target paper width;
- acronym definitions appear in caption or manuscript.

## Domain guidance

### Autonomous driving

Explicitly distinguish ego planner, learned model, other agents, simulator/environment, map/context, and feedback. If evaluation is closed-loop, show the feedback path; do not depict log replay as interactive simulation.

### FEM / scientific computing

Separate the expensive primal solve from post-processing/recovery. Show which quantities are available at nodes, quadrature/Gauss points, or reconstructed points when relevant. If the novelty claims no additional primal solve, make that visually explicit.

### Optimization / control

Show objective/cost evaluation and optimizer update separately. Distinguish model/dynamics rollout from optimizer logic. For stochastic search, show sampling/distribution update rather than implying gradient descent.

### ML/AI

Separate training and inference. Show additional supervision, teacher signals, online search, or external tools when they affect the method or fairness of comparison.

## Handoff

- If the figure requires measured numerical values, hand the quantitative panels to `academic-figure-skill` and compose them afterward.
- If the experiment evidence is incomplete, route back to `engineering-research` rather than inventing a clean story.
- If the figure reveals a novelty ambiguity, route the claim to literature/prior-art review before finalizing the caption.
