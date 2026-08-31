# Claim–Evidence Rules

## Purpose

Use a claim–evidence table to prevent manuscript claims from drifting beyond what experiments actually establish.

## Claim classes

- **Performance claim** — method improves a measurable metric.
- **Efficiency claim** — method reduces runtime, memory, samples, or evaluations.
- **Robustness claim** — method retains performance under perturbation or uncertainty.
- **Mechanism claim** — a component or design choice causes a specific behavior.
- **Generality claim** — result holds across datasets, regimes, tasks, or parameter ranges.
- **Practicality claim** — method meets deployment/online constraints.

## Evidence strength

### Strong

- direct experiment tests the exact claim;
- fair baseline/reference;
- enough regimes/seeds to support the stated scope;
- uncertainty or repeatability reported where needed;
- no material confounder.

### Partial

- evidence is directionally supportive but scope is narrower;
- only one benchmark/regime;
- compute budget mismatch remains;
- mechanism is inferred rather than isolated;
- stochastic variance is not fully characterized.

### Unsupported

- no direct experiment;
- only anecdotal visualization;
- comparison uses mismatched information/budget;
- claim generalizes beyond tested regimes.

### Contradicted

- evidence directly conflicts with the claim.

## Common claim inflation patterns

Avoid transforming:

- “better on two tested scenarios” → “generally superior”;
- “lower average runtime” → “real-time capable” without tail latency;
- “better open-loop metric” → “better closed-loop behavior”;
- “lower error on one mesh” → “higher convergence order”;
- “component removal hurts” → “component explains the mechanism” without a targeted test.

## Recommended status labels

`UNTESTED`, `PARTIAL`, `SUPPORTED`, `CONTRADICTED`.

Do not use `SUPPORTED` when a central confounder remains unresolved.
