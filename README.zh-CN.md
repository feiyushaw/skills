# Feiyu Skills

面向 Codex、Claude Code 及其他代码/科研 Agent 的可组合个人 Skill Monorepo。

仓库按照真实工作类别组织；跨领域复用行为放在 `core`；`packs` 负责安装组合；`experimental` 仅显式启用。

## 工作类别

| 类别 | 主要用途 | 状态 |
|---|---|---|
| `core` | 路由、Grilling、Handoff、Agent 文档规范 | 稳定 |
| `engineering` | Triage、设计、Spec、Tickets、实现、TDD、调试、Review、长任务 | 稳定 V2 |
| `research` | 文献、创新提炼、证据、科研绘图、论文结构/写作/翻译/审稿/返修 | 稳定 V2，已精简 |
| `presentation` | 汇报架构、Slidev、PPTX、最终 Review | 基本闭环 |
| `patent` | 中国发明专利：来源边界、挖掘、组合规划、检索、撰写、审查 | 稳定 V2 |
| `productivity` | GrillMe、教学、问卷、重新解释 | 稳定 |
| `experimental` | Session Retro、Skill Audit | 显式安装 |

当前共 **46 个 Skill**：`full` 安装 44 个稳定 Skill，另外 2 个 experimental 仅按需安装。

每个 `skills/<domain>/README.md` 都说明该 scope 的生命周期、每个 Skill 的用途、选择规则和常见联合使用方式。

## Research 精简后的生命周期

Research 从原来的 16 个顶层入口收缩为 11 个：

```text
Understand  → literature-research
Innovate    → research-idea-refiner
Prove       → engineering-research
Evidence    → result-harvester
Visualize   → method-figure / result-figure
Structure   → paper-architect
Write       → academic-writer / academic-translation
Review      → manuscript-review
Respond     → reviewer-response
```

原来的 `literature-scout`、`research-critic`、`experiment-designer`、`scientific-figure` 以及两个翻译 Skill 并没有丢失能力，而是分别合并为主 Skill 内的 mode/reference。详细生命周期和组合方式见 [skills/research/README.md](skills/research/README.md)。

## 其他主流程

Engineering：

```text
grill-with-docs → domain-modeling → to-spec → to-tickets
→ implement → code-review
```

Presentation：

```text
presentation-architect
→ Slidev 或 PPTX renderer
→ presentation-review
```

Patent：

```text
codebase-patent-diff
→ cn-patent-invention-mining
→ patent-portfolio-planner（多个候选时）
→ cn-patent-prior-art
→ cn-patent-drafting
→ cn-patent-review
```

## 使用与校验

```bash
python3 scripts/list-skills.py
python3 scripts/list-skills.py --domain research
python3 scripts/validate-skills.py
python3 scripts/validate-regressions.py
python3 scripts/smoke-test-distribution.py
python3 scripts/install-pack.py full --target /path/to/agent/skills
```

更多说明见 [docs/catalog.md](docs/catalog.md) 和各 domain 目录下的 README。
