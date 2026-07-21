# 生产 Pipeline

## 1. 主题简介

生产 Pipeline 将研究中的数据、特征、模型、信号和组合逻辑转化为可调度、可监控、可恢复和可审计的系统。关键目标是研究与生产语义一致。

## 2. 前置知识

- [金融数据工程](../finance/08-financial-data-engineering.md)、[验证与防泄漏](04-validation-and-leakage.md)、[回测](08-backtesting.md)
- API、数据库、调度、测试、容器与基本可观测性

## 3. 核心概念

- Data Ingestion、Schema Contract 与质量门槛
- Feature Engineering、Label Generation 与 Point-in-Time 一致性
- Model Training、Model Validation、Artifact 与 Model Registry
- Batch Inference、Online Inference 与特征新鲜度
- Signal Generation、Risk Control 与审批边界
- Order Execution、幂等性、状态同步和失败恢复
- Monitoring、Logging、数据/模型漂移与告警
- Replay、Lineage、Performance Attribution 与审计

## 4. 推荐学习顺序

1. 把研究函数拆为带输入输出 Schema 的数据、特征、模型和组合步骤。
2. 为数据版本、代码版本、配置、模型和预测建立统一标识。
3. 使用时间一致测试验证离线训练与批量推理。
4. 设计信号到风控、订单和成交的状态机及幂等键。
5. 建立数据质量、延迟、漂移、风险、订单和绩效监控。
6. 从任意历史时点重放全链路，并解释最终仓位来源。

## 5. 核心论文

- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems)：总结生产机器学习系统中的依赖与维护风险。
- [Qlib: An AI-oriented Quantitative Investment Platform](https://arxiv.org/abs/2009.11189)：展示量化研究从数据到训练、回测和工作流的系统结构。
- [TFX: A TensorFlow-Based Production-Scale Machine Learning Platform](https://dl.acm.org/doi/10.1145/3097983.3098021)：生产级机器学习平台的代表性系统论文。

## 6. 推荐开源仓库

- [Qlib](https://github.com/microsoft/qlib)：量化数据、训练、记录、回测与在线管理平台。
- [MLflow](https://github.com/mlflow/mlflow)：实验、模型与部署生命周期的官方仓库。
- [Apache Airflow](https://github.com/apache/airflow)：批处理工作流编排平台。

## 7. 推荐课程和官方文档

- [Qlib Workflow](https://qlib.readthedocs.io/en/latest/component/workflow.html)：任务、记录器和工作流管理。
- [MLflow Documentation](https://mlflow.org/docs/latest/)：实验跟踪、模型与注册表文档。
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)：调度、任务依赖和运行监控文档。

## 8. 建议实践

- 构建日频迷你 Pipeline：摄取 → 质量检查 → 特征 → 推理 → 风控 → 模拟订单。
- 为每次运行保存数据版本、代码提交、配置、模型摘要、信号和订单事件。
- 随机终止任一步骤，验证重试不会重复下单，并可从日志完整重放。

## 9. 与其他主题的关系

本章汇合三条路线：AI 提供模型和 Agent 能力，金融工程提供数据、风险和执行约束，机器学习金融提供标签、验证、回测与组合逻辑。

## 10. 常见误区

- Notebook 能运行不等于流程可重现、可监控或可恢复。
- Model Registry 只管理模型文件时，仍无法追踪数据与特征来源。
- 在线推理更快不代表适合所有低频策略。
- 监控模型分数分布不能替代数据质量、风险、执行和绩效监控。
