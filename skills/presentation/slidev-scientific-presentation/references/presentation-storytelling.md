# 科研 Presentation 的叙事规范

## 1. 一页只承担一个任务

每页应能回答一个明确问题，例如：我们解决什么问题？现有方法为什么不足？核心方法是什么？这个公式改变了什么？实验是否支持核心结论？如果一页同时承担背景、方法、实验三个任务，应拆分。

## 2. 标题使用中性、明确的科研语言

推荐：Problem setting、Diffusion optimal control、Multi-agent coordination、Quantitative results。避免含糊的营销式标题。

## 3. 内容组织

优先顺序：结论或问题 → 公式/图/动画/表 → 必要解释 → 次要细节放备注或后备页。

## 4. 论文转 slides 时不要逐节复制

```text
paper: Introduction / Related Work / Method / Experiments
presentation: Problem → Existing limitation → Key idea → Formulation → Method behavior → Evidence → Conclusion
```

## 5. 公式页面

说明输入/状态、优化变量、目标函数、与已有方法相比改变了什么。不要仅展示公式而不说明作用。

## 6. 实验页面

先确定问题（是否更快、更稳、在困难条件下是否有效、是否随规模保持性能），再选择图表或动画。

## 7. 后备页

适合放完整超参数、额外消融、完整实验表、详细推导和 implementation details。
