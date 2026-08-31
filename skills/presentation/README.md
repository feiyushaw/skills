# Presentation Skills 使用说明

Presentation scope 分成三层：**讲什么 → 用什么 renderer 实现 → 最终质量检查**。不要让渲染工具重新决定故事结构。

## 生命周期

| 阶段 | Skill | 什么时候用 | 主要输出 |
|---|---|---|---|
| Architecture | `presentation-architect` | 还在决定 audience、goal、storyline、slide roles、visual contract | storyline + slide map |
| Render: Slidev | `slidev-scientific-presentation` | 科研/技术汇报，希望 Markdown-first、公式和可复现可视化 | Slidev deck |
| Render: PPTX | `powerpoint-presentation` | 需要可编辑 PowerPoint/PPTX | editable PPTX deck |
| Review | `presentation-review` | deck 已渲染，需要 narrative/evidence/visual/delivery QA | review report + revision queue |

## 主工作流

```text
source material + audience + goal
→ presentation-architect
→ approved slide map
→ slidev-scientific-presentation OR powerpoint-presentation
→ presentation-review
```

## Renderer 怎么选

- 科研汇报、LaTeX 数学、代码/Markdown、可复现图较多 → Slidev。
- 企业内部汇报、需要大量手工编辑、跨团队继续编辑、客户交付 → PPTX。
- 先选故事，再选 renderer；不要因为模板方便而改变科学论证。

## 与 Research 联合

论文汇报常见组合：

```text
research/method-figure + research/result-figure
→ presentation-architect
→ renderer
→ presentation-review
```

Research figure 定义科学含义；Presentation 决定在口头叙事中如何裁剪、排序和呈现，但不得改变证据强度。
