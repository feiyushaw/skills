# Regression testing skills and workflows

The goal of regression testing in this repository is to protect **behavioral boundaries and handoffs** as skills evolve.

## Two layers

### 1. Static workflow contracts

Each `regressions/<id>/fixture.json` records a compact scenario with:

- workflow skill sequence;
- expected artifacts;
- required behaviors;
- forbidden behaviors;
- completion criteria.

`python3 scripts/validate-regressions.py` verifies the schema and ensures every referenced skill still exists. This catches renamed/deleted skills and malformed fixtures, but it does not evaluate model behavior.

### 2. Executable distribution smoke tests

`python3 scripts/smoke-test-distribution.py` installs packs into temporary directories using the real installer. It verifies:

- `full` resolves exactly the non-experimental skill set;
- dry-run writes nothing;
- repeated copy installation is safe by default;
- installed skills contain `SKILL.md`;
- `experimental` remains opt-in;
- symlink mode works in the Linux CI environment.

## Running an agent behavior regression

Render a fixture:

```bash
python3 scripts/show-regression.py research-claim-evidence
```

Then:

1. give the scenario and context to the agent;
2. make the listed skills available/invocable;
3. allow the workflow to complete without showing the expected checklist as hidden hints when doing a strict evaluation;
4. compare produced artifacts/actions against `required_behaviors`, `forbidden_behaviors`, and `completion_criteria`;
5. record the concrete failure mode if the workflow regresses.

The fixture is not a golden-answer prompt. Different valid wording and implementation choices are acceptable when the behavioral contract holds.

## When to add a fixture

Add or sharpen a fixture when:

- a real workflow failure exposes a missing guardrail;
- two skills start competing for the same job;
- a handoff loses important state;
- a skill begins inventing evidence, requirements, provenance, or results;
- a renderer changes domain meaning;
- a major refactor changes orchestration or invocation policy.

Prefer tightening a regression contract before adding more general instructions to every skill.

## Promotion policy

A high-risk stable workflow should have at least one fixture before being treated as mature. Experimental skills do not require fixtures initially, but repeated real-world use should produce fixtures before promotion into a stable pack.

`skill-audit` should treat missing regression coverage as a maintenance finding, especially for user-invoked orchestrators and workflows that can alter code, scientific claims, patent provenance, or published artifacts.
