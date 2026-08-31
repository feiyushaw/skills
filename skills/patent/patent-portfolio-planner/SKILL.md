---
name: patent-portfolio-planner
description: Organize multiple invention candidates into a coherent Chinese patent filing portfolio. Use after invention mining when the user needs candidate clustering, split/merge decisions, filing priority, overlap analysis, disclosure-risk tracking, or a staged filing roadmap.
---

# Patent Portfolio Planner

## Mission

Turn a set of invention candidates into a filing strategy that protects distinct technical mechanisms without unnecessary overlap or fragmentation.

This is an engineering planning aid, not legal advice. Final filing strategy should be reviewed by a qualified patent professional.

## Inputs

Prefer candidate cards from `cn-patent-invention-mining`, prior-art reports, implementation evidence, product roadmap information, and known public-disclosure dates.

## Workflow

1. Normalize each candidate's technical problem, inventive nucleus, essential relationship, technical effect, and provenance boundary.
2. Build an overlap matrix across candidates.
3. Cluster candidates that share the same inventive nucleus.
4. Split candidates when independently protectable mechanisms solve distinct technical problems or require materially different prior-art stories.
5. Identify candidates that should remain embodiments/dependent claims rather than separate filings.
6. Rank filing priority.
7. Record public-disclosure and evidence-capture risks.
8. Produce a staged filing roadmap.

## Priority dimensions

Consider:

- technical/business importance;
- expected product lifetime;
- breadth of protectable mechanism;
- ease of competitor reverse engineering;
- detectability of infringement;
- prior-art pressure;
- quality of current implementation evidence;
- dependency on confidential know-how;
- disclosure timing;
- overlap with other candidates.

Do not reduce priority to a single opaque score; explain the dominant reasons.

## Portfolio map

| Candidate | Inventive nucleus | Overlap cluster | Prior-art pressure | Evidence readiness | Disclosure urgency | Filing priority | Recommended action |
|---|---|---|---|---|---|---|---|

Recommended action may be `file`, `merge`, `split`, `hold`, `capture evidence`, `prior-art first`, or `drop`.

## Guardrails

- preserve the provenance gate from `codebase-patent-diff`;
- do not create artificial patent families by renaming the same mechanism;
- do not merge unrelated mechanisms just because they live in one repository;
- do not invent public-disclosure dates or ownership conclusions;
- keep patentability analysis separate from freedom-to-operate analysis.

## Handoff

Selected candidates proceed to `cn-patent-prior-art` and `cn-patent-drafting` with candidate IDs and portfolio relationships preserved.
