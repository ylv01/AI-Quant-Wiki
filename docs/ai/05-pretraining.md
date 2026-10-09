# 预训练

## 1. 主题简介

预训练通过大规模下一 Token 预测让模型学习语言和世界知识。本章连接模型、数据、优化器、数值精度、检查点和算力分配。

## 2. 前置知识

- [Transformer](02-transformer.md)与[训练数据](04-training-data.md)
- PyTorch 训练循环、概率分布、交叉熵和优化基础

## 3. 核心概念

- GPT 与 Autoregressive Objective
- Token Shift、Cross Entropy、Perplexity 与训练循环
- AdamW、Muon 及优化器状态
- Learning Rate Schedule、Warmup、Weight Decay
- Gradient Clipping、Gradient Accumulation、Mixed Precision
- Checkpoint、恢复语义和随机状态
- Scaling Laws 与 Compute-Optimal Training

## 4. 推荐学习顺序

1. 在单卡或 CPU 上闭环一个小型自回归语言模型。
2. 检查输入与标签错位、损失归一化和验证集 Perplexity。
3. 逐步加入 Warmup、学习率退火、梯度裁剪和累积。
4. 比较 FP32、BF16/FP16 的数值行为，并保存可恢复检查点。
5. 在固定算力预算下比较模型大小、Token 数和训练步数。
6. 阅读 AdamW 与 Muon 的原始说明，避免仅凭名称互换优化器。

## 5. 核心论文

- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)：理解大规模自回归预训练的代表性工作。
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)：研究损失与模型、数据和算力的经验关系。
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)：讨论固定算力下模型规模与训练 Token 的配置。

## 6. 推荐开源仓库

- [nanoGPT](https://github.com/karpathy/nanoGPT)：已标记弃用的经典 GPT 训练代码，适合分析最小训练循环。
- [nanochat](https://github.com/karpathy/nanochat)：原作者维护的后续仓库，提供 Tokenizer、预训练、微调、评价和推理的实验流程。
- [llm.c](https://github.com/karpathy/llm.c)：用 C/CUDA 展示 GPT 训练底层路径的原作者仓库。
- [PyTorch](https://github.com/pytorch/pytorch)：优化器、混合精度和检查点能力的官方实现。

## 7. 推荐课程和官方文档

- [Stanford CS336](https://cs336.stanford.edu/)：覆盖数据、模型、优化、系统和扩展规律。
- [PyTorch Automatic Mixed Precision](https://docs.pytorch.org/docs/stable/amp.html)：混合精度官方参考。
- [PyTorch Saving and Loading Models](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html)：检查点基础语义。

## 8. 建议实践

- 训练一个小型 GPT，并证明它能过拟合极小批次。
- 做学习率范围、梯度范数和不同累积步数的对照实验。
- 在任意中间步保存并恢复，验证后续损失与随机采样能够按预期延续。

## 9. 与其他主题的关系

预训练把数据和 Transformer 连接起来；规模扩大后进入 [训练系统](06-training-systems.md)，已有基座模型再进入 [微调](07-fine-tuning.md) 与 [后训练](08-post-training.md)。

## 10. 常见误区

- Perplexity 只能在相同 Tokenizer 和评价口径下直接比较。
- 梯度累积不保证与大批量训练完全等价，归一化和随机层会产生差异。
- 混合精度节省资源不等于所有算子都应使用低精度。
- Scaling Laws 是经验关系，不是忽略数据质量和系统瓶颈的理由。
