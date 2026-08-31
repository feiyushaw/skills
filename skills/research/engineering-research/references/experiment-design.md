# Experiment Design Guide

## 1. Start from claims

Each experiment must test at least one explicit claim or boundary condition. Avoid experiments that exist only because they are conventional.

## 2. Build a matrix

Dimensions may include:

- benchmark / dataset / scenario;
- physical or operating regime;
- baseline / proposed variant;
- random seed;
- mesh size / resolution / horizon / sample count;
- compute budget;
- noise or uncertainty level;
- hardware/runtime backend.

Record which dimensions are controlled and which are varied.

## 3. Reproduction before innovation

When extending an existing method:

1. reproduce the reference implementation/checkpoint/result as closely as practical;
2. document mismatches;
3. freeze a reproducible baseline;
4. apply modifications one at a time where possible;
5. compare all variants under the same evaluation protocol.

## 4. Fair compute accounting

Separate:

- offline preprocessing/training;
- one-time setup;
- per-instance inference/solve time;
- amortized cost;
- accelerator-specific speedups.

For search/optimization methods, report equivalent evaluation/sample budgets where that is the fairest comparison.

## 5. Statistical reliability

Use repeated trials/seeds when randomness can change conclusions. Report uncertainty appropriate to the metric rather than only the best run.

Do not average away catastrophic failures; report failure rates separately.

## 6. Scaling experiments

If claiming scalability, vary the quantity that defines scale:

- DOF / mesh resolution;
- agent count;
- horizon length;
- state/action dimension;
- dataset size;
- model size;
- number of samples/function evaluations.

Measure both quality and resources.

## 7. Ablation design

Every ablation must state:

- mechanism question;
- changed component;
- controlled variables;
- expected observation if hypothesis is true;
- alternative explanation if result is negative.

## 8. Failure suite

Add intentionally difficult cases, not just nominal benchmarks. Capture raw failure examples and categorize them.

## 9. Result integrity

Never silently exclude failed runs. Any exclusion criterion should be stated before interpretation and recorded with the results.
