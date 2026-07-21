# 组合构建

## 1. 主题简介

组合构建把模型分数转化为可执行仓位，同时控制风险暴露、集中度、换手和再平衡。模型预测与最终收益之间的大量差异来自这一层。

## 2. 前置知识

- [投资组合理论](../finance/05-portfolio-theory.md)与[风险管理](../finance/06-risk-management.md)
- [回测](08-backtesting.md)中的成本、持仓和会计

## 3. 核心概念

- Ranking、Threshold、Top-K 与分位数组合
- Long-Only、Long-Short 与现金管理
- Position Sizing、分数映射与风险预算
- Gross/Net Exposure、Leverage 与集中度
- Risk Constraint、Sector Neutrality、Beta Neutrality
- Volatility Targeting 与动态杠杆
- Rebalancing、缓冲区、换手惩罚和交易成本

## 4. 推荐学习顺序

1. 用排序和 Top-K 建立最透明的信号到仓位映射。
2. 比较等权、分数权重和波动调整权重。
3. 定义多空、净敞口、单名和杠杆约束。
4. 加入行业、Beta 和因子中性约束。
5. 实施波动目标、换手惩罚和再平衡缓冲区。
6. 用暴露、容量、成本和归因而不只用总收益评价组合。

## 5. 核心论文

- [Portfolio Selection](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x)：均值方差组合优化基础。
- [Global Portfolio Optimization](https://doi.org/10.2469/faj.v48.n5.28)：Black–Litterman 框架的经典论文。
- [Building Diversified Portfolios that Outperform Out of Sample](https://arxiv.org/abs/1602.06293)：层次风险平价的原作者工作。

## 6. 推荐开源仓库

- [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt)：组合优化、风险模型和约束实现。
- [Qlib](https://github.com/microsoft/qlib)：信号、策略、组合和回测工作流。

## 7. 推荐课程和官方文档

- [MIT Finance Theory I](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/)：组合理论和资产定价基础。
- [PyPortfolioOpt Documentation](https://pyportfolioopt.readthedocs.io/)：目标函数、风险模型与约束文档。
- [Qlib Strategy Documentation](https://qlib.readthedocs.io/en/latest/component/strategy.html)：策略与组合生成组件。

## 8. 建议实践

- 将同一模型分数分别映射为 Top-K、分数权重和风险调整权重。
- 加入行业/Beta 中性、单名上限和换手惩罚，记录每项约束代价。
- 对目标权重和实际成交权重分别做风险与绩效归因。

## 9. 与其他主题的关系

组合构建接收 [树模型](05-tree-models.md)、[神经网络](06-neural-networks.md) 或 [金融 Transformer](07-transformers-for-finance.md) 的输出，在 [回测](08-backtesting.md) 中评价，并把订单目标交给 [生产 Pipeline](10-production-pipeline.md)。

## 10. 常见误区

- 模型分数不能在未校准时直接解释为最优仓位比例。
- Beta 中性不代表对所有系统性因子中性。
- 波动率目标在波动上升时去杠杆，可能带来路径依赖与交易成本。
- 目标权重可行不代表在流动性、借券和涨跌停条件下可成交。
