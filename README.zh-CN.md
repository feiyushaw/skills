# Feiyu Skills

面向 Codex、Claude Code 及其他代码/科研 Agent 的可组合 Skill 仓库。

这个仓库现在是个人工作 Skills 的统一主仓库：代码开发、科研、Presentation、专利和通用效率工具按工作类别组织；跨领域复用的行为原语放在 `core`；`packs` 只负责组合安装。

## 工作类别

| 类别 | 主要用途 | V1 状态 |
|---|---|---|
| `core` | 路由、Grilling、Handoff、Agent 文档规范 | 稳定 |
| `engineering` | Spec、Tickets、架构、实现、TDD、调试、Review、长任务规划 | 核心集已完成 |
| `research` | 文献、创新提炼、实验、证据、科研绘图、论文组织/写作/审稿 | 已迁移 |
| `presentation` | 与工具无关的汇报架构 + Slidev 科研演示 | 已迁移，继续扩展 |
| `patent` | 中国发明专利：来源边界、挖掘、检索、撰写、审查 | 已迁移 |
| `productivity` | GrillMe、教学、问卷、重新解释、Handoff | 核心集已完成 |
| `experimental` | 尚未稳定的新 Skill | 保留 |

## 当前主工作流

### Engineering

```text
idea / task
  ↓
grilling / domain-modeling
  ↓
to-spec
  ↓
to-tickets
  ↓
implement
  ├── prototype
  ├── tdd
  └── diagnosing-bugs
  ↓
code-review
```

大规模、跨上下文且路线尚不清楚的任务先用 `wayfinder`。

### Research

```text
Understand → Innovate → Prove → Communicate → Review

literature-research
  ↓
research-idea-refiner + literature-scout + research-critic
  ↓
experiment-designer / engineering-research
  ↓
result-harvester → scientific-figure / method-figure / result-figure
  ↓
paper-architect
  ↓
chinese-to-academic-english / academic-writer
  ↓
manuscript-review
```

科研域继续坚持：

```text
Contribution → Claim → Required Evidence → Experiment / Analysis
→ Figure / Table → Paper Section
```

语言层不能静默改变科学层。

### Presentation

```text
source material + audience + goal
  ↓
presentation-architect
  ↓
storyline / slide map / visual requirements
  ↓
slidev-scientific-presentation
```

Presentation 的“怎么讲”与“用什么工具生成”已经拆开。PowerPoint/PPTX renderer 是下一阶段扩展。

### Patent

```text
code / architecture / experiments
  ↓
codebase-patent-diff
  ↓
cn-patent-invention-mining
  ↓
cn-patent-prior-art
  ↓
cn-patent-drafting
  ↓
cn-patent-review
```

专利工作流保留 provenance gate：仓库所有权、代码复杂度、大 diff 都不能自动等同于申请人的可专利发明。

### Productivity

`grill-me` 是显式用户入口，本身保持很薄，只启动 `core/grilling`。这样 Grilling 的 decision-tree/frontier 逻辑可以被工程、科研、Presentation 和专利共同复用，而不复制四份。

另外提供 `teach`、`to-questionnaire`、`wait-what` 和 core `handoff`。

## 统一设计原则

1. Skill 是边界清楚的行为原语或领域工作流，不做巨大 Prompt 集合。
2. Agent 能自行检查的事实由 Agent 调查；用户主要回答真正的决策。
3. 长任务将重要状态写入 Spec、Tickets、CONTEXT/ADR、Research Map、Claim-Evidence、Patent Candidate、Handoff 等持久产物。
4. 领域专业判断留在领域 Skill；通用交互机制才进入 `core`。
5. `SKILL.md` 放通用规则，分支性细节放当前 Skill 自己的 `references/templates/scripts`。
6. 每个 Skill 默认可独立安装，不依赖脆弱的跨目录相对路径。
7. 大型 orchestrator 默认禁止隐式触发；可复用 primitive 可以由模型按需调用。
8. 第三方 Skill 保留来源和许可证。

## Packs

当前有：`engineering`、`research`、`presentation`、`patent`、`productivity` 和 `full`。

## 迁移来源

- `feiyushaw/academic_skills` → `skills/research/`
- `feiyushaw/patent_skills` → `skills/patent/`
- `feiyushaw/presentation_skill` → `skills/presentation/`
- `mattpocock/skills` 中筛选并适配的通用工程/效率方法 → `core / engineering / productivity`

具体来源 commit 和适配说明见 [docs/provenance.md](docs/provenance.md)；第三方许可证见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 开发检查

```bash
python3 scripts/validate-skills.py
```

GitHub Actions 会执行相同结构校验。

## 下一步

下一阶段优先补 `powerpoint-presentation`、`presentation-review`、Pack 安装脚本/自动 Catalog，以及关键工作流的 regression fixtures。旧仓库暂时保留作为历史来源，不急于删除或 archive。
