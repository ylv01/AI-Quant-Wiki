# AI / LLM 学习路线

本路线从数学、编程和神经网络出发，逐步进入 Transformer、数据与训练系统，再延伸到微调、RAG、Agent、MCP 与多模态。推荐先用小规模实验理解机制，再阅读大型系统的工程设计。

## 阶段导航

1. [基础](01-foundations.md)：Python、NumPy、PyTorch、数学、反向传播与优化。
2. [Transformer](02-transformer.md)：注意力、掩码、解码器和自回归生成。
3. [Token Engineering](03-token-engineering.md)：子词算法、词表、模板与序列组织。
4. [训练数据](04-training-data.md)：采集、清洗、去重、混合、切分与泄漏。
5. [预训练](05-pretraining.md)：目标函数、训练循环、优化器与扩展规律。
6. [训练系统](06-training-systems.md)：GPU、分布式并行、内存与吞吐优化。
7. [微调](07-fine-tuning.md)：持续预训练、SFT、LoRA、QLoRA 与评价。
8. [后训练](08-post-training.md)：偏好学习、RLHF、DPO 及奖励评价。
9. [RAG](09-rag.md)：解析、检索、重排、上下文和引用评价。
10. [Context Engineering](10-context-engineering.md)：上下文选择、缓存、记忆和状态。
11. [Agent](11-agent.md)：工具调用、规划、工作流、安全执行与评价。
12. [Agent Skills、工具调用与 MCP](12-agent-skills.md)：能力封装、发现、路由、权限与协议。
13. [多模态](13-multimodal.md)：视觉、文本、音频、视频和多模态 Agent。
14. [推理与服务部署](14-inference-and-serving.md)：生成阶段、缓存、批处理、量化与服务测量。

## 建议入口

- 具备机器学习基础：从 Transformer 开始，但应确认能独立写出反向传播与训练循环。
- 具备 NLP 基础：从 Token Engineering 和 Decoder-only Transformer 开始。
- 关注应用系统：先理解生成与评价，再结合推理与服务部署进入 RAG、Context 与 Agent；推理章节可在 Transformer 与 Context 基础后提前学习。
- 关注训练基础设施：完成预训练最小闭环后进入训练系统，避免只学习并行名词。

## 与金融路线的交汇

AI 路线在 [金融 Transformer](../ml-finance/07-transformers-for-finance.md) 与文本、时序和多模态金融任务连接；训练与 Agent 方法则在 [生产 Pipeline](../ml-finance/10-production-pipeline.md) 中连接到数据、风险控制和执行系统。

论文、仓库和课程的集中索引见 [资源总览](../../resources/papers/README.md)。
