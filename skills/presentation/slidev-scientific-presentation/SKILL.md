---
name: slidev-scientific-presentation
description: Create scientific and technical presentations with Slidev. Use for research talks, paper presentations, algorithm/system explanations, mathematical derivations, experiment results, and dynamic visualizations. Prefer Markdown + LaTeX for ordinary slides, Vue/HTML/SVG only when richer layout or interaction is needed.
---

# Slidev Scientific Presentation

Use this skill to implement a presentation as a reproducible Slidev project. For substantial new decks, consume an approved storyline/slide map from `presentation-architect` when available.

## Core principles

1. Start from the scientific story, not slide decoration.
2. Preserve standard mathematical notation and LaTeX syntax whenever possible.
3. Use Markdown for the common case. Introduce HTML/Vue/components only when they materially improve explanation.
4. Prefer figures, equations, diagrams, animations, and quantitative results over dense prose.
5. Treat visualization as part of the argument. Every visual must answer a specific question.
6. Keep the project reproducible: source data and scripts should generate visual assets where practical.
7. Do not invent experimental results, citations, equations, or implementation claims.

## Recommended workflow

### 1. Inspect source material

Identify goal/audience, central problem/contribution, equations, architecture/algorithm flow, available figures/animations, raw CSV/JSON/Python outputs, and results supporting main claims.

### 2. Build or consume the narrative

For a paper/research talk, a common path is:

1. Title / one-sentence contribution
2. Problem and motivation
3. Existing limitation
4. Key idea
5. Mathematical formulation
6. Method / architecture
7. Algorithm behavior or visualization
8. Experiments
9. Main findings
10. Limitations / conclusion

Do not mechanically create one slide per paper section.

### 3. Choose representation

- Equation/derivation → LaTeX math.
- Static scientific plot → Python-generated SVG/PNG.
- Architecture → Mermaid for simple flows; SVG/HTML for custom diagrams.
- Algorithm evolution → fragments, SVG animation, or a small Vue component.
- Trajectory/simulation → existing GIF/video; JSON + Vue/SVG when interaction adds value.
- Large table → reduce to the comparison supporting the claim.

### 4. Progressive implementation complexity

Prefer in order: Markdown → Markdown + utility classes → HTML/CSS → Vue component → JS visualization library.

## Mathematical content

Use KaTeX/LaTeX notation. Keep one main equation per slide when possible, define symbols nearby, highlight structural changes, and split long derivations when the audience needs to follow the steps.

## Scientific visualization

```text
Python / simulation
  → SVG / PNG for static figures
  → GIF / MP4 for recorded dynamics
  → CSV / JSON for interactive visualization
  → Slidev for narrative, layout, animation, interaction
```

Prefer SVG for line art, trajectories, architecture diagrams, and publication figures when available. Keep generation scripts under `scripts/` and presentation assets under `public/`.

## Slide density

- one central claim per slide;
- 3–5 short bullets maximum when needed;
- avoid paragraph-length body text;
- titles state topic or claim directly;
- figures/labels must remain readable on projection.

## Animation

Use motion to reveal logical order: algorithm stages, before/after, optimization iterations, trajectories/interactions, or progressive equation terms. Avoid decorative transitions.

## Project layout

```text
presentation/
├── slides.md
├── package.json
├── components/
├── layouts/
├── public/
│   ├── figures/
│   ├── animations/
│   └── data/
├── scripts/
└── README.md
```

## Quality checks

Run dev/build, verify asset paths and equations, inspect at presentation scale, verify animation initial/final states, check GIF/video distraction, verify PDF fallback, and confirm technical claims against source material.

## Supporting references

- `references/slidev-authoring-guide.md`
- `references/scientific-visualization.md`
- `references/presentation-storytelling.md`
