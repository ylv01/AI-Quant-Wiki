# 金融数据工程

## 1. 主题简介

金融数据工程负责把行情、基本面、公司行为和参考数据转化为时间一致、可追踪、可重放的数据集。它是金融建模可信度的基础设施。

## 2. 前置知识

- Python、SQL、文件系统、数据库和批处理基础
- [金融市场基础](01-market-foundations.md)中的资产、交易时段和公司行动

## 3. 核心概念

- 行情数据、Tick、分钟 K 线、日 K 与聚合规则
- 前复权、后复权、分红、拆股与公司行为
- 期货主力、连续合约、换月和回溯调整
- 缺失值、异常值、重复、乱序和延迟到达
- 时区、夏令时、交易日历、Session 与跨午夜交易
- 行式/列式存储、Parquet、Arrow 与 DuckDB
- Data Pipeline、Schema、Feature Store、Data Versioning 与 Lineage
- Point-in-Time Join、发布时间和可用时间

## 4. 推荐学习顺序

1. 为每个源记录供应方、字段定义、时区、频率、许可与抓取时间。
2. 保留不可变原始层，再进行解析、类型校验和去重。
3. 使用交易日历和 Session 聚合 Tick/K 线。
4. 将公司行动、复权和期货换月作为显式变换保存。
5. 用 Parquet 分区和 DuckDB 建立可查询的研究层。
6. 实施 Point-in-Time Join、数据版本、质量报告和重放测试。

## 5. 核心论文

- [Qlib: An AI-oriented Quantitative Investment Platform](https://arxiv.org/abs/2009.11189)：从数据、训练、回测和工作流角度展示量化研究基础设施。

本主题还高度依赖格式、数据库和市场数据供应方的官方规范。

## 6. 推荐开源仓库

- [Apache Arrow](https://github.com/apache/arrow)：列式内存格式和多语言数据工具箱。
- [DuckDB](https://github.com/duckdb/duckdb)：适合本地分析 Parquet 的嵌入式分析数据库。
- [Qlib](https://github.com/microsoft/qlib)：含数据层、工作流、训练和回测的量化平台。
- [fredapi](https://github.com/mortada/fredapi)：Mortada Mehyar 的 FRED/ALFRED Python 客户端原仓库，可读取初次发布与历史修订版本；需要 FRED API key。

## 7. 推荐课程和官方文档

- [Apache Arrow Parquet Documentation](https://arrow.apache.org/docs/python/parquet.html)：Parquet 读写、分区和数据集接口。
- [DuckDB Documentation](https://duckdb.org/docs/stable/)：SQL、Parquet 扫描和数据导入参考。
- [Qlib Point-in-Time Database](https://qlib.readthedocs.io/en/latest/advanced/PIT.html)：季度/年度财报的历史版本存储、查询和适用边界。

## 8. 建议实践

- 将一份公开日线数据保存为带 Schema 和分区的 Parquet，并用 DuckDB 查询。
- 对分红拆股样例同时生成原始价、复权因子和复权价，验证收益连续性。
- 模拟迟到数据和修订数据，验证版本、质量报告和历史重放结果。
- 参考 [fredapi 修订数据示例](https://github.com/mortada/fredapi/blob/d0a0ba3001ebbbceafdcbdd3eb23828f0537cdff/README.md#working-with-data-revisions)，比较 GDP 的初次发布、历史决策日可得版本与最新版本。对 `get_series_all_releases` 返回的记录先筛选 `realtime_start <= 决策日`，再按观测期选择最后一个可用版本；保留快照并区分日级 vintage 日期、实际发布时间与接收延迟。
- 参考 [Qlib PIT 数据准备示例](https://github.com/microsoft/qlib/blob/54355232463878d2eebb91fe0ee5fa7fa1f5976c/scripts/data_collector/pit/README.md)，检查同一财报期间的多次发布如何进入历史查询。该示例在缺公告日时按季度 45 日或年度 90 日的日历偏移估算，需另行核对真实可用时间与数据修订完整性。

现成客户端和 PIT 存储可作为最小实践的起点；它们不自动完成所有市场数据的历史版本审计。[fredapi 的 `get_series_as_of_date` 实现](https://github.com/mortada/fredapi/blob/d0a0ba3001ebbbceafdcbdd3eb23828f0537cdff/fredapi/fred.py)只筛除决策日之后的修订，仍可能返回同一观测期的多个版本，不能直接当作每期唯一的最终特征值。

## 9. 与其他主题的关系

本章是 [统计与时间序列](../ml-finance/01-statistics-and-time-series.md)、[因子与特征工程](../ml-finance/02-feature-and-factor-engineering.md)、[验证与防泄漏](../ml-finance/04-validation-and-leakage.md) 和 [回测](../ml-finance/08-backtesting.md) 的共同上游。

## 10. 常见误区

- 缺失值可能代表停牌、未上市或数据故障，不能一律前向填充。
- 复权价格适合收益分析，但不等于真实历史成交价。
- 连续期货是研究构造，不是单一可交易合约。
- 事件日期、公告日期、数据库录入时间和策略可用时间必须区分。
