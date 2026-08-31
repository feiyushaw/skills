---
name: engineering-research
description: Plan and audit engineering research from claims to reproducible evidence. Use for numerical methods, scientific computing, optimization/control, autonomous-driving planning/evaluation, and implementation-heavy AI research when the user needs experiment design, baseline selection, ablation planning, benchmark structure, failure analysis, or claim-evidence tracking. Do not use as the primary skill for broad literature reviews or final manuscript prose when a dedicated literature/writing skill is available.
---

# Engineering Research

Use this skill to turn a research idea into an auditable evidence package.

## Core rule

Do not equate any of the following:

- code implemented,
- code runs,
- benchmark runs,
- scientific claim supported.

A claim is supported only when the experiment design, baselines, metrics, and results are sufficient to test it.

## Default workflow

1. **State the research question.**
2. **Write falsifiable claims/hypotheses.** Avoid vague goals such as “improves performance.”
3. **Define the evidence needed for each claim.**
4. **Choose fair baselines and references.** Distinguish reproduction baselines, competitive baselines, and oracle/reference solutions.
5. **Build the experiment matrix.** Include datasets/benchmarks, scenarios, parameter regimes, seeds, hardware/runtime conditions, and metrics.
6. **Specify ablations.** Each ablation should answer one mechanism question.
7. **Specify failure/boundary tests.** Include cases where the method is expected to degrade.
8. **Define reproducibility requirements.** Record configs, versions, random seeds, checkpoints, raw outputs, and scripts.
9. **Run or inspect experiments.** Never invent missing results.
10. **Build a claim-evidence table.** Mark each claim as supported, partially supported, contradicted, or untested.
11. **Design figures/tables from claims.** Every major figure should have one main scientific message.
12. **Prepare an evidence package for writing/review.** Hand off prose drafting only after identifying unsupported claims and missing experiments.

## Required research artifacts

For a substantial project, maintain at least these four artifacts:

- `research-plan.md`
- `experiment-matrix.md`
- `claim-evidence-table.md`
- `benchmark-plan.md`

Use the templates in `templates/` when useful.

## Claim discipline

For each main claim, capture:

- **Claim ID** — C1, C2, ...
- **Statement** — precise and falsifiable.
- **Comparison** — what baseline/reference the claim is relative to.
- **Metric(s)** — measurable quantities.
- **Required evidence** — experiments needed before accepting the claim.
- **Observed evidence** — actual outputs only.
- **Status** — untested / partial / supported / contradicted.
- **Caveats** — regimes where the conclusion may not hold.

Read `references/claim-evidence.md` for detailed rules.

## Baseline rules

Prefer comparisons that isolate the proposed contribution.

Check:

- same train/evaluation data where applicable;
- same scene/benchmark split;
- same metric definitions;
- comparable compute and optimization budgets;
- comparable stopping criteria;
- equivalent access to privileged information;
- tuned baselines when the proposed method is tuned;
- reference/oracle solutions clearly distinguished from deployable baselines.

A weak or unfair baseline does not provide strong evidence.

## Ablation rules

Every ablation needs a question, not just a variant name.

Bad:
- “w/o module A”

Better:
- “Does module A improve robustness under interaction uncertainty, or only nominal closed-loop score?”

Use ablations to test mechanisms, not to inflate table size.

## Negative results and boundary conditions

Actively search for:

- numerical instability;
- sensitivity to initialization/hyperparameters;
- out-of-distribution parameter ranges;
- compute/memory scaling limits;
- failure under tighter constraints;
- closed-loop regressions hidden by open-loop metrics;
- accuracy gains that disappear after matching compute budgets.

Preserve negative results when they define the method's applicability.

## Domain routing

### Numerical methods / FEM / scientific computing

Emphasize:

- manufactured solutions or high-accuracy references when available;
- discretization error vs solver error;
- mesh/DOF scaling;
- convergence rates;
- conditioning and tolerance;
- wall-clock time and memory;
- accuracy-cost Pareto comparisons;
- repeated solves vs one-time preprocessing costs.

Do not claim higher-order convergence from a single mesh pair.

### Optimization and control

Emphasize:

- objective quality;
- feasibility/constraint violations;
- convergence/failure rate;
- runtime distribution, not only mean runtime;
- sensitivity to warm starts and initial conditions;
- equal function-evaluation or compute budgets;
- online vs offline cost separation.

### Autonomous-driving planning / closed-loop evaluation

Separate:

- open-loop imitation metrics;
- planner-only simulation;
- log replay;
- reactive-agent closed loop;
- fully interactive closed loop.

Track safety, progress, comfort, rule compliance, interaction quality, intervention/failure rate, and runtime. Do not treat better open-loop displacement error as proof of better closed-loop driving.

### ML/AI methods

Separate gains from:

- architecture;
- data scale;
- training compute;
- inference compute;
- search/planning budget;
- additional supervision or privileged labels.

Report multiple seeds when stochastic training materially affects conclusions.

## Figure contract

Before generating a major figure, write a short figure contract:

- **Claim/message:** what should a reader learn?
- **Evidence:** which runs/data support it?
- **Visual form:** line/bar/scatter/field/diagram/etc.
- **Axes/units:** explicit and comparable.
- **Uncertainty:** CI/std/quantiles where appropriate.
- **Reference/baseline:** clearly visible.
- **Output:** prefer vector master for publication figures.

For quantitative publication plots, hand off to a dedicated scientific-figure skill when available. For method/workflow diagrams, follow `references/figure-design.md`.

## Handoff to literature and writing skills

Use a dedicated systematic-literature skill when the task is primarily prior-art coverage, novelty assurance, PRISMA, or evidence-map construction.

Use a dedicated academic-writing/review skill for final manuscript prose, citation checks, reviewer simulation, and rebuttal.

Before handoff, provide:

- final claim list;
- claim-evidence table;
- experiment matrix;
- unresolved gaps;
- selected figures/tables;
- known limitations and negative results.

## Stop conditions

Do not declare the research complete if any central claim is still `untested` or only supported by an experiment that does not isolate the claimed effect.

If results are missing, identify exactly which experiment would resolve the gap instead of filling it with speculative prose.
