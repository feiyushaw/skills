# Adversarial Research Stress Test

Attack the idea before expensive experiments or writing.

## Novelty

- Is this only A+B, a module/loss/optimizer swap, or engineering integration?
- Does novelty disappear when standard terminology is used?
- Is the same mechanism already known under another formulation?

## Necessity

- Is the stated problem scientifically or practically important?
- Would a simpler baseline solve it?
- Is added complexity actually necessary?

## Mechanism

- Why should the method work?
- Could gains instead come from more data, compute, parameters, privileged information, preprocessing, or tuning?
- Can competing explanations be separated experimentally?

## Evidence

- Which central claim has no direct test?
- Are baselines strong and fair?
- Are ablations diagnostic rather than cosmetic?
- What failure/boundary cases could overturn the claim?

## Scope and significance

- How narrow are the assumptions?
- Does the result generalize beyond one benchmark or configuration?
- Is the contribution new scientific knowledge or mostly implementation quality?

## Output

Record top fatal risks, major weaknesses, claim-by-claim verdicts, and the highest-value fixes. A valid stress test may recommend abandoning or narrowing the idea.
