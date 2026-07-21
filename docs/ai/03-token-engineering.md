# Token Engineering

## 1. 主题简介

Token Engineering 决定原始文本如何变成模型可处理的整数序列，以及哪些位置参与损失。它直接影响词表覆盖、序列长度、训练效率和对话边界。

## 2. 前置知识

- Unicode、UTF-8 和字符串处理
- [Transformer](02-transformer.md)中的 Embedding、上下文窗口和交叉熵

## 3. 核心概念

- Character、Word、Byte 与 Subword Tokenization
- BPE、WordPiece、Unigram 与 SentencePiece
- Vocabulary Design、未知字符和归一化
- Special Tokens、BOS、EOS、PAD
- Chat Template、角色边界与消息序列化
- Loss Mask、Sequence Packing、Padding、Truncation
- Token Compression Ratio 与不同语言的切分差异

## 4. 推荐学习顺序

1. 比较字符、单词和字节级切分的可逆性与序列长度。
2. 在小语料上手工执行若干轮 BPE 合并。
3. 学习 SentencePiece/Unigram 与 WordPiece 的目标和训练差异。
4. 设计特殊 Token、对话模板及输入输出边界。
5. 实现 Padding、Packing 和 Loss Mask，并检查标签位移。
6. 用多语言与代码样本统计压缩率、截断率和词表覆盖。

## 5. 核心论文

- [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909)：将 BPE 引入子词建模的代表性工作。
- [SentencePiece](https://arxiv.org/abs/1808.06226)：从原始句子训练语言无关子词模型的原始论文。

## 6. 推荐开源仓库

- [Hugging Face Tokenizers](https://github.com/huggingface/tokenizers)：训练和运行现代 Tokenizer 的官方库。
- [SentencePiece](https://github.com/google/sentencepiece)：SentencePiece 原作者仓库。
- [Transformers](https://github.com/huggingface/transformers)：可检查模型 Tokenizer 与 Chat Template 的集成方式。

## 7. 推荐课程和官方文档

- [Hugging Face Tokenizers 文档](https://huggingface.co/docs/tokenizers/)：Tokenizer 组件与训练流程。
- [Transformers Chat Templates](https://huggingface.co/docs/transformers/chat_templating)：官方对话模板说明。
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter6/1)：子词算法和 Tokenizer 构建课程。

## 8. 建议实践

- 在中英文与代码混合语料上训练小型 BPE 和 Unigram 词表。
- 对比词表大小、平均 Token 数、未知字符、截断比例与可逆性。
- 构造两轮对话，打印 input IDs、labels 和 loss mask，逐位置核对。

## 9. 与其他主题的关系

Tokenizer 把 [训练数据](04-training-data.md) 转换为 [预训练](05-pretraining.md) 和 [微调](07-fine-tuning.md) 的样本；Chat Template 和 Loss Mask 还决定 [后训练](08-post-training.md) 的监督边界。

## 10. 常见误区

- Token 不等于汉字、单词或字节，具体边界由词表和算法决定。
- 增大词表会缩短序列，但也增加嵌入参数和稀疏 Token 风险。
- PAD、EOS 和对话结束标记不应在未验证时随意复用。
- Packing 提升利用率，但必须隔离样本边界和损失位置。
