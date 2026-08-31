---
name: implement
description: Implement an approved spec or ticket set with focused testing, regular verification, and final code review.
disable-model-invocation: true
---

# Implement

Implement the approved work on the current branch.

- Respect the spec/ticket acceptance criteria and existing project instructions.
- Use `tdd` at pre-agreed seams when appropriate.
- Work through the dependency frontier rather than bypassing blockers.
- Run focused tests and type/static checks regularly.
- Run the appropriate broader test suite at the end.
- Use `code-review` before declaring completion.
- Commit coherent work when repository workflow permits.

Do not silently expand scope. If implementation exposes a decision that invalidates the spec, surface it and update the authoritative artifact rather than burying the change in code.
