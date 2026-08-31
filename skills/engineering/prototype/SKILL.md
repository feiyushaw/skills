---
name: prototype
description: Build deliberately throwaway code or artifacts to answer one design question quickly before production implementation.
---

# Prototype

A prototype is **throwaway work that answers a question**. The question decides its shape.

Typical branches:

- logic/state question → build the smallest executable harness or interactive representation that exposes state transitions;
- UI/interaction question → build multiple meaningfully different variants that can be compared quickly;
- architecture/interface question → make the competing designs concrete enough to compare behavior and consequences.

## Rules

1. Mark it clearly as a prototype.
2. Make it trivial to run or inspect.
3. Avoid persistence and production infrastructure unless they are the question being tested.
4. Skip production polish, exhaustive tests, and abstractions.
5. Surface relevant state/behavior so the decision is observable.
6. Capture the **answer** the prototype established.
7. Production code receives the validated decision, not accidental prototype structure.

Delete or isolate throwaway artifacts after the decision unless they are intentionally preserved as a primary source on a non-production branch.
