# Slidev 科研演示编写指南

## 目标

建立可复现、可版本控制、可由 Codex/Claude Code 维护的科研/技术演示工程，而不是把 PowerPoint 逐元素编辑模式搬到 Markdown。

## 默认技术栈

Slidev + Markdown；KaTeX；UnoCSS/utility classes；Mermaid；SVG；必要时 Vue；Python 负责数值与静态科学绘图。普通页面不要无必要加入复杂前端代码。

## 页面类型

Title、Problem、Formulation、Method、Visual behavior、Quantitative result、Qualitative result、Conclusion。每种页面都应有明确讲述任务。

## 布局原则

优先 Slidev 原生布局和简单 grid。常见结构：公式+解释、方法图+三条要点、左右对比、上结论下大图、2x2 实验可视化。不要切成过多小块。

## 公式

保留 LaTeX 习惯。长公式拆为定义、目标和约束；不要靠极小字号塞满页面。

## 代码

只展示 API 入口、核心循环、关键条件或配置差异。超过约 20–25 行通常继续裁剪。

## 动画/fragments

动画服务讲解顺序。算法过程优先逐层揭示，而不是一次展示复杂流程图。

## 资源管理

资源放 `public/figures`, `public/animations`, `public/videos`, `public/data`。可视化来自 Python 时保留生成脚本。

## 输出

至少验证开发和构建模式；需要静态备份时导出 PDF。动态内容在 PDF 中应有合理静态表达。

## Agent 编写规则

先读源论文/README/实验输出；先做 slide outline；不从文件名猜实验含义；不虚构结果；优先复用现有 GIF/SVG/图表；轻量复用 Python 可视化；最后检查每页讲述目的。
