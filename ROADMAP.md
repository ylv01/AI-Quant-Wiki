# 学习路线

本文只描述推荐学习顺序与知识依赖。三条路线可独立进入，也可在机器学习金融部分汇合。

## A. AI / LLM 路线

### 阶段 1：基础

Python → NumPy → PyTorch → 线性代数 → 概率统计 → 微积分 → 神经网络 → 反向传播 → 优化器 → 损失函数

目标是能用张量表达模型、手工推导梯度，并读懂一个最小训练循环。详见 [AI 基础](docs/ai/01-foundations.md)。

### 阶段 2：Transformer

Token Embedding → Position Encoding → Q、K、V → Scaled Dot-Product Attention → Multi-Head Attention → Causal Mask → Residual Connection → LayerNorm → MLP → Decoder-only Transformer → Cross Entropy → Autoregressive Generation

先理解张量形状和掩码，再实现单头、多头和完整解码器。详见 [Transformer](docs/ai/02-transformer.md)。

### 阶段 3：Token Engineering

Character Tokenization → Word Tokenization → BPE → WordPiece → SentencePiece → Vocabulary Design → Special Tokens → BOS、EOS、PAD → Chat Template → Loss Mask → Sequence Packing → Padding → Truncation → Token Compression Ratio

重点是理解文本边界、词表和训练样本格式如何共同决定模型看到的序列。详见 [Token Engineering](docs/ai/03-token-engineering.md)。

### 阶段 4：训练数据

数据采集 → 数据清洗 → 去重 → 质量过滤 → 数据配比 → 数据混合 → Curriculum → Synthetic Data → Instruction Data → Preference Data → Train、Validation、Test Split → Data Leakage

先定义来源、许可和数据谱系，再进行过滤、混合与切分。详见 [训练数据](docs/ai/04-training-data.md)。

### 阶段 5：预训练

GPT → Autoregressive Objective → Training Loop → AdamW → Muon → Learning Rate Schedule → Warmup → Weight Decay → Gradient Clipping → Gradient Accumulation → Mixed Precision → Checkpoint → Scaling Laws → Compute-Optimal Training

从小模型闭环入手，再分析优化器、数值稳定性和算力分配。详见 [预训练](docs/ai/05-pretraining.md)。

### 阶段 6：训练系统

GPU → CUDA 基础 → DDP → FSDP → ZeRO → Tensor Parallelism → Pipeline Parallelism → Data Parallelism → FlashAttention → Activation Checkpointing → Kernel Fusion → Communication Overhead → Throughput → MFU → Distributed Checkpoint

先建立单卡性能基线，再按内存、计算和通信瓶颈选择并行策略。详见 [训练系统](docs/ai/06-training-systems.md)。

### 阶段 7：微调

Continued Pretraining → Domain Adaptation → SFT → Full Fine-tuning → LoRA → QLoRA → Adapter → Dataset Formatting → Chat Template → Loss Masking → Evaluation

先明确适配目标与数据格式，再比较全量和参数高效方法。详见 [微调](docs/ai/07-fine-tuning.md)。

### 阶段 8：后训练

Preference Learning → Reward Model → RLHF → PPO → DPO → IPO → KTO → ORPO → GRPO → Rejection Sampling → Process Reward → Outcome Reward → Alignment Evaluation

从偏好数据与奖励定义出发，区分在线强化学习、离线偏好优化和采样筛选。详见 [后训练](docs/ai/08-post-training.md)。

### 阶段 9：RAG

文档解析 → Chunking → Embedding → Vector Database → BM25 → Dense Retrieval → Sparse Retrieval → Hybrid Retrieval → Reranker → Query Expansion → Query Rewriting → Multi-hop Retrieval → Context Compression → Citation → RAG Evaluation

先建设可评价的检索基线，再增加生成、重排和多跳策略。详见 [RAG](docs/ai/09-rag.md)。

### 阶段 10：Context Engineering

Prompt Structure → System Prompt → Context Window → Long Context → Context Selection → Context Compression → Context Caching → KV Cache → Memory → Conversation State → Retrieval Memory → Working Memory → Context Evaluation

把上下文视为有限预算下的状态与证据编排问题。详见 [Context Engineering](docs/ai/10-context-engineering.md)。

### 阶段 11：Agent

Tool Calling → Function Calling → ReAct → Planning → Reflection → Memory → Workflow → State Machine → Multi-Agent → Agent Evaluation → Sandboxed Execution → Human in the Loop

先构建确定性工具循环，再逐步加入规划、状态和人工控制。详见 [Agent](docs/ai/11-agent.md)。

### 阶段 12：Agent Skills

Skill Definition → Skill Packaging → Skill Discovery → Skill Routing → Skill Loading → Tool Registry → MCP → Connector → Permission Control → Skill Evaluation → Harness Engineering → Long-Running Agent

重点学习能力的声明、发现、加载、权限边界与长任务运行环境。详见 [Agent Skills、工具调用与 MCP](docs/ai/12-agent-skills.md)。

### 阶段 13：多模态

CNN → Vision Transformer → CLIP → Vision Encoder → Projector → Multimodal Tokens → Image-Text Alignment → VLM → Multimodal Pretraining → Multimodal SFT → OCR → Document Understanding → Audio → Video → Multimodal Agent

从视觉表征和跨模态对齐开始，再进入生成、文档和 Agent 场景。详见 [多模态](docs/ai/13-multimodal.md)。

### 阶段 14：推理与服务部署

Prefill → Decode → KV Cache → PagedAttention → Continuous Batching → Prefix Caching → Quantization → Speculative Decoding → TTFT → TPOT → Tail Latency → Serving Benchmark

先冻结模型与生成语义，再比较缓存、批处理和优化对延迟、吞吐、显存与质量的影响。本阶段可在 Transformer 与 Context 基础后提前进入。详见 [推理与服务部署](docs/ai/14-inference-and-serving.md)。

## B. 金融工程路线

### 阶段 1：金融市场基础

股票 → 债券 → 基金 → 指数 → 期货 → 期权 → 外汇 → 利率 → 收益率 → 风险溢价

先掌握合约、现金流、报价和参与者，再讨论模型。详见 [金融市场基础](docs/finance/01-market-foundations.md)。

### 阶段 2：金融数学

货币时间价值 → 单利与复利 → 贴现 → 现金流 → 随机变量 → 随机过程 → 布朗运动 → 伊藤过程 → Monte Carlo

从确定性现金流过渡到随机路径和数值估计。详见 [金融数学](docs/finance/02-financial-mathematics.md)。

### 阶段 3：固定收益

债券定价 → 到期收益率 → 即期利率 → 远期利率 → 收益率曲线 → 久期 → 凸性 → 利率风险 → 信用风险

先统一现金流和曲线表示，再学习敏感度与风险来源。详见 [固定收益](docs/finance/03-fixed-income.md)。

### 阶段 4：衍生品

远期 → 期货 → 套期保值 → 期权 → Black-Scholes → Binomial Tree → Greeks → Implied Volatility → Volatility Surface

从无套利和复制组合开始，再比较解析、树和数值方法。详见 [衍生品](docs/finance/04-derivatives.md)。

### 阶段 5：投资组合

均值方差模型 → Efficient Frontier → CAPM → Beta → Alpha → Factor Model → Risk Parity → Black-Litterman → Portfolio Optimization

从风险收益权衡进入因子暴露、观点融合与约束优化。详见 [投资组合理论](docs/finance/05-portfolio-theory.md)。

### 阶段 6：风险管理

Volatility → Drawdown → VaR → CVaR → Stress Testing → Scenario Analysis → Liquidity Risk → Counterparty Risk → Model Risk

同时学习统计度量、情景方法和非市场风险。详见 [风险管理](docs/finance/06-risk-management.md)。

### 阶段 7：市场微观结构

Order Book → Bid-Ask Spread → Market Order → Limit Order → Liquidity → Slippage → Price Impact → Order Flow → Execution Algorithm

将理论价格连接到真实成交、成本与执行风险。详见 [市场微观结构](docs/finance/07-market-microstructure.md)。

### 阶段 8：金融数据工程

行情数据 → Tick → 分钟 K 线 → 日 K → 复权 → 公司行为 → 连续期货合约 → 数据清洗 → 缺失值 → 异常值 → 时区 → 交易日历 → 数据库 → Parquet → DuckDB → Data Pipeline → Feature Store → Data Versioning

以时间一致性、可追溯性和可重放性为主线建设数据层。详见 [金融数据工程](docs/finance/08-financial-data-engineering.md)。

## C. 机器学习金融路线

### 阶段 1：统计与时间序列

描述统计 → 假设检验 → 相关性 → 自相关 → 平稳性 → ADF → AR → MA → ARIMA → GARCH → Regime → Structural Break → Distribution Shift

建立对时序依赖、波动聚集和分布变化的判断能力。详见 [统计与时间序列](docs/ml-finance/01-statistics-and-time-series.md)。

### 阶段 2：因子与特征

Momentum → Value → Quality → Volatility → Liquidity → Technical Indicators → Fundamental Factors → Cross-sectional Rank → Standardization → Neutralization → Feature Selection → Feature Stability

先定义经济含义和可用时间，再进行横截面处理与稳定性评估。详见 [因子与特征工程](docs/ml-finance/02-feature-and-factor-engineering.md)。

### 阶段 3：标签设计

Return Regression → Direction Classification → Multi-class Label → Triple Barrier → Event-Based Labeling → Forecast Horizon → Overlapping Labels → Class Imbalance → Sample Weight

标签必须与决策时点、持有期和交易目标一致。详见 [标签设计](docs/ml-finance/03-label-design.md)。

### 阶段 4：验证与防泄漏

Time-Series Split → Walk-Forward Validation → Rolling Window → Expanding Window → Purged Cross Validation → Embargo → Look-Ahead Bias → Survivorship Bias → Data Snooping → Leakage → Multiple Testing

先冻结时间语义和实验协议，再比较模型。详见 [验证与防泄漏](docs/ml-finance/04-validation-and-leakage.md)。

### 阶段 5：树模型

Decision Tree → Random Forest → XGBoost → LightGBM → CatBoost → Feature Importance → SHAP → Probability Calibration → Hyperparameter Search

从稳健基线进入提升树、解释、校准与受控搜索。详见 [树模型](docs/ml-finance/05-tree-models.md)。

### 阶段 6：神经网络

MLP → CNN for Time Series → RNN → LSTM → GRU → TCN → Autoencoder → Representation Learning

在简单基线和严格验证之上讨论序列表征。详见 [神经网络](docs/ml-finance/06-neural-networks.md)。

### 阶段 7：金融 Transformer

Time-Series Tokenization → Positional Encoding → Temporal Attention → Cross-Asset Attention → Patch-based Modeling → Multi-scale Modeling → Causal Mask → Forecasting → Classification → Time-Series Foundation Models → Zero-Shot Forecasting → Financial Language Models → Multimodal Financial Models

区分时间、资产和模态三个维度的注意力与信息可用边界。详见 [金融 Transformer](docs/ml-finance/07-transformers-for-finance.md)。

### 阶段 8：回测

Signal → Position → Transaction Cost → Commission → Slippage → Turnover → Leverage → Margin → Corporate Action → Futures Roll → Mark-to-Market → Performance Attribution

将预测转成可成交头寸，并显式模拟成本、约束和会计过程。详见 [回测](docs/ml-finance/08-backtesting.md)。

### 阶段 9：组合构建

Ranking → Threshold → Top-K → Long-Short → Position Sizing → Risk Constraint → Sector Neutrality → Beta Neutrality → Volatility Targeting → Rebalancing

从信号映射开始，加入风险预算、中性约束与调仓规则。详见 [组合构建](docs/ml-finance/09-portfolio-construction.md)。

### 阶段 10：生产 Pipeline

Data Ingestion → Feature Engineering → Label Generation → Model Training → Model Validation → Model Registry → Batch Inference → Online Inference → Signal Generation → Risk Control → Order Execution → Monitoring → Logging → Replay → Attribution

要求离线研究、在线推理和交易执行共享可追溯的数据定义。详见 [生产 Pipeline](docs/ml-finance/10-production-pipeline.md)。
