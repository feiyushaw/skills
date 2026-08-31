---
name: result-figure
description: Design quantitative scientific figures that communicate experimental evidence, trends, uncertainty, trade-offs, ablations, robustness, scaling, and failure behavior. Use when results must support a paper claim visually.
---

# Result Figure

## Mission

Design figures that make the reader **believe or evaluate a scientific claim from data**.

This skill owns quantitative result visualization. It decides what comparison matters, which visual encoding makes the claim testable, how uncertainty should be shown, and how the figure maps back to source evidence. Conceptual method diagrams belong to `scientific-figure`.

## First principle

Start from:

```text
Claim
  ↓
Scientific question
  ↓
Evidence needed
  ↓
Comparison structure
  ↓
Visual encoding
```

Do not start from “I have CSV columns; what plot can I make?”

## Figure contract

For each result figure define:

- claim / research question;
- reader takeaway;
- comparison being made;
- x/y variables and units;
- grouping/faceting variables;
- uncertainty/statistics;
- source data / run provenance;
- expected failure or edge cases;
- section where first introduced;
- caption message.

## Plot selection by scientific question

- **Trend / ordered progression** → line plot with uncertainty where appropriate.
- **Independent category comparison** → bar/dot/point-range; prefer point estimates + uncertainty when possible.
- **Distribution / variability** → box, violin, ECDF, histogram, swarm/strip depending sample structure.
- **Relationship / correlation** → scatter with justified fit/interval if needed.
- **Sensitivity / robustness** → line or heatmap across controlled factors.
- **Trade-off / Pareto behavior** → scatter/frontier plot.
- **Ablation** → comparison that isolates one mechanism, not a decorative collection of variants.
- **Scaling** → log/linear axes chosen from the scientific law/question, with units explicit.
- **Spatial/field error** → heatmap/contour only when geometry matters.
- **Failure taxonomy** → rate/composition plot plus representative cases when useful.

## Multi-panel logic

A strong result figure often builds an argument:

```text
(a) headline effect
(b) mechanism / ablation
(c) robustness / sensitivity
(d) efficiency / trade-off or failure boundary
```

Panels should share a central claim, not merely share a dataset.

## Statistical and uncertainty discipline

- Distinguish runs/seeds/samples from aggregated means.
- Show uncertainty when variability matters.
- State whether intervals are SD, SE, CI, quantiles, or another measure.
- Avoid significance stars without the underlying comparison definition.
- Do not hide failed runs or selectively crop regimes that weaken the conclusion.
- Do not use a truncated axis when it materially exaggerates effect size without clear justification.

## Claim-first examples

Claim: method remains robust as perturbation increases.

Better figure:

```text
x = perturbation strength
y = performance
series = methods
band = uncertainty
```

rather than several unrelated bar charts.

Claim: mechanism M causes the gain.

Better figure:

```text
full method vs matched control without M
under the regime where M should matter
```

rather than a generic component-removal table.

## Traceability

Every plotted number should map to a real source artifact when possible:

```text
Figure point
  → aggregated value
  → per-run records
  → config / seed / result path
```

Use `result-harvester` when experiment outputs need normalization first.

## Handoff

- Need experiment design / correct controls → `experiment-designer`.
- Need conceptual method figure → `scientific-figure`.
- Need paper placement and figure narrative → `paper-architect`.

## Quality audit

Ask:

- What exact claim does this figure support?
- Can the visual encoding answer that claim without reading the whole paper?
- Are baselines and conditions fair and clearly labeled?
- Is uncertainty visible and correctly defined?
- Is the effect size readable, not just significance?
- Are units, sample counts, and aggregation clear?
- Could one panel be removed without weakening the argument? If yes, consider removing it.
