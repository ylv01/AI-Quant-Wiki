# 从零实现 LLM 仓库

| 仓库 | 方向 | 主要内容 | 适合学习什么 | 难度 | 官方地址 |
|---|---|---|---|---|---|
| minGPT（半归档） | GPT 教学实现 | 紧凑呈现 GPT 模型、训练器和生成流程 | Decoder-only Transformer 的代码结构 | 入门 | [GitHub](https://github.com/karpathy/minGPT) |
| nanochat | LLM 完整训练流程 | 单一代码库实现 Tokenizer、预训练、微调、评价与推理 | 理解模型从数据到聊天接口的完整闭环 | 中级 | [GitHub](https://github.com/karpathy/nanochat) |
| build-nanogpt | 逐步构建 GPT | 配合视频和清晰提交历史逐步复现 GPT-2 训练代码 | 按提交理解训练系统的形成过程 | 中级 | [GitHub](https://github.com/karpathy/build-nanogpt) |
| llm.c | C/CUDA 训练 | 用 C/CUDA 实现 GPT-2/GPT-3 风格训练路径 | 框架之下的张量、Kernel 与训练循环 | 进阶 | [GitHub](https://github.com/karpathy/llm.c) |
| LLMs-from-scratch | 教学实现 | 与原作者教材配套，从 Tokenizer 到预训练和微调构建 GPT | 分章节实现和实验 LLM 组件 | 入门 | [GitHub](https://github.com/rasbt/LLMs-from-scratch) |

[nanoGPT](https://github.com/karpathy/nanoGPT) 已由作者标注为 deprecated，并推荐后继 nanochat；仍可作为 GPT-2 训练流程的历史教学参考。minGPT 已由作者标注为半归档状态，仍适合学习基础模型结构，运行示例时应核对依赖兼容性。
