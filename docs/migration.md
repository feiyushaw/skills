# Migration Plan

## Safety gate

At bootstrap time, `feiyushaw/skills` is public while the source repositories `academic_skills`, `patent_skills`, and `presentation_skill` are private. Do not copy their contents into this repository until publication has been explicitly approved or the destination visibility has been changed.

This bootstrap PR therefore records target mappings without migrating private content.

## Phase 1 — Bootstrap

- establish repository architecture;
- create `core` primitives;
- define invocation and authoring rules;
- add pack manifests;
- add validation CI;
- document third-party provenance.

## Phase 2 — Domain migration

### Research

Source: `feiyushaw/academic_skills`

Target: `skills/research/`

Planned skill mapping includes:

- `literature-research`
- `literature-scout`
- `faithful-paper-translation`
- `research-idea-refiner`
- `research-critic`
- `experiment-designer`
- `result-harvester`
- `scientific-figure`
- `result-figure`
- `paper-architect`
- `chinese-to-academic-english`
- `academic-writer`
- `manuscript-review`

Migration rule: preserve the existing Understand -> Innovate -> Prove -> Communicate -> Review lifecycle and claim-evidence discipline. Reuse `core` only for genuinely generic behavior.

### Patent

Source: `feiyushaw/patent_skills`

Target: `skills/patent/`

Planned skills:

- `codebase-patent-diff`
- `cn-patent-invention-mining`
- `cn-patent-prior-art`
- `cn-patent-drafting`
- `cn-patent-review`
- `autonomous-driving-patent`

Migration rule: preserve provenance as a mandatory gate. Do not weaken the distinction between upstream prior art, common engineering, user modification, and potential invention.

### Presentation

Source: `feiyushaw/presentation_skill`

Target: `skills/presentation/`

Planned skills:

- existing `slidev-scientific-presentation`;
- new `presentation-architect` for tool-independent storyline and slide planning;
- future `powerpoint-presentation` renderer;
- future `presentation-review` quality gate.

Migration rule: separate presentation reasoning from rendering technology.

## Phase 3 — Engineering foundation

Selectively adapt high-value engineering patterns from `mattpocock/skills`, with attribution:

- `grilling` / `grill-with-docs`
- `domain-modeling`
- `codebase-design`
- `to-spec`
- `to-tickets`
- `prototype`
- `implement`
- `tdd`
- `diagnosing-bugs`
- `code-review`
- `resolving-merge-conflicts`
- `wayfinder`

Do not import upstream skills blindly. Adapt naming, artifact conventions, Codex metadata, and integration points to this repository.

## Phase 4 — Integration

- finalize pack installer;
- add catalog generation;
- add skill dependency checks;
- add regression examples for high-value workflows;
- document recommended workflows by job type.

## Phase 5 — Legacy repository retirement

Only after migrated skills are stable:

1. update legacy README files with the new canonical location;
2. keep historical commit provenance accessible;
3. optionally archive old repositories;
4. do not delete source repositories merely to make the monorepo canonical.

## Migration record format

For each migrated skill record:

```text
source repository
source commit SHA
source path
destination path
visibility approval
content changes
third-party provenance, if any
validation status
```
