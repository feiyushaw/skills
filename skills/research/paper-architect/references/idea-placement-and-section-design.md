# Idea Placement and Section Design

## Purpose

Use this reference when the researcher has scattered thoughts, observations, mechanisms, implementation ideas, experimental findings, or tentative claims and needs to decide **where each idea belongs in the paper and how it should be expressed**.

The central transformation is:

```text
raw idea
  ↓
scientific role
  ↓
section placement
  ↓
subsection role + title
  ↓
representation form
  ↓
required evidence
  ↓
cross-section callbacks
```

## 1. Classify the scientific role first

Before assigning a section, classify each idea as one or more of:

- **Motivation** — why the problem matters.
- **Observed limitation** — what current approaches fail to handle.
- **Root-cause explanation** — why that limitation occurs.
- **Gap** — what remains unresolved in the literature or paradigm.
- **Key insight** — the conceptual realization behind the method.
- **Contribution** — what this work newly provides.
- **Definition / formulation** — formal problem statement or representation.
- **Mechanism** — the part that explains why the approach should work.
- **Algorithm / procedure** — how the method is executed.
- **Implementation detail** — necessary reproducibility detail that is not itself a contribution.
- **Evidence** — result that supports a claim.
- **Interpretation** — what a result means.
- **Boundary / limitation** — where the claim does not hold.
- **Implication** — broader lesson or consequence.

Do not decide section placement from keywords alone. Decide from the scientific role in the paper argument.

## 2. Default placement rules

### Introduction

Place an idea here when it helps answer:

- Why care?
- What is the current paradigm?
- What important limitation remains?
- What is the key insight?
- What is proposed at a high level?
- What are the main contributions?

Introduction should state the insight but usually not fully derive it.

### Related Work

Place an idea here when its purpose is to distinguish the work from prior paradigms, assumptions, formulations, or mechanisms.

Do not move a core methodological explanation into Related Work merely because previous work is discussed nearby.

### Problem Formulation

Place an idea here when it defines:

- state/variables/objects;
- assumptions;
- objective;
- constraints;
- task setting;
- evaluation target needed to state the contribution precisely.

### Method

Place an idea here when it explains:

- the key mechanism;
- the proposed formulation;
- why the design follows from the insight;
- the algorithmic procedure;
- necessary implementation details.

### Experiments / Results

Place an idea here when it is fundamentally an empirical question, observation, comparison, mechanism test, robustness test, efficiency trade-off, or boundary test.

### Discussion

Place an idea here when it interprets evidence, explains broader implications, discusses trade-offs or alternative explanations, or states boundaries not captured cleanly by the main experimental narrative.

## 3. Decide whether an idea deserves a subsection

Create a subsection only when at least one condition is true:

1. it develops a central contribution;
2. it answers a distinct research question;
3. it introduces a concept/formulation needed by later sections;
4. it requires multiple paragraphs/equations/figures to explain coherently;
5. readers will benefit from being able to locate it directly from the table of contents.

Do **not** create a subsection merely because a code module exists.

## 4. Subsection title design

A strong subsection title should reveal the **scientific role** of the subsection.

Prefer:

- `Action-Conditioned Value Representation`
- `Optimization-Compatible Value Learning`
- `Value-Guided Online Optimization`
- `Mechanism Analysis under Distribution Shift`

Avoid generic implementation labels when they hide the contribution:

- `Network`
- `Module 1`
- `Decoder`
- `Training`
- `Implementation`

## 5. Choose the representation form

For each idea, decide whether the reader needs **definition, intuition, procedure, evidence, or comparison**. Use text, equations, algorithms, method figures, quantitative figures, tables, or supplementary material intentionally.

## 6. Figure placement rule

A major figure should be linked to a scientific sentence:

> After seeing this figure, the reader should believe or understand ______.

## 7. Cross-section callback map

Important ideas often appear more than once, but with different depth. Do not repeat identical prose. Each callback must advance the reader's understanding.

## 8. Required output for scattered ideas

When given a list of ideas, produce a placement table:

| Idea | Scientific role | First placement | Subsection | Representation | Evidence needed | Later callback |
|---|---|---|---|---|---|---|

Then propose the revised section hierarchy.

## 9. Section hierarchy audit

Verify every major contribution has a home, titles reveal scientific roles, ideas are introduced before use, Method does not contain empirical conclusions, Results do not introduce unexplained mechanisms, and figures appear where needed.
