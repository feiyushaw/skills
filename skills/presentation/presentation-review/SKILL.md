---
name: presentation-review
description: Review a near-complete technical, scientific, or business presentation for narrative, evidence, density, visual hierarchy, readability, timing, and delivery risks. Use as the final quality gate for Slidev, PPTX, PDF, or other deck formats.
---

# Presentation Review

## Mission

Identify the highest-risk reasons a presentation may fail to communicate its intended message to its actual audience.

## Review axes

### Narrative

- Can the audience recover the central question and takeaway?
- Does every slide have a clear role?
- Are transitions causal and understandable rather than merely chronological?
- Are important terms introduced before use?

### Evidence

- Does every strong claim have appropriate evidence?
- Are plots/tables readable and fairly presented?
- Are citations and source claims traceable?
- Are limitations hidden or overstated?

### Slide design

- one dominant message per slide;
- title/headline matches the slide's role;
- figures are large enough;
- text density is appropriate;
- alignment, spacing, typography, and visual hierarchy are consistent;
- color is not the only carrier of essential meaning.

### Delivery

- estimated time fits the slot;
- dense derivations have enough explanation time;
- animations have stable initial/final states;
- critical content survives PDF/static fallback;
- backup slides cover predictable questions without interrupting the main story.

## Severity

- `S0` — presentation blocker: wrong story, unsupported claim, unreadable critical slide, broken asset.
- `S1` — major communication risk.
- `S2` — polish or local clarity improvement.

## Output

Return:

1. overall verdict;
2. top 3 risks;
3. slide-by-slide findings for slides that need action;
4. narrative/evidence consistency findings;
5. prioritized revision queue;
6. optional backup-slide recommendations.

Do not redesign every slide when a small number of structural fixes will remove most risk.
