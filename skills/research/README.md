# Research Skills 使用说明

Research scope 覆盖一项科研工作从理解领域、形成创新、设计证据、整理结果、论文表达、投稿前审查到 Reviewer Response 的完整生命周期。

顶层 Skill 只保留能独立成为用户任务入口的能力。实验设计、novelty scout、idea stress-test 等子步骤已经收进对应主 Skill，不再作为并列入口。

## 完整生命周期

```text
Understand
  ↓
literature-research
  ↓
Innovate
  ↓
research-idea-refiner
  ↓
Prove
  ↓
engineering-research
  ↓
result-harvester
  ↓
Communicate evidence
  ├─ method-figure
  └─ result-figure
  ↓
Structure
  ↓
paper-architect
  ↓
Write / Translate
  ├─ academic-writer
  └─ academic-translation
  ↓
Review
  ↓
manuscript-review
  ↓
Respond
  ↓
reviewer-response
```

核心约束始终是：

```text
Contribution → Claim → Required Evidence → Experiment / Analysis
→ Figure / Table → Paper Section
```

## 11 个 Skill 怎么选

| 生命周期 | Skill | 什么时候使用 | 主要产物 |
|---|---|---|---|
| Understand | `literature-research` | 需要理解领域，或检查一个具体 idea 的 closest work / novelty threat | literature map、taxonomy、positioning table、gap evidence |
| Innovate | `research-idea-refiner` | 想法还在形成，novelty、mechanism、significance 或 scope 不稳定 | idea canvas、contribution map、claims、stress test |
| Prove | `engineering-research` | 贡献基本稳定，需要设计实验/基线/ablation/benchmark 或审计证据 | research plan、experiment matrix、claim-evidence table |
| Evidence ops | `result-harvester` | 实验已跑但结果散落，需要统一 provenance、run、metric、failure | normalized evidence package |
| Explain method | `method-figure` | Figure 1、方法图、机制图、流程图、架构图、graphical abstract | editable conceptual figure contract/master |
| Show evidence | `result-figure` | 曲线、bar/point、ablation、robustness、scaling、uncertainty、failure plot | claim-first quantitative figure |
| Structure paper | `paper-architect` | 贡献和证据已有，需要决定论文故事、章节、idea placement、图表角色 | paper blueprint、section map |
| Write paper | `academic-writer` | blueprint 与证据稳定，需要写/改 Abstract、Introduction、Method、Results 等 | manuscript prose |
| Translate | `academic-translation` | EN→ZH 忠实阅读翻译，或 ZH→EN 论文翻译 | fidelity-preserving translated text |
| Pre-submit | `manuscript-review` | 论文接近完成，需要找 rejection risk | fatal/major/minor risks + revision queue |
| Post-review | `reviewer-response` | 已收到 Reviewer/Editor comments | response matrix、revision plan、point-by-point response |

## `literature-research` 的两个 mode

不要再区分两个顶层 Skill：

```text
Landscape mode
  → 领域结构、范式、代表工作、open problems

Novelty-scout mode
  → specific idea 的 closest work、术语、novelty threat、positioning
```

当 `research-idea-refiner` 发现 novelty uncertainty 时，回到 `literature-research` 的 novelty-scout mode，而不是启动一个新的并列生命周期。

## `engineering-research` 内部包含实验设计

实验设计已经是它的一个 mode：

```text
Claim
→ RQ / Hypothesis
→ Alternative explanation
→ Baseline / Control
→ Experiment
→ Metric
→ Decision rule
→ Evidence status
```

因此“帮我设计 ablation / benchmark / robustness experiment”直接使用 `engineering-research`。

## 两类 Figure 不要混

```text
method-figure → 让读者理解方法/机制
result-figure → 让读者根据数据判断 claim
```

如果一张图既有 method schematic 又有 quantitative panel，可以先分别用两个 Skill 定义各自 scientific message，再由 `paper-architect` 决定是否组合成同一 Figure。

## Writer 与 Translation 的边界

```text
已有科学论证 + blueprint + evidence
→ academic-writer

已有源语言文本，只需要跨语言表达且科学含义不变
→ academic-translation
```

翻译不应静默修改 claim strength、scope、uncertainty、terminology、notation、citation 或 scientific argument。

## 常见联合使用

### 从新 idea 到实验

```text
literature-research (landscape)
→ research-idea-refiner
→ literature-research (novelty scout, only if needed)
→ engineering-research
```

### 从实验结果到论文

```text
result-harvester
→ engineering-research (claim-evidence audit)
→ method-figure / result-figure
→ paper-architect
→ academic-writer
```

### 中文先写、英文投稿

```text
paper-architect
→ 中文科学内容形成
→ academic-translation (ZH→EN manuscript mode)
→ academic-writer（仅当需要进一步基于 blueprint 做英文重写）
→ manuscript-review
```

### 收到审稿意见

```text
reviewer-response
├─ 文献/novelty → literature-research
├─ 新实验       → engineering-research → result-harvester/result-figure
├─ 结构问题     → paper-architect
├─ 图问题       → method-figure / result-figure
└─ 语言问题     → academic-writer / academic-translation
```

## 已退休的旧入口

这些能力没有丢失，只是降为主 Skill 内部 mode/reference：

| 旧 Skill | 新位置 |
|---|---|
| `literature-scout` | `literature-research` novelty-scout mode |
| `research-critic` | `research-idea-refiner` adversarial stress test |
| `experiment-designer` | `engineering-research` experiment-design mode |
| `scientific-figure` | 合并进 `method-figure` |
| `chinese-to-academic-english` | `academic-translation` ZH→EN mode |
| `faithful-paper-translation` | `academic-translation` EN→ZH mode |
