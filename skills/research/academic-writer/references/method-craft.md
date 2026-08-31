# Method Writing Craft

## Purpose

Use this reference after `paper-architect` has chosen the scientific subsection structure. This guide helps execute each Method subsection clearly without turning the section into a source-code walkthrough.

## The subsection triad

For each central method subsection, make three things explicit:

```text
Motivation
→ Design
→ Technical Advantage / Expected Mechanism
```

### Motivation

Answer:

- What unresolved problem makes this component or formulation necessary?
- Which limitation from the Introduction does it address?
- Why is a simpler alternative insufficient?

### Design

Describe the actual mechanism in a reproducible order:

```text
input / assumptions
→ representation or formulation
→ transformations / updates / optimization
→ output
```

Use equations, algorithms, or figures when they carry the idea more precisely than prose.

### Technical Advantage / Expected Mechanism

Explain why the design should improve the relevant property. Tie the explanation to a measurable or testable claim where possible.

Do not claim an advantage merely because a component is new. Distinguish:

- intended mechanism;
- measured evidence;
- interpretation.

## Method overview

A useful overview usually gives:

1. setting and notation needed immediately;
2. core scientific insight;
3. high-level method flow;
4. pointer to the main method figure when useful;
5. map of subsequent subsections.

The overview should help the reader see the logic before details.

## Pipeline figures and subsection structure

A pipeline sketch is useful for checking completeness, but do not mechanically create one subsection per software module.

Use this order:

```text
contribution / scientific role
→ figure contract
→ method-flow sketch
→ subsection design
```

If the sketch produces sections named only after code modules, reconsider whether the hierarchy exposes the scientific argument.

## Forward-process clarity

When explaining a mechanism, define important objects first and then describe the forward process in execution order. Avoid jumping between training, inference, notation, and motivation within the same paragraph unless the relation is essential.

## Implementation details

Keep reproducibility details, hyperparameters, dimensions, preprocessing, or engineering choices near the end of Method or in an implementation subsection / appendix unless they are themselves part of a scientific claim.

## Method audit

For each subsection ask:

1. Why does this subsection exist?
2. What new object/mechanism/formulation is introduced?
3. Can a knowledgeable reader reconstruct the process?
4. Is the intended advantage explicit?
5. Which claim or contribution does it serve?
6. Which experiment or analysis later tests the claimed advantage?
