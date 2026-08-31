# Third-party notices

## mattpocock/skills

- Upstream: https://github.com/mattpocock/skills
- Snapshot used for the initial V1/V2 adaptation: `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`
- Author: Matt Pocock
- License: MIT
- Copyright: Copyright (c) 2026 Matt Pocock
- Preserved license text: `licenses/mattpocock-skills-MIT.txt`

The MIT license permits use, modification, merging, publication, distribution, sublicensing, and sale provided its copyright and permission notice are retained as required.

### Adapted reusable primitives / architecture

- `core/grilling`
- `core/handoff`
- `core/writing-for-agents`
- small composable skills
- user-invoked vs model-invoked separation
- decision frontier / persistent artifact patterns

### Adapted productivity skills

- `productivity/grill-me`
- `productivity/teach`
- `productivity/to-questionnaire`
- `productivity/wait-what`

### Adapted engineering skills

- `engineering/grill-with-docs`
- `engineering/triage`
- `engineering/domain-modeling`
- `engineering/codebase-design`
- `engineering/improve-codebase-architecture`
- `engineering/to-spec`
- `engineering/to-tickets`
- `engineering/prototype`
- `engineering/implement`
- `engineering/tdd`
- `engineering/diagnosing-bugs`
- `engineering/code-review`
- `engineering/resolving-merge-conflicts`
- `engineering/wayfinder`

### Experimental adaptations

- `experimental/retro`

The local versions intentionally remove Matt-specific setup, tracker configuration, personal routing assumptions, and environment-specific output requirements. They retain the reusable behavior and are adapted to this monorepo's self-contained skill and Codex invocation conventions.

Skills materially influenced by the upstream should retain this notice even after later local rewrites.
