---
name: engineering-research
description: Plan and audit engineering research from falsifiable claims to reproducible evidence. Owns experiment design, baselines, controls, ablations, benchmark matrices, failure tests, reproducibility, claim-evidence tracking, and evidence readiness for numerical/scientific-computing, optimization/control, autonomous-driving, and implementation-heavy AI research.
---

# Engineering Research

## Mission

Turn a stable research idea into an auditable evidence program.

Never equate:

```text
implemented → runs → benchmark completed → scientific claim supported
```

A claim is supported only when the design, baselines, metrics, controls, and observed results are sufficient to test it.

## Canonical chain

```text
Contribution
→ Claim
→ Research question / hypothesis
→ Alternative explanation
→ Baseline / control
→ Experiment matrix
→ Metric / observation
→ Decision rule
→ Observed evidence
→ Claim status
→ Figure / table
```

## Modes

### Research-plan mode

Build `research-plan.md`, `benchmark-plan.md`, and a claim-evidence map for the project.

### Experiment-design mode

For each central claim define hypothesis, alternative explanations, controls, baselines, independent variables, metrics, uncertainty/statistics, decision rules, and output figure/table. Use `references/experiment-design.md` and `templates/experiment-plan.md`.

### Evidence-audit mode

After runs exist, classify each claim as `untested`, `partial`, `supported`, or `contradicted`; expose missing seeds, unfair baselines, hidden compute/information differences, failed runs, and boundary conditions.

## Required artifacts

For substantial work maintain:

- `research-plan.md`;
- `experiment-matrix.md`;
- `claim-evidence-table.md`;
- `benchmark-plan.md`.

## Experimental discipline

- Every expensive experiment must test a claim, mechanism, boundary, or alternative explanation.
- Every ablation must answer one mechanism question.
- Match data, compute, information access, tuning budget, and stopping criteria where scientific fairness requires it.
- Pre-state what observations would support, weaken, contradict, or leave a claim unresolved.
- Preserve failed/null results and distinguish exploratory from confirmatory evidence.

## Domain emphasis

For FEM/scientific computing separate discretization error from solver error and report mesh/DOF scaling, tolerances, convergence, memory, and accuracy-cost trade-offs. For optimization/control match evaluation budgets and expose feasibility/failure. For autonomous driving distinguish open-loop/log-replay/reactive/interactive evaluation and closed-loop regressions. For ML/AI expose extra supervision, data, compute, and test-time search.

## Handoff

- Raw outputs need normalization/provenance → `result-harvester`.
- Conceptual/method visual → `method-figure`.
- Quantitative evidence visual → `result-figure`.
- Evidence changes the core contribution → back to `research-idea-refiner`.
- Evidence is mature and needs paper placement → `paper-architect`.
