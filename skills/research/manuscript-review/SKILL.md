---
name: manuscript-review
description: Audit a near-complete academic manuscript for submission-stage rejection risks across contribution clarity, empirical strength, method soundness, claim-evidence alignment, writing, figures/tables, and reproducibility. Use after research, paper architecture, and prose are largely complete.
---

# Manuscript Review

## Mission

Act as a skeptical submission-stage reviewer and identify concrete reasons the current manuscript could be rejected or require major revision.

This is a late lifecycle gate. Early idea stress-testing belongs inside `research-idea-refiner`.

## Workflow

1. Reconstruct the thesis and claimed contributions from the manuscript alone.
2. Build a claim-evidence audit for Abstract and Introduction.
3. Audit Method soundness, assumptions, reproducibility, and design rationale.
4. Audit Experiments for fair baselines, controls, ablations, robustness, failure cases, uncertainty, and scope.
5. Audit figures/tables/captions and terminology/notation consistency.
6. Audit section/paragraph flow and paper architecture.
7. Classify fatal, major, and minor risks.
8. Produce a prioritized revision queue.

## Rejection dimensions

Evaluate contribution strength/clarity, comprehension, empirical strength, evaluation completeness, method soundness/net value, scope/generalization, and reproducibility.

For every major Abstract/Introduction claim record evidence location, evidence type, status (`supported`, `partial`, `unsupported`, `overstated`), and action.

## Handoff

- Novelty/positioning problem → `literature-research` + `research-idea-refiner`.
- Missing/weak evidence → `engineering-research`.
- Paper structure → `paper-architect`.
- Figure problem → `method-figure` / `result-figure`.
- Prose problem after science is settled → `academic-writer`.
- After real reviewer comments arrive → `reviewer-response`.
