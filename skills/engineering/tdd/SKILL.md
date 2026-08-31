---
name: tdd
description: Use red-green test-driven development for features and bug fixes, testing behavior through agreed public seams rather than implementation details.
---

# Test-Driven Development

TDD is a tight **red → green** feedback loop.

## Tests worth keeping

Test externally meaningful behavior through public interfaces. Expected values should come from an independent source of truth: spec, worked example, known-good literal, reference solution, or accepted behavior.

Avoid:

- implementation-coupled tests of private methods/internal collaborators;
- tautological expectations that recompute the implementation;
- horizontal “write all tests, then all code” phases.

## Seams

A seam is where behavior can be observed or replaced without reaching into internals. Before significant test work, identify the seams that matter. Prefer the highest stable interface that still gives a tight feedback loop.

When interface shape itself is the design question, consult `codebase-design`.

## Loop

1. Select one small behavior slice at one seam.
2. Write a test that fails for the intended reason.
3. Run it and observe red.
4. Add only enough implementation for green.
5. Run the focused test again.
6. Continue with the next behavior slice.

Keep the loop fast and deterministic. Broader refactoring/design cleanup belongs after behavior is locked down rather than being mixed invisibly into each cycle.
