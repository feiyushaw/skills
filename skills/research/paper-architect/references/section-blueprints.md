# Section Blueprints

These are argument patterns, not mandatory templates.

## Abstract

1. Problem / context
2. Limitation / gap
3. Key insight
4. Proposed method
5. Main evidence
6. Takeaway / significance

Each sentence should earn space. Avoid detailed literature review and unsupported adjectives.

## Introduction

Recommended paragraph roles:

- P1 — important context and problem;
- P2 — current paradigm and why it is attractive;
- P3 — critical unresolved limitation;
- P4 — why the limitation matters;
- P5 — key insight / hypothesis;
- P6 — proposed approach;
- P7 — evidence preview;
- P8 — precise contribution bullets.

Shorter introductions may merge roles. Do not add paragraphs only to satisfy the count.

## Related Work

For each conceptual family:

1. define the family;
2. summarize representative approaches;
3. state what capability they provide;
4. state the limitation/distinction relevant to this paper;
5. position the current work without exaggerated novelty language.

Prefer taxonomy over paper-by-paper chronology.

## Problem Formulation

1. define entities and notation;
2. state assumptions;
3. define objective / task;
4. expose the limitation of the standard formulation when relevant;
5. state what must change for the proposed contribution.

## Method

A useful default:

- Overview and design goal
- Core insight
- Proposed formulation / mechanism
- Algorithm / optimization / inference
- Analysis or explanation of why it works
- Implementation details

Subsections should align with contributions, not merely source-code modules.

## Experiments

Start with evaluation protocol, then organize results by research question.

Possible RQs:

- effectiveness;
- mechanism / ablation;
- robustness / generalization;
- efficiency / scaling;
- sensitivity;
- failure / limitation.

For each RQ:

```text
question → experiment design → comparison → result → interpretation → implication for claim
```

## Discussion

Address:

- what the results mean;
- why the method likely behaves this way;
- alternative explanations;
- scope and boundary conditions;
- tradeoffs;
- surprising or negative findings;
- implications and future questions.

## Conclusion

Restate the problem, key insight, supported contribution, and main implication. Do not introduce new claims.
