# Context Engineering

## 1. 主题简介

Context Engineering 将提示、检索证据、工具结果、记忆和会话状态组织进有限上下文窗口。目标是让模型在正确时刻看到最相关、可信且结构清晰的信息。

## 2. 前置知识

- [Transformer](02-transformer.md)中的位置、注意力与 KV Cache
- [RAG](09-rag.md)中的检索、重排和压缩

## 3. 核心概念

- Prompt Structure、System Prompt 与指令层级
- Context Window、Long Context 与位置效应
- Context Selection、Compression、Ordering 与去重
- Context Caching、Prefix Cache 与 KV Cache
- Conversation State、Working Memory、Retrieval Memory
- 摘要、状态快照、来源追踪与 Context Evaluation

## 4. 推荐学习顺序

1. 把系统指令、用户输入、证据、工具结果和输出约束分层。
2. 计算 Token 预算并定义各类上下文的优先级。
3. 比较截断、检索选择、摘要和结构化压缩。
4. 区分 KV Cache、前缀缓存、会话状态和持久记忆。
5. 设计跨轮状态更新及冲突处理规则。
6. 用长上下文定位、证据使用和指令遵循测试评价编排策略。

## 5. 核心论文

- [Transformer-XL](https://arxiv.org/abs/1901.02860)：研究跨片段循环记忆与长依赖。
- [Longformer](https://arxiv.org/abs/2004.05150)：使用局部与全局稀疏注意力扩展上下文。
- [Lost in the Middle](https://arxiv.org/abs/2307.03172)：分析相关信息位置对长上下文使用的影响。

## 6. 推荐开源仓库

- [Transformers](https://github.com/huggingface/transformers)：可检查长上下文模型、生成与 Cache 接口。
- [vLLM](https://github.com/vllm-project/vllm)：面向高吞吐推理和 KV Cache 管理的官方仓库。

## 7. 推荐课程和官方文档

- [Transformers Cache Strategies](https://huggingface.co/docs/transformers/kv_cache)：生成缓存策略官方说明。
- [vLLM Documentation](https://docs.vllm.ai/)：推理、调度与缓存相关文档。

## 8. 建议实践

- 构造关键信息位于开头、中间和末尾的长上下文测试集。
- 在相同 Token 预算下比较完整拼接、检索选择和摘要压缩。
- 为多轮任务显式保存结构化状态，测试中断恢复和冲突信息处理。

## 9. 与其他主题的关系

本章接收 [RAG](09-rag.md) 的证据并为 [Agent](11-agent.md) 编排状态、工具结果和记忆；KV Cache 的系统实现与 [训练系统](06-training-systems.md) 中的内存和吞吐分析相连。

## 10. 常见误区

- 上下文窗口足够长不代表模型能同等利用所有位置。
- KV Cache 是推理中间状态，不等于长期记忆。
- 摘要会丢失信息，不能只评价压缩率。
- System Prompt 不是安全边界，权限仍需由外部系统强制执行。
