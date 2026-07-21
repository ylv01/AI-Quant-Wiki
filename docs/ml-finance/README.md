# 机器学习金融学习路线

本路线把金融问题转化为可验证的机器学习研究流程。核心不是追求模型复杂度，而是确保特征、标签、切分、回测与上线使用同一套时间语义和决策约束。

## 阶段导航

1. [统计与时间序列](01-statistics-and-time-series.md)：平稳性、自相关、波动、状态与分布变化。
2. [因子与特征工程](02-feature-and-factor-engineering.md)：经济含义、横截面处理、中性化和稳定性。
3. [标签设计](03-label-design.md)：预测目标、持有期、事件标签、重叠和样本权重。
4. [验证与防泄漏](04-validation-and-leakage.md)：时间切分、走步验证、清洗区间与偏差控制。
5. [树模型](05-tree-models.md)：随机森林、提升树、解释、校准与参数搜索。
6. [神经网络](06-neural-networks.md)：MLP、卷积、循环网络、TCN 与表征学习。
7. [金融 Transformer](07-transformers-for-finance.md)：时间、资产、Patch、语言和多模态建模。
8. [回测](08-backtesting.md)：信号、头寸、成本、会计、换月和绩效归因。
9. [组合构建](09-portfolio-construction.md)：排序、仓位、约束、中性化和再平衡。
10. [生产 Pipeline](10-production-pipeline.md)：数据、训练、推理、执行、监控、重放与归因。

## 推荐实验顺序

1. 固定数据版本、可用时间、标签定义和评价区间。
2. 建立简单统计或线性基线，再训练树模型。
3. 只有在基线和验证流程稳定后才增加神经网络或 Transformer。
4. 把预测输出转换为含交易成本和风险约束的组合。
5. 用可重放 Pipeline 验证研究和生产的一致性。

## 两条上游路线

- 金融工程提供资产、定价、组合、风险和市场机制约束。
- AI / LLM 提供特征学习、Transformer、训练、RAG、多模态和 Agent 方法。

集中资源见 [机器学习金融论文](../../resources/papers/machine-learning-finance.md) 与 [量化研究仓库](../../resources/repositories/quantitative-finance.md)。
