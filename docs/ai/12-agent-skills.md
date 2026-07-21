# Agent Skills、工具调用与 MCP

## 1. 主题简介

Agent Skill 是把可复用能力的说明、资源、工具和执行约束封装为可发现单元的工程模式；MCP 是连接 AI 应用与外部工具、资源和提示的开放协议。两者都需要明确能力边界、加载方式与权限控制。

## 2. 前置知识

- [Agent](11-agent.md)中的工具循环、状态机和沙箱
- JSON Schema、客户端/服务端、进程通信、HTTP 与认证基础

## 3. 核心概念

- Skill Definition、指令边界与适用条件
- Skill Packaging、版本、依赖和资源布局
- Skill Discovery、Routing、Loading 与冲突处理
- Tool Registry、Schema、能力协商和生命周期
- MCP Client、Server、Tools、Resources、Prompts 与 Transport
- Connector、Authentication、Permission Control 与审计
- Skill Evaluation、Harness Engineering 与 Long-Running Agent

## 4. 推荐学习顺序

1. 将一个已有工具封装为明确的名称、描述、输入和错误契约。
2. 定义 Skill 的触发条件、依赖资源、加载边界与评价样例。
3. 实现能力注册表和路由，处理名称冲突及不可用依赖。
4. 阅读 MCP 架构与核心原语，再运行官方参考 Server。
5. 在 Client 侧实施认证、允许列表、参数验证、超时和审计。
6. 为长任务加入检查点、恢复、幂等写入和人工接管。

## 5. 核心论文

- [Toolformer](https://arxiv.org/abs/2302.04761)：提供模型学习何时以及如何调用工具的研究视角。
- [ReAct](https://arxiv.org/abs/2210.03629)：理解推理、行动和观察的基础循环。

MCP 与 Skill Packaging 以协议规范和工程文档为主要来源，不将项目约定误写为学术共识。

## 6. 推荐开源仓库

- [MCP Specification and Documentation](https://github.com/modelcontextprotocol/modelcontextprotocol)：MCP 规范与文档仓库。
- [MCP Reference Servers](https://github.com/modelcontextprotocol/servers)：由 MCP Steering Group 维护的少量参考实现。
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)：官方 Python Client/Server SDK。
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)：官方交互式测试工具。

## 7. 推荐课程和官方文档

- [MCP Introduction](https://modelcontextprotocol.io/docs/getting-started/intro)：协议定位和架构入口。
- [MCP Specification](https://modelcontextprotocol.io/specification/latest)：协议规范。
- [MCP Build a Server](https://modelcontextprotocol.io/docs/develop/build-server)：官方 Server 入门。

## 8. 建议实践

- 用官方 SDK 创建只读资源 Server 和一个纯函数工具，并用 Inspector 检查交互。
- 为同一能力编写 Skill 描述、触发样例、反例和错误恢复用例。
- 测试未授权路径、恶意参数、超时、断线重连和重复请求。

## 9. 与其他主题的关系

本章建立在 [Agent](11-agent.md) 的工具循环之上，并把能力连接到 RAG、数据库、金融数据和执行系统；长任务的状态管理依赖 [Context Engineering](10-context-engineering.md) 与生产级日志。

## 10. 常见误区

- MCP 规定通信原语，不自动提供业务权限和安全策略。
- Skill、Tool、Prompt 和 Workflow 是不同抽象，不应混为同一文件格式。
- 能被发现的工具不等于应被自动授权执行。
- 长运行 Agent 不能仅依赖上下文窗口，需要外部持久状态和恢复语义。
