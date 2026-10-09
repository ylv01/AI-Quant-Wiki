# 时序基础模型仓库

时序基础模型可作为零样本预测和概率预测的研究基线。模型代际、Python 包版本和权重许可分别记录，便于选择明确的实验环境。

| 仓库 | 方向 | 主要内容 | 适合学习什么 | 难度 | 官方地址 |
|---|---|---|---|---|---|
| TimesFM（2.5 基线） | 时序基础模型 | Google Research 的预训练时序模型与推理代码 | 零样本预测、分位数输出与基线比较 | 中级 | [GitHub](https://github.com/google-research/timesfm) |
| Chronos（Chronos-2 基线） | 时序基础模型 | Amazon 的预训练时序模型与推理代码 | 单变量、多变量、协变量和概率预测 | 中级 | [GitHub](https://github.com/amazon-science/chronos-forecasting) |

## 基线版本与许可

| 模型基线 | Python 包版本 | 仓库代码许可 | 权重与模型卡许可 |
|---|---|---|---|
| TimesFM 2.5 | `timesfm[torch]==2.0.2`，对应已发布的 [v2.0.2](https://github.com/google-research/timesfm/releases/tag/v2.0.2) | [Apache-2.0](https://github.com/google-research/timesfm/blob/v2.0.2/LICENSE) | [`google/timesfm-2.5-200m-pytorch`](https://huggingface.co/google/timesfm-2.5-200m-pytorch)：Apache-2.0 |
| Chronos-2 | `chronos-forecasting==2.3.2`，对应已发布的 [v2.3.2](https://github.com/amazon-science/chronos-forecasting/releases/tag/v2.3.2) | [Apache-2.0](https://github.com/amazon-science/chronos-forecasting/blob/v2.3.2/LICENSE) | [`amazon/chronos-2`](https://huggingface.co/amazon/chronos-2)：Apache-2.0 |

- TimesFM 的包版本 `2.0.2` 与模型版本 `2.5` 使用不同编号；该包导出 `TimesFM_2p5_200M_torch` 接口。以上版本均要求 Python 3.10 或更高版本，具体依赖以相应发布标签的 `pyproject.toml` 为准。
- TimesFM 3.0 的下载权重另采用[非商业、非生产许可证](https://huggingface.co/google/timesfm-3.0-pytorch/blob/main/LICENSE)。代码与权重需分别核对许可，本页选择 Apache-2.0 权重的 2.5 基线。
- 复现实验应固定完整依赖、模型 revision、数据切分、预测窗口与协变量可获得时间。将通用预测能力用于金融研究时，需核对预训练数据覆盖范围及评估数据重叠，并独立评价交易成本与回测表现。
