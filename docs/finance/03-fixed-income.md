# 固定收益

## 1. 主题简介

固定收益研究如何用利率曲线折现合约现金流，并衡量价格对利率、曲线和信用变化的敏感度。

## 2. 前置知识

- [金融数学](02-financial-mathematics.md)中的贴现、现金流和复利约定
- 债券、票息、到期和信用主体的基本概念

## 3. 核心概念

- 债券定价、净价、全价、应计利息与结算
- 到期收益率及其局限
- 贴现因子、即期利率、远期利率和互换利率
- Bootstrap、收益率曲线插值和曲线形状
- Macaulay Duration、Modified Duration、DV01 与 Convexity
- 平移、陡峭化和曲率等曲线风险
- 信用利差、违约概率、回收率与信用风险

## 4. 推荐学习顺序

1. 从确定现金流的债券现值和应计利息开始。
2. 比较价格、到期收益率和持有期收益率。
3. 从市场工具 Bootstrap 贴现曲线并推导远期利率。
4. 用久期、DV01 和凸性近似价格变化。
5. 从单一收益率变化扩展到多曲线与关键期限风险。
6. 最后加入信用利差、违约与流动性影响。

## 5. 核心论文

- [An Econometric Approach to the Term Structure of Interest Rates](https://doi.org/10.1016/0304-405X(77)90016-2)：Vasicek 利率模型的原始论文。
- [Parsimonious Modeling of Yield Curves](https://doi.org/10.1086/296409)：Nelson–Siegel 曲线表示的经典工作。

## 6. 推荐开源仓库

- [QuantLib](https://github.com/lballabio/QuantLib)：包含债券、日历、现金流、曲线和敏感度计算。

## 7. 推荐课程和官方文档

- [MIT Finance Theory I](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/)：包含固定收益证券和现值关系。
- [QuantLib Documentation](https://www.quantlib.org/docs.shtml)：固定收益类和曲线工具的官方入口。

## 8. 建议实践

- 实现固定息债券的全价、净价、应计利息、YTM、久期和凸性。
- 用一组存款或债券报价 Bootstrap 简化贴现曲线。
- 对平行移动和非平行移动比较全量重定价与久期近似。

## 9. 与其他主题的关系

固定收益把 [金融数学](02-financial-mathematics.md) 应用于利率现金流，并为 [衍生品](04-derivatives.md) 的远期、互换和利率期权提供曲线基础；敏感度进入 [风险管理](06-risk-management.md)。

## 10. 常见误区

- YTM 把多个现金流压缩成单一内部收益率，不是一条完整曲线。
- 久期只是一阶近似，且对非平行曲线变化可能不足。
- 信用利差同时可能包含违约、流动性和风险溢价。
- 净价与全价混用会导致结算金额错误。
