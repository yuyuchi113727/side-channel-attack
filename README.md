# 基于深度学习的侧信道攻击（PyTorch）

本项目使用 PyTorch 实现基于深度学习的侧信道攻击（Side-Channel Attack, SCA），包含：

- CNN 模型
- ASCAD 风格数据集读取
- Rank 演化分析
- Loss 曲线绘制
- 模型权重保存

适用于：

探究密码学与深度学习跨学科融合

---

# 项目结构

```text
project/
│
├── main.py
├── model_framework.py
├── train_model.py
├── test_model.py
├── datafactory.py
│
├── config.yaml
├── requirements.txt
├── README.md
├── .gitignore
├── (ASCAD.h5)
├── (ascad_cnn_model.pth)
│
├── rank.png
└── loss.png
```

括号表示需要自己生成

---

# 环境配置

推荐：

- Python 3.10
- CUDA 11.8
- PyTorch 2.1.2

安装依赖：

```bash
pip install -r requirements.txt
```

若使用 NVIDIA GPU，推荐安装 CUDA 版本 PyTorch：

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

---


# 数据集说明

本项目使用 ASCAD 风格 HDF5 数据集

下载网址：

https://www.data.gouv.fr/api/1/datasets/r/e7ab6f9e-79bf-431f-a5ed-faf0ebe9b08e

下载完成后解压缩，找到ASCAD.h5数据集即可

数据集通常包含：

```python
Profiling_traces/
Attack_traces/

traces
labels
metadata
```

其中：

- traces：功耗波形
- labels：中间值（Sbox）标签
- metadata：明文、密钥等信息

---

# 训练方法

直接运行：

```bash
python main.py
```

程序将：

- 读取数据集
- 训练模型
- 保存权重
- 绘制 Loss 曲线
- 绘制 Rank 曲线

---


# Rank 演化说明

项目支持 Rank Evolution 分析。

含义：

- Rank = 0：正确密钥排名第一，攻击成功
- Rank < 5：实际攻击中通常已可接受

随着攻击 traces 增加：

- Rank 越低越好
- 理想情况下最终收敛到 0

---

# Loss 曲线说明

使用交叉熵损失函数：

- ln(256) ≈ 5.545：随机猜测水平
- ln(5) ≈ 1.609：攻击底线，为Rank=5时的理想最大交叉熵

Loss 越低表示模型区分能力越强。

---

# 可视化结果

训练结束后会生成：

- `rank.png`
- `loss.png`

---

# 项目说明

本项目主要用于：

密码学导论课程大作业开源

不用于任何非法用途。

---

# License

MIT License