# Agent Skills、工具调用与 MCP

## 1. 主题简介

Agent Skill 是把可复用能力的说明、资源、工具和执行约束封装为可发现单元的工程模式；MCP 是连接 AI 应用与外部工具、资源和提示的开放协议。两者都需要明确能力边界、加载方式与权限控制。Agent Skills 开放格式用包含 `SKILL.md` 的目录承载元数据和操作说明；它与 MCP 的工具连接职责不同，实际加载和授权仍取决于客户端实现。

## 2. 前置知识

- [Agent](11-agent.md)中的工具循环、状态机和沙箱
- JSON Schema、客户端/服务端、进程通信、HTTP 与认证基础

## 3. 核心概念

- Skill Definition、指令边界与适用条件
- Skill Packaging、版本、依赖和资源布局
- `SKILL.md`、YAML Frontmatter、`name`、`description` 与目录约束
- Progressive Disclosure：元数据发现、正文激活与资源按需加载
- Skill Discovery、Routing、Loading 与冲突处理
- Tool Registry、Schema、能力协商和生命周期
- MCP Client、Server、Tools、Resources、Prompts 与 Transport
- Connector、Authentication、Permission Control 与审计
- Skill Evaluation、Harness Engineering 与 Long-Running Agent

## 4. 推荐学习顺序

1. 将一个已有工具封装为明确的名称、描述、输入和错误契约。
2. 按 Agent Skills 规范编写 `SKILL.md`，让 `description` 说明能力及触发条件，并按需组织 `scripts/`、`references/` 和 `assets/`。
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
- [Agent Skills](https://github.com/agentskills/agentskills)：开放格式的规范、文档及演示用 Python 参考校验库 `skills-ref`。

## 7. 推荐课程和官方文档

- [Agent Skills Specification](https://agentskills.io/specification)：目录、Frontmatter、渐进加载与格式校验的官方规范。
- [MCP Specification](https://modelcontextprotocol.io/specification/latest)：协议规范。
- [MCP Build a Server](https://modelcontextprotocol.io/docs/develop/build-server)：官方 Server 入门。

## 8. 建议实践

- 用官方 SDK 创建只读资源 Server 和一个纯函数工具，并用 Inspector 检查交互。
- 为同一能力创建下面的最小 Skill，再增加触发样例、反例和错误恢复用例。安装官方仓库中的 `skills-ref` 后，运行 `skills-ref validate ./skills/table-audit`，或使用其 Python API 验证格式；该参考库是演示实现，不是生产授权系统。
- 测试未授权路径、恶意参数、超时、断线重连和重复请求。

```text
skills/table-audit/
└── SKILL.md
```

`SKILL.md` 示例：

```markdown
---
name: table-audit
description: 检查表格数据中的缺失值和重复记录；在用户要求数据质量检查时使用。
---

读取用户指定的数据，报告缺失值与重复记录，并说明统计口径。
```

Python 校验示例：

```python
from pathlib import Path
from skills_ref import validate

problems = validate(Path("skills/table-audit"))
if problems:
    raise ValueError(problems)
```

## 9. 与其他主题的关系

本章建立在 [Agent](11-agent.md) 的工具循环之上，并把能力连接到 RAG、数据库、金融数据和执行系统；长任务的状态管理依赖 [Context Engineering](10-context-engineering.md) 与生产级日志。

## 10. 常见误区

- MCP 规定通信原语，不自动提供业务权限和安全策略。
- Skill、Tool、Prompt 和 Workflow 是不同抽象，不应混为同一文件格式。
- 能被发现的工具不等于应被自动授权执行。
- 长运行 Agent 不能仅依赖上下文窗口，需要外部持久状态和恢复语义。
- 格式校验通过不代表 Skill 可信；脚本执行、外部访问和工具权限仍应由运行环境控制。
