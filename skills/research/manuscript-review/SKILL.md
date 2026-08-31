---
name: manuscript-review
description: Audit a near-complete academic manuscript for submission-stage rejection risks after the research, experiments, paper architecture, and prose are largely complete. Use for reviewer-style pre-submission checks across contribution clarity, writing, empirical strength, evaluation completeness, method soundness, claim-evidence alignment, figures/tables, and reproducibility. Distinct from research-critic, which attacks the research idea earlier.
---

# Manuscript Review

## Mission

Act as a skeptical submission-stage reviewer and identify concrete reasons a mature manuscript could be rejected or require major revision.

This skill answers:

> **Is the current manuscript submission-ready, and what are the highest-risk reasons a reviewer might reject it?**

It does not replace `research-critic`:

```text
research-critic  → Is the research idea / claim scientifically defensible?
manuscript-review → Does the finished manuscript present and support it convincingly enough for submission?
```

## Inputs

Prefer:

- full manuscript or near-complete draft;
- contribution map;
- paper blueprint / section map;
- key figures and tables;
- experiment plan and results;
- target venue constraints if available.

## Review workflow

1. Reconstruct the paper's claimed thesis and contributions from the manuscript alone.
2. Build a claim-evidence audit for Abstract and Introduction first.
3. Audit Method reproducibility and design rationale.
4. Audit Experiments for strong/fair baselines, ablations, controls, robustness, and scope.
5. Audit figures/tables/captions and visual consistency.
6. Audit writing clarity with reverse outlining where needed.
7. Identify fatal, major, and minor risks.
8. Convert findings into a prioritized revision queue.

## Five primary rejection dimensions

### 1. Contribution strength and clarity

Ask:

- What new knowledge, formulation, mechanism, method, or finding is contributed?
- Can the contribution be stated without marketing language?
- Does the paper solve an important problem or merely a convenient benchmark gap?
- Could a reviewer reduce the work to a predictable `A + B` combination?
- Are the contribution bullets aligned with what is actually developed and tested?

If novelty itself is unstable, route to `research-idea-refiner` / `literature-scout` rather than polishing language.

### 2. Writing and comprehension

Ask:

- Can an informed reader recover the paper's story from title → abstract → introduction → section headings → figures?
- Does each paragraph have a clear role?
- Are motivation and design rationale explicit for key method components?
- Are terms, notation, and method names stable?
- Does Method explain `why`, `what`, and `how`, rather than only implementation?

Use reverse outlining when a section feels difficult to follow.

### 3. Empirical strength

Ask:

- Are improvements meaningful and consistent enough to support the stated claims?
- Are strong and relevant baselines included?
- Are comparisons fair?
- Are important gains isolated from confounders such as extra data, parameters, compute, privileged information, or tuning effort?
- Are robustness, boundary conditions, or failure cases tested where the claims require them?

### 4. Evaluation completeness

Ask:

- Does every major claim have direct evidence?
- Are key design choices ablated or otherwise justified?
- Are metrics sufficient to evaluate the claimed properties?
- Are evaluation settings challenging and representative enough?
- Are uncertainty/statistical summaries reported when needed?
- Are important negative or boundary results omitted?

### 5. Method soundness and net value

Ask:

- Are assumptions realistic and clearly stated?
- Is the mechanism technically coherent?
- Does the method require fragile per-setting tuning?
- Does added complexity buy enough scientific or practical value?
- Could a simpler alternative explain the same gains?
- Do new limitations outweigh the claimed benefits?

## Claim-evidence hard constraint

For every major claim in the Abstract and Introduction, build:

```text
Claim:
Evidence location:
Evidence type:
Status: supported / partially supported / unsupported / overstated
Required action:
```

If unsupported, choose one:

- add evidence;
- narrow the claim;
- qualify the claim;
- remove the claim.

Do not solve unsupported claims by rewriting them to sound more confident.

## Visual and presentation audit

Check:

- every major figure/table has one clear message;
- captions are self-contained enough for quick reviewer scanning;
- metric direction and units are explicit;
- table precision and highlighting are consistent;
- figures/tables are readable at final publication size;
- visual terminology matches the text;
- teaser / Figure 1 communicates the central insight rather than only showing implementation boxes.

## Severity levels

### Fatal

Likely to invalidate or collapse the paper's central contribution, e.g. novelty already covered, core claim unsupported, unfair comparison, invalid formulation, or decisive confounder.

### Major

Could reasonably trigger rejection or major revision, e.g. missing strong baseline, incomplete ablation, unclear technical challenge, weak generalization evidence, unreproducible Method.

### Minor

Presentation or local clarity issues that do not undermine the central contribution.

## Output contract

Return:

### 1. Submission verdict

```text
Overall: not ready / borderline / ready with minor revision
Top rejection risk:
Second risk:
Third risk:
```

### 2. Risk table

| Severity | Dimension | Issue | Evidence in manuscript | Recommended action |
|---|---|---|---|---|

### 3. Claim-evidence audit

Focus especially on Abstract and Introduction claims.

### 4. Section-by-section audit

Cover at least:

- Abstract;
- Introduction;
- Related Work / positioning;
- Method;
- Experiments / Results;
- figures/tables;
- Discussion / limitations;
- Conclusion.

### 5. Prioritized revision queue

Order by expected reduction in rejection risk, not by ease of editing.

## Handoff

- contribution/novelty collapse → `research-idea-refiner` + `literature-scout`;
- missing experiments / confounders → `experiment-designer`;
- paper structure/storyline → `paper-architect`;
- prose/flow/captions → `academic-writer`;
- method/result visual redesign → `scientific-figure` / `result-figure`.
