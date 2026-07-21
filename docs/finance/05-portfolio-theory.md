# 投资组合理论

## 1. 主题简介

投资组合理论研究如何把多个资产的预期收益、风险和相关性转化为持仓。本章重点是估计误差、约束和风险模型，而不只是一条最优前沿曲线。

## 2. 前置知识

- 线性代数、概率统计、协方差矩阵和约束优化
- [金融市场基础](01-market-foundations.md)中的收益率与风险溢价

## 3. 核心概念

- 组合收益、方差、协方差与分散化
- 均值方差模型、Efficient Frontier 与切点组合
- CAPM、Beta、Alpha 与市场组合
- 单因子、多因子模型和因子暴露
- Risk Parity、风险贡献与风险预算
- Black–Litterman 的均衡收益与观点融合
- Portfolio Optimization、约束、换手和稳健性

## 4. 推荐学习顺序

1. 从两资产组合推导相关性与分散化效果。
2. 实现无约束和含权重约束的均值方差优化。
3. 学习 CAPM、Beta 与 Alpha 的假设和估计。
4. 用因子模型分解共同风险和特异风险。
5. 比较风险平价与均值方差对输入估计的敏感性。
6. 加入观点、交易成本、仓位和行业约束。

## 5. 核心论文

- [Portfolio Selection](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x)：均值方差组合选择的奠基论文。
- [Capital Asset Prices](https://doi.org/10.1111/j.1540-6261.1964.tb02865.x)：CAPM 的经典论文。
- [Common Risk Factors in the Returns on Stocks and Bonds](https://doi.org/10.1016/0304-405X(93)90023-5)：股票与债券共同风险因子的代表性实证工作。

## 6. 推荐开源仓库

- [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt)：原作者维护的组合优化实现与示例。
- [QuantLib](https://github.com/lballabio/QuantLib)：金融工具和风险计算基础设施。

## 7. 推荐课程和官方文档

- [MIT Finance Theory I](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/)：组合理论、CAPM 与资产定价基础。
- [PyPortfolioOpt Documentation](https://pyportfolioopt.readthedocs.io/)：组合优化、目标和约束的项目文档。

## 8. 建议实践

- 用模拟资产画出可行集和有效前沿，验证相关性变化的影响。
- 对样本均值和协方差做轻微扰动，观察最优权重稳定性。
- 比较等权、最小方差、风险平价和受约束均值方差的样本外结果与换手。

## 9. 与其他主题的关系

组合理论为 [风险管理](06-risk-management.md) 和 [组合构建](../ml-finance/09-portfolio-construction.md) 提供目标与约束；因子模型连接 [因子与特征工程](../ml-finance/02-feature-and-factor-engineering.md)。

## 10. 常见误区

- 分散化降低特异风险，不保证消除市场和尾部风险。
- 最优权重对预期收益估计通常非常敏感。
- Beta 是给定市场基准和估计窗口下的统计量。
- 优化器给出可行解不代表输入假设可靠或可交易。
