# 知识库搭建

## 当前状态
截至 2026-09-09。
基础建设已完成初版；CUMCM 论文知识库和 Paper Miner 写作记忆已完成一次端到端验证。
本次已完成数学建模研究室面向 2026 CUMCM 的结构精进：新增统一赛中入口、2026 项目模板、赛中 AI 使用边界、72 小时作战表、Codex/教授休息室分工、论文内容骨架、AI 记录模板、PDF 转换预演和提交前清单。
## 已完成事项
环境检查、结构与规范生成；建立 `C:\Users\18928\Desktop\数学建模研究室\Research\cumcm-excellent-papers`；导入 2020 C、2021 C、2023 A 三组论文/代码/数据材料；建立 3 份来源笔记和 3 张方法卡；使用 Paper Miner 从 3 篇完整 PDF 提取写作模式并更新 `C:\Users\18928\.codex\skills\ml-paper-writing\references\knowledge\paper-miner-writing-memory.md`；新增并升级可插拔 Supervisor Skill，现含关闭/轻量/终审/严格四种模式、Executor/Supervisor/Reviewer/Reconciler 分工、PASS/REVISE/BLOCK 协议、返工上限、Reviewer/Reconciler 模板、数学建模审查清单、用户教程与 Skill 索引条目；已用普通 Python 与数学建模最小场景验证 REVISE → PASS；确认数学建模比赛的最小 Skill 组合，并将本地 scientific-visualization-book 接入图表 SOP；新增 `mermaid-diagram` 与 `academic-figure-workflow` 作为流程图/机制图专用补充 Skill，并已在 2025C NIPT 项目的图示说明中完成验证。
## 待办事项
GitHub 登录和外部插件仍待单独确认；用真实赛题测试论文经验检索、方法迁移和正式写作调用；用实际队伍电脑完成正式论文模板套用、AI 工具详情 PDF 导出和提交包演练。
## 下一步
继续推进真实 CUMCM 赛题的论文级整改：在 2025C 已完成可复现基线和图示说明的基础上，优先处理风险函数、删失/选择效应、变量覆盖、标签循环、折内预处理和显著性解释。
## 风险
外部同步仍未验证；论文获奖等级部分只记录来源仓库声明；来源论文经验不能替代当前题目的数据、模型和验证；研究室新建论文文件是内容骨架，不是已确认的官方 Word/LaTeX 格式；赛中 AI 合规边界仍需以组委会最新公告复核。
## 决策
原始文件永久保留；分类不明待审；来源事实与可复用方法分层；Paper Miner 只写入全局写作记忆，不建立项目级重复记忆；Supervisor 默认终审以控制额度，严格模式仅用于高风险或正式提交任务；比赛默认不叠加多个全流程 Skill，图表教材只作本地参考，真实赛题验证前不把该组合视为完全验证；2026 CUMCM 赛中以本地资料和人工核验为默认边界，Codex 负责审题/记录/复现支持，教授休息室负责唯一终审；正式计算解释器必须在项目内登记且不得写死个人绝对路径；不把未经测试的 Python 3.13 环境作为硬依赖。

## 本次验证
日期：2026-09-08。证据：`C:\Users\18928\Desktop\数学建模研究室\CUMCM-2026赛中总入口.md`、`projects\2026-CUMCM-模板\`、`projects\2025-CUMCM-C\src\analysis_2025c.py`、`Research\cumcm-excellent-papers\_system\registry.md`。已确认模板关键文件存在，2025C 脚本通过 Python 语法编译，知识库注册表实际登记 6 篇来源论文和 3 张方法卡；未删除原始题面、附件或历史资料。适用范围：数学建模研究室的 2026 CUMCM 赛前/赛中工作流。

日期：2026-09-09。证据：`C:\Users\18928\.codex\skills\mermaid-diagram-skill\SKILL.md`、`C:\Users\18928\.codex\skills\academic-figure-workflow\SKILL.md`、`C:\Users\18928\Desktop\数学建模研究室\skills\mermaid-diagram-skill`、`C:\Users\18928\Desktop\数学建模研究室\skills\academic-figure-workflow`、`C:\Users\18928\Desktop\数学建模研究室\projects\2025-CUMCM-C\outputs\figures\2025_c_modeling_diagram_usage.md`。已确认两个图示 Skill 安装并复制到工作区；2025C 图示说明已绑定 README、题面说明、数据账本、分析报告、最终验证报告和教授终审问题清单。适用范围：数学建模研究室的流程图和机制图任务；不代表 2025C 竞赛论文已通过终审。
