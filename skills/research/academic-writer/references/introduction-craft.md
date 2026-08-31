# Introduction Writing Craft

## Purpose

Use this reference after `paper-architect` has established the Introduction's scientific role and paragraph sequence. This file helps turn that structure into reviewer-friendly prose without changing the underlying contribution.

## Core chain

A strong Introduction usually makes this chain visible:

```text
important task / problem
→ current paradigm
→ observed limitation
→ technical reason for the limitation
→ precise research challenge
→ key insight
→ proposed solution
→ why the solution should work
→ evidence preview
→ contributions
```

The crucial distinction is:

```text
observed limitation ≠ technical challenge

observed limitation + technical reason = technical challenge
```

Do not stop at `existing methods perform poorly under X`. Explain why the failure occurs if the paper's contribution depends on that mechanism.

## Backward-first planning

Before drafting, answer:

1. What exact technical problem does this paper solve?
2. Why is the problem unresolved rather than merely under-optimized?
3. What are the paper's real contributions?
4. What benefit follows from each contribution?
5. Why should the proposed mechanism solve the challenge?
6. What prior-work path naturally leads the reader to this challenge?

Then write forward from context to contribution.

## Avoid incremental-patch storytelling

Weak narrative:

```text
naive solution
→ problem A
→ add module A
→ problem B
→ add module B
```

This can make the work appear as a predictable chain of patches.

Prefer, when scientifically accurate:

```text
existing paradigm
→ underlying technical challenge
→ key insight
→ unified mechanism / formulation
→ evidence
```

Do not hide genuine incremental scope; the goal is to expose the deepest defensible scientific rationale, not to market ordinary modifications as fundamental innovation.

## Opening choices

Choose an opening that fits reader familiarity:

- unfamiliar task: define the task, then explain why it matters;
- familiar task: begin with importance or target requirements;
- new setting within a familiar field: start broad, then narrow to the specific setting;
- mature field with a crisp unresolved failure: expose the challenge early if that improves clarity.

## Contribution paragraph

Contribution bullets should state scientific contributions rather than implementation inventory. Prefer forms such as:

```text
We identify / formulate / establish ...
We introduce ... to address ...
We show / demonstrate / analyze ... under ...
```

Every strong contribution bullet should map to a later Method/Analysis/Experiment section and to evidence where applicable.

## Introduction audit

Before finalizing, check:

- limitation and technical reason are distinguished;
- the proposed method answers the stated challenge directly;
- the key insight appears before excessive implementation detail;
- contributions are not broader than the later evidence;
- the experiment preview supports the central claims;
- the Introduction does not require the reader to infer why the method exists.
