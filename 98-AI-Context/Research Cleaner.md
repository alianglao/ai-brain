# Research Cleaner

运行 tools/kb.py clean。程序保留下载文件及每份原始字节副本，以 SHA-256 去重。输出仅增加元数据和关系区，不改写原文；识别标题层级、编号列表、段落并记录统计。为避免破坏公式/代码，不自动重排正文。关键词规则可在 research-config.json 调整；分类不确定时进入 Cleaned。运行 tools/kb.py graph 重建基于真实研究笔记的主题索引。
