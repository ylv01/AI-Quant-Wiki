# 神经网络

## 1. 主题简介

神经网络通过可学习的非线性表示处理高维和序列数据。本章重点比较 MLP、卷积、循环和自编码结构，并要求它们在同一时间验证框架下与简单基线比较。

## 2. 前置知识

- [AI 基础](../ai/01-foundations.md)中的反向传播、损失和优化
- [统计与时间序列](01-statistics-and-time-series.md)与[验证与防泄漏](04-validation-and-leakage.md)

## 3. 核心概念

- MLP、非线性、正则化、Batch 与 Early Stopping
- CNN for Time Series、局部感受野与因果卷积
- RNN、隐藏状态、BPTT 与梯度问题
- LSTM、GRU 与门控记忆
- TCN、扩张卷积、残差与并行计算
- Autoencoder、瓶颈、重构与异常检测
- Representation Learning、预训练和迁移

## 4. 推荐学习顺序

1. 用 MLP 建立固定窗口特征基线。
2. 用一维 CNN 学习局部时间模式，并确保 Padding 不读取未来。
3. 实现 RNN，再理解 LSTM/GRU 对梯度与记忆的改进。
4. 比较 TCN 的因果卷积、感受野和并行性。
5. 用 Autoencoder 学习无监督表示，防止在全样本上拟合。
6. 在相同切分、输入和成本假设下比较全部结构。

## 5. 核心论文

- [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735)：LSTM 的原始论文。
- [An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling](https://arxiv.org/abs/1803.01271)：系统比较 TCN 与循环结构的代表性工作。
- [Reducing the Dimensionality of Data with Neural Networks](https://doi.org/10.1126/science.1127647)：深层自编码器表征学习的经典论文。

## 6. 推荐开源仓库

- [PyTorch](https://github.com/pytorch/pytorch)：神经网络、优化器与序列模块的官方实现。
- [Qlib](https://github.com/microsoft/qlib)：包含多类量化深度学习基线和统一工作流。

## 7. 推荐课程和官方文档

- [PyTorch Sequence Models Tutorial](https://docs.pytorch.org/tutorials/beginner/nlp/sequence_models_tutorial.html)：LSTM 序列模型官方教程。
- [Stanford CS231n](https://cs231n.stanford.edu/)：神经网络、卷积、优化与表示基础。

## 8. 建议实践

- 在相同固定窗口数据上比较线性模型、MLP、CNN、LSTM 与 TCN。
- 可视化每种结构的有效感受野并测试输入末端的未来值污染。
- 在每个训练窗口内拟合标准化器和 Autoencoder，再应用到验证期。

## 9. 与其他主题的关系

本章从 [树模型](05-tree-models.md) 基线进入序列表征，并为 [金融 Transformer](07-transformers-for-finance.md) 提供卷积、循环和表示学习对照。

## 10. 常见误区

- 序列模型接收时间序列不代表自动遵守因果方向。
- 更长输入窗口可能增加噪声和参数，不保证有效记忆更长。
- Autoencoder 重构误差低不等于表示适合收益预测。
- 深度模型多次调参后与一次训练的简单基线比较并不公平。
