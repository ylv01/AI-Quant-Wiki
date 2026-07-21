# 微调

## 1. 主题简介

微调让预训练模型适配领域、任务或对话格式。本章比较持续预训练、监督微调、全量更新与参数高效方法，并强调数据格式和评价设计。

## 2. 前置知识

- [预训练](05-pretraining.md)中的语言模型目标和优化过程
- [Token Engineering](03-token-engineering.md)中的 Chat Template 与 Loss Mask

## 3. 核心概念

- Continued Pretraining 与 Domain Adaptation
- Supervised Fine-Tuning（SFT）
- Full Fine-tuning、Adapter、LoRA、QLoRA
- Rank、Target Modules、量化基座与可训练参数
- Dataset Formatting、Chat Template、Packing、Loss Masking
- 训练集、开发集、任务评价与灾难性遗忘

## 4. 推荐学习顺序

1. 明确目标是领域知识适配、行为学习还是输出格式约束。
2. 建立原始基座模型的任务与通用能力基线。
3. 核对对话模板、labels 和 loss mask，再运行小批次过拟合测试。
4. 从 LoRA/SFT 小实验开始，比较 Target Modules 和 Rank。
5. 资源允许时与全量微调或持续预训练做受控比较。
6. 同时评价目标任务、通用能力、安全性和输出稳定性。

## 5. 核心论文

- [LoRA](https://arxiv.org/abs/2106.09685)：低秩参数高效适配的原始论文。
- [QLoRA](https://arxiv.org/abs/2305.14314)：研究量化基座上的高效微调。
- [Parameter-Efficient Transfer Learning for NLP](https://arxiv.org/abs/1902.00751)：Adapter 方法的代表性工作。

## 6. 推荐开源仓库

- [PEFT](https://github.com/huggingface/peft)：Hugging Face 参数高效微调官方库。
- [TRL](https://github.com/huggingface/trl)：提供 SFT 与多种后训练 Trainer。
- [Transformers](https://github.com/huggingface/transformers)：模型、Tokenizer 与训练接口的官方仓库。

## 7. 推荐课程和官方文档

- [PEFT Documentation](https://huggingface.co/docs/peft/)：LoRA、Adapter 与模型集成说明。
- [TRL SFT Trainer](https://huggingface.co/docs/trl/sft_trainer)：SFT 数据与训练接口。
- [Transformers Training](https://huggingface.co/docs/transformers/training)：官方训练流程概览。

## 8. 建议实践

- 用少量公开指令样本对小模型做 LoRA SFT，并检查仅回答区域参与损失。
- 保存 Adapter 后重新加载，验证推理输出与合并前一致。
- 对基座、LoRA 与不同 Rank 运行同一组任务和通用能力评价。

## 9. 与其他主题的关系

微调承接预训练模型与指令数据，并为 [后训练](08-post-training.md)、[RAG](09-rag.md) 和领域模型提供基线。其序列格式由 [Token Engineering](03-token-engineering.md) 决定。

## 10. 常见误区

- LoRA 减少可训练参数，不代表训练时无需加载基座和激活。
- QLoRA 的量化对象与推理量化不是同一个评价问题。
- 持续预训练和 SFT 的数据形态、目标和风险不同。
- 训练损失更低不能证明指令遵循或事实性更好。
