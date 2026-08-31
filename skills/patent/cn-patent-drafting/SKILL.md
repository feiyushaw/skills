---
name: cn-patent-drafting
description: Draft Chinese invention-patent technical disclosures, claim architectures, specifications, abstracts, and figure plans from a selected invention candidate and prior-art analysis.
---

# CN Patent Drafting

Use only after the technical mechanism is reconstructed and, when feasible, first-pass prior art is complete. Use `references/cnipa-baseline.md` as a working baseline and verify current CNIPA sources before filing-quality output.

## Drafting objective

Produce a filing-oriented engineering draft that a Chinese patent professional can review efficiently. Preserve support for broad claims while documenting concrete embodiments sufficiently.

## Mandatory drafting order

1. invention nucleus;
2. claim architecture;
3. terminology normalization;
4. specification support map;
5. technical disclosure/specification draft;
6. abstract and figures;
7. internal consistency check.

Do not begin with long background prose.

## Claim architecture

For supported software/system inventions consider method, apparatus/system/device, computer-readable storage medium, and computer program product forms when appropriate under current practice.

Independent claims should contain the minimum interacting feature set producing the technical effect. Avoid unnecessary framework/library/model names, exact thresholds, network depth, vehicle/dataset names, database/file formats, implementation language, or unnecessary ordering.

Use dependent claims for meaningful fallback variants including state representations, triggers, confidence/uncertainty, temporal aggregation, agent-response models, distributed execution, caching/index/scheduling, fallback logic, calibration/update, and scenario-specific embodiments.

## Specification support map

| Claim feature | Support section | Embodiment | Alternative wording | Evidence source |
|---|---|---|---|---|

Every material claim term needs support.

## Technical disclosure structure

```markdown
# 发明名称
## 一、技术领域
## 二、背景技术
## 三、现有技术存在的技术问题
## 四、发明目的
## 五、技术方案
## 六、有益效果
## 七、附图说明
## 八、具体实施方式
## 九、可替代实施方式
## 十、建议保护点与权利要求架构
```

Full mode additionally includes 权利要求书、说明书、说明书摘要、摘要附图建议.

## AI/software disclosure requirements

When material, describe technical origin of inputs, state variables, processing dependencies, algorithm/model modules, training/inference/update, key parameters/classes, outputs/downstream actions, interaction between algorithm and system features, failure handling, and at least one concrete implementation path.

## Technical-effect discipline

Tie each benefit to a feature combination. Never invent quantitative improvements; if measurements exist, cite their source in internal notes.

## Figure plan

Typical useful figures: overall architecture, data flow, method flowchart, state-transition/feedback, key sub-flow, deployment topology, scenario timeline.

## Output package

```text
<Candidate-ID>/
  invention-summary.md
  claim-tree.md
  disclosure.md
  specification-draft.md
  abstract.md
  figures.md
  support-matrix.md
  open-questions.md
```

Mark output as an engineering draft pending professional patent review; do not guarantee grantability, validity, non-infringement, or FTO.
