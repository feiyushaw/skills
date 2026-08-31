# Engineering Research Workflow

## Phase 0 — Research framing

Define:

- problem and scope;
- target scientific contribution;
- assumptions;
- central claims;
- closest competing explanations/methods;
- required novelty/prior-art review.

## Phase 1 — Baseline reproduction

For work extending prior methods:

- identify canonical implementation/checkpoint;
- reproduce representative published behavior;
- record environment and discrepancies;
- freeze a baseline configuration before introducing modifications.

A failed reproduction is a research result that must be explained, not silently bypassed.

## Phase 2 — Proposed method isolation

Map each proposed modification to a claim and expected mechanism. Avoid changing many unrelated variables simultaneously unless the experiment is explicitly an end-to-end system comparison.

## Phase 3 — Benchmark design

Select benchmarks that jointly test:

- nominal performance;
- difficult regimes;
- scaling;
- robustness;
- computational practicality.

Use synthetic/manufactured tests when they provide exact references, then include realistic benchmarks where external validity matters.

## Phase 4 — Evidence collection

Preserve:

- configs;
- commits;
- environment/dependency versions;
- raw outputs;
- seeds;
- logs;
- hardware;
- generated figures and scripts.

Do not manually transcribe numerical results when automated collection is feasible.

## Phase 5 — Evidence audit

For every claim:

1. locate the supporting experiment;
2. check baseline fairness;
3. check metric relevance;
4. check repeatability/uncertainty;
5. inspect counterexamples;
6. downgrade the claim if evidence is narrower than the wording.

## Phase 6 — Scientific communication

Build figures and tables from the claim-evidence map. Then hand the verified evidence package to the academic-writing/review workflow.

## Phase 7 — Reviewer attack

Before submission, attempt to falsify the work from at least these angles:

- novelty/prior art;
- unfair baseline;
- missing ablation;
- inadequate benchmark coverage;
- statistical weakness;
- hidden compute/data advantage;
- poor scaling;
- failure cases;
- mismatch between claim and evidence.

Turn valid attacks into experiments or limitations before polishing prose.
