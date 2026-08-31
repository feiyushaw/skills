# Productivity Skills 使用说明

Productivity scope 放跨具体专业领域、但面向用户日常工作方式的显式工具。它们通常不是长生命周期，而是按当前交互问题选一个。

| Skill | 什么时候用 | 主要作用 |
|---|---|---|
| `grill-me` | 用户明确希望被追问、把模糊想法问清楚 | 启动 `core/grilling` 的显式入口 |
| `teach` | 希望跨多次会话系统学习一个主题 | persistent learning workspace |
| `to-questionnaire` | 需要把未知信息发送给外部专家/同事收集 | 生成高信息量、可回答的 questionnaire |
| `wait-what` | 前一版解释没听懂，需要换上下文/粒度重新讲 | context-aware re-pitch |

## 常见组合

```text
grill-me → domain workflow
```

例如先通过 `grill-me` 澄清创业/研究/产品决策，再进入对应 research / engineering / patent 流程。

```text
teach → wait-what
```

当长期学习过程中某一概念没有理解时，用 `wait-what` 重讲局部，不必重启整个 `teach` workspace。

`handoff` 不放在 productivity，因为它是所有 domain 都会复用的 core primitive。
