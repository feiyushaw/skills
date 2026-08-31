---
name: codebase-design
description: Shared vocabulary and principles for designing deep modules, clean seams, small interfaces, locality, leverage, and testability.
---

# Codebase Design

Design **deep modules**: substantial behavior behind a small interface, placed at a clean seam and testable through that interface.

## Vocabulary

- **Module**: anything with an interface and implementation.
- **Interface**: everything a caller must know to use the module correctly, including invariants/error modes/config/performance assumptions.
- **Implementation**: code hidden behind the interface.
- **Depth**: behavior/leverage delivered per unit of interface a caller must learn.
- **Seam**: a place where behavior can be altered/replaced without editing the caller.
- **Adapter**: a concrete implementation occupying a seam.
- **Leverage**: capability callers gain from one interface.
- **Locality**: change/knowledge/verification concentrated behind the interface.

Use this vocabulary consistently when discussing architecture.

## Principles

- Depth is a property of the interface, not line count.
- Apply the **deletion test**: if deleting a module makes complexity reappear across callers, the module was earning its keep; if complexity simply vanishes, it may have been pass-through ceremony.
- The interface is the natural test surface.
- One adapter is a hypothetical seam; multiple real adapters are stronger evidence the seam earns its cost.
- Accept dependencies instead of constructing them invisibly when replacement/testability matters.
- Return meaningful results instead of forcing side effects when practical.
- Prefer small surface area and hide complexity internally.

When comparing designs, deliberately produce multiple materially different interface shapes and compare them on depth, locality, seam placement, caller burden, and testability before committing to one.
