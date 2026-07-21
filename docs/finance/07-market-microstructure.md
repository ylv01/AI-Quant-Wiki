# 市场微观结构

## 1. 主题简介

市场微观结构研究订单如何形成报价和成交，以及信息、流动性和交易规则如何影响价格。它把理论信号连接到真实执行成本。

## 2. 前置知识

- [金融市场基础](01-market-foundations.md)中的交易场所和订单概念
- 概率统计、基本博弈和时间序列

## 3. 核心概念

- Limit Order Book、Bid、Ask、Depth 与 Queue
- Market Order、Limit Order、Cancel 与 Time-in-Force
- Bid-Ask Spread、Quoted/Effective/Realized Spread
- Liquidity、Resiliency、Slippage 与 Implementation Shortfall
- Temporary/Permanent Price Impact
- Order Flow、Trade Sign、Adverse Selection 与 Inventory Risk
- TWAP、VWAP、POV 等 Execution Algorithm

## 4. 推荐学习顺序

1. 从订单生命周期和撮合优先级理解订单簿状态。
2. 计算中间价、价差、深度和成交方向。
3. 区分滑点、显性费用、机会成本和价格冲击。
4. 学习订单流、信息不对称和做市商库存模型。
5. 比较市价单和限价单的成交概率与逆向选择。
6. 在参与率、风险和冲击约束下研究执行算法。

## 5. 核心论文

- [Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders](https://doi.org/10.1016/0304-405X(85)90044-3)：信息不对称与价差形成的经典模型。
- [Continuous Auctions and Insider Trading](https://doi.org/10.2307/1913210)：Kyle 市场冲击与知情交易模型。

## 6. 推荐开源仓库

- [Qlib](https://github.com/microsoft/qlib)：包含量化工作流、回测和嵌套执行组件。

## 7. 推荐课程和官方文档

- [Qlib High-Frequency Trading Documentation](https://qlib.readthedocs.io/en/latest/component/highfreq.html)：高频数据与嵌套执行文档入口。
- [Qlib Strategy and Backtest](https://qlib.readthedocs.io/en/latest/component/strategy.html)：策略、执行与回测组件说明。

## 8. 建议实践

- 从公开样例订单簿重建最优买卖价、深度和订单事件序列。
- 计算固定时间窗内的价差、订单不平衡和短期价格响应。
- 用相同目标数量比较立即成交、TWAP 和参与率执行的成本与未成交风险。

## 9. 与其他主题的关系

本章影响 [回测](../ml-finance/08-backtesting.md) 的成本和成交模型，也决定 [生产 Pipeline](../ml-finance/10-production-pipeline.md) 中订单执行、监控与重放所需的数据粒度。

## 10. 常见误区

- 中间价不是任何数量都能成交的价格。
- 滑点、价差和市场冲击相互关联但不是同一指标。
- 限价单避免跨越价差，但承担不成交和逆向选择风险。
- 仅用 K 线无法可靠重建队列位置和逐笔成交路径。
