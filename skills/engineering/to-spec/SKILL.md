---
name: to-spec
description: Turn the current conversation and codebase understanding into an implementation-ready specification without re-interviewing the user about already settled decisions.
disable-model-invocation: true
---

# To Spec

Synthesize what is already known. Do not restart discovery or ask the user to repeat decisions already present in context.

## Process

1. Inspect the repository enough to understand current behavior and existing conventions.
2. Read `CONTEXT.md`, ADRs, and project instructions when present.
3. Identify the highest practical testing seams; prefer existing seams and a small number of public interfaces.
4. Surface only genuinely unresolved decisions that block a correct spec.
5. Write/publish the spec to the configured tracker if one exists; otherwise create a local Markdown spec.

## Spec structure

```markdown
## Problem Statement
## Solution
## User Stories
## Implementation Decisions
## Testing Decisions
## Out of Scope
## Further Notes
```

User stories describe externally meaningful behavior. Implementation Decisions record settled architecture/contracts without prematurely pinning fragile file paths. Testing Decisions define behavior and seams, not implementation-coupled tests.

Do not include speculative implementation detail merely to make the spec look complete. A prototype snippet may be retained only when it encodes a decision more precisely than prose.
