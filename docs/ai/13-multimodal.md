# 多模态

## 1. 主题简介

多模态模型联合处理图像、文本、音频和视频。本章从视觉编码与图文对齐出发，进入视觉语言模型、文档理解和多模态 Agent。

## 2. 前置知识

- [Transformer](02-transformer.md)、卷积神经网络与表示学习
- 图像张量、采样、分辨率和基本信号处理

## 3. 核心概念

- CNN、Vision Transformer 与 Patch Embedding
- CLIP、Contrastive Learning 与 Image-Text Alignment
- Vision Encoder、Projector、Multimodal Tokens 与 VLM
- Multimodal Pretraining、Multimodal SFT 与数据配对
- OCR、版面、表格与 Document Understanding
- 音频表征、视频采样、时间建模
- 多模态工具使用、Grounding 与 Multimodal Agent

## 4. 推荐学习顺序

1. 用 CNN 和 ViT 完成小型图像分类，理解空间归纳偏置。
2. 学习 CLIP 的双编码器、对比损失与零样本分类。
3. 将视觉编码器通过 Projector 接入语言模型，理解视觉 Token。
4. 比较预训练对齐与多模态 SFT 的目标和数据。
5. 进入 OCR、文档版面、音频和视频的专门表示。
6. 为多模态 Agent 加入定位、工具调用和证据评价。

## 5. 核心论文

- [An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929)：Vision Transformer 的代表性工作。
- [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)：CLIP 图文对齐的原始论文。
- [Flamingo](https://arxiv.org/abs/2204.14198)：视觉语言少样本学习的代表性工作。
- [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485)：多模态指令微调的代表性工作。

## 6. 推荐开源仓库

- [CLIP](https://github.com/openai/CLIP)：OpenAI 发布的 CLIP 模型与推理代码。
- [Vision Transformer](https://github.com/google-research/vision_transformer)：Google Research 的 ViT 实现。
- [LLaVA](https://github.com/haotian-liu/LLaVA)：论文作者发布的视觉指令微调仓库。
- [Transformers](https://github.com/huggingface/transformers)：包含多类视觉、音频和多模态模型接口。

## 7. 推荐课程和官方文档

- [Stanford CS231n](https://cs231n.stanford.edu/)：计算机视觉与深度学习基础课程。
- [Transformers Multimodal Chat Templates](https://huggingface.co/docs/transformers/chat_templating_multimodal)：多模态消息和处理接口说明。
- [PyTorch Computer Vision Tutorials](https://docs.pytorch.org/tutorials/intermediate/torchvision_tutorial.html)：官方视觉任务实践入口。

## 8. 建议实践

- 用预训练 CLIP 对小型图像集做零样本分类，并分析提示词敏感性。
- 对文档页面比较纯 OCR、版面信息和视觉语言模型的字段抽取结果。
- 构造需要读图再调用计算工具的任务，检查视觉证据与最终答案是否一致。

## 9. 与其他主题的关系

多模态延伸 [Transformer](02-transformer.md)、[微调](07-fine-tuning.md) 和 [Agent](11-agent.md)，并在 [金融 Transformer](../ml-finance/07-transformers-for-finance.md) 中连接图表、公告、表格和时间序列。

## 10. 常见误区

- OCR 正确不代表模型理解了版面、表格关系或数值单位。
- 图文对齐模型与生成式视觉语言模型的目标不同。
- 增加图像分辨率会增加 Token 和计算，不保证信息利用率同步提高。
- 多模态回答流畅不代表视觉定位和证据可靠。
