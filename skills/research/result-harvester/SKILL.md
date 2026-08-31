---
name: result-harvester
description: Collect experiment outputs, configs, seeds, metrics, runtime metadata, and artifact provenance into a normalized evidence package for engineering and AI research. Use after experiments or when consolidating benchmark folders; do not invent missing results.
---

# Result Harvester

## Mission

Turn scattered experiment folders into a traceable evidence package that can be audited, plotted, and connected to paper claims.

This skill owns **result consolidation**, not scientific interpretation by itself.

Use it when:

- multiple experiment runs live in nested directories;
- metrics are spread across JSON/CSV/text logs;
- configs/checkpoints/seeds need to be matched to results;
- the user wants a benchmark summary or evidence table;
- reproducibility metadata needs to be audited;
- figures should be generated only from normalized source data.

## Non-negotiable rules

1. Never fabricate a missing metric, seed, config, runtime, or failure reason.
2. Preserve the original source path for every harvested value.
3. Distinguish `missing`, `not applicable`, `failed`, and numeric zero.
4. Keep raw per-run records; aggregate only as a derived layer.
5. Do not silently drop failed or incomplete runs.
6. Record units and metric direction whenever known.
7. Treat experiment identity as configuration + code/data version + seed, not folder name alone.

## Canonical evidence package

Prefer this project-local layout:

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

### `runs.csv`

One row per run. Recommended fields:

- `run_id`
- `method`
- `benchmark`
- `scenario`
- `seed`
- `status`
- `config_path`
- `result_path`
- `checkpoint`
- `git_commit`
- `data_version`
- `device`
- `start_time`
- `runtime_s`
- `notes`

### `metrics_long.csv`

One row per metric observation:

- `run_id`
- `metric`
- `value`
- `unit`
- `direction` (`higher` / `lower` / `target`)
- `split`
- `step` or `epoch`, if relevant
- `source_path`

Long format is preferred because it is easier to audit and plot.

## Workflow

### 1. Inventory

Identify:

- experiment roots;
- run naming conventions;
- config formats;
- metric/log formats;
- code version information;
- dataset/version identifiers;
- checkpoint linkage.

Before harvesting, state which file patterns are trusted as sources of truth.

### 2. Normalize run identity

Create a stable `run_id`. Prefer an explicit run identifier if available; otherwise derive one from method + benchmark/scenario + seed + config identity.

Detect duplicate or conflicting identities and report them instead of overwriting.

### 3. Collect metadata

Capture the dimensions needed for fair comparison:

- method/variant;
- benchmark/case/scenario;
- seed;
- hyperparameters relevant to the claim;
- compute budget;
- model/checkpoint;
- code revision;
- data revision;
- runtime/device when relevant.

### 4. Collect metrics

Preserve raw observations. If the source contains time series or per-case metrics, do not replace them with only a mean.

For every metric, track the source file and unit when possible.

### 5. Capture failures explicitly

A failed run is evidence. Record:

- failure class;
- last valid stage;
- error/log path;
- whether retry occurred;
- whether the failure is method-specific or infrastructure-related, if known.

### 6. Audit completeness

Check expected experiment cells against observed runs. Use the experiment matrix from `engineering-research` when present.

Report:

- missing seeds;
- missing baselines;
- unmatched configs;
- missing code/data versions;
- unequal evaluation budgets;
- metric schema mismatches;
- duplicate runs;
- failed runs.

### 7. Aggregate only after audit

If aggregation is requested, declare:

- grouping keys;
- statistic (mean/median/etc.);
- uncertainty (std/SEM/CI/quantiles);
- treatment of failed/missing runs;
- outlier policy.

Keep the raw tables alongside aggregates.

### 8. Handoff

- To `engineering-research`: provide completeness/fairness findings and the evidence package.
- To `academic-figure-skill`: provide normalized data tables and metric semantics.
- To `method-figure`: only pass architecture/method metadata, not quantitative plots.
- To `academic-research-suite`: provide evidence-backed summaries, never prose unsupported by the harvested records.

## Domain checks

### FEM / numerical methods

Harvest mesh/DOF, element/order, quadrature, nonlinear/linear solver tolerances, iterations, assembly/solve/post-process times, memory when available, reference-solution identity, and error norms. Distinguish one-time preprocessing from repeated solve cost.

### Autonomous driving

Harvest dataset/split, scenario IDs, open-loop vs log-replay vs reactive vs interactive closed-loop mode, horizon, planner frequency, latency distribution, collision/off-road/progress/comfort/interaction metrics, and simulator/agent version.

### Optimization / control

Harvest objective, feasibility, constraint violation, function evaluations, iterations, wall-clock, success/failure, initialization, and random seed. Fair comparisons should retain compute/evaluation budgets.

### ML / AI

Harvest training data/version, checkpoint, seed, training compute when relevant, inference budget, test-time search/sampling budget, and all evaluation splits. Preserve per-seed/per-dataset results.

## Completion criterion

The harvest is complete only when another researcher can trace each reported result back to a concrete run and source artifact, and the missing/failed portions of the experiment matrix are visible rather than hidden.
