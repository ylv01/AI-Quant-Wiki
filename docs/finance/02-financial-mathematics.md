# 金融数学

## 1. 主题简介

金融数学用贴现、概率过程和数值方法表达跨时间、不确定条件下的现金流。它是固定收益、衍生品和风险管理的共同基础。

## 2. 前置知识

- 代数、微积分、线性代数和概率统计
- [金融市场基础](01-market-foundations.md)中的现金流与利率

## 3. 核心概念

- 货币时间价值、单利、复利与连续复利
- 贴现因子、现值、终值、年金与现金流时间轴
- 随机变量、条件期望、协方差与分布
- 随机过程、Filtration 与 Martingale 直觉
- 布朗运动、几何布朗运动、伊藤过程和伊藤引理
- 风险中性定价与测度变化的基本直觉
- Monte Carlo 抽样、误差、方差缩减和收敛诊断

## 4. 推荐学习顺序

1. 熟练转换单利、离散复利和连续复利。
2. 用贴现因子统一任意现金流的现值计算。
3. 复习条件概率、条件期望和协方差。
4. 从随机游走过渡到布朗运动与随机积分。
5. 用伊藤引理理解随机过程函数的变化。
6. 实现 Monte Carlo 并报告统计误差，而不仅是点估计。

## 5. 核心论文

- [The Pricing of Options and Corporate Liabilities](https://doi.org/10.1086/260062)：展示连续时间随机过程与无套利定价的经典应用。
- [Option Pricing: A Simplified Approach](https://doi.org/10.1016/0304-405X(79)90015-1)：用二项树建立离散时间定价路径。

## 6. 推荐开源仓库

- [QuantLib](https://github.com/lballabio/QuantLib)：可检查日期、现金流、随机过程和数值定价抽象。
- [SciPy](https://github.com/scipy/scipy)：概率分布、积分、优化和数值计算的官方仓库。

## 7. 推荐课程和官方文档

- [MIT Finance Theory I](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/)：现值、风险收益与衍生品基础。
- [QuantLib Documentation](https://www.quantlib.org/docs.shtml)：QuantLib 设计和使用文档入口。
- [SciPy User Guide](https://docs.scipy.org/doc/scipy/tutorial/)：统计、积分和优化的官方教程。

## 8. 建议实践

- 实现现金流现值函数，支持不同复利频率和日计数约定。
- 模拟布朗运动与几何布朗运动，比较经验均值、方差和理论值。
- 用 Monte Carlo 定价欧式期权，报告置信区间并测试方差缩减。

## 9. 与其他主题的关系

贴现与随机过程直接进入 [固定收益](03-fixed-income.md) 和 [衍生品](04-derivatives.md)；Monte Carlo 也用于 [风险管理](06-risk-management.md) 的情景和尾部风险估计。

## 10. 常见误区

- 连续复利是计息约定，不代表价格路径连续可预测。
- 风险中性概率不是现实世界事件发生概率的直接预测。
- Monte Carlo 样本很多不代表模型设定正确。
- 计算现值时忽略日期、日计数和支付日调整会造成系统性误差。
