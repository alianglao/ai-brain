# GitHub Sync Guide

当前 Vault 无远程地址，未验证 GitHub 登录或 push。先登录 GitHub 并确定已有私有仓库 URL；不要把 token 写入笔记。首次连接先检查远程历史，非空仓库须先 fetch 并审查差异，禁止 force push。Git 用户身份需真实配置。Obsidian 社区插件中安装 Git 后，成功完成一次手动 pull/commit/push，再开启每 10 分钟自动 commit-and-sync、每 10 分钟 pull 及启动 pull。冲突时停下解决；同步不替代备份。
