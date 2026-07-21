# 金融工程学习路线

本路线围绕现金流、无套利、风险收益权衡和真实市场机制组织。学习顺序从金融工具与报价开始，进入定价、组合和风险，最后落到市场微观结构与数据工程。

## 阶段导航

1. [金融市场基础](01-market-foundations.md)：主要资产、合约、利率、收益率与风险溢价。
2. [金融数学](02-financial-mathematics.md)：贴现、随机过程、伊藤过程与 Monte Carlo。
3. [固定收益](03-fixed-income.md)：曲线、债券定价、久期、凸性与信用风险。
4. [衍生品](04-derivatives.md)：远期、期货、期权、无套利、Greeks 与波动率。
5. [投资组合理论](05-portfolio-theory.md)：均值方差、CAPM、因子、风险平价与优化。
6. [风险管理](06-risk-management.md)：VaR、CVaR、压力测试及流动性、对手方和模型风险。
7. [市场微观结构](07-market-microstructure.md)：订单簿、价差、订单流、冲击和执行。
8. [金融数据工程](08-financial-data-engineering.md)：行情、公司行为、时区、存储、版本和 Pipeline。

## 学习主线

- 每个定价问题先画现金流和时间轴，再选择概率模型与数值方法。
- 每个组合结果同时报告目标函数、约束、估计窗口和交易成本假设。
- 每个数据字段都说明观测时间、发布时间、调整方式和可用范围。
- 微观结构与数据工程不是附录，它们决定理论信号能否被可靠评价和执行。

## 与机器学习金融的交汇

[金融数据工程](08-financial-data-engineering.md) 为 [因子与特征工程](../ml-finance/02-feature-and-factor-engineering.md)、[验证与防泄漏](../ml-finance/04-validation-and-leakage.md) 和 [回测](../ml-finance/08-backtesting.md) 提供时间一致的数据基础；组合与风险知识则直接进入 [组合构建](../ml-finance/09-portfolio-construction.md)。

集中资源见 [金融工程论文](../../resources/papers/financial-engineering.md) 与 [金融工程仓库](../../resources/repositories/financial-engineering.md)。
