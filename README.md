<p align="center">
  <img src="assets/hero.svg" width="100%" alt="秦嘉言 Jiayan Qin · Full-stack Agent Developer · From context to action" />
</p>

<p align="center">
  <a href="README.en.md">English</a> · <a href="#selected-work">精选项目</a> · <a href="#experience">实践经历</a> · <a href="mailto:qjyvictory@163.com">联系我 ↗</a>
</p>

# 你好，我是秦嘉言。

**全栈 Agent 开发者，把模型能力接进真实业务。**

我关注 Agent 从理解上下文到可靠执行的完整链路：记忆与检索、工作流编排、工具调用，以及用户真正能用起来的产品界面。目前在 **特赞 Tezign** 从事全栈 Agent 开发实习。

- **正在做**：EchoAgent，一套围绕人物记忆、表达风格和可控工具执行构建的个人 Agent 工作台。
- **实践方向**：多阶段研究 Agent、企业知识库 RAG、多模态订单交互、SSO / IAM 与私有化交付。
- **教育背景**：北京交通大学 · 计算机科学与技术本科（2022–2026）；澳大利亚国立大学 · 计算机科学硕士已获录取（2027 年 7 月入学）。
- **交流与机会**：欢迎交流 Agent / RAG / 全栈工程，也欢迎长期实习机会，可实习至 2027 年 7 月。

> 我希望做的 Agent：知道依据在哪里，知道什么时候该停，也能把任务交付完。

<a id="selected-work"></a>

## 01 / Selected work

### EchoAgent · 有记忆、有边界的个人 Agent

<a href="projects/echoagent.md"><img src="assets/echoagent.svg" width="100%" alt="EchoAgent：授权资料经过记忆与风格检索，进入 Agent 工作流，再由用户确认工具执行。当前为开发中原型。" /></a>

从授权资料建立人物记忆与表达风格，让回答有来源，让工具执行经过确认。重点探索 **记忆与风格分离、来源隔离、可撤回的数据和可追踪的执行过程**。

`Python` `FastAPI` `LangGraph` `React` `TypeScript` `PostgreSQL` `pgvector` `Docker`

- **产品**：统一的聊天、人设、记忆、资料导入、反馈和费用工作台。
- **工程**：混合检索、时序事实、会话持久化、工具审批与执行追踪。
- **当前阶段**：开发中原型；已有合成数据演示与工程验证，完整 Live 验收及正式版本发布尚未完成。语音和数字人形象属于后续方向。

**[阅读项目介绍 ↗](projects/echoagent.md)** · [源码仓库（私有，需授权）](https://github.com/QinJiayan-maker/virtual-human)

### 视觉目标跟踪 · 从识别到云台控制

将 YOLO 检测、NanoTrack 跟踪与卡尔曼滤波接入实时视频流程，通过串口联动 STM32 舵机，并提供桌面与 Web 两种交互方式。

`Python` `OpenCV` `YOLO` `NanoTrack` `STM32`

**[阅读项目介绍 ↗](projects/visual-tracking.md)** · 本地项目，源码尚未在此主页发布。

<a id="experience"></a>

## 02 / Applied engineering

以下是我的项目实践与实习经历摘要；企业项目仅展示职责与技术思路。

**特赞 Tezign · 全栈 Agent 开发实习生**  
2026.05 – 至今

- **研究交付平台**：参与七阶段多 Agent 研究流程，以状态机、阶段确认和可回溯引用组织研究；结合 PostgreSQL / pgvector 建设团队知识库，区分历史结论与独立证据。
- **企业数字资产管理**：参与企业 SSO 与网关鉴权、多模态素材检索及私有化部署，涉及 Milvus、ETCD 和对象存储签名访问。

**智能订单 Agent · 项目实践**  
2026.02 – 2026.04

- 基于 Next.js H5 支持语音、文字和拍照改单，以 SKU / 单位校验、工具步数限制和待确认状态约束执行。
- 衔接订单草稿、会话与调用日志、原生下单页；完成 IAM 登录与组织同步相关对接。

**北京市计算中心 · Java 工程师实习**  
2024.07 – 2024.09

- 基于 Spring Boot / MyBatis Plus 参与数字藏品平台后端，完成藏品分页筛选及用户基础接口。

## 03 / Toolkit

**Agent & retrieval**  
工具调用 · 状态机编排 · Prompt 设计 · RAG · pgvector · Milvus

**Full-stack delivery**  
TypeScript · React · Next.js · Python / FastAPI · Java / Spring Boot

**Data & integration**  
PostgreSQL · MySQL · Redis · SSO / IAM · Docker · OSS

## 04 / Let's build something useful

我对有真实使用场景的 Agent 产品、可靠的检索与记忆系统，以及从前端到服务端的完整交付感兴趣。

**[qjyvictory@163.com](mailto:qjyvictory@163.com)** · [GitHub](https://github.com/QinJiayan-maker)

---

<sub>From context to action. Built with evidence, shipped with care.</sub>
