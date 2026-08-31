# Scientific Figure Design Guide

## Figure-first thinking

A major figure should answer one scientific question. Start from the claim, not from the available plotting API.

## Quantitative figures

Prefer reproducible scripts and source data. Typical forms:

- convergence curves;
- error vs compute / accuracy-cost Pareto;
- runtime and memory scaling;
- robustness curves;
- ablation bars/lines;
- field or spatial error maps;
- trajectory/planning metric distributions;
- failure-rate summaries.

Always preserve units, sample counts, uncertainty definitions, and baseline/reference meaning.

## Method and architecture figures

Use editable vector sources when practical (`SVG`, `drawio`, or equivalent). Keep:

- left-to-right or top-to-bottom information flow;
- consistent module shapes;
- concise labels;
- clear distinction between offline and online stages;
- explicit feedback loops;
- legends only when visual encodings are not self-evident.

Avoid decorative 3D elements that do not carry information.

## Figure contract template

Before implementation, define:

```text
Figure ID:
Scientific message:
Claim IDs:
Source experiments/data:
Panels:
Baselines/reference:
Axes and units:
Uncertainty:
Required annotations:
Editable master format:
Publication export:
```

## Multi-panel figures

Each panel should have a role. A common engineering pattern is:

- (a) problem/setup;
- (b) method or qualitative result;
- (c) quantitative accuracy;
- (d) efficiency/scaling;
- (e) failure or robustness view.

Do not create panels merely to fill space.

## Visual integrity

- use identical axis ranges when direct visual comparison is intended;
- avoid truncated axes that exaggerate differences unless explicitly justified;
- show reference/oracle consistently;
- do not hide failed runs;
- do not use interpolation that visually implies unmeasured accuracy;
- verify every plotted point against its source.
