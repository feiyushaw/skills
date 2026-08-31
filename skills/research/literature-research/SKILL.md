---
name: literature-research
description: Unified literature workflow for broad field understanding and targeted novelty scouting. Use landscape mode to map a field and novelty-scout mode to test a scoped idea against closest work, terminology, missing citations, and prior-art threats.
---

# Literature Research

## Mission

Use one literature entry point for two related tasks:

```text
Landscape mode      → What is known and how is the field structured?
Novelty-scout mode  → Has this specific idea/mechanism/formulation already been done?
```

Do not infer novelty from a small search sample and never invent papers, metadata, claims, or results.

## Choose the mode

### Landscape mode

Use when the research area is still broad or the user needs a structured understanding of paradigms, assumptions, representative works, evolution, limitations, and open problems.

Typical artifacts:

- `literature-map.md`;
- research taxonomy;
- representative-work / comparison matrix;
- open-problem list.

Workflow:

```text
scope → terminology expansion → seed works → citation chains
→ taxonomy → comparison matrix → paradigm evolution
→ recurring limitations → candidate gaps
```

### Novelty-scout mode

Use when the proposed contribution is already reasonably scoped and the main uncertainty is positioning or novelty.

Typical questions:

- Has the same mechanism appeared under another name?
- What are the 3–10 closest works?
- Which work most threatens the novelty claim?
- Which standard terminology should replace local wording?
- Which citations support or contradict the motivation?

Read `references/novelty-scout.md` for the targeted workflow and positioning table.

## Shared comparison dimensions

Compare only dimensions that change scientific interpretation, such as:

- problem formulation;
- assumptions / information access;
- representation and mechanism;
- optimization / inference;
- supervision / data requirements;
- theoretical guarantees;
- compute cost;
- evaluation regime;
- failure modes and scope.

## Handoff

- Candidate gap or novelty statement needs refinement → `research-idea-refiner`.
- Literature reveals missing experiment or baseline → `engineering-research`.
- Related-work organization is needed for a paper → `paper-architect`, then `academic-writer`.

## Completion

The literature output should make clear what is known, what the closest threats are, what terminology experts use, which uncertainty remains, and which gap statements are defensible versus merely absent from a small sample.
