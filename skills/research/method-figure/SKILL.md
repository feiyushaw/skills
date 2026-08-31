---
name: method-figure
description: Design editable academic method, architecture, mechanism, workflow, and graphical-abstract figures for engineering and AI research. Prefer structured SVG or Draw.io sources over raster-only output; use this skill for conceptual/method figures, not quantitative experiment plots.
---

# Method Figure

## Mission

Turn a research method into a clear, editable visual argument. The output should explain the method, not decorate it.

Use this skill for paper Figure 1/method overviews, algorithm architecture, closed-loop workflows, FEM/numerical pipelines, optimization loops, mechanism schematics, training/inference comparisons, and structured graphical abstracts.

Do **not** use this skill for numerical curves, bar charts, box plots, convergence plots, heatmaps, or statistical figures. Route those to `result-figure`.

## Figure contract

Before drawing, define:

1. scientific claim/message;
2. audience;
3. reading order;
4. semantic blocks;
5. data/control/supervision/feedback arrows;
6. editable master format;
7. preview/export needs;
8. caption logic.

Use `templates/figure-contract.md` when useful.

## Workflow

### 1. Extract the method graph

```text
inputs → transformation → intermediate representation → decision/solver → output
                                ↑                         ↓
                           supervision              feedback/environment
```

Remove implementation details that do not support the paper claim.

### 2. Choose a figure grammar

Use pipeline, closed loop, two-stage, hierarchy, comparison, mechanism, or optimization-loop structure according to the scientific message.

### 3. Preserve semantics visually

Keep shapes/grouping consistent; mark learned/fixed and training/inference roles explicitly; show loops as loops; optional paths as optional; do not encode essential meaning by color alone.

### 4. Use equations selectively

Include equations only when they explain an interface, objective, constraint, state, or novelty. Avoid full derivations inside the figure.

### 5. Produce editable source

Prefer SVG, then Draw.io when interactive editing helps, then PPTX when explicitly desired. Raster output should normally be a derivative preview rather than the only master.

### 6. QA

Check one dominant message, manuscript terminology consistency, unambiguous arrows, visible training/inference distinctions, no hidden dependencies, fair baseline/proposed comparison, grayscale readability, and final-size text readability.

## Domain guidance

- **Autonomous driving:** distinguish ego planner, learned model, other agents, simulator/environment, map/context, and actual feedback. Do not depict log replay as interactive closed loop.
- **FEM/scientific computing:** separate expensive primal solve from recovery/post-processing and make data locations/extra solves explicit when relevant.
- **Optimization/control:** distinguish rollout/model from optimizer/update logic; stochastic search should show sampling/distribution updates rather than imply gradients.
- **ML/AI:** separate training and inference and expose extra supervision, teacher signals, search, or external tools when they affect the method.

## Handoff

- measured quantitative panels → `result-figure`;
- incomplete experiment evidence → `engineering-research` / `experiment-designer`;
- paper role/placement → `paper-architect`;
- novelty ambiguity → `literature-scout` / `research-idea-refiner`.
