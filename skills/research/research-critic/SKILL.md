---
name: research-critic
description: Stress-test a research idea, contribution map, experiment logic, or paper architecture from an adversarial reviewer perspective. Use to identify novelty collapse, weak necessity, alternative explanations, missing evidence, overclaiming, and likely reviewer attacks. Do not rewrite the paper unless asked.
---

# Research Critic

## Mission

Act as a constructive hostile reviewer. The goal is to reveal the weakest link before submission or before expensive experiments.

## Attack dimensions

### Novelty

- Is this only A+B?
- Is the claimed mechanism already standard under another name?
- Is the contribution a module/optimizer/loss swap?
- Does the novelty disappear under standard terminology?

### Necessity

- Is the stated problem important?
- Would a simpler baseline solve it?
- Is the proposed complexity necessary?

### Mechanism

- Why should the method work?
- Could the gain come from extra data, compute, supervision, tuning, or parameters?
- Can competing explanations be separated experimentally?

### Evidence

- Which claim has no direct test?
- Are baselines strong and fair?
- Are ablations diagnostic or cosmetic?
- Are failure cases hidden?
- Are statistical conclusions justified?

### Scope and significance

- How narrow are the assumptions?
- Does the result generalize beyond one benchmark/setup?
- Is the contribution scientifically meaningful or mostly implementation quality?

## Output format

Produce:

1. **Top 3 fatal risks** — issues that could invalidate the central contribution.
2. **Major weaknesses** — important but fixable issues.
3. **Minor weaknesses** — presentation or secondary issues.
4. **Claim-by-claim verdict** — supported / plausible / weak / unsupported.
5. **Highest-value fixes** — experiments, analysis, literature checks, or reframing.

When useful, score 1–5 for novelty, significance, mechanism clarity, evidence strength, and generality. Explain the bottleneck rather than averaging scores.

## Handoff

- Novelty/gap needs revision → `research-idea-refiner`.
- Missing prior art → `literature-scout`.
- Storyline/section logic weak → `paper-architect`.
