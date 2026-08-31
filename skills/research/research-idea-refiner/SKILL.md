---
name: research-idea-refiner
description: Refine a raw research idea into a defensible research gap, falsifiable hypothesis, contribution structure, claim-evidence map, and prioritized next questions. Use when the user is still shaping novelty, significance, mechanism, positioning, or contribution scope. Do not jump directly to manuscript prose.
---

# Research Idea Refiner

## Mission

Turn a vague research intuition into a research contribution that can survive prior-art and reviewer pressure.

The default transformation is:

```text
raw idea
  ↓
problem framing
  ↓
status quo / closest paradigm
  ↓
limitation and root cause
  ↓
research gap
  ↓
core hypothesis
  ↓
novel mechanism / formulation
  ↓
contribution tree
  ↓
claims
  ↓
required evidence
```

## First principle

Never equate `apply A to B` with a publishable contribution. Ask what limitation in B exists, why it exists, why mechanism A addresses that root cause, why a direct transfer is insufficient, and what genuinely new formulation/mechanism is introduced.

## Default workflow

### 1. Normalize the raw idea

Extract:

- target problem;
- proposed mechanism or intuition;
- current paradigm being challenged;
- expected benefit;
- assumptions;
- what is still uncertain.

### 2. Build the problem chain

Write a compact chain:

```text
important problem
→ current solution paradigm
→ unresolved limitation
→ root cause
→ consequence
→ missing capability
```

Do not accept a gap that is merely "few papers have studied X" unless the absence itself has scientific significance.

### 3. Formulate the hypothesis

A useful hypothesis states why the proposed mechanism should change an observable outcome.

Prefer:

> Because mechanism M changes property P, method A should improve outcome Y under condition C.

Avoid:

> We expect the proposed framework to perform better.

### 4. Run the novelty ladder

Classify the idea using `references/novelty-ladder.md`. State the current level and what would be required to move up one level.

### 5. Build the contribution tree

Separate contribution types when applicable:

- problem/diagnostic contribution;
- conceptual/formulation contribution;
- methodological/mechanistic contribution;
- algorithmic/technical contribution;
- empirical/measurement contribution;
- theoretical contribution.

Do not inflate the list. Three strong contributions are better than six overlapping bullets.

### 6. Convert contributions to claims

For every contribution, define one or more falsifiable claims with required evidence. Use the contribution map template.

### 7. Stress-test the idea

Attack:

- novelty — is this only A+B, a module swap, a new optimizer, or engineering integration?
- necessity — would a simpler baseline solve the same problem?
- mechanism — is the proposed explanation distinguishable from alternatives?
- significance — does the solved limitation matter in practice or theory?
- evidenceability — can the central claim actually be tested?
- generality — is the contribution tied to one narrow benchmark?

### 8. Produce the next-question queue

Do not merely praise or summarize the idea. End with the highest-value unresolved research questions, prioritized by how much they could strengthen or kill the contribution.

## Required output artifacts

For substantial idea-refinement work, produce or update:

- `idea-canvas.md`
- `contribution-map.md`
- a short `idea-stress-test` section
- a prioritized `next-research-questions` section

## Handoff

- Need targeted prior-art validation → `literature-scout` or a systematic literature-review skill.
- Need adversarial challenge → `research-critic`.
- Need manuscript structure after the contribution stabilizes → `paper-architect`.
- Need paragraph-level drafting only after the blueprint is stable → `academic-writer`.

## Stop conditions

Do not call an idea mature when any of the following remains unresolved:

- the gap is only rhetorical;
- the closest competing formulation is unknown;
- the core hypothesis is not falsifiable;
- contributions overlap heavily;
- central claims lack possible evidence;
- the claimed novelty disappears when expressed in standard terminology.
