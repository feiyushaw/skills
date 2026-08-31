---
name: improve-codebase-architecture
description: Audit a codebase for high-value deepening opportunities and turn one selected opportunity into an architecture decision. Use when the user wants systematic architecture improvement, better test seams, reduced cross-file cognitive load, or improved agent navigability.
---

# Improve Codebase Architecture

Use `codebase-design` as the architecture vocabulary and `domain-modeling` for domain terms and ADRs.

## Goal

Find architectural changes that increase **depth**, **leverage**, and **locality** rather than performing cosmetic refactors.

## Scan

1. Determine scope from the user's pain point or recent-change hotspots.
2. Read `CONTEXT.md`, relevant ADRs, tests, and recent history.
3. Look for concrete friction:
   - one concept requires bouncing through many shallow modules;
   - callers must understand implementation details;
   - behavior is hard to test through a stable seam;
   - the same domain rule is duplicated across callers;
   - changes repeatedly require shotgun edits;
   - adapters or interfaces exist without real variation.
4. Apply the deletion test from `codebase-design` before recommending a new abstraction.

## Candidate report

For each serious candidate record:

```text
Area / domain concept
Current interface and implementation shape
Observed friction
Proposed deeper module / seam
What moves behind the interface
Expected leverage and locality
Testing improvement
Migration risk
Recommendation: strong / worth exploring / speculative
```

Use Mermaid or a compact before/after diagram when structure is easier to understand visually.

Do not propose exact interfaces until the user selects a candidate.

## Decision phase

For the selected candidate:

1. use `grilling` to resolve constraints and trade-offs;
2. update domain terminology through `domain-modeling`;
3. record an ADR only for durable, surprising, hard-to-reverse trade-offs;
4. hand off to `to-spec` when the architecture is settled.

## Guardrails

- recent pain and expected future change matter more than abstract cleanliness;
- prefer removing or deepening a seam over adding another layer;
- do not reopen an ADR without concrete new evidence;
- do not confuse a large refactor with architectural value.
