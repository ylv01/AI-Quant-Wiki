# 推理与服务部署

## 1. 主题简介

推理系统把模型权重和生成过程变成可测量、可限制资源的服务。先验证输出与生成语义，再讨论缓存、批处理、量化和调度；吞吐、延迟、显存与答案质量需要分别评价。

## 2. 前置知识

- [Transformer](02-transformer.md)中的自回归生成与 KV Cache
- [Context Engineering](10-context-engineering.md)中的 Token 预算与前缀缓存
- HTTP、并发、进程、GPU 内存和基础性能分析

## 3. 核心概念

- Prefill、Decode、KV Cache 与 PagedAttention
- Continuous Batching、请求排队、并发与调度
- Prefix Caching、缓存命中与多租户隔离
- 权重量化、激活量化、KV Cache 量化与精度损失
- Speculative Decoding、草稿模型、接受率与验证开销
- TTFT（首 Token 延迟）、TPOT（首 Token 后的平均每 Token 耗时）、ITL（Token 间延迟）、端到端延迟
- 输入/输出 Tokens/s、请求吞吐、显存峰值与错误率
- 服务超时、输入/输出长度上限、限流与可观测性

## 4. 推荐学习顺序

1. 对固定权重、Tokenizer、Chat Template 和采样配置建立单请求输出基线。
2. 区分 Prefill 与 Decode，测量短输入/长输入、短输出/长输出的成本。
3. 用同一工作负载比较串行请求与服务端批处理，记录排队时间和尾部延迟。
4. 逐项启用前缀缓存、量化或推测解码，分别检查速度、显存与任务质量。
5. 在固定请求到达率下做并发压力测试，并加入超时、取消和恢复场景。

## 5. 核心论文

- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)：连接 KV Cache 的分页管理、共享与服务端批处理。

## 6. 推荐开源仓库

- [vLLM](https://github.com/vllm-project/vllm)：官方推理与服务系统，包含服务接口、缓存管理和基准工具。
- [Transformers](https://github.com/huggingface/transformers)：用于检查生成、采样、Tokenizer 和缓存语义的基线实现。

## 7. 推荐课程和官方文档

- [vLLM Online Serving](https://docs.vllm.ai/en/latest/serving/online_serving/)：服务接口、启动与调用方式。
- [vLLM bench serve](https://docs.vllm.ai/en/latest/cli/bench/serve/)：负载生成、基准参数与服务指标。
- [Transformers Cache Strategies](https://huggingface.co/docs/transformers/kv_cache)：缓存类别与适用约束。

## 8. 建议实践

- 从官方服务与基准入口选择一个能在当前设备运行的小模型。冻结软件版本、模型 revision、硬件、Tokenizer、模板、采样参数和随机种子，保留请求输入及基准原始输出。
- 固定输入长度、输出长度和请求数，分别测试低/高并发以及缓存冷/热两种场景；报告 TTFT、TPOT、ITL、端到端延迟的中位数与 P95、输出吞吐、显存和错误率。
- 对一个确定的任务集逐项启用量化或推测解码，同时报告任务质量。固定预算并记录草稿模型的额外显存与计算，避免只比较生成速度。
- 现有仓库提供启动与测量工具；工作负载设计、硬件适配、质量评价和实验结果仍需实践者完成，本章不提供未经运行的性能结论。

## 9. 与其他主题的关系

本章承接 [Transformer](02-transformer.md) 和 [Context Engineering](10-context-engineering.md)，为 [RAG](09-rag.md)、[Agent](11-agent.md) 和 [生产 Pipeline](../ml-finance/10-production-pipeline.md) 提供模型服务基础。集中入口见 [推理与服务仓库](../../resources/repositories/inference-and-serving.md)。

## 10. 常见误区

- 只报总 Tokens/s 会掩盖 Prefill/Decode 差异、排队与尾部延迟。
- 量化后仍需重新评价质量，不能从显存下降直接推断效果不变。
- 推测解码的收益依赖接受率、草稿成本和负载，不保证所有场景加速。
- 共享缓存的性能设计不能替代服务端鉴权、隔离和资源限制。
