# 建模比赛图表与 Skill 最小工作流

分类：建模工作流
topics: #数学建模 #Skill组合 #科学可视化 #图表
适用范围：`C:\Users\18928\Desktop\数学建模研究室` 的 CUMCM/数学建模比赛任务
日期：2026-09-09
状态：已确认并完成工作区文档同步；2025C 已完成流程图/机制图说明级验证，完整竞赛论文仍为 REVISE

## 长期有效结论

数学建模比赛默认采用“一个主流程 + 一个选模审查 + 两个按需模块”的最小组合：

1. `paper-workflow-orchestrator`：题目拆解、数据检查、代码运行和结果整理。
2. `cumcm-taste`：审查候选模型是否匹配问题机制、数据和论文证据。
3. `results-analysis`：仅在需要严格统计、模型比较、敏感性或稳健性检验时启用。
4. `publication-chart-skill`：仅在需要论文级图表或表格时启用。

本地 `scientific-visualization-book` 不作为独立 Skill，而是图表设计参考，重点用于受众/主张/媒介判断、图形选择、颜色、版式、图注和发布前 QA。

流程图和机制图采用新的专用补充组合：

1. `mermaid-diagram`：用于流程图、工作流图、架构图、ProcessOn/draw.io 导入草稿和 Mermaid 源文件。
2. `academic-figure-workflow`：用于机制图、概念模型图、论文级 SVG 解释图和需要视觉 QA 的学术示意图。

这两个 Skill 已安装到 `C:\Users\18928\.codex\skills\`，并复制到 `C:\Users\18928\Desktop\数学建模研究室\skills\`。它们不是替代主建模链路的全流程 Skill，只在需要图示表达时调用。

## 已移出默认组合

`autoresearch`、`scientific agent skills`、`paper spine`、`research studio`、`academic research skills`、`cloud scholar`、`nature-polishing` 和 PPT/Beamer 工具不再进入比赛默认链路；仅在文献研究、自动实验、英文润色、知识库维护或汇报制作等明确任务中按需启用。

## 证据与同步

- 工作区图表 SOP：`C:\Users\18928\Desktop\数学建模研究室\建模比赛图表工作流.md`
- 工作区流程对照表：`C:\Users\18928\Desktop\数学建模研究室\数学建模流程与科研Skill对照表.md`
- CUMCM 使用说明：`C:\Users\18928\Desktop\数学建模研究室\claude-scholar-codex\CUMCM使用说明.md`
- 设计参考教材：`C:\Users\18928\Desktop\数学建模研究室\scientific-visualization-book`
- 2025C 图示说明：`C:\Users\18928\Desktop\数学建模研究室\projects\2025-CUMCM-C\outputs\figures\2025_c_modeling_diagram_usage.md`

原始教材和原始 Skill 文件未删除；本记录只保存已确认的调用边界和适用范围，不保存逐字聊天记录。
