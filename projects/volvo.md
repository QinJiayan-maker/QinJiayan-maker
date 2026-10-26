# Volvo / 多阶段研究 Agent

[← 项目索引](../PROJECTS.md) · [源码与原始文档（私有）](https://github.com/QinJiayan-maker/project-reference-notes/tree/main/projects/volvo-research-agent)

## 场景

将模糊的研究课题逐步转化为可交付的结构化报告。我的实践重点是研究流程编排、团队知识检索与资料来源的区分。

## 实践内容

- 用七阶段流程组织洞察搜索、方案设计、人群筛选、访谈大纲、人设访谈、报告生成与归档。
- 不同阶段承担独立职责，保留追加式上下文，通过用户确认推进；已完成的旧阶段只读。
- 将历史文档解析、分片后接入 PostgreSQL / pgvector，并按团队与来源约束检索。
- 区分内部历史洞察和外部独立证据；来源选择与工具开放范围由工作流约束。
- 结合人设库与服务端 ID 校验，减少模型编造候选名单的问题。

## 技术与状态

TypeScript · Next.js · Agent 工具编排 · Prisma · PostgreSQL / pgvector。

脱敏快照位于私有资料仓库的独立项目目录，并有单独的文件清单与处理报告。公开介绍仅概述职责与设计，不公开企业数据、客户配置或交付文件；本次归档未重新执行原项目验收。
