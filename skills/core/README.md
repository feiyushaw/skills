# Core Skills 使用说明

`core` 只放跨领域复用的行为原语。它们不负责工程、科研、Presentation 或专利中的专业判断。

## Scope

| Skill | 什么时候用 | 主要产物 |
|---|---|---|
| `workflow-router` | 不确定该进入哪个 domain / Skill 时 | 最小可执行 Skill 或短工作流 |
| `grilling` | 真正存在未决设计/研究决策，需要系统澄清时 | decision tree、frontier、已确认决策 |
| `handoff` | 跨 session、跨 Agent、跨机器继续任务时 | 紧凑、可恢复的状态交接 |
| `writing-for-agents` | 写 AGENTS.md、Skill、Agent brief、规范等供 Agent 消费的文档时 | 低认知负担的 Agent 文档 |

## 联合使用

典型模式：

```text
workflow-router
  → domain skill
  → grilling（仅在存在真正未决决策时）
  → domain artifact
  → handoff（需要跨上下文时）
```

`writing-for-agents` 通常作为工程/Skill 维护的辅助规范，不应替代具体 domain 的设计判断。

## 边界

- 能由 Agent 自己检查的事实，不要用 `grilling` 反问用户。
- `handoff` 只压缩状态，不重新做规划。
- `workflow-router` 负责选路，不执行完整下游任务。
- domain-specific 规则不要搬进 `core`。
