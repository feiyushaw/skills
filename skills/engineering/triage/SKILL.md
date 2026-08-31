---
name: triage
description: Triage repository issues and external pull requests into verified, actionable states. Use when the user wants to inspect incoming work, reproduce reported bugs, reject duplicates, request missing information, or produce an agent-ready implementation brief.
---

# Triage

Turn incoming issues and external pull requests into a small set of explicit states instead of leaving them as ambiguous requests.

## Canonical roles

Category:

- `bug`
- `enhancement`

State:

- `needs-triage`
- `needs-info`
- `ready-for-agent`
- `ready-for-human`
- `wontfix`

If the repository uses different label names, map these concepts to the local vocabulary rather than forcing new labels.

## Workflow

1. Read the full issue or PR, including discussion and existing labels.
2. Inspect relevant code, `CONTEXT.md`, ADRs, and project standards.
3. Check whether the requested behavior already exists or was previously rejected.
4. Verify the report before interviewing anyone:
   - bug: reproduce the reported symptom where practical;
   - PR: inspect the diff and run the smallest relevant checks;
   - enhancement: verify the current limitation in the codebase.
5. Recommend category + state with evidence.
6. If the request is underspecified, use `grilling` and `domain-modeling`; do not re-ask facts that can be inspected.
7. Produce the appropriate outcome.

## Agent-ready brief

For `ready-for-agent`, write a compact brief containing:

```text
Problem
Verified current behavior
Desired behavior
Relevant domain/context
Acceptance criteria
Testing seam / verification command
Constraints / out of scope
Pointers to primary sources
```

Avoid detailed implementation instructions unless the design is already settled. The brief should describe the behavior and evidence needed, not micromanage file edits.

## Completion

Every triaged item should end with a clear state and the evidence or missing information required to move it forward.
