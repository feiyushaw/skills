---
name: workflow-router
description: Route a user's work request to the smallest suitable skill or skill sequence in this repository. Use when the user asks which workflow to use, invokes a general work request without a clear skill, or wants to discover available capabilities. Do not perform the full downstream workflow unless explicitly asked.
---

# Workflow Router

## Mission

Identify the user's current job category and recommend the smallest useful next skill or short skill sequence.

This is a router, not a super-agent.

## Routing process

1. Identify the primary work product: code, research artifact, presentation, patent artifact, or general productivity task.
2. Identify the current stage. Prefer the skill that starts at the user's actual stage rather than restarting an entire lifecycle.
3. Inspect `docs/catalog.md` when available to distinguish implemented from planned skills.
4. Recommend one primary skill. Add a short sequence only when the handoff between stages is already clear.
5. State why the selected skill fits and what artifact it should produce.

## Default routes

```text
software feature / repository change
  -> engineering workflow

research direction / literature / paper / experiments
  -> research workflow

slides / talk / scientific or business presentation
  -> presentation workflow

patent mining / prior art / drafting / review
  -> patent workflow
```

## Constraints

- Do not pretend a planned skill is installed.
- Do not launch multiple expensive workflows merely because they might eventually be useful.
- Do not replace domain-specific reasoning with router logic.
- When the user already names a precise skill that fits, route directly to it.

## Completion

Stop when the user has a concrete next skill or short workflow and understands the expected output.
