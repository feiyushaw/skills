---
name: retro
description: Retrospect on an agent coding/work session and propose changes to the environment that make future sessions more reliable, cheaper, and easier to navigate. Experimental: recommendations should be reviewed before modifying global instructions.
---

# Retro

Retrospect on the specified session, defaulting to the current session when no other primary source is supplied.

Use `writing-for-agents` when proposing changes to agent-facing documentation.

## Improvement categories

Look for concrete evidence in:

- **Navigation** — time lost finding files, domain context, ownership, or entry points.
- **Automated checks** — mistakes that lint/type/test/schema checks could catch.
- **Review standards** — recurring defects better enforced during review.
- **Instruction pressure** — bloated or conflicting `AGENTS.md` / agent docs.
- **Tool economy** — repeated expensive calls or avoidable context loading.
- **No-op instructions** — rules that did not change behavior.
- **Information access** — missing logs, docs, APIs, fixtures, or read-only observability.
- **Skill routing** — work that repeatedly used the wrong skill or lacked a useful skill.

## Output

Rank recommendations by expected future value:

| Priority | Observed friction | Evidence | Proposed environment change | Expected benefit | Risk |
|---|---|---|---|---|---|

Prefer the lowest-complexity durable fix: automated check > review rule > navigation pointer > new long instruction.

Do not automatically rewrite global agent instructions from one anecdotal session. Separate one-off mistakes from recurring environmental problems.
