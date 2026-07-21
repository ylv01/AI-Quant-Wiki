# 统计与时间序列

## 1. 主题简介

本章建立分析金融序列所需的统计基础，重点处理自相关、非平稳、波动聚集、结构突变和分布漂移，而不是默认样本独立同分布。

## 2. 前置知识

- 概率分布、期望、方差、协方差与线性回归
- [金融数据工程](../finance/08-financial-data-engineering.md)中的时间、频率和数据质量

## 3. 核心概念

- 描述统计、分位数、偏度、峰度和稳健统计量
- 假设检验、置信区间、效应量与统计功效
- 相关性、自相关、偏自相关与滞后
- 弱平稳、单位根、ADF 与差分
- AR、MA、ARMA、ARIMA
- 条件异方差、ARCH、GARCH 与波动聚集
- Regime、Structural Break、Concept/Distribution Shift

## 4. 推荐学习顺序

1. 区分价格、简单收益、对数收益和实现波动率。
2. 用图形、ACF/PACF 和滚动统计观察时序依赖。
3. 学习单位根与 ADF 的原假设、滞后选择和局限。
4. 拟合 AR/MA/ARIMA，并检查残差而不只看拟合度。
5. 用 ARCH/GARCH 建模条件波动并评价区间预测。
6. 用滚动窗口、变点和分层统计分析状态与分布变化。

## 5. 核心论文

- [Distribution of the Estimators for Autoregressive Time Series with a Unit Root](https://doi.org/10.1080/01621459.1979.10482531)：Dickey–Fuller 单位根检验的基础工作。
- [Autoregressive Conditional Heteroscedasticity](https://doi.org/10.2307/1912773)：ARCH 条件波动模型的原始论文。
- [Generalized Autoregressive Conditional Heteroskedasticity](https://doi.org/10.1016/0304-4076(86)90063-1)：GARCH 模型的原始论文。

## 6. 推荐开源仓库

- [statsmodels](https://github.com/statsmodels/statsmodels)：统计模型、检验和时间序列分析的官方仓库。
- [arch](https://github.com/bashtage/arch)：原作者维护的 ARCH/GARCH 与相关计量工具。

## 7. 推荐课程和官方文档

- [statsmodels Time Series Analysis](https://www.statsmodels.org/stable/tsa.html)：ARIMA、状态空间与检验的官方文档。
- [arch Documentation](https://bashtage.github.io/arch/)：条件波动模型和单位根检验文档。
- [NYU Statistics Online Class](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/webcaststatistics.htm)：面向金融学习的统计课程材料。

## 8. 建议实践

- 对价格和收益分别运行 ADF，解释为何结果不同。
- 使用走步窗口拟合 ARIMA/GARCH，评价均值和波动预测。
- 将样本按波动状态分层，比较分布、相关性和模型误差。

## 9. 与其他主题的关系

本章为 [因子与特征工程](02-feature-and-factor-engineering.md)、[标签设计](03-label-design.md) 和 [验证与防泄漏](04-validation-and-leakage.md) 提供统计假设；分布变化也决定生产监控。

## 10. 常见误区

- ADF 未拒绝单位根不等于证明序列一定是随机游走。
- 相关性不表示因果，也可能被共同趋势制造。
- 平稳性不是一次检验后永久成立的属性。
- 高阶模型的样本内拟合更好，不保证样本外预测更好。
