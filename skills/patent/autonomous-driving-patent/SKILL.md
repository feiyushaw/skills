---
name: autonomous-driving-patent
description: Lightweight domain guidance for mining Chinese invention-patent candidates from autonomous-driving software systems, especially framework, platform, data-loop, evaluation, simulation, tooling, and engineering infrastructure.
---

# Autonomous-Driving Patent Domain Guidance

Use this as a lightweight domain layer together with the generic patent-mining workflow. It must not steer invention mining toward particular planning, control, perception, learning, or optimization algorithms.

## Core principle

Start from the applicant's actual code and design. Let the implementation determine where the invention is.

For many autonomous-driving engineering repositories, the protectable contribution may be framework-level rather than algorithm-level. Examples include data closed loops, evaluation platforms, simulation infrastructure, workflow orchestration, cross-module state management, automated diagnosis, version traceability, scenario-processing pipelines, and scalable engineering mechanisms.

Do not assume that an algorithm is more patent-worthy than a framework mechanism.

## What to reconstruct

Inspect the repository and identify, only when present:

- system inputs and outputs;
- module boundaries and interfaces;
- data and control flow;
- persistent state and lifecycle state;
- online/offline boundaries;
- feedback paths;
- orchestration and scheduling;
- storage, indexing, synchronization, caching, and version relationships;
- failure detection, diagnosis, recovery, and fallback;
- evaluation and validation flow;
- human-in-the-loop boundaries;
- external system integration;
- technical downstream actions.

These are discovery dimensions, not a required architecture.

## Framework-level invention mining

Pay particular attention to engineering mechanisms that solve a concrete technical problem across modules or lifecycle stages, for example:

- automatically connecting evaluation results to source data and subsequent processing;
- closing a feedback loop between testing, failure discovery, data selection, processing, training, deployment, or regression;
- maintaining reproducible relationships among data, software, model, map, configuration, and evaluation versions;
- synchronizing heterogeneous data or state across modules and time bases;
- reducing repeated computation, storage, bandwidth, latency, or manual processing through a specific system mechanism;
- automatically locating, classifying, routing, or reproducing technical failures;
- coordinating distributed or large-scale autonomous-driving data processing;
- preserving scenario or state consistency across simulation, evaluation, replay, and data processing;
- providing a technical state machine or lifecycle mechanism that changes subsequent system processing.

Treat these only as prompts for inspection. Never manufacture one merely because it appears in this list.

## Data closed-loop test

Do not call a pipeline a closed loop merely because several stages are connected.

For a claimed closed-loop mechanism, identify:

1. what technical result or state is produced by an earlier stage;
2. how that result is converted into a feedback state, selection, configuration, trigger, or processing instruction;
3. which subsequent technical operation changes because of that feedback;
4. what new result is generated after the change;
5. whether the implementation contains an actual repeatable feedback relation.

If the system is only a one-way ETL or reporting pipeline, describe it accordingly.

## Abstraction rule

Generalize from implementation without replacing it with vague platform language.

Use this ladder:

```text
specific code / service / table / job
    -> functional module
    -> cross-module technical relationship
    -> system-level technical mechanism
    -> claim terminology
```

The novelty center may lie in a relationship between otherwise known components. Preserve that relationship explicitly.

## Algorithm neutrality

Algorithms may appear in the repository, but this domain skill must not preselect any specific algorithm family as an invention target.

When an algorithm is third-party, published, inherited, or conventional:

- record it as technical context or prior art;
- avoid presenting the algorithm itself as the applicant's contribution;
- inspect whether the applicant created a new system-level use, interface, feedback relation, lifecycle mechanism, or engineering architecture around it;
- include algorithm details in a claim only when they are necessary to support the actual invention.

Do not maintain lists of favored planning, control, topology, optimization, neural-network, or simulation algorithms in this skill.

## Evidence useful for framework patents

Prefer concrete engineering evidence such as architecture diagrams, service/module interfaces, database/artifact relationships, workflow definitions, state-transition definitions, configuration propagation, job scheduling/dependency logic, version/lineage metadata, test/evaluation traces, failure examples, operational measurements, and commit/PR history explaining why a framework mechanism was introduced.

Quantitative evidence is useful when available but must never be invented.

## Candidate decomposition

A large platform should not automatically become one omnibus patent. Split candidates according to independently protectable technical mechanisms. Conversely, do not split every service or module into a separate patent merely because the code is modular.

For each candidate ask what concrete technical problem is solved, what cross-module or lifecycle mechanism solves it, which relationships are essential, whether the mechanism can operate independently, what evidence supports it, and what technical effect follows.

## Repository-scale output

| ID | Framework mechanism | Technical problem | Essential relationship | Evidence | Technical effect | Prior-art pressure | Priority |
|---|---|---|---|---|---|---|---|

The table must be derived from inspected implementation evidence rather than populated from a predefined taxonomy.

## Avoid

Reject vague labels such as “建立自动驾驶数据闭环平台”, “通过AI提高数据处理效率”, “构建自动驾驶评测系统”, “自动发现问题数据”, or “对多个模块进行统一管理”. Continue inspecting until the concrete data/state/control relationship that realizes the result is identified.

## Relationship to generic skills

This file supplies autonomous-driving vocabulary and framework-level inspection guidance only. Generic patent skills remain responsible for provenance, candidate mining, prior-art search, drafting, and review.
