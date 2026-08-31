---
name: domain-modeling
description: Actively build and sharpen a project's domain vocabulary, scenarios, CONTEXT.md glossary, and durable architectural decisions.
---

# Domain Modeling

Use when the domain model itself is changing, not merely when another skill reads existing vocabulary.

## Persistent artifacts

Use `CONTEXT.md` as a glossary of domain concepts and relationships, free of implementation detail. If the repository genuinely has multiple bounded contexts, use a small `CONTEXT-MAP.md` pointing to context-specific glossaries. Store durable architectural decisions as ADRs under an existing project convention (commonly `docs/adr/`).

Create artifacts lazily when the first real content exists.

## Discipline

- Challenge user language that conflicts with the established glossary.
- Sharpen vague or overloaded nouns into canonical concepts.
- Stress-test relationships with concrete edge-case scenarios.
- Compare stated behavior against code and surface contradictions.
- Update the glossary when a term is actually resolved.

## ADR threshold

Create/offer an ADR only when a decision is:

1. meaningfully hard to reverse;
2. surprising without historical context;
3. the result of a genuine trade-off among alternatives.

An ADR should capture context, decision, important alternatives, consequences, and status. Do not turn every implementation choice into an ADR.
