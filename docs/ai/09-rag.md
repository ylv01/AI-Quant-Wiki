# RAG

## 1. 主题简介

Retrieval-Augmented Generation（RAG）在生成前检索外部证据，使回答能够利用可更新、可引用的知识。系统质量由解析、召回、排序、上下文组织和生成共同决定。

## 2. 前置知识

- 文本处理、向量相似度、信息检索基础
- [Transformer](02-transformer.md)与基本语言模型推理

## 3. 核心概念

- 文档解析、结构保留、Chunking 与元数据
- Embedding、Vector Database 与近似最近邻
- BM25、Sparse Retrieval、Dense Retrieval 与 Hybrid Retrieval
- Reranker、Query Expansion 与 Query Rewriting
- Multi-hop Retrieval、Context Compression 与去重
- Citation、答案归因、检索评价和端到端 RAG Evaluation

## 4. 推荐学习顺序

1. 为小语料建立问题、相关文档和答案证据的评价集。
2. 先实现 BM25，再实现 Dense Retrieval，比较 Recall@k。
3. 调整 Chunk 粒度、重叠和元数据过滤。
4. 增加混合检索和 Reranker，观察召回与排序变化。
5. 将检索结果组织为带来源的上下文并生成引用。
6. 分开评价解析、召回、排序、证据支持和最终回答。

## 5. 核心论文

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)：RAG 的代表性原始工作。
- [REALM](https://arxiv.org/abs/2002.08909)：将可微检索引入语言模型预训练的工作。
- [ColBERT](https://arxiv.org/abs/2004.12832)：使用 Late Interaction 兼顾细粒度匹配和检索效率。

## 6. 推荐开源仓库

- [FAISS](https://github.com/facebookresearch/faiss)：高效稠密向量相似搜索与聚类库。
- [LangChain](https://github.com/langchain-ai/langchain)：包含检索和生成组件的官方框架仓库。
- [LlamaIndex](https://github.com/run-llama/llama_index)：面向数据接入、索引和检索工作流的官方仓库。

## 7. 推荐课程和官方文档

- [FAISS Documentation](https://faiss.ai/)：索引结构、搜索与聚类文档。
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)：数据连接、索引、检索与评价入口。
- [LangChain Retrieval](https://docs.langchain.com/oss/python/langchain/retrieval)：检索组件官方说明。

## 8. 建议实践

- 对同一文档集实现 BM25、Dense 和 Hybrid 三个基线。
- 建立至少包含答案证据位置的查询集，报告 Recall@k、MRR 和引用支持率。
- 人为加入扫描错误、重复页和超长表格，检查解析及 Chunking 的失败模式。

## 9. 与其他主题的关系

RAG 为 [Context Engineering](10-context-engineering.md) 提供可选择的外部证据，也常作为 [Agent](11-agent.md) 的知识工具。文档和索引更新属于数据工程问题。

## 10. 常见误区

- 向量数据库不是 RAG 的全部，BM25 和重排常是重要基线。
- Chunk 越小不一定召回越好，语义完整性与定位精度需要权衡。
- 模型给出引用不代表引用真的支持答案。
- 端到端答案错误不能直接归因于生成模型，可能来自解析或检索。
