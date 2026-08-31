# Feiyu Skills

面向 Codex、Claude Code 及其他代码/科研 Agent 的可组合个人 Skill Monorepo。

仓库按照实际工作类别组织；跨领域复用的交互/上下文原语放在 `core`；`packs` 负责安装组合；`experimental` 用于尚未经过足够实际使用验证的新能力。

## 工作类别

| 类别 | 主要用途 | 状态 |
|---|---|---|
| `core` | 路由、Grilling、Handoff、Agent 文档规范 | 稳定 |
| `engineering` | 澄清、Spec、Tickets、架构、实现、TDD、调试、Review、Issue Triage、长任务规划 | 稳定 V2 |
| `research` | 文献、创新提炼、实验、证据、科研绘图、论文组织/写作/审稿/Reviewer Response | 稳定 V2 |
| `presentation` | 汇报架构、Slidev、PPTX、最终 Review | 基本闭环 |
| `patent` | 中国发明专利：来源边界、挖掘、组合规划、检索、撰写、审查 | 稳定 V2 |
| `productivity` | GrillMe、教学、问卷、重新解释、Handoff | 稳定 |
| `experimental` | Session Retro、Skill Audit 等尚未稳定的能力 | 显式安装 |

当前共 **51 个 skills**；`full` 默认安装 49 个稳定 skills，不包含 `experimental`。

## Engineering

```text
incoming issue / PR ──→ triage
                         |
idea / design ──→ grill-with-docs
                  ↓
          domain-modeling
                  ↓
              to-spec
                  ↓
            to-tickets
                  ↓
             implement
          ┌───────┼────────┐
       prototype  tdd  diagnosing-bugs
                  ↓
             code-review
```

架构维护使用：

```text
codebase-design
      ↓
improve-codebase-architecture
      ↓
grilling / domain-modeling
      ↓
to-spec
```

跨多个上下文、路线尚不清楚的大任务使用 `wayfinder`。

## Research

```text
Understand → Innovate → Prove → Communicate → Review → Respond

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
  ↓
reviewer-response
```

Reviewer 要求新实验、补文献或重构论文时，`reviewer-response` 会把任务重新路由回对应的科研 skill，而不是把所有问题都当成语言润色。

## Presentation

```text
source + audience + goal
        ↓
presentation-architect
        ↓
storyline / slide map / visual contract
        ↓
   ┌────┴─────┐
 Slidev      PPTX
   ↓           ↓
slidev-      powerpoint-
scientific-  presentation
presentation
   └────┬─────┘
        ↓
presentation-review
```

这样“怎么讲”“用什么 renderer”“最终质量检查”已经分层。

## Patent

```text
code / architecture / experiments
  ↓
codebase-patent-diff
  ↓
cn-patent-invention-mining
  ↓
patent-portfolio-planner   # 多候选时
  ↓
cn-patent-prior-art
  ↓
cn-patent-drafting
  ↓
cn-patent-review
```

继续保留 provenance gate：仓库所有权、代码复杂度和大 diff 都不能自动等同于申请人的可专利发明。

## Productivity 与 Experimental

`grill-me` 是显式用户入口，底层复用 `core/grilling`。`handoff` 位于 core，因为它被所有工作域复用。

`experimental/retro` 用来从一次 Agent 工作中提炼环境改进；`experimental/skill-audit` 用来检查 skill 重叠、路由冲突、自包含、Pack 与安装问题。实验 Skill 不进入 `full`。

## 使用

列出 skills：

```bash
python3 scripts/list-skills.py
python3 scripts/list-skills.py --domain research
```

校验：

```bash
python3 scripts/validate-skills.py
```

安装 Pack 时显式指定目标目录：

```bash
python3 scripts/install-pack.py engineering --target /path/to/agent/skills --dry-run
python3 scripts/install-pack.py full --target /path/to/agent/skills
```

详细说明见 [docs/using-skills.md](docs/using-skills.md)。

## 设计原则

1. Skill 是边界清楚的行为原语或领域工作流，不做巨大 Prompt 集合。
2. Agent 能自行调查的事实由 Agent 调查；用户主要回答决策。
3. 长任务把状态写入明确的持久产物，而不是无限依赖聊天上下文。
4. 领域判断留在领域 Skill；跨领域重复行为才进入 `core`。
5. 一个 skill 单独安装后应仍可理解和工作。
6. 大型 orchestrator 默认禁止隐式触发。
7. `experimental` 必须经过重复实际使用后再提升为稳定 Pack。
8. 第三方来源与许可证持续保留。

完整目录见 [docs/catalog.md](docs/catalog.md)，来源记录见 [docs/provenance.md](docs/provenance.md)。
