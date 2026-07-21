# 因子与特征工程

## 1. 主题简介

因子与特征工程把价格、基本面和市场结构信息转化为模型输入。金融特征必须同时说明经济含义、计算窗口、横截面处理和真实可用时间。

## 2. 前置知识

- [统计与时间序列](01-statistics-and-time-series.md)
- [金融数据工程](../finance/08-financial-data-engineering.md)与[投资组合理论](../finance/05-portfolio-theory.md)

## 3. 核心概念

- Momentum、Value、Quality、Volatility 与 Liquidity
- Technical Indicators 与 Fundamental Factors
- 时间序列特征与 Cross-sectional Rank
- Winsorization、Standardization 与缺失值处理
- 行业、规模、Beta 等 Neutralization
- Feature Selection、共线性与多重检验
- Feature Stability、IC、分组收益与换手

## 4. 推荐学习顺序

1. 为每个特征写出经济假设、公式、窗口和数据可用时间。
2. 从收益、波动、成交量等透明特征开始。
3. 加入横截面排序、标准化和极值处理。
4. 明确中性化变量和回归方向，保存处理前后暴露。
5. 在时间切分内做特征选择，避免使用全样本统计量。
6. 评价 IC、分组单调性、稳定性、容量和换手。

## 5. 核心论文

- [Common Risk Factors in the Returns on Stocks and Bonds](https://doi.org/10.1016/0304-405X(93)90023-5)：经典多因子资产定价研究。
- [Returns to Buying Winners and Selling Losers](https://doi.org/10.1111/j.1540-6261.1993.tb04702.x)：动量效应的代表性实证论文。

## 6. 推荐开源仓库

- [Qlib](https://github.com/microsoft/qlib)：包含表达式特征、数据处理和量化工作流。
- [pandas](https://github.com/pandas-dev/pandas)：时间序列和表格特征处理的官方仓库。

## 7. 推荐课程和官方文档

- [Qlib Building Formulaic Alphas](https://qlib.readthedocs.io/en/latest/advanced/alpha.html)：公式化因子构建说明。
- [pandas Time Series Guide](https://pandas.pydata.org/docs/user_guide/timeseries.html)：索引、重采样和时间窗口参考。

## 8. 建议实践

- 在公开数据上实现动量、波动和流动性特征，并记录每个值的可用时点。
- 做月度横截面排序、标准化和行业中性化，检查处理后暴露。
- 用滚动窗口报告 IC 均值、方差、符号稳定性、分组收益和换手。

## 9. 与其他主题的关系

特征进入 [标签设计](03-label-design.md) 和各类模型；其时间处理必须遵守 [验证与防泄漏](04-validation-and-leakage.md)，经济风险暴露则连接 [组合构建](09-portfolio-construction.md)。

## 10. 常见误区

- 技术指标名称不同可能只是同一价格变换的重复表达。
- 横截面标准化不能修复未来数据或修订数据泄漏。
- 中性化会改变信号含义，也可能放大噪声和换手。
- 全样本 Feature Importance 不能用于决定历史训练期的特征集合。
