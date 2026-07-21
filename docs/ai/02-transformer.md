# Transformer

## 1. 主题简介

Transformer 用注意力在序列位置之间传递信息。本章聚焦 Decoder-only 架构，解释从 Token Embedding 到自回归生成的完整计算路径。

## 2. 前置知识

- [AI 基础](01-foundations.md)中的矩阵乘法、Softmax、交叉熵和反向传播
- 序列建模与语言模型的基本概念

## 3. 核心概念

- Token Embedding 与 Position Encoding
- Query、Key、Value 及 Scaled Dot-Product Attention
- Multi-Head Attention、Causal Mask 与注意力张量形状
- Residual Connection、LayerNorm、MLP
- Decoder-only Transformer、Logits 与 Cross Entropy
- Teacher Forcing、自回归生成、Temperature 与采样

## 4. 推荐学习顺序

1. 手工计算单个注意力头的 Q、K、V、分数和加权求和。
2. 加入缩放、因果掩码和多头拼接，并逐项检查张量形状。
3. 组合 Pre-Norm 残差块与 MLP，形成 Decoder Block。
4. 连接词嵌入、语言模型头和下一 Token 交叉熵。
5. 实现缓存前后的自回归生成，比较贪心与随机采样。

## 5. 核心论文

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)：注意力与 Transformer 架构的基础论文。
- [Layer Normalization](https://arxiv.org/abs/1607.06450)：理解 Transformer 中归一化机制的原始工作。
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)：连接 Decoder-only 语言模型、规模和上下文学习。

## 6. 推荐开源仓库

- [minGPT](https://github.com/karpathy/minGPT)：原作者风格的紧凑 GPT 教学实现。
- [nanoGPT](https://github.com/karpathy/nanoGPT)：适合追踪小型 GPT 的训练和生成代码路径。
- [Transformers](https://github.com/huggingface/transformers)：模型定义、训练和推理的官方框架仓库。

## 7. 推荐课程和官方文档

- [Stanford CS224N](https://web.stanford.edu/class/cs224n/)：覆盖深度 NLP、注意力和 Transformer。
- [Stanford CS336](https://cs336.stanford.edu/)：从零实现语言模型并连接数据、系统和扩展规律。
- [PyTorch Transformer 教程](https://docs.pytorch.org/tutorials/beginner/transformer_tutorial.html)：官方序列建模示例。

## 8. 建议实践

- 实现一个字符级 Decoder-only Transformer，在极小文本上验证过拟合能力。
- 可视化因果掩码并确认每个位置不能读取未来 Token。
- 对相同前缀比较无 KV Cache 与有 KV Cache 的逐 Token 输出一致性。

## 9. 与其他主题的关系

Transformer 接收 [Token Engineering](03-token-engineering.md) 产生的序列，在 [预训练](05-pretraining.md) 中学习参数，并作为 [金融 Transformer](../ml-finance/07-transformers-for-finance.md) 的结构基础。

## 10. 常见误区

- 注意力权重不是因果解释。
- Causal Mask 与 Padding Mask 的目的不同。
- 多头注意力不是简单重复同一个注意力头。
- 训练时并行计算全部位置，不等于推理时可以并行生成未来 Token。
