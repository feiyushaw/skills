# Workflow regression fixtures

These fixtures protect **behavioral contracts**, not exact wording.

A fixture describes:

- the user scenario;
- the skill sequence expected to handle it;
- required artifacts and behaviors;
- forbidden behaviors that represent a regression;
- completion criteria.

The repository validator checks fixture structure and referenced skill names. It does **not** pretend that static validation proves an LLM will follow the workflow. For agent evaluation, run the scenario through the listed workflow and score the result against the required/forbidden behavior lists.

## Current critical fixtures

- `engineering-grill-to-spec`
- `engineering-debug-feedback-loop`
- `research-claim-evidence`
- `research-reviewer-response`
- `patent-provenance-negative-control`
- `presentation-architecture-render-review`

## Principles

1. Test semantic behavior, not prose style.
2. Include negative controls where hallucinating a plausible answer would be harmful.
3. Keep fixtures small enough to understand without loading an entire project.
4. When a production failure reveals a new class of regression, add or sharpen a fixture before adding more instructions.
5. Prefer one fixture per high-risk handoff or workflow boundary.

See `docs/regression-testing.md` for the evaluation workflow.
