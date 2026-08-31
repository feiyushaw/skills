---
name: paper-architect
description: Design the argument, storyline, section and subsection hierarchy, titles, idea placement, research-question flow, figure/table/equation roles, and claim-to-section mapping of an academic paper before paragraph-level drafting. Use when the user has research ideas or a reasonably stable contribution and needs to decide how the paper should be organized, where specific thoughts belong, how subsections should be named, or how ideas should be expressed through text, equations, algorithms, figures, or tables.
---

# Paper Architect

## Mission

Turn research contributions, evidence, and scattered researcher thoughts into a coherent paper argument before writing prose.

The default transformation is:

```text
research question + gap + hypothesis + contribution map + evidence + raw ideas
  ↓
paper storyline
  ↓
idea placement
  ↓
section / subsection hierarchy
  ↓
subsection titles and scientific roles
  ↓
claim-to-section map
  ↓
text / equation / algorithm / figure / table plan
  ↓
paragraph blueprint
  ↓
academic-writer
```

## First principle

Do not organize the paper around the codebase. Organize it around the scientific argument.

A software decomposition such as `encoder / decoder / loss / training` is not automatically a good Method structure. Ask which section explains each contribution and why the reader needs it at that point in the argument.

## Step 1 — Build the paper storyline

Answer, in order:

1. Why should the reader care?
2. What important problem remains unresolved?
3. How is it currently approached?
4. Why is the current paradigm insufficient?
5. What is the key insight?
6. What is proposed?
7. Why should it work?
8. What evidence establishes the claims?
9. What should the reader conclude?

If this chain is weak, fix it before drafting sections.

## Step 2 — Place scattered ideas before finalizing the outline

When the researcher provides notes, new thoughts, observations, explanations, implementation ideas, or experimental findings, do not force them immediately into the nearest section.

For each idea determine:

```text
scientific role
  → first placement
  → subsection role
  → representation form
  → required evidence
  → later callbacks
```

Read `references/idea-placement-and-section-design.md` for the full placement rules.

For a substantial reorganization, maintain `templates/section-map.md` as a living artifact.

## Step 3 — Build the paper blueprint

At minimum specify:

- working title and one-sentence thesis;
- abstract logic;
- Introduction paragraph roles;
- Related Work taxonomy and positioning goal;
- Problem Formulation purpose;
- Method subsection logic;
- Experiment research questions;
- expected figures/tables/equations/algorithms and their scientific messages;
- Discussion / limitations questions;
- Conclusion takeaway.

Use `templates/paper-blueprint.md`.

## Step 4 — Design subsection hierarchy and titles

A subsection should exist because it serves a distinct scientific role, not because a code module exists.

For every subsection define:

- question answered;
- contribution or claim served;
- prerequisite knowledge;
- takeaway the reader should leave with;
- paragraph sequence;
- equations / algorithms / figures / tables required;
- 2–3 candidate titles when framing is ambiguous.

Prefer titles that expose the scientific role, e.g.:

- `Action-Conditioned Value Representation`
- `Optimization-Compatible Value Learning`
- `Value-Guided Online Optimization`

rather than generic labels such as `Network`, `Decoder`, or `Training` when those labels conceal the argument.

## Step 5 — Map contributions to sections

Every central contribution should have a home:

```text
Contribution → Claim → Evidence → Figure/Table → Section
```

Flag contributions that appear in the Introduction but are not developed or tested later.

## Step 6 — Architect each major section

Read `references/section-blueprints.md`.

### Introduction

Prefer a causal argumentative flow:

```text
context → status quo → critical limitation → consequence
→ insight → proposed approach → evidence preview → contributions
```

### Related Work

Organize by conceptual dimensions that position the paper, not by a chronological list of papers. End each subsection with the unresolved distinction relevant to the current work.

### Problem Formulation

Introduce only notation, assumptions, objectives, and constraints needed to make the contribution precise. Do not bury the novelty in notation.

### Method

Prefer:

```text
overview → core insight → proposed mechanism/formulation
→ algorithm/optimization → analysis → implementation details
```

The method section should explain why the method exists before every implementation detail.

### Experiments

Organize around research questions rather than a pile of benchmark tables. Typical roles:

- RQ1 effectiveness — does it work?
- RQ2 mechanism — why does it work?
- RQ3 robustness/generalization — when does it work?
- RQ4 efficiency — what does it cost?
- RQ5 limitations — where does it fail?

Use only the RQs needed by the actual claims.

### Discussion

Interpret, do not repeat results. Address mechanism, scope, boundary conditions, tradeoffs, alternative explanations, and implications.

## Step 7 — Choose how each idea should be expressed

For every important idea choose the representation form intentionally:

- **text** — conceptual explanation, interpretation, transition;
- **equation** — precise relationships, objectives, constraints, decomposition;
- **algorithm** — execution order, iteration, update/control flow;
- **method figure** — architecture, information flow, hierarchy, feedback, training/inference split;
- **quantitative figure** — trends, comparisons, distributions, trade-offs, ablations, sensitivity;
- **table** — exact values or systematic categorical comparison;
- **supplement** — necessary detail that would interrupt the main storyline.

Do not add a figure merely because one is conventional.

## Step 8 — Architect figures and tables

For each major figure/table define:

- scientific question;
- claim/concept supported;
- message the reader should retain;
- why prose alone is insufficient;
- source evidence;
- required panels/content;
- section where first introduced.

A figure without a claim or concept role is a candidate for removal or supplementary material.

## Step 9 — Create paragraph blueprints

Before prose, define each paragraph as:

```text
role → topic claim → supporting evidence/reasoning → transition
```

Paragraph drafting belongs to `academic-writer` after this structure is stable.

## Living-paper workflow

Treat the blueprint and section map as living documents. When a new thought appears, assess:

1. Is it scientifically important?
2. Does it modify the thesis, contribution, or only interpretation?
3. Where should it first appear?
4. Does it deserve a new subsection?
5. Does it require new evidence?
6. Does it require a figure/table/equation?
7. Which later section should revisit it at greater depth?

Do not rebuild the whole paper for every new note unless the central storyline changes.

## Consistency audit

Check:

- Title ↔ central contribution
- Abstract ↔ full paper
- Introduction gap ↔ Method mechanism
- Contribution bullets ↔ actual sections
- Subsection titles ↔ scientific roles
- New ideas ↔ explicit section homes
- Experiment RQs ↔ claims
- Figures ↔ concepts/evidence
- Discussion ↔ observed results
- Conclusion ↔ demonstrated claims

## Handoff

- Novelty/gap still unstable → `research-idea-refiner`.
- Need targeted literature positioning → `literature-scout`.
- Need hostile pre-review → `research-critic`.
- Need paragraph/LaTeX drafting → `academic-writer`.
- Need to draw a conceptual method figure → optional `method-figure`.
