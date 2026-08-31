---
name: wayfinder
description: Plan work too large or uncertain for one agent session as a persistent map of decision tickets, dependencies, resolved decisions, and still-unclear fog.
disable-model-invocation: true
---

# Wayfinder

Use for efforts where the destination is meaningful but the route cannot yet be represented as an implementation plan.

Wayfinder manages **decision tickets**, not build tickets. Once the route is clear, hand off to `to-spec` / `to-tickets` / the relevant domain workflow.

## Map

Maintain one canonical map (tracker issue when configured, otherwise local Markdown):

```markdown
## Destination
<what must be clear/decided when wayfinding is done>

## Notes
<standing constraints and skills/domain context>

## Decisions so far
- <decision name>: <one-line gist + pointer to full resolution>

## Not yet specified
<in-scope fog that cannot yet be phrased as a precise ticket>

## Out of scope
<explicitly excluded work>
```

## Tickets and frontier

Each decision ticket contains one precise question and explicit blockers. The **frontier** is the set of open decisions whose blockers are resolved. Keep unknown future territory in `Not yet specified` until it can be phrased precisely.

Useful ticket modes:

- research — acquire an external fact;
- prototype — make a cheap artifact to decide behavior/shape;
- grilling — resolve a human decision;
- task — perform prerequisite work solely to unblock a decision.

## Charting

1. Use `grilling` and `domain-modeling` to name the destination.
2. Explore breadth-first to identify current decision frontier and fog.
3. If everything already fits one session, stop: no map is needed.
4. Create currently specifiable tickets and wire blockers.
5. Record fog without pretending it is already understood.

## Working the map

In each session, load the low-resolution map, choose/claim one frontier decision, resolve it with the appropriate skill, record the resolution, update `Decisions so far`, and graduate newly clarified fog into tickets.

Do not resolve multiple unrelated decision tickets in one session merely to empty the map faster. The map is complete when the way to the destination is clear, not when implementation is finished.
