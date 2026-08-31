---
name: resolving-merge-conflicts
description: Resolve an in-progress Git merge or rebase conflict hunk-by-hunk from the intent of both sides, then verify and finish the operation.
---

# Resolving Merge Conflicts

1. Inspect current merge/rebase state, history, and every conflicting file.
2. Find primary sources for both sides: commits, PRs, issues/specs, and surrounding code.
3. Resolve each hunk by intent. Preserve both intents where compatible; where incompatible, choose what matches the merge goal and record the trade-off. Do not invent unrelated behavior.
4. Discover and run the project's automated checks, typically static/type checks, focused tests, broader tests, then formatting as appropriate.
5. Stage resolved files and finish the merge/rebase through all remaining commits.

Do not use abort as a substitute for resolving the requested conflict unless the user explicitly changes the goal.
