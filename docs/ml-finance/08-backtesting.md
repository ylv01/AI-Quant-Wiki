# 回测

## 1. 主题简介

回测把历史时点可用的信号映射为订单、成交、头寸和损益，用于检验研究假设在成本与约束下是否成立。可靠回测必须能解释每笔状态变化。

## 2. 前置知识

- [验证与防泄漏](04-validation-and-leakage.md)与[市场微观结构](../finance/07-market-microstructure.md)
- 收益、持仓、现金、杠杆和基本会计

## 3. 核心概念

- Signal、Target Position、Order、Fill 与 Position
- Transaction Cost、Commission、Bid-Ask 与 Slippage
- Turnover、Capacity、Leverage、Margin 与 Borrow
- Corporate Action、现金股息、拆股与退市
- Futures Roll、合约乘数、保证金和连续合约
- Mark-to-Market、现金账簿和收益归属
- Performance Attribution、基准、风险暴露和成本分解

## 4. 推荐学习顺序

1. 定义决策时点、信号可用时间、下单时点和成交价格规则。
2. 从单资产、无成本、日频回测验证现金和头寸会计。
3. 加入手续费、价差、滑点、换手和成交限制。
4. 正确处理公司行动、退市、期货换月与每日盯市。
5. 加入杠杆、保证金、借券和风险限额。
6. 分解信号、市场、因子、成本和执行对绩效的贡献。

## 5. 核心论文

- [The Probability of Backtest Overfitting](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253)：研究大量策略选择导致的回测过拟合。
- [The Deflated Sharpe Ratio](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551)：调整非正态与多重试验影响的绩效统计量。

## 6. 推荐开源仓库

- [Qlib](https://github.com/microsoft/qlib)：包含信号、策略、执行和回测工作流。
- [vectorbt](https://github.com/polakowo/vectorbt)：原作者维护的向量化研究和回测工具。
- [backtrader](https://github.com/mementum/backtrader)：事件驱动的 Python 回测框架。
- [arch](https://github.com/bashtage/arch)：提供时间序列 Bootstrap 与多模型比较方法，可评价 Sharpe 不确定性和策略搜索后的统计证据。

## 7. 推荐课程和官方文档

- [Qlib Strategy and Backtest](https://qlib.readthedocs.io/en/latest/component/strategy.html)：组合策略与回测组件说明。
- [vectorbt Documentation](https://vectorbt.dev/)：向量化信号、组合和记录文档。
- [arch Bootstrap Examples](https://bashtage.github.io/arch/bootstrap/bootstrap_examples.html)：Sharpe 置信区间、随机种子与时间序列 Bootstrap 的官方示例。

## 8. 建议实践

- 对一组手工可核算的价格和订单逐日验证现金、持仓和净值。
- 在同一信号上逐项加入手续费、价差、滑点和成交量限制。
- 对公司行动和期货换月构造单元测试，并输出逐笔归因。
- 参考 [arch Sharpe Bootstrap 示例](https://github.com/bashtage/arch/blob/3ff735de8fd37ed7164656e7ee38086cb7e26e11/examples/bootstrap_examples.ipynb)，用适合时间依赖的 Stationary/Block Bootstrap 估计置信区间并固定随机种子。它评估统计不确定性，不自动完成 DSR 或 PBO；后两项仍需保存全部策略试验并按本章原论文核验实现。
- 参考 [Qlib 嵌套决策执行示例](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/examples/nested_decision_execution/workflow.py)，比较同一组合目标在日频与更细执行频率下的成本前后绩效。再按 [Exchange 实现](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/qlib/backtest/exchange.py)显式配置成交量上限 `volume_threshold` 和冲击成本 `impact_cost`，改变订单规模、参与率上限与执行频率，报告实际成交、未成交和净值敏感性。

Qlib 上述示例的手续费是演示配置，未设置成交量上限或冲击成本；`impact_cost` 默认值为 0。容量分析仍需对应市场的数据、成本校准和规模压力测试，K 线模拟也不还原队列与逐笔撮合。现成框架提供实验组件，不保证研究流程已经避免泄漏或能直接用于真实执行。

## 9. 与其他主题的关系

回测接收模型信号，经 [组合构建](09-portfolio-construction.md) 形成目标仓位，并使用 [市场微观结构](../finance/07-market-microstructure.md) 的成本与成交假设；最终逻辑应能迁移到 [生产 Pipeline](10-production-pipeline.md)。

## 10. 常见误区

- 用收盘价计算信号又假设同一收盘价成交会产生前视偏差。
- 复权价适合收益分析，但现金和成交会计仍需公司行动事件。
- 固定基点成本不能表达容量、参与率和市场冲击。
- Sharpe Ratio 高不能单独排除多重试验、尾部风险和数据偏差。
