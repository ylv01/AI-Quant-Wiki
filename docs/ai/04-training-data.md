# 训练数据

## 1. 主题简介

训练数据工程把来源各异的原始内容转化为可追溯、可切分和可评价的语料。数据质量、配比、重复和泄漏会直接改变模型行为与评价可信度。

## 2. 前置知识

- 文件格式、文本编码、哈希和基础数据处理
- [Token Engineering](03-token-engineering.md)中的词表、长度和样本格式

## 3. 核心概念

- 数据采集、许可、来源记录与数据谱系
- 解析、语言识别、清洗、精确去重与近似去重
- 质量过滤、安全过滤、污染检测
- 数据配比、数据混合、Curriculum 与采样权重
- Synthetic、Instruction 与 Preference Data
- Train、Validation、Test Split 及时间、来源、实体隔离
- Benchmark Contamination 与 Data Leakage

## 4. 推荐学习顺序

1. 先定义数据用途、许可、来源字段与可删除机制。
2. 建立解析和规范化流程，并保留原始数据的不可变引用。
3. 分别实施精确去重、近似去重与质量过滤，记录每步影响。
4. 按语言、领域和质量分层，设计透明的数据混合策略。
5. 在去重与过滤之后切分数据，并检查基准污染。
6. 用 Token 分布、长度、重复率和抽样审计评价处理结果。

## 5. 核心论文

- [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683)：C4 数据构建与文本到文本训练的代表性工作。
- [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499)：研究训练数据重复对语言模型与评价的影响。

## 6. 推荐开源仓库

- [Hugging Face Datasets](https://github.com/huggingface/datasets)：数据集加载、处理和流式读取的官方库。
- [Dolma](https://github.com/allenai/dolma)：AllenAI 用于大规模语言模型语料处理的官方工具集。

## 7. 推荐课程和官方文档

- [Hugging Face Datasets 文档](https://huggingface.co/docs/datasets/)：数据加载、映射、过滤与流式处理。
- [Stanford CS336](https://cs336.stanford.edu/)：覆盖语言模型数据处理与训练实践。

## 8. 建议实践

- 对一个可公开使用的小语料建立“原始 → 解析 → 规范化 → 去重 → 切分”流水线。
- 为每一步输出行数、Token 数、重复率、语言比例和随机样本。
- 向语料注入已知重复和测试短语，验证去重与污染检测能否发现它们。

## 9. 与其他主题的关系

本章承接 [Token Engineering](03-token-engineering.md)，向 [预训练](05-pretraining.md)、[微调](07-fine-tuning.md) 和 [后训练](08-post-training.md) 提供不同类型的数据。

## 10. 常见误区

- 数据量大不等于数据质量高或覆盖均衡。
- 随机切分不能自动防止同源文档或时间信息泄漏。
- 合成数据仍需追踪生成模型、提示、过滤规则和许可边界。
- 去重阈值越激进并不总越好，模板化内容和合法重复可能被误删。
