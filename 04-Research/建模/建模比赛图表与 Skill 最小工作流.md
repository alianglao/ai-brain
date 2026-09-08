# 建模比赛图表与 Skill 最小工作流

分类：建模工作流
topics: #数学建模 #Skill组合 #科学可视化 #图表
适用范围：`C:\Users\18928\Desktop\数学建模研究室` 的 CUMCM/数学建模比赛任务
日期：2026-09-08
状态：已确认并完成工作区文档同步；尚未用真实赛题完成端到端验证

## 长期有效结论

数学建模比赛默认采用“一个主流程 + 一个选模审查 + 两个按需模块”的最小组合：

1. `paper-workflow-orchestrator`：题目拆解、数据检查、代码运行和结果整理。
2. `cumcm-taste`：审查候选模型是否匹配问题机制、数据和论文证据。
3. `results-analysis`：仅在需要严格统计、模型比较、敏感性或稳健性检验时启用。
4. `publication-chart-skill`：仅在需要论文级图表或表格时启用。

本地 `scientific-visualization-book` 不作为独立 Skill，而是图表设计参考，重点用于受众/主张/媒介判断、图形选择、颜色、版式、图注和发布前 QA。

## 已移出默认组合

`autoresearch`、`scientific agent skills`、`paper spine`、`research studio`、`academic research skills`、`cloud scholar`、`nature-polishing` 和 PPT/Beamer 工具不再进入比赛默认链路；仅在文献研究、自动实验、英文润色、知识库维护或汇报制作等明确任务中按需启用。

## 证据与同步

- 工作区图表 SOP：`C:\Users\18928\Desktop\数学建模研究室\建模比赛图表工作流.md`
- 工作区流程对照表：`C:\Users\18928\Desktop\数学建模研究室\数学建模流程与科研Skill对照表.md`
- CUMCM 使用说明：`C:\Users\18928\Desktop\数学建模研究室\claude-scholar-codex\CUMCM使用说明.md`
- 设计参考教材：`C:\Users\18928\Desktop\数学建模研究室\scientific-visualization-book`

原始教材和原始 Skill 文件未删除；本记录只保存已确认的调用边界和适用范围，不保存逐字聊天记录。
