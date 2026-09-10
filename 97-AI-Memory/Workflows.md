# Workflows

[[98-AI-Context/Research Collection Workflow]]

## CUMCM 论文与写作工作流

1. 在 `C:\Users\18928\Desktop\数学建模研究室\Research\cumcm-excellent-papers` 保存来源、论文笔记和方法卡。
2. 先完成当前赛题拆解和 EDA，再检索 `Knowledge` 方法卡。
3. 回读对应 `Sources\Papers` 来源笔记，判断经验是否适用于当前数据和约束。
4. 使用 `cumcm-taste` 审查方法匹配、baseline、失败条件和证据边界。
5. 在当前数据上重新建模、运行和验证，不复制论文结果。
6. 撰写论文时读取全局 Paper Miner 记忆文件 `C:\Users\18928\.codex\skills\ml-paper-writing\references\knowledge\paper-miner-writing-memory.md`。

验证状态：2026-09-07 已用 2020 C、2021 C、2023 A 三篇完整 PDF 完成 Paper Miner 写作模式提取；三篇来源笔记和三张方法卡已登记。

## CUMCM 流程图与机制图工作流

1. 先从当前项目的 `README.md`、题面说明、数据账本、模型决策记录、证据账本、分析报告、最终验证报告和终审问题清单重建建模流程。
2. 流程图、工作流图、ProcessOn/draw.io 导入草稿和 Mermaid 源文件优先调用 `mermaid-diagram`。
3. 机制图、概念模型图和论文级 SVG 解释图优先调用 `academic-figure-workflow`。
4. 图示说明必须写清楚证据来源、使用位置、阅读顺序、论文图注建议和结论边界。
5. 工程基线 PASS 不能写成竞赛论文 PASS；正式论文仍要单独处理风险函数、删失/选择效应、变量覆盖、标签循环、折内预处理和显著性解释。

验证状态：2026-09-09 已在 `C:\Users\18928\Desktop\数学建模研究室\projects\2025-CUMCM-C\outputs\figures\2025_c_modeling_diagram_usage.md` 中完成 2025C NIPT 项目的说明级验证；适用范围为当前数学建模工作区的流程图和机制图任务。
