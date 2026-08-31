---
name: result-harvester
description: Collect experiment outputs, configs, seeds, metrics, runtime metadata, and artifact provenance into a normalized evidence package for engineering and AI research. Use after experiments or when consolidating benchmark folders; do not invent missing results.
---

# Result Harvester

## Mission

Turn scattered experiment folders into a traceable evidence package that can be audited, plotted, and connected to paper claims. This skill owns result consolidation, not scientific interpretation by itself.

## Non-negotiable rules

1. Never fabricate a missing metric, seed, config, runtime, or failure reason.
2. Preserve the original source path for every harvested value.
3. Distinguish `missing`, `not applicable`, `failed`, and numeric zero.
4. Keep raw per-run records; aggregate only as a derived layer.
5. Do not silently drop failed or incomplete runs.
6. Record units and metric direction whenever known.
7. Treat experiment identity as configuration + code/data version + seed, not folder name alone.

## Canonical evidence package

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

Use `templates/evidence-manifest.example.json` when useful. `scripts/inventory_results.py` can conservatively inventory candidate experiment artifacts without inventing project-specific metric semantics.

## Workflow

### 1. Inventory

Identify experiment roots, run naming, config/metric/log formats, code/data versions, and checkpoint linkage. State which artifacts are trusted sources of truth.

### 2. Normalize run identity

Prefer an explicit run ID; otherwise derive one from method + benchmark/scenario + seed + config identity. Report duplicate/conflicting identities instead of overwriting them.

### 3. Collect comparison metadata

Capture method/variant, benchmark/scenario, seed, relevant hyperparameters, compute budget, checkpoint, code/data revision, runtime/device, and any other dimension needed for fair comparison.

### 4. Collect metrics

Preserve raw per-run/per-case/per-step observations. Track source file, unit, and metric direction when possible.

### 5. Capture failures explicitly

Record failure class, last valid stage, error/log path, retries, and whether infrastructure or method-specific attribution is known. Failed runs are evidence.

### 6. Audit completeness

Compare observed runs against the experiment matrix from `engineering-research` / `experiment-designer`. Report missing seeds/baselines, unmatched configs, version gaps, unequal budgets, schema mismatches, duplicates, and failed runs.

### 7. Aggregate only after audit

Declare grouping keys, statistic, uncertainty definition, handling of failed/missing runs, and outlier policy. Keep raw tables beside derived aggregates.

## Handoff

- `engineering-research`: completeness/fairness findings + normalized evidence package.
- `experiment-designer`: missing cells or controls requiring new experiments.
- `result-figure`: normalized quantitative data + metric semantics.
- `paper-architect` / `academic-writer`: evidence-backed summaries and traceability only after claim-evidence audit.
- `method-figure`: architecture/method metadata only, not quantitative plots.

## Domain checks

### FEM / numerical methods

Harvest mesh/DOF, element/order, quadrature, solver tolerances/iterations, assembly/solve/post-process time, memory, reference-solution identity, and error norms. Distinguish one-time preprocessing from repeated solve cost.

### Autonomous driving

Harvest dataset/split, scenario IDs, open-loop/log-replay/reactive/interactive mode, horizon, planner frequency, latency distribution, safety/progress/comfort/interaction metrics, and simulator/agent version.

### Optimization / control

Harvest objective, feasibility, constraint violations, function evaluations, iterations, wall-clock, success/failure, initialization, and random seed; retain fair compute/evaluation budgets.

### ML / AI

Harvest training data/version, checkpoint, seed, training compute where relevant, inference/test-time search budget, and all evaluation splits. Preserve per-seed/per-dataset results.

## Completion criterion

Another researcher must be able to trace every reported result to a concrete run/source artifact, while missing and failed portions remain visible rather than hidden.
