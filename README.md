# AI-Quant-Roadmap

从大模型底层、RAG、Agent、多模态，到金融工程和机器学习金融的系统学习路线。

本仓库是中文为主的公开知识导航，整理推荐学习顺序以及可核验的论文、课程、官方文档和开源仓库。它包含各种教材、课程、论文原文。

作者：ylv

## Knowledge Map

### AI / LLM 路线

基础 → Transformer → Token Engineering → 训练数据 → 预训练 → 训练系统  
→ 微调 → 后训练 → RAG → Context Engineering → Agent → Agent Skills / MCP → 多模态

入口：[AI / LLM 路线](docs/ai/README.md)

### 金融工程路线

市场基础 → 金融数学 → 固定收益 → 衍生品  
→ 投资组合 → 风险管理 → 市场微观结构 → 金融数据工程

入口：[金融工程路线](docs/finance/README.md)

### 机器学习金融路线

统计与时间序列 → 因子与特征 → 标签设计  
→ 验证与防泄漏 → 树模型 → 神经网络  
→ 金融 Transformer → 回测 → 组合构建 → 生产 Pipeline

入口：[机器学习金融路线](docs/ml-finance/README.md)

三条路线可以独立学习。AI 与金融工程在机器学习金融路线交汇：金融数据和金融理论定义问题、约束与评价方式，机器学习与大模型方法负责表示、预测和交互，回测及生产系统负责把研究假设置于可审计的决策流程中。

## 推荐的总体学习顺序

1. 先补齐 Python、数学、统计和基本金融市场知识。
2. AI 方向依次学习神经网络、Transformer、Tokenizer、数据与训练，再进入微调、RAG、Agent 和多模态。
3. 金融方向依次学习资产、定价、组合、风险与市场机制，再建设可靠的金融数据层。
4. 在统计与时间序列基础上设计特征、标签和时间顺序验证，之后比较树模型、神经网络与 Transformer。
5. 最后把预测信号接入含成本、约束和归因的回测，再讨论生产 Pipeline。

完整阶段说明见 [ROADMAP.md](ROADMAP.md)。

## 论文资源

- [论文索引总览](resources/papers/README.md)
- [Transformer 与 LLM](resources/papers/transformer-and-llm.md)
- [训练与扩展规律](resources/papers/training-and-scaling.md)
- [微调与对齐](resources/papers/fine-tuning-and-alignment.md)
- [RAG 与上下文](resources/papers/rag-and-context.md)
- [Agent 与 Skills](resources/papers/agents-and-skills.md)
- [多模态](resources/papers/multimodal.md)
- [金融工程](resources/papers/financial-engineering.md)
- [机器学习金融](resources/papers/machine-learning-finance.md)

## 开源仓库

- [仓库索引总览](resources/repositories/README.md)
- [从零实现 LLM](resources/repositories/llm-from-scratch.md)
- [训练系统](resources/repositories/training-systems.md)
- [RAG 与 Agent](resources/repositories/rag-and-agents.md)
- [多模态](resources/repositories/multimodal.md)
- [金融工程与数据](resources/repositories/financial-engineering.md)
- [量化研究](resources/repositories/quantitative-finance.md)

## 课程、书籍与官方文档

- [课程](resources/courses/README.md)
- [书籍](resources/books/README.md)
- [官方文档](resources/official-docs/README.md)

## 仓库维护原则

- 只描述知识依赖、推荐顺序和资源导航。
- 优先收录原论文、会议页面、大学课程、官方文档及官方或原作者仓库。
- 外部资源介绍采用简短的原创概括，不复制论文摘要或项目 README。
- 无法确认题名、年份、来源归属或链接的资源不纳入索引。
- 不根据仓库名称猜测用途，不记录 Stars、性能排名或未经核验的硬件成本。
- 每个主题首轮至多列出 5 篇论文、5 个仓库以及 3 门课程或官方文档。
- 贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 检查相对链接

在仓库根目录运行：

```bash
python scripts/check_markdown_links.py
```

脚本只检查 Markdown 中的本地相对路径；外部链接仍需在内容维护时人工核验其来源与归属。

## 内容免责声明

本仓库仅用于教育与研究导航，不构成投资建议、交易建议、法律意见或任何收益承诺。金融模型与回测都可能受数据偏差、估计误差、市场变化、交易成本和执行约束影响；使用者应独立判断并承担相应风险。外部资源的版权和许可归各自权利人所有。
