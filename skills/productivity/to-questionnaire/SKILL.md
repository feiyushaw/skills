---
name: to-questionnaire
description: Turn a decision that depends on another person's knowledge into a focused Markdown discovery questionnaire.
disable-model-invocation: true
---

# To Questionnaire

Turn a knowledge gap into a document another person can answer asynchronously or in a meeting.

## Principle

**Grill the send, not the subject.** The user cannot answer the missing domain facts; ask only what they can know: who the recipient is and what must come back.

## Workflow

1. Identify recipient role, expertise, relationship, and context they already know.
2. Identify the exact facts/decisions the user needs back.
3. Write a questionnaire ordered by importance.
4. Cover every needed output with at least one question.

## Document structure

```markdown
# <Questionnaire title>

**Purpose:** <decision this supports>
**From:** <user>
**To:** <recipient role/name if provided>
**How answers will be used:** <downstream use>

## Context
<one concise orienting paragraph>

## How to answer
<deadline/effort if known; partial answers and uncertainty are useful>

## <Theme>
### <one question, one idea>
_Why this matters: ..._   # only when useful

>

## Anything else?
Anything we did not ask that we should know?
```

Do not ask compound questions when separate answers could matter.
