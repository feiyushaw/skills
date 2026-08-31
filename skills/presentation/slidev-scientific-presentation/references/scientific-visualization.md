# 科研可视化与 Slidev

## 分工

```text
Python / simulator / experiment
        ↓
SVG / PNG / GIF / MP4 / CSV / JSON
        ↓
Slidev
```

Python 负责数值计算和数据生成；Slidev 负责叙事、布局、逐步揭示和交互。

## 静态科学图

优先 SVG。适合 loss/convergence、trajectory、ablation、FEM/CFD 后处理和 optimization history。

## GIF / 视频

已有仿真动画不应强制改成 JavaScript。只有同步播放、暂停、时间跳转或多场景联动等需求才升级为更复杂交互。

## JSON 驱动交互

当目标是解释过程，可让 Python 输出结构化迭代/轨迹数据，再由轻量 Vue/SVG 展示。适合 CMA-ES/CEM、MPC rollout、trajectory distribution、multi-agent interaction、diffusion trajectory、optimization landscape 等。

## 什么时候不要交互

只传达一个定量结论、论文图已清晰、演讲没有时间操作、或交互没有增加解释维度时，静态图更好。

## 可读性

优先大字号轴标签、少量曲线、直接标注关键点、避免图例遮挡、避免过多近似颜色编码，不依赖 hover 才能理解核心结果。

## PDF fallback

动态页面应有可理解的静态状态：GIF 选择合理首帧，slider 默认关键阶段，多步动画必要时补 summary slide，视频提供封面帧和一句说明。
