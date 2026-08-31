---
name: handoff
description: Create a compact, durable handoff for another agent or future session. Use when work will continue across context windows, machines, agents, or sessions and the next worker needs decisions, state, evidence, files, and next actions without replaying the full conversation.
---

# Handoff

## Mission

Compress the current working state into a durable continuation artifact.

## Required content

A useful handoff captures only continuation-critical information:

1. objective and current scope;
2. decisions already made and why they matter;
3. current repository/branch/artifact state;
4. important evidence, commands, file paths, issue/PR identifiers, or source links;
5. work completed;
6. unresolved decisions and blockers;
7. exact next actions;
8. constraints that must not be lost.

## Rules

- Prefer concrete state over narrative chronology.
- Preserve stable identifiers and exact names.
- Distinguish verified facts from hypotheses.
- Do not claim a command, experiment, merge, publication, or review occurred unless it actually occurred.
- Remove conversational filler that does not help continuation.

## Completion

A fresh agent should be able to read the handoff and continue safely without asking the user to reconstruct prior work.
