# 风险管理

## 1. 主题简介

风险管理识别、度量并控制可能造成损失的市场、信用、流动性、对手方和模型风险。单一指标不能覆盖所有风险，需要统计分布、情景和治理共同作用。

## 2. 前置知识

- 概率分布、分位数、相关性和 Monte Carlo
- [投资组合理论](05-portfolio-theory.md)与基本衍生品敏感度

## 3. 核心概念

- Volatility、Downside Risk、Drawdown 与 Recovery
- VaR 的历史、参数与 Monte Carlo 方法
- CVaR / Expected Shortfall 与尾部损失
- Stress Testing、Scenario Analysis 与反向压力测试
- Liquidity Risk、Funding Risk 与集中度
- Counterparty Risk、Exposure 与净额结算
- Model Risk、假设、验证、限额和治理

## 4. 推荐学习顺序

1. 从收益分布、波动和回撤建立描述性风险画像。
2. 实现多种 VaR，并做覆盖率和独立性回测。
3. 学习 Expected Shortfall 对尾部损失的表达。
4. 设计历史、假设和反向压力情景。
5. 将流动性、杠杆、保证金和对手方暴露加入情景。
6. 建立模型清单、假设记录、独立验证和限额升级流程。

## 5. 核心论文

- [Conditional Value-at-Risk for General Loss Distributions](https://doi.org/10.1016/S0378-4266(02)00271-6)：CVaR 优化与一般损失分布的经典工作。
- [Volatility Estimation and Comparison Using Unbiased Extreme-Value Estimators](https://doi.org/10.1086/296072)：基于高低价估计波动率的代表性研究。

## 6. 推荐开源仓库

- [QuantLib](https://github.com/lballabio/QuantLib)：可用于重定价、敏感度和情景分析。
- [SciPy](https://github.com/scipy/scipy)：统计分布、优化和数值计算工具。

## 7. 推荐课程和官方文档

- [Basel Committee — Market Risk](https://www.bis.org/bcbs/publ/d457.htm)：市场风险资本框架的权威文件入口。
- [QuantLib Documentation](https://www.quantlib.org/docs.shtml)：风险计算所需定价组件参考。

## 8. 建议实践

- 对同一组合实现历史、正态参数和 Monte Carlo VaR/CVaR。
- 使用滚动窗口做 VaR 超损回测，并报告例外次数和聚集性。
- 设计利率、波动率、相关性和流动性同时恶化的联合压力情景。

## 9. 与其他主题的关系

风险管理使用 [固定收益](03-fixed-income.md)、[衍生品](04-derivatives.md) 和 [投资组合理论](05-portfolio-theory.md) 的敏感度与暴露，并向 [组合构建](../ml-finance/09-portfolio-construction.md) 和生产风控提供限额。

## 10. 常见误区

- VaR 是给定置信水平和期限的分位数，不表示超过 VaR 后会损失多少。
- 历史模拟仍隐含未来与样本历史相似的假设。
- 压力测试不是用极端但互相矛盾的参数随意拼接。
- 风险模型输出精确小数不代表模型风险很小。
