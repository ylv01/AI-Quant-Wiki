# Agent

## 1. 主题简介

Agent 将模型置于“观察—决策—调用工具—更新状态”的循环中，用于完成需要外部操作或多步推理的任务。可靠性来自工具契约、状态机、权限和评价，而不只来自提示词。

## 2. 前置知识

- [Context Engineering](10-context-engineering.md)与结构化输出
- API、异常处理、幂等性、权限和基本软件测试

## 3. 核心概念

- Tool Calling、Function Calling 与参数 Schema
- ReAct、Planning、Reflection 与任务分解
- Memory、Workflow、State Machine 与事件日志
- 单 Agent 与 Multi-Agent 的通信和职责边界
- Agent Evaluation、轨迹评价与任务成功率
- Sandboxed Execution、最小权限、确认与 Human in the Loop

## 4. 推荐学习顺序

1. 从一个只读、确定性工具开始，定义输入、输出和错误 Schema。
2. 实现有步数上限的工具循环，并保存完整事件轨迹。
3. 使用状态机表达分支、重试、回滚和终止条件。
4. 再加入规划、反思和记忆，逐项验证是否带来收益。
5. 对写入、网络和代码执行设置沙箱、权限与人工确认。
6. 建立任务集，评价成功率、成本、延迟、错误恢复和安全性。

## 5. 核心论文

- [ReAct](https://arxiv.org/abs/2210.03629)：将推理轨迹与外部行动交错的代表性工作。
- [Toolformer](https://arxiv.org/abs/2302.04761)：研究模型自监督学习工具调用的方法。
- [AgentBench](https://arxiv.org/abs/2308.03688)：面向多环境 Agent 能力评价的基准工作。

## 6. 推荐开源仓库

- [smolagents](https://github.com/huggingface/smolagents)：Hugging Face 的轻量 Agent 库。
- [AutoGen](https://github.com/microsoft/autogen)：已进入维护模式的事件驱动 Agent 框架，可用于阅读已有系统和理解消息运行时。
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)：Microsoft 面向新项目推荐的后续框架，连接 Agent、工具与多步工作流。
- [LangGraph](https://github.com/langchain-ai/langgraph)：用图和状态构建长运行工作流的官方仓库。

## 7. 推荐课程和官方文档

- [smolagents Documentation](https://huggingface.co/docs/smolagents/)：工具、Agent 和执行模型说明。
- [AutoGen → Microsoft Agent Framework 迁移指南](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/)：新旧抽象、工具与工作流的官方迁移说明。
- [LangGraph Documentation](https://docs.langchain.com/oss/python/langgraph/overview)：状态图和持久化工作流入口。

## 8. 建议实践

- 构建只读文件检索 Agent，工具参数使用 JSON Schema 并限制根目录。
- 注入超时、无结果、参数错误和工具异常，验证重试与终止条件。
- 对确定性 Workflow、ReAct Agent 和多 Agent 方案比较成功率、调用数与延迟。

## 9. 与其他主题的关系

Agent 使用 [RAG](09-rag.md) 作为知识工具，依赖 [Context Engineering](10-context-engineering.md) 管理状态，并在 [Agent Skills、工具调用与 MCP](12-agent-skills.md) 中进一步标准化能力发现和连接。

## 10. 常见误区

- 多 Agent 不天然优于清晰的单 Agent 或确定性 Workflow。
- Reflection 生成更多文本不等于纠正了错误。
- 模型拒绝执行不是权限控制，真实权限必须由运行环境实施。
- 只评价最终答案会遗漏危险工具调用和不可恢复的中间状态。
