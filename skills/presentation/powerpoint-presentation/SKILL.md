---
name: powerpoint-presentation
description: Implement an approved presentation architecture as an editable PowerPoint/PPTX deck. Use when the user needs a real PPTX rather than Slidev, especially for business, internal review, editable delivery, or environments where PowerPoint is the required final format.
---

# PowerPoint Presentation

## Mission

Render an approved storyline and slide map into a maintainable, editable PPTX without weakening the technical argument.

Prefer `presentation-architect` first when audience, narrative, or slide roles are still unstable.

## Inputs

Use, when available:

- audience and talk objective;
- slide map / storyline;
- figures, tables, equations, diagrams, videos, and citations;
- organization/template constraints;
- target duration and aspect ratio.

## Implementation rules

1. One dominant message per slide.
2. Prefer editable text, shapes, charts, and vector assets over screenshots.
3. Preserve mathematical notation and technical terminology.
4. Reuse source figures when they already communicate the claim; do not redraw merely for style consistency.
5. Keep font sizes, margins, grid, alignment, and visual hierarchy consistent.
6. Avoid dense prose and decorative elements without information value.
7. Use animations only when they encode sequence or comparison and the target environment supports them reliably.
8. Keep speaker-facing details in notes or backup slides when possible.

## Slide implementation contract

For each slide maintain mentally or explicitly:

```text
slide role
headline / takeaway
primary evidence or visual
supporting explanation
source / provenance
speaker action
```

## Technical decks

- equations: use native equation objects or high-quality vector rendering where practical;
- plots: preserve axis labels, units, legends, uncertainty, and source data provenance;
- architecture: prefer editable vector/shapes;
- videos/GIFs: provide a static fallback frame for PDF or incompatible environments.

## QA

Check the deck in slideshow mode and, when required, exported PDF:

- no clipping or overflow;
- readable from presentation distance;
- consistent terminology and figure numbering;
- local assets resolve;
- all technical claims trace back to supplied sources/evidence;
- layout still works on common 16:9 presentation displays;
- backup slides are separated from the main narrative.

## Handoff

Run `presentation-review` before final delivery.
