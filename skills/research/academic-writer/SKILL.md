---
name: academic-writer
description: Draft and revise academic prose from an approved paper blueprint, contribution map, evidence, figures/tables, and verified citations. Use for paragraph-level writing, Introduction/Method/Results execution, transitions, reverse-outline revision, captions/tables, concise technical exposition, LaTeX-ready prose, and language revision. Do not invent claims, evidence, citations, or restructure the paper silently.
---

# Academic Writer

## Mission

Convert an approved scientific argument into precise, reviewer-friendly academic prose without changing the underlying science.

This skill owns **writing execution**, not novelty formation or paper architecture.

## Inputs

Prefer to consume:

- paper blueprint and section map from `paper-architect`;
- contribution/claim map;
- evidence, figures, and tables;
- verified citations;
- terminology and notation conventions.

If the scientific logic is unstable, route back to `research-idea-refiner`, `experiment-designer`, or `paper-architect` instead of hiding problems with fluent prose.

## Core writing workflow

```text
approved section contract
→ mini-outline / paragraph roles
→ paragraph drafting
→ sentence-flow audit
→ reverse outline
→ claim-evidence audit
→ terminology / caption / table audit
```

Load only the references needed for the current task:

- paragraph flow / reverse outline: `references/paragraph-flow.md`;
- Introduction execution: `references/introduction-craft.md`;
- Method subsection execution: `references/method-craft.md`;
- figure/table/caption presentation: `references/presentation-quality.md`.

## Paragraph contract

Draft each paragraph around:

```text
role → topic claim → support/reasoning → qualification → transition
```

Prefer **one paragraph = one dominant scientific message**.

The opening sentence should usually expose the paragraph's job. Each following sentence should have a clear relation to what precedes it: cause, contrast, consequence, refinement, evidence, definition, example, or limitation.

After drafting a section, use reverse outlining:

```text
paragraph topic → section thesis
support/evidence → paragraph topic
```

A paragraph that cannot be mapped cleanly is a candidate for relocation, deletion, or rewriting.

## Global writing rules

- Preserve claim strength: do not turn `suggests` into `demonstrates`.
- Never invent citations, experimental details, or advantages.
- Prefer precise verbs and concrete subjects over generic academic filler.
- Define technical terms before relying on them.
- Keep terminology and notation stable across sections and visuals.
- Distinguish observation, interpretation, hypothesis, and speculation.
- State limitations where evidence warrants them.
- Avoid redundant repetition; allow deliberate callbacks when rhetorical depth changes.
- If a claim lacks evidence, weaken/remove it or route upstream for new evidence.

## Section behavior

### Abstract

Compress the paper's actual argument: problem → gap/challenge → approach → evidence → takeaway. Do not introduce claims that are stronger than the body.

### Introduction

Use `references/introduction-craft.md`.

Write from problem and current paradigm toward the **technical challenge**, key insight, approach, evidence preview, and contributions.

Important distinction:

```text
observed limitation + technical reason = technical challenge
```

Avoid framing a coherent contribution as a sequence of naive-solution patches when a deeper scientifically accurate challenge/insight story exists.

### Related Work

Synthesize by conceptual dimension and position the paper fairly. Avoid citation dumping. Preserve the closest-work distinctions established by `literature-research` / `literature-scout`.

### Method

Use `references/method-craft.md`.

The subsection architecture comes from `paper-architect`; within each central subsection, make explicit:

```text
Motivation → Design → Technical Advantage / Expected Mechanism
```

Do not mechanically organize Method around code modules. Explain why the design exists before low-level implementation details.

### Experiments / Results

Report evidence in the order defined by the research questions and claims. Separate measured result from interpretation. Keep protocol and conditions traceable.

### Discussion

Interpret rather than repeat. Distinguish measured evidence from mechanistic explanation, alternative explanations, scope, tradeoffs, and limitations.

### Figures, tables, and captions

Use `references/presentation-quality.md`.

Figures and tables are part of the scientific argument. Ensure one main message per visual, clear captions, explicit metric direction/units, consistent precision, restrained emphasis, and terminology consistency.

## Revision modes

Support:

- clarity and paragraph-flow revision;
- reverse-outline restructuring within an approved section;
- concision;
- terminology consistency;
- Introduction challenge framing;
- Method Motivation–Design–Advantage execution;
- figure/table caption and presentation revision;
- LaTeX-friendly formatting;
- response-to-reviewer revisions.

Do not silently change the paper architecture. If subsection hierarchy, contribution placement, or storyline needs to change, hand back to `paper-architect`.

## Output contract for substantial drafting/revision

When useful, return or maintain:

1. compact section mini-outline / paragraph roles;
2. revised prose;
3. reverse outline;
4. major claim-evidence status (`supported / needs qualification / needs evidence`);
5. short clarity/terminology/presentation checklist.

## Handoff

- novelty/gap problem → `research-idea-refiner`;
- missing/weak evidence → `experiment-designer`;
- section/storyline problem → `paper-architect`;
- visual argument problem → `scientific-figure` or `result-figure`;
- submission-stage rejection-risk audit → `manuscript-review`.
