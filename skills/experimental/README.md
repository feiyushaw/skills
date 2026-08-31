# Experimental Skills 使用说明

`experimental` 只放尚未经过足够真实使用验证的 Skill。它们不会进入 `full` pack，也不应被 `workflow-router` 隐式选择。

| Skill | 什么时候用 | 目标 |
|---|---|---|
| `retro` | 一次 Agent/coding session 结束后，想分析环境为何让 Agent 工作低效 | 提炼 navigation、checks、tool economy、information access 等改进 |
| `skill-audit` | Skills 仓库本身变大，担心重叠、路由冲突、自包含、Pack、regression 问题 | 产生 merge/split/rewrite/add-test 等维护动作 |

## 使用关系

```text
真实工作
→ 暴露重复摩擦
→ retro
→ 环境 / docs / checks 改进
```

```text
Skill 仓库扩展
→ skill-audit
→ merge / split / rename / regression fixture
→ 多次真实使用
→ 决定是否晋升 stable
```

## 晋升条件

Experimental Skill 只有在以下条件大体成立后才考虑加入 stable pack：

- 在不同真实任务中重复有用；
- 与已有 Skill 边界清楚；
- 有稳定输入/输出或可观察行为；
- 不会高频误触发；
- 关键失败模式有 regression fixture 或其他检查。
