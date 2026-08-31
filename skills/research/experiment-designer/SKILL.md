---
name: experiment-designer
description: Convert research claims into falsifiable experiments, controls, baselines, ablations, metrics, and evidence plans. Use when the contribution is reasonably defined and the user needs to decide how to prove or falsify it.
---

# Experiment Designer

## Mission

Turn **Claim → Evidence requirement** into a concrete experimental program.

This skill answers **“How do we prove it?”**. It should not create experiments merely because they are conventional; every major experiment must test a claim, mechanism, boundary, or alternative explanation.

## Canonical chain

```text
Contribution
  ↓
Claim
  ↓
Research Question
  ↓
Hypothesis
  ↓
Alternative Explanation
  ↓
Baseline / Control
  ↓
Experiment
  ↓
Metric / Observation
  ↓
Decision Rule
  ↓
Figure / Table
```

## Workflow

1. **Collect claims.** Import claims from `contribution-map.md` or restate them precisely.
2. **Classify claims.** Effectiveness, mechanism, efficiency, robustness, generality, theory, or limitation.
3. **Create research questions.** Each RQ should correspond to a meaningful uncertainty.
4. **Specify hypotheses.** State what result would support and what result would weaken the claim.
5. **List alternative explanations.** More parameters, more data, tuning effort, extra compute, privileged information, preprocessing, regularization, etc.
6. **Choose baselines and controls.** Include the closest scientific baseline and controls needed to isolate the proposed mechanism.
7. **Design ablations.** Every ablation must answer one mechanism question.
8. **Choose metrics.** Define direction, units, aggregation, uncertainty, and statistical treatment when appropriate.
9. **Define boundary tests.** Include stress/failure regimes, not only nominal cases.
10. **Specify decision rules.** Pre-state what observations would support, partially support, contradict, or leave a claim unresolved.
11. **Plan evidence presentation.** Map each experiment to the most informative figure/table form.
12. **Audit completeness.** Ensure every central claim has evidence and every expensive experiment has a scientific purpose.

## Experiment card

For each major experiment, write:

```text
Experiment ID:
Research question:
Claim tested:
Hypothesis:
Alternative explanation(s):
Baseline/control:
Controlled variables:
Independent variable:
Dependent metric(s):
Protocol:
Expected supporting observation:
Falsifying / weakening observation:
Statistical / uncertainty treatment:
Output figure/table:
Interpretation limits:
```

## Ablation discipline

Bad ablation:

> Remove every module one by one because that is standard.

Better ablation:

> Claim: mechanism M is responsible for improvement under condition X.
> Compare full method against a capacity/compute-matched variant without M under X.
> Measure the metric directly tied to the claimed mechanism.

## Evidence hierarchy

Prefer evidence that isolates causality/mechanism over evidence that merely repeats the headline metric.

Typical sequence:

- **RQ1 Effectiveness** — does the method improve the target outcome?
- **RQ2 Mechanism** — is the claimed mechanism actually responsible?
- **RQ3 Robustness / generality** — when does it hold?
- **RQ4 Efficiency / trade-off** — what does it cost?
- **RQ5 Limitations** — where does it fail?

Use only the RQs needed by the actual contribution.

## Handoff

- If claims are vague or novelty is unstable → `research-idea-refiner`.
- If an experiment reveals a competing explanation → `research-critic`.
- If evidence needs visual presentation → `result-figure`.
- If experiment RQs need paper placement → `paper-architect`.

## Integrity rules

- Never invent results.
- Never choose a metric after seeing results solely because it favors the proposed method.
- Keep failed/null results visible.
- Match data, compute, information access, and tuning budgets where scientifically required.
- Distinguish exploratory experiments from confirmatory evidence.
