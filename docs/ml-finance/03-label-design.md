# 标签设计

## 1. 主题简介

标签设计把投资决策转化为监督学习目标。标签必须对应明确的决策时点、预测区间、持有规则、成本假设和可执行动作。

## 2. 前置知识

- 收益率、分类与回归损失、抽样和时间索引
- [因子与特征工程](02-feature-and-factor-engineering.md)中的信息可用时间

## 3. 核心概念

- Return Regression 与风险调整收益目标
- Direction Classification、Multi-class Label 与阈值
- Forecast Horizon、入场时点和退出时点
- Triple Barrier、止盈、止损与垂直时间边界
- Event-Based Labeling 与事件抽样
- Overlapping Labels、并发事件和依赖样本
- Class Imbalance、Sample Weight 与标签噪声

## 4. 推荐学习顺序

1. 从固定期限未来收益回归开始，明确价格和时间戳。
2. 将回归目标阈值化为方向或多分类，检查类别稳定性。
3. 比较日历时间与事件驱动的预测区间。
4. 实现 Triple Barrier 并记录首次触及的边界和持有期。
5. 统计标签重叠、并发度和类别不平衡。
6. 让标签评价与最终仓位、成本和风险目标保持一致。

## 5. 核心论文

首轮不将 Triple Barrier 错列为独立论文；该方法的主要权威来源是本章列出的原作者书籍。与标签可靠性相关的实验设计论文见 [验证与防泄漏](04-validation-and-leakage.md)。

## 6. 推荐开源仓库

- [Qlib](https://github.com/microsoft/qlib)：可检查数据集、标签表达式和训练工作流。
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)：分类、回归、权重和指标的官方实现。

## 7. 推荐课程和官方文档

- [Advances in Financial Machine Learning](https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086)：Triple Barrier 与金融机器学习实验设计的原作者书籍页面。
- [scikit-learn Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)：分类、回归和概率指标参考。

## 8. 建议实践

- 对相同数据构造固定期限收益、方向分类和 Triple Barrier 三类标签。
- 比较标签分布、平均持有期、重叠率和对成本阈值的敏感性。
- 逐条抽查特征截止时间、入场价格、退出价格和标签时间戳。

## 9. 与其他主题的关系

标签与 [因子与特征工程](02-feature-and-factor-engineering.md) 共同定义监督样本，并决定 [验证与防泄漏](04-validation-and-leakage.md) 所需的 Purge/Embargo 区间以及 [回测](08-backtesting.md) 的持有逻辑。

## 10. 常见误区

- 未来 N 日收益标签并不保证策略实际持有 N 日。
- 阈值改变会同时改变类别比例、换手和交易成本。
- 重叠标签不是独立样本，随机打乱会夸大有效样本量。
- Sample Weight 不能修复错误时间戳或未来信息泄漏。
