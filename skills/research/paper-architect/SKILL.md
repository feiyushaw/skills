---
name: paper-architect
description: Design an academic paper's argument, storyline, section/subsection hierarchy, idea placement, titles, research-question flow, and figure/table/equation roles before paragraph-level drafting. Use after the contribution and evidence are reasonably stable.
---

# Paper Architect

## Mission

Turn stable contributions, evidence, and researcher notes into a coherent paper argument before prose drafting.

```text
research question + gap + hypothesis + claims + evidence
→ paper storyline
→ idea placement
→ section/subsection hierarchy
→ claim-to-section map
→ text/equation/algorithm/figure/table plan
→ paragraph blueprint
→ academic-writer
```

Do not organize the paper around the codebase. Organize around the scientific argument.

## Storyline test

The architecture should answer, in order:

1. Why should the reader care?
2. What important problem remains unresolved?
3. How is it currently approached?
4. Why is the current paradigm insufficient?
5. What is the key insight/hypothesis?
6. What is proposed?
7. Why should it work?
8. What evidence establishes the claims?
9. What should the reader conclude?

## Idea placement

For every note or finding decide scientific role → first placement → subsection role → representation form → required evidence → later callbacks. Use `references/idea-placement-and-section-design.md` and `templates/section-map.md`.

## Paper blueprint

Specify at least working thesis, abstract logic, Introduction paragraph roles, Related Work taxonomy/positioning, Problem Formulation purpose, Method subsection logic, experiment RQs, visual/equation/algorithm roles, limitations/discussion questions, and conclusion takeaway. Use `templates/paper-blueprint.md` and `references/section-blueprints.md`.

## Handoff

- Literature taxonomy/closest-work uncertainty → `literature-research`.
- Claim/evidence gaps → `engineering-research` or `research-idea-refiner`.
- Conceptual figure structure → `method-figure`; quantitative evidence → `result-figure`.
- Blueprint is stable → `academic-writer`.
- Existing Chinese/English text needs translation rather than redesign → `academic-translation`.
