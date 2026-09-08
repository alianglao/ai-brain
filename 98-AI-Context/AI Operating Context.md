# AI Operating Context

开始前读取 About Me、Current Focus、User Preferences、Decisions 和相关项目状态。完成后仅沉淀长期有效、已确认或已验证的信息；默认不保存逐字聊天记录；引用具体文件。

长期约定：维护 ai-brain 时，优先检查 88-Skills/00-Skill Index.md 与 88-Skills/Skills/，把它们当作 Skills 的主索引与教程区。

2026-09-08 已验证的 Supervisor Skill：主规则位于 `C:\Users\18928\Desktop\ai brain\88-Skills\Skills\supervisor\SKILL.md`，教程和索引分别位于 `88-Skills\Skills\supervisor.md` 与 `88-Skills\00-Skill Index.md`；支持关闭、轻量、终审、严格四种模式，使用 PASS/REVISE/BLOCK 协议，默认推荐终审以控制额度。数学建模审查清单覆盖题意、假设、模型、数据、求解、敏感性/稳健性、图表、论文逻辑和可复现性；已完成普通 Python 与数学建模最小场景的 REVISE → PASS 验证。该 Skill 是 Vault 内的可复用规范，是否安装为全局 Codex Skill 需另行确认。

当前已验证的 Codex 环境：Claude Scholar 的 Codex 分支组件位于 `C:\Users\18928\.codex\`，可跨项目使用；数学建模工作区另有 `scientific-visualization-book` 教材资料，仅在该工作区按需读取，不作为全局 skill 加载。

2026-09-08 已确认的数学建模比赛最小 Skill 组合：`paper-workflow-orchestrator` 负责主流程，`cumcm-taste` 负责选模审查；只有在需要严格统计/敏感性/稳健性分析时启用 `results-analysis`，只有在需要论文级图表/表格时启用 `publication-chart-skill`。`C:\Users\18928\Desktop\数学建模研究室\scientific-visualization-book` 仅作为图形结构、配色、版式和媒介适配参考，不作为独立流程控制器。该组合适用于当前数学建模工作区的比赛任务，已同步到工作区图表 SOP、建模流程对照表和 CUMCM 使用说明；未用真实赛题完成端到端验证。

2026-09-07 已验证的数学建模工作流：CUMCM 论文知识库位于 `C:\Users\18928\Desktop\数学建模研究室\Research\cumcm-excellent-papers`，采用 `Sources\Papers` 保存来源、`Knowledge` 保存方法卡的分层结构。Paper Miner 的全局写作记忆位于 `C:\Users\18928\.codex\skills\ml-paper-writing\references\knowledge\paper-miner-writing-memory.md`，已完成 2020 C、2021 C、2023 A 三篇完整 PDF 的写作模式提取。适用范围是当前数学建模工作区和正式 CUMCM 论文辅助写作；经验必须在当前赛题数据上重新验证。

2026-09-08 已验证的可复用建模环境：工作区根目录 `C:\Users\18928\Desktop\数学建模研究室\python-dependencies-py312-win64` 保存 Python 3.12 Windows x64 的数据分析与绘图库依赖，`python-wheels-cache` 保存 matplotlib wheel 安装包。2025C 项目脚本已在该环境下成功生成中文图表；复用到其他赛题前需核对 Python 版本、操作系统、依赖版本和路径，不把平台相关 wheel 视为跨系统通用环境。适用范围：本机数学建模项目。

2026-09-08 已确认的数学建模终审经验：工程基线 PASS 只表示输入、脚本、输出和复跑链路通过，不能升级为竞赛论文 PASS。竞赛论文还必须逐小问核对目标函数与风险、变量覆盖、重复测量与删失、标签来源与标签—特征循环、折内预处理、显著性检验、模型方向一致性、稀疏组和不确定性。题目要求“最优/最小风险”时不得用无论证的固定通过率阈值替代显式风险函数；发现可修问题必须执行“定位—修正—重跑—复查”。证据来源：`C:\Users\18928\Desktop\数学建模研究室\projects\2025-CUMCM-C\notes\教授终审问题清单.md`；适用范围：CUMCM 及同类数学建模竞赛，状态：已由 2025C 材料和独立复核结果验证。
