# 金融验证与执行实践仓库

这些项目提供可复用组件与官方示例；数据许可、参数选择、环境冻结和完整实验仍需实践者完成。

| 仓库 | 方向 | 主要内容 | 适合学习什么 | 难度 | 官方地址 |
|---|---|---|---|---|---|
| fredapi | 历史修订数据 | FRED/ALFRED 查询、初次发布值和修订版本接口 | 数据版本与当时可知信息的差异 | 中级 | [GitHub](https://github.com/mortada/fredapi) |
| arch | 时间序列统计与检验 | 波动模型、Bootstrap、SPA、StepM 与 Model Confidence Set | 时序相关性、多策略搜索和统计检验 | 中级 | [GitHub](https://github.com/bashtage/arch) |
| Qlib | 量化数据与执行 | PIT 数据层、策略、嵌套执行和工作流示例 | 数据时间语义、组合与执行的衔接 | 进阶 | [GitHub](https://github.com/microsoft/qlib) |

- 历史修订与 as-of 数据选择见 [金融数据工程](../../docs/finance/08-financial-data-engineering.md)。宏观 vintage 是日级时间信息，不自动等于策略接收时间。
- 纯噪声策略搜索与多重检验见 [验证与防泄漏](../../docs/ml-finance/04-validation-and-leakage.md)。arch 的 SPA、Bootstrap 等接口不等于 DSR 或 PBO 实现。
- 嵌套执行与成本敏感性见 [回测](../../docs/ml-finance/08-backtesting.md)。执行示例不能代替真实成交、冲击参数和容量的校准。
