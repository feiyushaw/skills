---
name: result-figure
description: Design quantitative scientific figures that communicate experimental evidence, trends, uncertainty, trade-offs, ablations, robustness, scaling, and failure behavior. Use when data must support or challenge a paper claim visually; conceptual method diagrams belong to method-figure.
---

# Result Figure

## Mission

Design figures that let the reader evaluate a scientific claim from real data.

```text
Claim → scientific question → evidence needed
→ comparison structure → visual encoding → traceable figure
```

Do not start from available CSV columns and search for a decorative plot.

## Figure contract

Define claim/RQ, reader takeaway, comparison, variables/units, grouping/faceting, uncertainty/statistics, source run provenance, failure/edge cases, paper placement, and caption message.

## Plot choice by question

- ordered trend → line/point-range with uncertainty where needed;
- independent categories → dot/bar/point-range;
- distribution/variability → box/violin/ECDF/histogram/swarm as appropriate;
- relationship → scatter with justified fit/interval;
- sensitivity/robustness → controlled line/heatmap;
- trade-off → scatter/Pareto frontier;
- ablation → matched comparison isolating one mechanism;
- scaling → axes chosen from the scientific scaling question;
- spatial/field error → heatmap/contour when geometry matters;
- failure taxonomy → rate/composition plus representative cases when useful.

## Evidence discipline

- distinguish runs/seeds/samples from aggregates;
- state SD/SE/CI/quantiles explicitly;
- do not hide failed runs or crop regimes that weaken the claim;
- do not exaggerate effect size with misleading axes;
- keep every plotted value traceable to source runs when possible.

## Handoff

- Scattered outputs/configs need normalization → `result-harvester`.
- Experiment comparison is scientifically ill-posed → `engineering-research`.
- Need conceptual mechanism/architecture figure → `method-figure`.
- Need paper placement/caption role → `paper-architect`.
