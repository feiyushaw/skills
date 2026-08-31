---
name: literature-research
description: Systematically investigate a research topic before or during paper conception. Build a research landscape, taxonomy, representative-work map, comparison matrix, open-problem list, and candidate gaps. Use when the user needs to understand a field rather than only check one specific closest-work novelty question.
---

# Literature Research

## Mission

Turn a broad research topic into a structured understanding of what is known, how the field is organized, what assumptions dominate, where paradigms differ, and which unresolved problems are plausible research opportunities.

This skill answers **“What is known, and how is the field structured?”**. It does not by itself certify novelty for a specific proposed contribution; hand targeted novelty threats to `literature-scout` and contribution synthesis to `research-idea-refiner`.

## Core workflow

1. **Define scope.** Clarify the research problem, application boundary, time horizon, inclusion/exclusion criteria, and desired depth.
2. **Expand terminology.** Generate synonyms, older/newer terminology, formulation names, task names, mechanism names, and related communities.
3. **Identify seed works.** Prefer surveys, seminal papers, strong recent papers, and representative methods from different paradigms.
4. **Citation-chain.** Use backward references and forward citations to discover lineage and follow-up work.
5. **Build a taxonomy.** Organize papers by scientific dimensions, not only chronology.
6. **Construct a comparison matrix.** Compare problem setting, formulation, mechanism, assumptions, supervision/data, optimization/inference, evidence, strengths, and limitations.
7. **Trace paradigm evolution.** Explain why later paradigms emerged and which limitations they attempted to resolve.
8. **Extract unresolved issues.** Record contradictions, recurring failure modes, restrictive assumptions, unexplored regimes, and weakly supported claims.
9. **Form candidate gaps.** Distinguish true unresolved scientific questions from mere missing combinations or benchmark gaps.
10. **Hand off.** Send candidate gaps and closest-work threats to `research-idea-refiner` / `literature-scout`.

## Required artifacts

For substantial work, maintain:

- `literature-map.md` — important papers and their roles;
- `research-taxonomy.md` — paradigms and comparison dimensions;
- `paper-comparison-matrix.md` — structured closest/representative-work table;
- `open-problems.md` — unresolved issues and gap candidates.

## Taxonomy dimensions

Choose only dimensions that change scientific interpretation. Common dimensions include:

- problem formulation;
- assumptions and constraints;
- representation;
- core mechanism;
- optimization / inference procedure;
- training signal / supervision;
- data requirements;
- theoretical guarantees;
- computational cost;
- evaluation regime;
- failure modes;
- scope / generality.

## Research-landscape test

A literature review is not complete merely because many papers were collected. Before handoff, the researcher should be able to answer:

- What are the 2–5 major paradigms?
- Why did each paradigm arise?
- What limitation of earlier approaches did it address?
- What assumptions remain shared across paradigms?
- Which papers are the strongest novelty threats to a new idea?
- Which unresolved issues recur across multiple papers?
- Which apparent gaps are probably unimportant or already saturated?

## Separation from other skills

- Broad field understanding / research landscape → `literature-research`.
- “Has this exact mechanism/formulation already been done?” → `literature-scout`.
- Turn landscape + gap candidates into a contribution → `research-idea-refiner`.
- Systematic-review manuscript / PRISMA-style exhaustive review → optional external systematic-review skill.

## Integrity rules

- Never invent citations, publication metadata, claims, or results.
- Separate paper-authored claims from your interpretation.
- Mark uncertain taxonomy assignments explicitly.
- Do not infer novelty from absence in a small search sample.
- Prefer primary papers for method claims; use surveys for navigation and taxonomy.
