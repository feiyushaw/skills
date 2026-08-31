---
name: code-review
description: Review a diff along two independent axes: repository standards/design quality and fidelity to the originating specification or request.
---

# Code Review

Review the same diff on two separate axes so one cannot mask the other.

## Axis 1 — Standards

Check repository instructions (`AGENTS.md`, `CONTRIBUTING`, coding standards, ADRs) and apply design judgement to the changed code. Look for unclear naming, duplication, data clumps, primitive obsession, repeated conditionals, shotgun surgery, divergent responsibilities, speculative generality, message chains, middle-man layers, and other maintainability risks.

Tool-enforced formatting/lint findings need not be manually duplicated.

## Axis 2 — Spec

Find the originating issue/spec/request when available and check:

- required behavior missing or partial;
- behavior implemented incorrectly;
- scope creep not requested;
- acceptance criteria without evidence.

If no spec exists, say so rather than reconstructing one from the implementation.

## Process

1. Pin the comparison point and inspect the complete diff/commit list.
2. Identify standards sources and spec source.
3. Review the two axes independently; parallel subagents are useful when available.
4. Report them separately under `Standards` and `Spec`.
5. End with counts/severity within each axis, not one blended score.

A change may satisfy the spec while violating project standards, or be beautifully written while implementing the wrong thing. Preserve that distinction.
