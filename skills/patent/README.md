# Patent Skills 使用说明

Patent scope 以中国发明专利的工程挖掘流程为主。核心原则是先建立 provenance，再谈 invention；代码是证据来源，不自动等于申请人的创新。

## 生命周期

| 阶段 | Skill | 什么时候用 | 主要输出 |
|---|---|---|---|
| Provenance | `codebase-patent-diff` | 代码基于 upstream/fork/第三方，需要先分清来源 | provenance / exclusion map |
| Mining | `cn-patent-invention-mining` | 从用户修改、系统架构、数据闭环、工程机制中寻找候选 | invention candidate cards |
| Portfolio | `patent-portfolio-planner` | 同时存在多个候选，需要 split/merge/priority/staged filing | portfolio plan |
| Prior art | `cn-patent-prior-art` | 候选已形成，需要检索最接近现有技术 | prior-art matrix |
| Draft | `cn-patent-drafting` | 候选和 prior art 基本稳定 | disclosure / claim-oriented draft |
| Review | `cn-patent-review` | 草稿已形成，需要一致性、支持性、来源与 CNIPA 风格审查 | review findings / revision queue |
| Domain overlay | `autonomous-driving-patent` | 自动驾驶相关项目，需要领域边界与术语 guidance | domain guidance，不替代上述阶段 |

## 推荐主流程

```text
codebase-patent-diff
→ cn-patent-invention-mining
→ patent-portfolio-planner（多个候选时）
→ cn-patent-prior-art
→ cn-patent-drafting
→ cn-patent-review
```

## 联合使用原则

`autonomous-driving-patent` 是 overlay，不是独立流水线。例如自动驾驶数据闭环项目应使用：

```text
autonomous-driving-patent (domain context)
+
codebase-patent-diff
→ cn-patent-invention-mining
→ ...
```

Provenance labels 在下游持续有效，除非出现新的直接证据。若 provenance 不清，应保留 `UNKNOWN_PROVENANCE`，不要为了形成专利候选而强行归属。
