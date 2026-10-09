# 训练系统

## 1. 主题简介

训练系统研究如何在 GPU 集群上可靠、高效地执行模型训练。核心是在显存、计算、通信和容错之间做可测量的权衡。

## 2. 前置知识

- [预训练](05-pretraining.md)的训练循环、优化器状态和检查点
- GPU、进程、网络通信与基础性能分析概念

## 3. 核心概念

- GPU、CUDA、Kernel、显存层次与异步执行
- Data Parallelism、DDP、FSDP2、DTensor 与 ZeRO
- Tensor Parallelism、Pipeline Parallelism 与混合并行
- FlashAttention、Activation Checkpointing、Kernel Fusion
- All-Reduce、通信开销、计算通信重叠
- Throughput、Latency、Tokens/s、MFU 与显存峰值
- Distributed Checkpoint、故障恢复与拓扑

## 4. 推荐学习顺序

1. 分析单卡时间、显存和算子占比，建立正确性基线。
2. 使用 DDP 理解梯度同步和全局批量大小。
3. 学习 FSDP2/ZeRO 如何切分参数、梯度与优化器状态；区分旧 FSDP1 包装 API 与 FSDP2 的 `fully_shard` 接口。
4. 当单个算子或层无法放入设备时，再进入张量和流水线并行。
5. 用 FlashAttention、激活重计算和融合优化局部瓶颈。
6. 设计分布式检查点、失败恢复和多规模一致性测试。

## 5. 核心论文

- [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053)：理解模型并行的代表性工作。
- [ZeRO](https://arxiv.org/abs/1910.02054)：系统化切分训练状态以降低数据并行显存开销。
- [FlashAttention](https://arxiv.org/abs/2205.14135)：从 IO 复杂度理解精确注意力加速。

## 6. 推荐开源仓库

- [PyTorch](https://github.com/pytorch/pytorch)：DDP、FSDP2、Profiler 与分布式检查点的官方实现。
- [DeepSpeed](https://github.com/deepspeedai/DeepSpeed)：ZeRO 与大模型训练系统的官方仓库。
- [Megatron-LM](https://github.com/NVIDIA/Megatron-LM)：NVIDIA 的大模型并行训练仓库。
- [FlashAttention](https://github.com/Dao-AILab/flash-attention)：论文作者维护的实现。

## 7. 推荐课程和官方文档

- [PyTorch Distributed Overview](https://pytorch.org/tutorials/beginner/dist_overview.html)：官方分布式组件导航。
- [PyTorch FSDP2 教程](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)：`fully_shard`、DTensor、检查点与 FSDP1 迁移说明；官方已将 FSDP1 标为弃用。
- [NVIDIA CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)：CUDA 执行和内存模型参考。

## 8. 建议实践

- 对同一小模型比较单卡与两进程 DDP 的损失一致性和吞吐。
- 分别记录 DDP、FSDP2 的参数、梯度、优化器状态及激活显存。
- 用 Profiler 找出算子和通信瓶颈，再验证一种优化是否真正提高 Tokens/s。

## 9. 与其他主题的关系

本章扩展 [预训练](05-pretraining.md) 和 [微调](07-fine-tuning.md)；推理阶段的 KV Cache 与吞吐问题在 [Context Engineering](10-context-engineering.md) 中继续出现。

## 10. 常见误区

- 并行度增加不保证吞吐线性增加。
- 峰值显存下降与训练速度提升是两个不同目标。
- MFU 的计算口径依赖硬件峰值与模型 FLOPs 定义。
- FlashAttention 改变计算实现，不改变标准注意力的数学结果。
