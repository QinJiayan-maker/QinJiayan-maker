# 项目索引 / Projects

[← 返回主页](README.md) · [技术笔记](notes/README.md)

这里是个人项目、实习实践与代码归档的公开索引。介绍页均可直接阅读；源码仓库和 F1 发行包设为私有，未获授权时 GitHub 会返回 404。

## Agent 与企业应用

- [EchoAgent：人物记忆与可控执行](projects/echoagent.md) — 开发中个人 Agent 工作台；完整 Live 验收与稳定发布尚未完成。
- [Volvo：多阶段研究 Agent](projects/volvo.md) — 研究流程编排、团队知识库与来源治理。
- [金龙鱼：智能订单 Agent](projects/order-agent.md) — 文字、语音与拍照改单，订单草稿和原生交互。
- [金龙鱼 GEA：工作台与企业身份集成](projects/gea.md) — 应用工作台、SSO / IAM 与组织同步。
- [Disney DAM：企业数字资产管理](projects/disney.md) — 鉴权、资产检索、媒体处理和私有化适配。
- [礼来：AI 内容引擎](projects/lilly.md) — 内容创作、素材与模板工作台代码归档；不扩写未经核实的个人职责。

## 后端、视觉与交互项目

- [融矩阵数字藏品平台](projects/fusion-matrix.md) — Java 后端、数据库表结构及项目文档合并归档。
- [视觉目标跟踪](projects/visual-tracking.md) — YOLO、NanoTrack、卡尔曼滤波与 STM32 云台控制。
- [区块链电子合同](projects/blockchain-contract.md) — 基于已有框架的电子合同项目归档，保留第三方归属。
- [F1 / Unreal Engine Windows 程序](projects/f1.md) — Windows 打包交付物，尚未提供工程源码；完整程序包上传未完成，已成功的 6 卷保留为私有草稿。

## 参考资料

项目架构图与通用参考笔记保存在 [project-reference-notes（私有）](https://github.com/QinJiayan-maker/project-reference-notes)，Volvo 源码位于该仓库独立的 `projects/volvo-research-agent` 目录。Disney 技术附件已归入对应私有仓库。面试准备、个人简历、销售合同和重复压缩包不列为项目。

## 归档说明

本轮上传的是清理后的项目快照，没有搬入原 Git 历史。上传副本移除了运行凭据、私钥、临时导出、缓存、日志和完整业务数据库导出；需要表结构的数据库导出仅保留 DDL。原文件保留在本机。

每个新建源码仓库都有文件清单与处理报告。项目介绍不等于本轮重新通过构建、业务验收或线上效果测试。
