---
name: method-figure
description: Design editable conceptual scientific figures for a paper's method, mechanism, formulation, architecture, workflow, optimization loop, training/inference structure, or graphical abstract. Use for visual explanation; quantitative experimental evidence belongs to result-figure.
---

# Method Figure

## Mission

Design figures that make the reader understand the scientific idea. This is the single entry point for conceptual/method figures.

Before drawing, complete the sentence:

> After seeing this figure, the reader should understand that ______.

If that sentence is unclear, the figure is not ready.

## Figure contract

Define:

- scientific message and contribution served;
- reader question;
- paper placement;
- reading order and panel roles;
- semantic objects and relations;
- data/control/supervision/feedback arrows;
- equations/symbols that expose a real interface or novelty;
- editable master format;
- caption logic.

Use `templates/figure-contract.md` when useful.

## Common grammars

- problem → limitation → proposed idea;
- sequential pipeline;
- closed feedback/control loop;
- offline/online or training/inference split;
- baseline vs proposed mechanism;
- hierarchy/system decomposition;
- optimization/search loop;
- mechanism chain;
- conceptual formulation landscape.

## Semantic rules

- learned vs fixed, training vs inference, data flow vs control/feedback must be explicit when scientifically relevant;
- optional paths must not look mandatory;
- repeated operations should visibly form a loop;
- essential meaning must not depend only on color;
- do not hide extra supervision, search, privileged information, or extra solves.

## Domain guidance

- Autonomous driving: distinguish ego planner, learned model, other agents, simulator/environment, map/context, and actual feedback; do not depict log replay as interactive closed loop.
- FEM/scientific computing: separate expensive primal solve, recovery/post-processing, data locations, and any additional solves.
- Optimization/control: distinguish rollout/model from optimizer/update; stochastic search should show sampling/distribution updates rather than imply gradients.
- ML/AI: separate training and inference and expose teacher signals or external tools when they affect the method.

## Output

Prefer editable SVG, Draw.io, or PPTX masters; raster files should normally be derivative previews.

## Handoff

- Quantitative experimental panels → `result-figure`.
- Evidence is incomplete or scientifically ambiguous → `engineering-research`.
- Paper role/placement is unclear → `paper-architect`.
- Novelty is unclear → `literature-research` novelty-scout mode or `research-idea-refiner`.
