# Skill Catalog

The V2 catalog contains **51 skills across seven domains**. Stable packs contain 49 skills; two repository-maintenance experiments remain opt-in.

## Core — 4

| Skill | Invocation | Role |
|---|---|---|
| `workflow-router` | user | route a task to the smallest suitable workflow |
| `grilling` | model/user | decision-tree/frontier interview discipline |
| `handoff` | model/user | durable cross-session/agent handoff |
| `writing-for-agents` | model/user | write agent-consumed instructions and docs |

## Engineering — 14

`grill-with-docs`, `triage`, `domain-modeling`, `codebase-design`, `improve-codebase-architecture`, `to-spec`, `to-tickets`, `prototype`, `implement`, `tdd`, `diagnosing-bugs`, `code-review`, `resolving-merge-conflicts`, `wayfinder`.

Primary build flow:

```text
grill-with-docs / domain-modeling
  → to-spec
  → to-tickets
  → implement
  → code-review
```

`triage` handles incoming work. `improve-codebase-architecture` audits architectural friction. `wayfinder` handles multi-session work whose route is still under decision.

## Research — 16

`academic-writer`, `chinese-to-academic-english`, `engineering-research`, `experiment-designer`, `faithful-paper-translation`, `literature-research`, `literature-scout`, `manuscript-review`, `method-figure`, `paper-architect`, `research-critic`, `research-idea-refiner`, `result-figure`, `result-harvester`, `reviewer-response`, `scientific-figure`.

Lifecycle:

```text
Understand → Innovate → Prove → Communicate → Review → Respond
```

`reviewer-response` closes the post-review loop and routes substantive requests back to literature, experiments, architecture, or writing rather than treating every reviewer comment as prose editing.

## Presentation — 4

- `presentation-architect` — audience, narrative, slide roles, evidence/visual requirements.
- `slidev-scientific-presentation` — reproducible Slidev renderer.
- `powerpoint-presentation` — editable PPTX renderer.
- `presentation-review` — narrative/evidence/visual/delivery quality gate.

## Patent — 7

`codebase-patent-diff`, `cn-patent-invention-mining`, `patent-portfolio-planner`, `cn-patent-prior-art`, `cn-patent-drafting`, `cn-patent-review`, `autonomous-driving-patent`.

`patent-portfolio-planner` is used when multiple candidate inventions need split/merge, priority, overlap, and staged filing decisions.

## Productivity — 4

- `grill-me`
- `teach`
- `to-questionnaire`
- `wait-what`

`handoff` remains in `core` because every domain reuses it.

## Experimental — 2

- `retro` — turn session friction into durable environment improvements.
- `skill-audit` — audit skill boundaries, routing, self-containment, packs, and maintainability.

Experimental skills are deliberately excluded from `full`.
