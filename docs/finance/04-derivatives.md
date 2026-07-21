# 衍生品

## 1. 主题简介

衍生品用合约把标的价格、利率、波动率或信用风险重新分配。本章以无套利、复制组合和风险敏感度为主线学习定价与对冲。

## 2. 前置知识

- [金融数学](02-financial-mathematics.md)中的贴现、随机过程和 Monte Carlo
- [固定收益](03-fixed-income.md)中的曲线与远期利率

## 3. 核心概念

- 远期、期货、结算、基差与套期保值
- 期权 Payoff、Moneyness、Put-Call Parity
- 无套利、复制组合与风险中性定价
- Black–Scholes–Merton 模型及假设
- Binomial Tree、有限差分与 Monte Carlo
- Delta、Gamma、Vega、Theta、Rho
- Implied Volatility、Smile、Skew 与 Volatility Surface

## 4. 推荐学习顺序

1. 画出远期、期货和基础期权的到期收益图。
2. 用持有成本和无套利推导远期价格与 Put-Call Parity。
3. 通过一时期和多时期二项树理解复制与风险中性概率。
4. 学习 Black–Scholes 公式、假设和 Greeks。
5. 从市场价格反解隐含波动率并构建简单波动率曲面。
6. 比较解析、树、有限差分和 Monte Carlo 的适用范围。

## 5. 核心论文

- [The Pricing of Options and Corporate Liabilities](https://doi.org/10.1086/260062)：Black–Scholes 期权定价的经典论文。
- [Theory of Rational Option Pricing](https://doi.org/10.2307/3003143)：Merton 对连续时间期权定价的重要扩展。
- [Option Pricing: A Simplified Approach](https://doi.org/10.1016/0304-405X(79)90015-1)：二项树定价方法的原始论文。

## 6. 推荐开源仓库

- [QuantLib](https://github.com/lballabio/QuantLib)：提供多类衍生品、定价引擎和风险计算。

## 7. 推荐课程和官方文档

- [MIT Finance Theory I](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/)：远期、期货、期权与风险收益基础。
- [QuantLib Documentation](https://www.quantlib.org/docs.shtml)：定价引擎和金融工具文档入口。

## 8. 建议实践

- 实现欧式期权的 Black–Scholes 与二项树定价并比较收敛。
- 用数值差分和解析公式对照 Delta、Gamma 与 Vega。
- 从一组期权价格反解隐含波动率，检查无套利与插值问题。

## 9. 与其他主题的关系

衍生品依赖利率曲线和随机过程，其 Greeks 与压力情景进入 [风险管理](06-risk-management.md)，实际对冲与成交成本则连接 [市场微观结构](07-market-microstructure.md)。

## 10. 常见误区

- Black–Scholes 的常数波动率等假设不是市场事实。
- 隐含波动率是模型下的反解参数，不是未来实现波动率的保证。
- Delta 对冲不能消除跳跃、离散调仓、流动性和模型风险。
- 期货与远期在每日盯市和资金路径上可能不同。
