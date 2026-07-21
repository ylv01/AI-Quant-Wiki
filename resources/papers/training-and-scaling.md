# 训练与扩展规律核心论文

| 年份 | 论文 | 主题 | 推荐理由 | 难度 | 官方来源 |
|---:|---|---|---|---|---|
| 2017 | Decoupled Weight Decay Regularization | AdamW | 澄清自适应优化器中权重衰减与 L2 正则项的实现差异。 | 中级 | [arXiv](https://arxiv.org/abs/1711.05101) |
| 2019 | Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism | 模型并行 | 展示 Transformer 内部张量并行的切分方式和训练实践。 | 进阶 | [arXiv](https://arxiv.org/abs/1909.08053) |
| 2019 | ZeRO: Memory Optimizations Toward Training Trillion Parameter Models | 分布式内存 | 将参数、梯度和优化器状态的冗余拆分为可分析的阶段。 | 进阶 | [arXiv](https://arxiv.org/abs/1910.02054) |
| 2020 | Scaling Laws for Neural Language Models | 扩展规律 | 用经验关系讨论损失与模型规模、数据和算力的变化。 | 进阶 | [arXiv](https://arxiv.org/abs/2001.08361) |
| 2022 | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | 注意力系统优化 | 从显存层次和 IO 开销解释精确注意力的加速路径。 | 进阶 | [arXiv](https://arxiv.org/abs/2205.14135) |
