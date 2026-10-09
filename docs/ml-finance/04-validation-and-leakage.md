# 验证与防泄漏

## 1. 主题简介

金融模型验证必须模拟信息随时间到达的过程。时间切分、标签重叠、资产存续、数据修订和反复试验都可能使样本外结果被高估。

## 2. 前置知识

- [统计与时间序列](01-statistics-and-time-series.md)与[标签设计](03-label-design.md)
- 训练、验证、测试集和超参数选择基础

## 3. 核心概念

- Time-Series Split 与时间顺序不变性
- Walk-Forward Validation、Rolling Window、Expanding Window
- Purged Cross Validation、Embargo 与标签区间
- Look-Ahead Bias、修订数据与发布时间
- Survivorship Bias、退市、成分股历史与 Point-in-Time Universe
- Data Snooping、Leakage、Researcher Degrees of Freedom
- Multiple Testing、选择偏差和最终留出集

## 4. 推荐学习顺序

1. 为每个字段定义观测、发布、接收和策略可用时间。
2. 建立按时间排序的训练、验证和最终测试区间。
3. 用 Walk-Forward 比较滚动与扩展窗口。
4. 根据标签起止区间实施 Purge，并按依赖长度设计 Embargo。
5. 使用历史成分、退市和 Point-in-Time 基本面检查生存偏差。
6. 记录全部试验并为最终结论保留未参与选择的数据。

## 5. 核心论文

- [A Reality Check for Data Snooping](https://doi.org/10.1111/1468-0262.00152)：处理大量策略搜索下数据窥探偏差的经典论文。
- [The Probability of Backtest Overfitting](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253)：量化回测选择偏差与过拟合风险的代表性工作。

## 6. 推荐开源仓库

- [scikit-learn](https://github.com/scikit-learn/scikit-learn)：包含时间序列切分和模型选择基础设施。
- [Qlib](https://github.com/microsoft/qlib)：提供基于时间区间的量化训练与回测工作流。
- [arch](https://github.com/bashtage/arch)：Kevin Sheppard 的金融计量工具原仓库，提供时间序列 Bootstrap、SPA/RealityCheck、StepM 与 Model Confidence Set。

## 7. 推荐课程和官方文档

- [scikit-learn TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)：时间顺序交叉验证的官方接口说明。
- [Qlib Workflow](https://qlib.readthedocs.io/en/latest/component/workflow.html)：任务、记录和工作流文档。
- [arch Multiple Comparison Procedures](https://bashtage.github.io/arch/multiple-comparison/multiple-comparison-reference.html)：多个候选与基准的损失比较及相应检验接口。

## 8. 建议实践

- 在同一模型上比较随机切分、普通时间切分和 Purged Walk-Forward。
- 向特征中注入一个显式未来字段，验证审计是否能发现异常高分。
- 构造成分股历史与当前成分股两个 Universe，比较生存偏差影响。
- 参考 [arch 多模型比较示例](https://github.com/bashtage/arch/blob/3ff735de8fd37ed7164656e7ee38086cb7e26e11/examples/multiple-comparison_examples.ipynb)，固定随机种子，先生成零均值纯噪声候选收益，以零收益为预先指定的基准、负收益为损失；逐步增加候选数量，保存全部候选在同一评价期的损失矩阵。只在选择区间选取最佳候选，比较其样本内 Sharpe 与独立最终留出期表现，再运行 SPA/RealityCheck 或 StepM 检验。真实策略实验还需明确损失定义、时间依赖与基准，不能反复查看最终测试区间。

这些开源检验可以补充策略搜索的统计评价，但不等同于 Deflated Sharpe Ratio 或 PBO/CSCV，也不自动实现 Purge/Embargo。DSR 与 PBO 仍需按原论文核验实现、记录全部试验及其依赖关系；任何统计检验都不能修复错误的 Point-in-Time 数据。

## 9. 与其他主题的关系

本章约束所有 [树模型](05-tree-models.md)、[神经网络](06-neural-networks.md) 和 [金融 Transformer](07-transformers-for-finance.md) 实验；验证输出必须在 [回测](08-backtesting.md) 与 [生产 Pipeline](10-production-pipeline.md) 中保持相同时间语义。

## 10. 常见误区

- 按时间切分仍可能因重叠标签或全样本预处理而泄漏。
- Embargo 不是固定百分比，应与信息和标签依赖区间相关。
- 测试集被反复查看后就参与了模型选择。
- 更复杂的交叉验证不能弥补错误的 Point-in-Time 数据。
