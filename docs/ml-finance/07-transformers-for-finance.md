# 金融 Transformer

## 1. 主题简介

金融 Transformer 将注意力用于价格序列、横截面资产、新闻文本、公告、图表和表格。本章强调 Token 定义、时间因果性、跨资产结构和多模态对齐。

## 2. 前置知识

- [Transformer](../ai/02-transformer.md)与[Token Engineering](../ai/03-token-engineering.md)
- [统计与时间序列](01-statistics-and-time-series.md)及严格时间验证

## 3. 核心概念

- Time-Series Tokenization、连续值嵌入与离散化
- Positional/Temporal Encoding、日历和不规则间隔
- Temporal Attention 与 Causal Mask
- Cross-Asset Attention、资产身份和动态图结构
- Patch-based Modeling 与 Multi-scale Modeling
- Forecasting、Classification 与预训练目标
- Financial Language Models、文本时间戳和实体对齐
- Multimodal Financial Models：时序、文本、表格和图像

## 4. 推荐学习顺序

1. 用标准 Decoder/Encoder 在合成序列上验证位置和掩码。
2. 比较逐点、窗口/Patch 和离散化 Token 表示。
3. 建立时间注意力基线，再加入多尺度结构。
4. 将资产维度显式建模，处理上市、退市和缺失资产。
5. 对齐新闻/公告的发布时间、实体与市场数据。
6. 最后进入多模态，并与树模型、TCN 和简单注意力基线比较。

## 5. 核心论文

- [Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting](https://arxiv.org/abs/1912.09363)：多步预测、变量选择和可解释组件的代表性工作。
- [A Time Series is Worth 64 Words](https://arxiv.org/abs/2211.14730)：PatchTST 的 Patch 与通道独立设计。
- [FinBERT: Financial Sentiment Analysis with Pre-trained Language Models](https://arxiv.org/abs/1908.10063)：金融文本领域预训练与情感任务的代表性工作。

## 6. 推荐开源仓库

- [PatchTST](https://github.com/yuqinie98/PatchTST)：论文作者发布的官方实现。
- [Transformers](https://github.com/huggingface/transformers)：文本、时序和多模态 Transformer 接口。
- [Qlib](https://github.com/microsoft/qlib)：统一数据、模型和回测的量化研究平台。

## 7. 推荐课程和官方文档

- [Stanford CS224N](https://web.stanford.edu/class/cs224n/)：Transformer 与语言模型基础。
- [Transformers Documentation](https://huggingface.co/docs/transformers/)：模型、训练与多模态接口参考。
- [Qlib Model Documentation](https://qlib.readthedocs.io/en/latest/component/model.html)：量化预测模型集成说明。

## 8. 建议实践

- 在同一时序数据上比较线性、LightGBM、TCN 和 Patch Transformer。
- 用合成“未来脉冲”测试 Causal Mask、窗口构造和归一化是否泄漏。
- 将带发布时间的新闻与资产对齐，比较文本单模态、时序单模态和融合模型。

## 9. 与其他主题的关系

本章是 AI 与金融路线的主要交汇点：模型结构来自 [Transformer](../ai/02-transformer.md)，数据和评价受 [金融数据工程](../finance/08-financial-data-engineering.md) 与 [验证与防泄漏](04-validation-and-leakage.md) 约束，输出进入 [回测](08-backtesting.md)。

## 10. 常见误区

- 把连续数值称为 Token 不代表它具有自然语言 Token 的统计性质。
- Cross-Asset Attention 若使用未来成分股会引入生存偏差。
- 文本发布日期不一定等于市场可获得时间。
- 注意力热图不能直接解释收益预测的因果来源。
