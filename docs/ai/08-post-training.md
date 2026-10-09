# 后训练

## 1. 主题简介

后训练使用人类或模型偏好、奖励信号和筛选策略调整模型行为。重点是理解偏好数据如何进入目标函数，以及评价是否真的反映预期行为。可验证奖励的推理后训练还需要区分偏好判断与可自动核验的任务正确性，并控制在线采样和评价预算。

## 2. 前置知识

- [微调](07-fine-tuning.md)与概率语言模型
- 强化学习中的策略、奖励、价值、重要性采样与 KL 约束基础

## 3. 核心概念

- Preference Data、Pairwise Ranking 与 Preference Learning
- Reward Model、Process Reward 与 Outcome Reward
- RLHF、PPO、参考策略与 KL Regularization
- DPO、IPO、KTO、ORPO、GRPO 的数据与目标差异
- Rejection Sampling 与 Best-of-N
- Verifiable Reward、在线 Rollout、Group-relative Advantage 与推理蒸馏
- 训练算力、测试时计算、采样数和正确性评价口径
- Reward Hacking、长度偏差与 Alignment Evaluation

## 4. 推荐学习顺序

1. 从偏好标注协议、一致性和数据切分开始。
2. 训练并校准奖励模型，检查长度、格式和主题偏差。
3. 理解 PPO 式 RLHF 的策略、价值、奖励和 KL 各组件。
4. 推导 DPO 目标，再比较其他离线偏好目标的假设。
5. 比较 Rejection Sampling、GRPO 在线生成和可验证奖励，检查组内奖励方差、长度偏差及被截断的回答。
6. 使用任务、安全、事实性和过度优化指标进行多维评价。

## 5. 核心论文

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)：SFT、奖励模型与 PPO 式 RLHF 的代表性系统。
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290)：无需显式奖励模型的偏好优化方法。
- [KTO: Model Alignment as Prospect Theoretic Optimization](https://arxiv.org/abs/2402.01306)：研究非成对偏好反馈的一种目标。
- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)：GRPO 的原始来源，连接数学数据、在线采样和组内相对奖励。
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)：可验证任务上的推理强化学习与向小模型迁移的代表性研究。

## 6. 推荐开源仓库

- [TRL](https://github.com/huggingface/trl)：SFT、奖励建模和多种偏好优化方法的官方实现集合。
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)：面向大模型 RLHF 的开源训练框架。

## 7. 推荐课程和官方文档

- [TRL Documentation](https://huggingface.co/docs/trl/)：后训练 Trainer 与数据格式参考。
- [Stanford CS224N](https://web.stanford.edu/class/cs224n/)：课程安排包含语言模型后训练主题。
- [TRL GRPO Trainer](https://huggingface.co/docs/trl/grpo_trainer)：奖励函数、在线生成、损失选项和训练指标的官方说明。

## 8. 建议实践

- 构造可解释的小型偏好数据，训练奖励模型并分析长度相关性。
- 在同一 SFT 基线和数据切分上比较 DPO 与 Rejection Sampling。
- 对比胜率之外的输出长度、拒答、事实性和分布外任务表现。
- 用小模型和可自动核验答案的任务运行 GRPO；记录奖励、独立测试准确率、生成长度、截断率和组内奖励方差。
- 与相同基座的 SFT、Best-of-N 基线比较，固定测试题和总生成 Token 预算，并报告训练预算；避免把更多采样当成训练收益。

## 9. 与其他主题的关系

后训练通常以 [微调](07-fine-tuning.md) 模型为起点，并为 [Agent](11-agent.md) 的工具使用和遵循约束提供行为基础；评价设计也会影响 Agent 级指标。

## 10. 常见误区

- 偏好标签不等于客观真值。
- Reward Model 分数提高不保证真实用户效用提高。
- DPO 不是无假设的通用替代方案，它依赖参考策略和偏好数据分布。
- 方法缩写相近不代表训练数据、在线程度和目标函数相同。
- 可验证奖励只覆盖定义好的核验规则；数学或代码任务的收益不能直接证明开放金融判断更可靠。
