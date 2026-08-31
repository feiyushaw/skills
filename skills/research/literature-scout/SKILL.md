---
name: literature-scout
description: Perform targeted literature scouting to test a research idea's novelty, identify closest competing formulations, standard terminology, missing citations, and prior-art threats. Use when the research question is already reasonably scoped and the goal is positioning rather than a full systematic review.
---

# Literature Scout

## Mission

Answer the literature questions that most affect the strength or survival of a research idea.

This is a targeted scout, not a substitute for a full systematic review.

## Typical questions

- Has this idea already been formulated under another name?
- What are the 3–10 closest papers, not merely topical papers?
- Which existing method most threatens the novelty claim?
- What terminology would an expert use for this mechanism?
- Which papers support the stated limitation?
- Which papers contradict the proposed motivation?
- What adjacent literature should be cited to position the work fairly?

## Workflow

1. Start from the current gap, hypothesis, contribution map, and novelty uncertainty.
2. Generate synonym/mechanism/formulation queries, not only application keywords.
3. Search for both supporting and threatening prior art.
4. Separate:
   - exact/near duplicates;
   - same mechanism, different application;
   - same problem, different mechanism;
   - adjacent conceptual work.
5. Compare the closest papers on problem, information assumptions, formulation, mechanism, optimization/inference, and evidence.
6. Update the novelty statement conservatively.

## Required output

Prefer a compact positioning table:

| Work | Same problem? | Same mechanism? | Same formulation? | Key difference | Novelty threat |
|---|---|---|---|---|---|

Then state:

- strongest novelty threat;
- terminology corrections;
- defensible gap statement;
- unresolved search questions.

## Handoff

Return the positioning evidence to `research-idea-refiner`. If broad coverage assurance is required, route to the systematic literature-review skill.
