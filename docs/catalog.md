# Skill Catalog

The V1 catalog contains 42 skills across six active domains.

## Core — 4

| Skill | Invocation | Role |
|---|---|---|
| `workflow-router` | user | route a task to the right workflow |
| `grilling` | model/user | reusable decision-tree/frontier interview discipline |
| `handoff` | model/user | compact durable cross-agent/session handoff |
| `writing-for-agents` | model/user | write effective agent-consumed instructions/docs |

## Engineering — 11

`domain-modeling`, `codebase-design`, `to-spec`, `to-tickets`, `prototype`, `implement`, `tdd`, `diagnosing-bugs`, `code-review`, `resolving-merge-conflicts`, `wayfinder`.

The primary flow is `grilling/domain-modeling → to-spec → to-tickets → implement → code-review`. `wayfinder` handles work whose route is not yet clear enough for a spec.

## Research — 15

`academic-writer`, `chinese-to-academic-english`, `engineering-research`, `experiment-designer`, `faithful-paper-translation`, `literature-research`, `literature-scout`, `manuscript-review`, `method-figure`, `paper-architect`, `research-critic`, `research-idea-refiner`, `result-figure`, `result-harvester`, `scientific-figure`.

Lifecycle: `Understand → Innovate → Prove → Communicate → Review`.

## Presentation — 2

- `presentation-architect` — tool-independent audience/storyline/slide architecture.
- `slidev-scientific-presentation` — reproducible Slidev renderer for scientific/technical decks.

Planned extensions: PowerPoint/PPTX renderer and presentation-review quality gate.

## Patent — 6

`codebase-patent-diff`, `cn-patent-invention-mining`, `cn-patent-prior-art`, `cn-patent-drafting`, `cn-patent-review`, `autonomous-driving-patent`.

## Productivity — 4

- `grill-me` — explicit thin wrapper over `grilling`.
- `teach` — persistent multi-session learning workspace.
- `to-questionnaire` — async discovery questionnaire generator.
- `wait-what` — context-aware re-pitching.

`handoff` remains in `core` because all domains reuse it.
