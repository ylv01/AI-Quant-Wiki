# 树模型

## 1. 主题简介

树模型能够处理非线性、交互和混合尺度特征，是表格型金融数据的重要基线。本章关注模型差异、概率校准、解释稳定性和受控参数搜索。

## 2. 前置知识

- 决策边界、损失函数、偏差—方差和交叉验证
- [验证与防泄漏](04-validation-and-leakage.md)中的时间切分协议

## 3. 核心概念

- Decision Tree、分裂、叶节点和剪枝
- Bagging、Random Forest 与特征子采样
- Gradient Boosting、XGBoost、LightGBM、CatBoost
- 深度、叶子数、学习率、迭代轮数和正则化
- Split/Gain/Permutation Feature Importance
- SHAP 的局部与全局解释
- Probability Calibration、阈值和排序指标
- Hyperparameter Search 与早停

## 4. 推荐学习顺序

1. 用单棵树理解分裂、过拟合和缺失值路径。
2. 用 Random Forest 建立 Bagging 基线。
3. 学习梯度提升目标，再比较 XGBoost、LightGBM 和 CatBoost。
4. 在每个时间训练窗内部完成早停和参数选择。
5. 比较 Gain、Permutation 与 SHAP，并检查跨时间稳定性。
6. 对分类概率做走步校准，最后再选择交易阈值。

## 5. 核心论文

- [Random Forests](https://doi.org/10.1023/A:1010933404324)：随机森林的经典论文。
- [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/abs/1603.02754)：XGBoost 系统与算法论文。
- [LightGBM](https://papers.nips.cc/paper_files/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html)：LightGBM 的 GOSS 与 EFB 方法论文。
- [A Unified Approach to Interpreting Model Predictions](https://arxiv.org/abs/1705.07874)：SHAP 统一解释框架的论文。

## 6. 推荐开源仓库

- [scikit-learn](https://github.com/scikit-learn/scikit-learn)：决策树、随机森林、校准和模型选择。
- [XGBoost](https://github.com/dmlc/xgboost)：XGBoost 官方仓库。
- [LightGBM](https://github.com/microsoft/LightGBM)：LightGBM 官方仓库。
- [CatBoost](https://github.com/catboost/catboost)：CatBoost 官方仓库。
- [SHAP](https://github.com/shap/shap)：SHAP 原作者维护的解释工具。

## 7. 推荐课程和官方文档

- [scikit-learn Ensemble Guide](https://scikit-learn.org/stable/modules/ensemble.html)：树集成方法官方说明。
- [XGBoost Documentation](https://xgboost.readthedocs.io/)：参数、训练和预测文档。
- [LightGBM Documentation](https://lightgbm.readthedocs.io/)：算法特性与参数参考。

## 8. 建议实践

- 在固定 Walk-Forward 切分上比较逻辑回归、随机森林、XGBoost 与 LightGBM。
- 同时报告排序、分类、校准、换手和含成本回测指标。
- 比较不同窗口的 SHAP 排名和方向，识别不稳定解释。

## 9. 与其他主题的关系

树模型使用 [因子与特征工程](02-feature-and-factor-engineering.md) 和 [标签设计](03-label-design.md) 的输出，并作为 [神经网络](06-neural-networks.md) 与 [金融 Transformer](07-transformers-for-finance.md) 的强基线。

## 10. 常见误区

- Feature Importance 高不代表因果关系或未来稳定性。
- 随机搜索若查看同一测试期，仍会发生选择偏差。
- 概率排序好不代表概率已经校准。
- 不同提升树库的叶生长、缺失值和类别特征处理不能只按参数名类比。
