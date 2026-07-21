# AI 基础

## 1. 主题简介

本章建立阅读和实现神经网络所需的编程、数学与优化基础，目标是理解数据如何经过前向计算、损失函数和反向传播更新参数。

## 2. 前置知识

- 基本命令行、Git 与 Python 语法
- 高中代数、函数和求导直觉

## 3. 核心概念

- Python 数据结构、NumPy 数组、广播和向量化
- PyTorch Tensor、自动微分、Dataset 与 DataLoader
- 向量、矩阵、范数、特征值和矩阵乘法
- 概率分布、期望、方差、条件概率与最大似然
- 导数、偏导、链式法则和梯度
- 神经元、激活函数、计算图、反向传播
- MSE、交叉熵、梯度下降、Momentum、AdamW

## 4. 推荐学习顺序

1. 用 NumPy 熟悉张量形状、广播和批量矩阵运算。
2. 推导线性回归、逻辑回归和两层 MLP 的损失与梯度。
3. 先手写反向传播，再与 PyTorch Autograd 结果对照。
4. 使用 Dataset、优化器和验证集组成可复现的最小训练循环。
5. 比较学习率、初始化、正则化和损失函数对训练动态的影响。

## 5. 核心论文

- [Learning representations by back-propagating errors](https://www.nature.com/articles/323533a0)：理解反向传播作为多层网络训练基础的经典论文。
- [Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101)：说明 AdamW 中权重衰减与梯度正则项的区别。

## 6. 推荐开源仓库

- [PyTorch](https://github.com/pytorch/pytorch)：张量、自动微分、训练与分布式能力的官方实现。
- [NumPy](https://github.com/numpy/numpy)：数组计算与向量化操作的官方仓库。

## 7. 推荐课程和官方文档

- [PyTorch Tutorials](https://docs.pytorch.org/tutorials/)：从张量和自动微分进入完整训练流程。
- [Stanford CS231n](https://cs231n.stanford.edu/)：神经网络、优化和视觉建模课程。
- [NumPy User Guide](https://numpy.org/doc/stable/user/)：数组、广播、索引和线性代数参考。

## 8. 建议实践

- 只用 NumPy 实现两层分类网络，并做数值梯度检查。
- 用 PyTorch 重写相同模型，记录训练损失、验证损失和梯度范数。
- 固定随机种子，对比 SGD、Momentum 与 AdamW 的收敛曲线。

## 9. 与其他主题的关系

张量形状、交叉熵和反向传播是 [Transformer](02-transformer.md) 的直接前置；优化器和训练循环会在 [预训练](05-pretraining.md) 中扩展到语言模型。

## 10. 常见误区

- 自动微分能计算梯度，不等于可以忽略链式法则与计算图。
- 训练损失下降不代表泛化性能提升。
- 广播虽然语法简洁，但错误形状可能产生不报错的错误计算。
- 权重衰减、L2 正则化和梯度裁剪解决的是不同问题。
