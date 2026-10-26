# 金龙鱼 GEA / 工作台与身份集成

[← 项目索引](../PROJECTS.md) · [源码（私有）](https://github.com/QinJiayan-maker/jinlongyu-gea)

## 项目构成

归档目录包含 `chatdam` 工作台和 `tezign-user-center` 用户中心。它与智能订单 H5 分别保留，避免把不同应用的边界混在一起。

## 实践重点

- 将 SSO 登录和组织账号同步视为不同的身份接入过程。
- 同步侧处理部门与用户更新、幂等控制和结果回传，登录侧完成身份对齐。
- 保持应用工作台与身份服务的职责划分，处理企业账户接入需求。

## 技术与状态

Next.js · TypeScript · Java · Spring Boot · PostgreSQL · Redis · SSO / IAM。

公开页面概述集成方向；私有快照保留工作台与用户中心代码。真实组织同步导出、凭据和运行缓存未随源码上传，本次未重新做企业 IAM 验收。
