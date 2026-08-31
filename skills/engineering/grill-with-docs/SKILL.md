---
name: grill-with-docs
description: Explicitly sharpen an engineering plan or design while maintaining domain vocabulary and durable architectural decisions. Use when the user wants a rigorous design interview and the repository has or should gain CONTEXT.md / ADR documentation.
---

# Grill With Docs

This is a thin user-invoked engineering workflow built from two shared disciplines:

1. use `grilling` to resolve the decision frontier;
2. use `domain-modeling` to capture canonical terms and durable trade-offs as they crystallize.

Do not duplicate either skill's logic here.

## Use when

- the design is not yet ready for `to-spec`;
- vocabulary is fuzzy or overloaded;
- important trade-offs need to be made with the user;
- the discussion is changing the domain model or producing ADR-worthy decisions.

## Workflow

```text
current design / question
  → grilling
  → domain-modeling updates inline
  → unresolved frontier
  → next grilling round
  → stable decision set
  → to-spec / prototype / implementation handoff
```

Facts that can be learned from the codebase or documentation are the agent's responsibility. Reserve user questions for decisions, priorities, constraints, and domain knowledge that cannot be inspected directly.

## Completion

Stop when the active decision frontier is empty enough for the next concrete artifact. Summarize the resolved decisions, remaining uncertainties, and the recommended next skill.
