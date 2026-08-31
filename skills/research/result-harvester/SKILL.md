---
name: result-harvester
description: Collect experiment outputs, configs, seeds, metrics, runtime metadata, failures, and artifact provenance into a normalized evidence package. Use after experiments or when consolidating benchmark folders; do not invent missing results or silently drop failed runs.
---

# Result Harvester

## Mission

Turn scattered experiment folders into a traceable evidence package that can be audited, plotted, and connected to claims. Own result consolidation, not scientific interpretation.

## Canonical package

```text
research_evidence/
├── manifest.json
├── runs.csv
├── metrics_long.csv
├── failures.csv
├── provenance.csv
├── aggregation.md
└── notes.md
```

## Rules

1. Never fabricate a missing metric, seed, config, runtime, or failure reason.
2. Preserve source path/provenance for every harvested value.
3. Distinguish `missing`, `not applicable`, `failed`, and numeric zero.
4. Keep raw per-run records; aggregate only as a derived layer.
5. Do not silently drop failed/incomplete runs.
6. Treat run identity as configuration + code/data version + seed, not folder name alone.

## Workflow

Inventory result roots and trusted sources; normalize run identity; collect comparison metadata and raw metrics; record failures explicitly; compare observed runs against the `engineering-research` experiment matrix; only then aggregate with declared grouping/statistics/failure handling.

Use `scripts/inventory_results.py` and `templates/evidence-manifest.example.json` when useful.

## Domain metadata

For FEM/scientific computing include mesh/DOF, order/quadrature, solver tolerance/iterations, timing/memory, reference solution and error norms. For autonomous driving include split/scenario IDs, evaluation mode, horizon/frequency/latency, simulator/agent versions and safety/progress/comfort metrics. For optimization/control include objective, feasibility, evaluations, wall-clock, initialization and seed. For ML/AI include data/checkpoint/version, seed, training compute where relevant and test-time search budget.

## Handoff

- Completeness/fairness findings and normalized evidence → `engineering-research`.
- Quantitative data ready for visualization → `result-figure`.
- Paper summaries only after claim-evidence audit → `paper-architect` / `academic-writer`.
