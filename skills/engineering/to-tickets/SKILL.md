---
name: to-tickets
description: Break a plan or spec into tracer-bullet vertical slices with explicit blocking dependencies and acceptance criteria.
disable-model-invocation: true
---

# To Tickets

Convert a plan/spec into **tracer-bullet tickets**: narrow but complete, independently verifiable paths through the system.

## Rules

- Prefer vertical behavior slices over layer tickets such as “database”, “backend”, “frontend”, “tests”.
- A completed ticket is demoable or verifiable on its own.
- Size each ticket for one fresh agent context when practical.
- Record explicit blockers. Tickets with all blockers completed form the **frontier**.
- Put enabling prefactors first when they make later changes substantially easier.

## Wide refactor exception

When one mechanical change has a broad blast radius and cannot land green as vertical slices, use **expand–contract**:

1. expand: add the new form beside the old;
2. migrate callers in bounded batches;
3. contract: remove the old form after all migrations.

## Drafting workflow

1. Read the source plan/spec and relevant codebase context.
2. Draft tickets and blocker graph.
3. Present title, blocked-by, deliverable, and acceptance criteria.
4. Ask only if granularity/dependency decisions genuinely require user input.
5. Publish to the configured tracker; if none exists, write one Markdown file per ticket under a local work directory.

Do not force file paths into tickets when they are likely to go stale. Keep the ticket centered on behavior and acceptance criteria.
