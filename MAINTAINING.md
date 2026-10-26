# 主页维护说明

## 布局与参考

本版按用户指定的 [Simon Willison 主页](https://github.com/simonw) 重做：简短介绍、三列顶端对齐内容、正文链接与简洁页尾。参考结构与比例，介绍、项目及笔记均换成自己的内容。

三列对应 Projects、Case studies、Notes。不伪造博客、发布版本、Star 数或技术经历。

## 文件组织

- README.md 与 README.en.md：由脚本生成的中英文首页。
- projects.json：公开项目名称、短描述与私有仓库名称。
- scripts/build_readme.py：从公开元数据生成首页，不访问私有源码 API。
- PROJECTS.md：完整项目索引。
- projects/：公开介绍；notes/：技术笔记。
- assets/：保留首版 SVG，首页当前不使用大横幅。

运行 `python scripts/build_readme.py` 可以重建主页。这是本地生成脚本，不是定时发布服务。

## 增加项目

1. 提供项目文件夹或仓库、本人职责及公开范围。
2. 核对实际功能、第三方归属和当前验证状态，先整理私有源码。
3. 在 projects/ 增加简介，更新 projects.json 和 PROJECTS.md。
4. 调整脚本中的精选项目列表，再生成中英文首页。

新增源码和交付物默认进入私有仓库。整份简历、凭据、私钥、真实业务导出和企业配置不进入公开主页。

## 本轮归档对应关系

- 金龙鱼 GEA → jinlongyu-gea，保留工作台与用户中心。
- 金龙鱼 → jinlongyu-order-agent，保留两个订单应用版本。
- 礼来 → lilly-content-engine。
- Disney 与技术附件 → disney-dam。
- volvo → project-reference-notes 私有仓库的 projects/volvo-research-agent 独立目录；GitHub 临时限制新建仓库，故复用已有私有归档。
- fusion-matrix、fusion_matrix 与融矩阵文档 → fusion-matrix，数据导出仅保留表结构。
- he_contract-master → blockchain-contract。
- 视觉跟踪目录 → visual-target-tracking。
- 架构图与通用笔记 → project-reference-notes。
- F1 打包程序 → f1-racing-demo 私有草稿 Release；上传未完成，仅 6 个原始分卷通过远端校验。仓库保存恢复脚本、校验清单和 UPLOAD_STATUS.json，当前云端分卷不能恢复完整程序。
- EchoAgent → 既有 virtual-human 私有仓库；已核对本地提交与远端一致。

各新建源码仓库有 ARCHIVE_REPORT.json 和 FILE_MANIFEST.json，记录上传文件与排除项。上传的是清理后的快照，没有原 Git 历史。凭据检查通过只指扫描范围，不等于业务或安全验收；本次没有重跑全部原项目测试。

## 资料准确性

教育背景依据简历，澳国立写“已获录取”。用户已明确确认礼来、电子合同和 F1 均由本人完成，项目介绍据此标注负责完整项目实现；所用框架、引擎与第三方资源保留各自归属。开发职责的确认不改变功能验证和文件上传状态。

侧栏姓名与简介需要账号资料修改权限；此前连接修改个人资料返回 404，没有改动侧栏资料。
