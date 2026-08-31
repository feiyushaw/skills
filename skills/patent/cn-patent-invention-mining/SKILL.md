---
name: cn-patent-invention-mining
description: Mine patentable technical inventions from running software, source code, architecture documents, experiments, and engineering workflows for Chinese invention patents, especially AI and software systems.
---

# CN Patent Invention Mining

Use this skill when the user has an implemented or partially implemented technical system and wants to identify what should be protected by Chinese invention patents before drafting claims.

Use `references/cnipa-baseline.md` as a working examination baseline and verify current CNIPA sources before filing-quality output.

## Mandatory provenance gate

Before mining inventions from a repository, determine whether the target is a fork, derivative work, paper-associated implementation, vendor SDK integration, or a system assembled from public components. If any apply, use `codebase-patent-diff` first.

Preserve provenance labels. Items classified `UPSTREAM_PRIOR_ART`, `THIRD_PARTY_PRIOR_ART`, `COMMON_ENGINEERING`, `EXCLUDE`, or `BACKGROUND_ONLY` must not be promoted unless new contrary evidence is explicitly recorded. A correct result may be that no material user delta exists.

## Core principle

Do not start by writing claims. First reconstruct:

1. engineering problem before the invention;
2. concrete mechanism introduced;
3. measurable/explainable technical effect;
4. minimum feature combination causing that effect;
5. optional implementation details that should not unnecessarily narrow protection.

For software/AI inventions, tie algorithms to technical data, system state, computing behavior, sensing/simulation/control processes, or other concrete technical mechanisms.

## Inputs to inspect

Prefer source code/configuration, architecture/design docs, tests/evaluation scripts, experiments, commit/PR history explaining design changes, then papers/slides/notes/user explanation. Never infer a feature from a filename when implementation can be inspected.

## Workflow

### Stage 0 — Provenance and exclusion map

Import disclosure timeline, Patent Provenance Matrix, excluded/background mechanisms, eligible user deltas, and unresolved provenance questions from `codebase-patent-diff` when applicable.

### Stage 1 — System reconstruction

Map inputs, modules/interfaces, retained state, control/data flow, offline/online and open/closed-loop boundaries, failure/fallback paths, outputs, and downstream technical use. Mark inherited/background modules separately.

### Stage 2 — Change-point mining

Locate user-introduced mechanisms such as custom state representations, feedback paths, evaluators, adaptive thresholds/confidence fusion, active sampling, interactive simulation response, replay/counterfactual generation, synchronization/indexing/caching/scheduling/distributed execution, fault attribution, uncertainty-aware planning/evaluation, or mechanisms reducing compute/memory/bandwidth/latency/errors. A diff proves change, not inventiveness.

### Stage 3 — Candidate decomposition

Create independent candidate cards when feature groups solve distinguishable technical problems. Each candidate gets a stable ID.

```markdown
# <ID> <candidate title>
## Provenance boundary
## Technical problem
## Existing engineering limitation
## Core technical mechanism
## Minimum essential features
## Optional / dependent features
## Technical effect
## Evidence in implementation
## Alternative embodiments
## Likely prior-art pressure
## Recommended protection forms
## Filing priority
## Open questions
```

### Stage 4 — Essential-feature test

For every proposed independent-claim feature, test whether removal preserves the effect, whether it is mechanism vs parameter, whether it can be generalized above code/framework/file/vendor details without losing support, and whether it is actually user delta or inherited context.

### Stage 5 — Combination-invention test

Identify the user-added coupling: information crossing boundaries, state/hypothesis updates, feedback modifying later computation/simulation/evaluation/control, the technical effect of coupling, and whether side-by-side use would yield the same effect.

### Stage 6 — Evidence traceability

| Candidate | Feature | Provenance | Code/doc evidence | Technical effect evidence | Confidence |
|---|---|---|---|---|---|

## China-specific screening

Check technical subject matter, novelty risk, inventive-step story, and sufficient disclosure. For AI-related inventions capture material model/module relationships, training/inference flow, key parameter/loss construction, input/output definitions, and relationship to the concrete technical scene.

## Output priorities

Rank by business/technical importance, reverse-engineering ease, product lifetime, breadth, evidence quality, prior-art density, and infringement detectability. Use `P0`, `P1`, `P2`.

## Negative-control behavior

Use `examples/guidance-planner/provenance-regression.md` to check that known upstream mechanisms do not become applicant inventions.

## Handoff

After candidate selection, use `cn-patent-prior-art` before final claim drafting. Preserve candidate ID, provenance boundary, and evidence links downstream.
