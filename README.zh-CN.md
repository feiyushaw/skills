# Feiyu Skills

面向 Codex、Claude Code 及其他代码/科研 Agent 的可组合 Skill 仓库。

这个仓库用于统一管理日常工作的 Agent 能力：代码开发、科研、Presentation、专利和通用效率工具。总体设计采用“小而可组合”的原则：领域 Skill 负责领域推理，跨领域重复出现的交互和工作流原语放在 `core`，`packs` 只负责组合安装。

## 工作类别

| 类别 | 主要用途 | 当前状态 |
|---|---|---|
| `core` | 通用 Agent 原语、路由、交互规范 | V1 骨架 |
| `engineering` | 需求澄清、Spec、Tickets、实现、测试、调试、Review | 规划中 |
| `research` | 文献、创新提炼、实验、科研绘图、论文、审稿 | 待迁移 |
| `presentation` | 汇报结构、Slidev、PPTX、Presentation Review | 待迁移 |
| `patent` | 中国发明专利挖掘、检索、撰写、审查 | 待迁移 |
| `productivity` | handoff、教学、问卷、长任务辅助 | 规划中 |
| `experimental` | 尚未稳定的新 Skill | 保留 |

## 总体结构

```text
                         core
                 通用路由 / 交互原语
                           |
        +------------------+------------------+
        |                  |                  |
   engineering          research        presentation
        |                  |                  |
        +------------------+------------------+
                           |
                         patent

packs = 对已有 skills 的安装组合，不承载领域逻辑
```

依赖方向保持简单：

- `core` 不依赖具体工作类别；
- 领域 Skill 可以调用 `core`；
- 不让一个领域静默接管另一个领域的专业判断；
- `packs` 只描述组合，不复制 Skill 正文。

## 调用类型

统一区分三类：

- **User-invoked workflow/router**：会启动较完整的工作流，默认禁止模型无意中自动触发；
- **Model-invoked primitive**：可复用的行为原语，允许 Agent 按需调用；
- **Domain context**：领域术语、约束和审查标准，可与工作流组合加载。

## Skill 自包含规则

每个 Skill 默认采用：

```text
skills/<domain>/<skill-name>/
  SKILL.md
  agents/openai.yaml        # 可选 Codex 元数据
  references/               # 可选
  templates/                # 可选
  scripts/                  # 可选
```

单独安装一个 Skill 后应能正常工作。避免依赖 `../../../shared/...` 之类脆弱的跨目录引用。

## V1 范围

第一阶段只建立总仓库的架构、规范、Core、Pack 定义、校验工具和迁移清单。现有私有仓库内容不会在本次 bootstrap 中复制到当前 public 仓库。

计划迁移来源：

- `feiyushaw/academic_skills` -> `skills/research/`
- `feiyushaw/patent_skills` -> `skills/patent/`
- `feiyushaw/presentation_skill` -> `skills/presentation/`
- 从 `mattpocock/skills` 选择性吸收并改造工程/效率类 Skill

正式迁移前先阅读 [docs/migration.md](docs/migration.md)。

## 设计原则

1. Skill 应是明确的行为原语或完整但边界清楚的领域工作流，不做巨大 Prompt 集合。
2. Agent 能自行检查的事实由 Agent 调查；需要用户回答的问题主要保留为决策。
3. 长任务的重要状态写入明确的外部产物，不依赖无限增长的上下文。
4. 科研、专利等领域的 claim 必须能追溯到 evidence；语言层不得静默改变技术含义。
5. 使用 progressive disclosure：通用规则放 `SKILL.md`，分支性细节放当前 Skill 的 `references/`。
6. 每个 Skill 应能独立安装、独立理解、独立验证。
7. 吸收第三方 Skill 时保留来源和许可证信息。

## 开发检查

```bash
python3 scripts/validate-skills.py
```

GitHub Actions 会执行相同检查。

## 下一阶段

PR2 重点迁移 `research / patent / presentation`；随后再建立完整的 `engineering` 工作流和安装脚本。
