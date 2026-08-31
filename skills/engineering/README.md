# Engineering Skills 使用说明

Engineering scope 覆盖从“任务进入仓库”到“设计、规格、实现、调试、Review 和长期维护”的完整软件工程生命周期。

## 生命周期

| 阶段 | Skill | 什么时候使用 | 主要输出 |
|---|---|---|---|
| Intake | `triage` | Issue / 外部 PR / bug report 需要验证和分流 | ready-for-agent / needs-info / wontfix 等结论 |
| Clarify | `grill-with-docs` | 设计目标存在真实未决决策 | 决策 + CONTEXT/ADR/术语更新 |
| Model | `domain-modeling` | 领域术语、实体、状态、关系不清 | 领域模型 / glossary |
| Architecture | `codebase-design` | 要设计 module / interface / seam | 架构候选与接口原则 |
| Architecture maintenance | `improve-codebase-architecture` | 现有仓库出现浅模块、测试困难、理解成本高 | 深化候选与重构方向 |
| Specification | `to-spec` | 关键决策已基本稳定 | implementation-ready spec |
| Planning | `to-tickets` | Spec 需要拆成可独立推进的垂直工作 | tickets / dependency frontier |
| Explore | `prototype` | 技术可行性未知，需要低成本验证 | 原型与结论，不等于生产实现 |
| Implement | `implement` | Spec/ticket 已稳定 | 实现 + checks |
| Test discipline | `tdd` | 需要以行为/接口为测试 seam 推进实现 | red/green/refactor loop |
| Debug | `diagnosing-bugs` | 已存在失败、回归或异常行为 | 可复现反馈环 + root cause |
| Review | `code-review` | Diff 已形成，需要独立质量检查 | blocker/major/minor findings |
| Conflict | `resolving-merge-conflicts` | 正在发生 Git merge/rebase conflict | 语义正确的冲突解决 |
| Long work | `wayfinder` | 跨多 session 且路径仍在发现中 | durable context + next frontier |

## 主工作流

新功能通常走：

```text
grill-with-docs / domain-modeling
→ to-spec
→ to-tickets
→ implement
   ├─ prototype（只有技术不确定时）
   ├─ tdd
   └─ diagnosing-bugs（出现失败时）
→ code-review
```

Incoming Issue/PR：

```text
triage
→ ready-for-agent
→ to-spec / implement（取决于上下文是否已经充分）
→ code-review
```

架构治理：

```text
codebase-design
→ improve-codebase-architecture
→ grilling / domain-modeling（选中候选后）
→ to-spec
```

## 选择规则

- 路线不清 ≠ 规格不清：长期路线不清用 `wayfinder`；单个设计决策不清用 `grill-with-docs`。
- `prototype` 只回答“不确定性”，不要把原型默认升级为正式实现。
- `diagnosing-bugs` 从可捕获真实 bug 的反馈环开始，不凭猜测直接改代码。
- `code-review` 是独立质量 gate，不应由实现者的自我说明替代。
