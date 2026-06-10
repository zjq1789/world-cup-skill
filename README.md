<div align="right">
  中文
</div>

<div align="center">
  <img src="./docs/images/world-cup-banner.svg" alt="世界杯" width="100%">
  <h1>World Cup Skill</h1>
  <h3>⚽ 世界杯专业比分预测 Skill</h3>
  <p><em>多模态识别比赛，联网查询最新数据，结合历史数据与赛果回写，输出一个主预测比分。</em></p>
  <img src="https://img.shields.io/badge/Skill-ChatGPT-blue?style=flat" alt="Skill">
  <img src="https://img.shields.io/badge/World%20Cup-Only-brightgreen?style=flat" alt="World Cup Only">
  <img src="https://img.shields.io/badge/Output-Scoreline-orange?style=flat" alt="Scoreline">
  <img src="https://img.shields.io/badge/language-Chinese-green?style=flat" alt="Language">
</div>

---

## 🎯 项目介绍

`World Cup Skill` 是一个面向 **世界杯比赛预测** 的 ChatGPT Skill。它的目标不是输出复杂冗长的分析报告，而是在充分利用数据的基础上，给出一个清晰的主预测结果：

> **主预测比分：A 队 x-y B 队**

同时，它会提供少量参考指标，方便解释预测依据：胜平负、大小球、双方进球、晋级概率和爆冷概率。

本项目支持三类输入：

- **文字输入**：直接告诉它“预测阿根廷 vs 法国”。
- **截图输入**：上传世界杯赛程截图，它先识别比赛，再判断哪些已经踢完、哪些还没开赛。
- **CSV / Excel 输入**：上传历史赛果、球队参数、过往预测记录，用于校准后续预测。

预测前，Skill 会要求联网查询最新信息，包括赛程状态、真实赛果、阵容、伤病停赛、近期状态、排名或 Elo、xG、赔率市场信号等。已结束比赛不会被当作未赛比赛预测，而是输出实际结果并支持写入赛果库。

> 本项目用于数据分析、学习研究和赛前讨论，不构成投注建议。

---

## 🚀 快速开始

### 1. 在 ChatGPT 中使用 Skill

上传本项目的 Skill 文件夹或打包后的 `skill.zip`，然后直接输入：

```text
预测世界杯：阿根廷 vs 法国
```

也可以上传截图：

```text
这张图里有哪些世界杯比赛？帮我只预测还没踢的比赛。
```

### 2. 使用结构化数据

如果你有历史数据，可以上传 CSV / Excel，例如：

```text
我上传了世界杯历史赛果和近期球队状态，请结合最新联网数据预测巴西 vs 德国。
```

Skill 会把上传数据作为本地历史信息，同时联网补充最新赛前信息。

---

## ✨ 核心功能

- 🖼️ 支持世界杯赛程截图识别
- 📝 支持明确文字比赛输入
- 📊 支持 CSV / Excel 历史数据
- 🌐 预测前必须联网查询最新数据
- ✅ 自动判断比赛是否已结束
- ⚽ 主要输出一个预测比分
- 📈 附带胜平负、大小球、双方进球、晋级概率、爆冷概率
- 💾 保存历史预测和真实赛果
- 🔁 根据真实赛果更新后续预测参数

---

## 🧩 模块介绍

| 模块 | 作用 | 主要文件 |
|---|---|---|
| 输入识别模块 | 识别文字、截图、CSV、Excel 中的比赛信息 | `skill/world-cup-skill/SKILL.md` |
| 比赛状态模块 | 判断比赛是未开赛、进行中，还是已经结束 | `docs/模块介绍.md` |
| 联网数据模块 | 预测前查询最新赛程、阵容、伤病、排名、xG、赔率等 | `docs/数据来源.md` |
| 历史数据模块 | 读取历史赛果、过往预测、球队参数 | `docs/数据结构.md` |
| 预测模型模块 | 结合 Elo、Poisson、xG、阵容和市场信号输出概率 | `docs/预测方法.md` |
| 输出报告模块 | 默认只给一个主预测比分，其他指标作为参考 | `docs/运行效果.md` |
| 结果回写模块 | 保存真实赛果，更新预测命中情况 | `skill/world-cup-skill/scripts/update_results.py` |

---

## 📖 内容导航

| 内容 | 说明 | 路径 |
|---|---|---|
| 快速开始 | 怎么输入、怎么使用、怎么上传数据 | [`docs/快速开始.md`](./docs/快速开始.md) |
| 模块介绍 | 各模块职责和完整工作流 | [`docs/模块介绍.md`](./docs/模块介绍.md) |
| 数据结构 | CSV / Excel 字段设计 | [`docs/数据结构.md`](./docs/数据结构.md) |
| 数据来源 | 联网查询时优先看的信息类型 | [`docs/数据来源.md`](./docs/数据来源.md) |
| 预测方法 | Elo + Poisson + 状态修正的思路 | [`docs/预测方法.md`](./docs/预测方法.md) |
| 运行效果 | 输入输出示例 | [`docs/运行效果.md`](./docs/运行效果.md) |
| 示例数据 | 示例赛程与预测输出 | [`examples/`](./examples) |
| Skill 源码 | ChatGPT Skill 主体 | [`skill/world-cup-skill/`](./skill/world-cup-skill) |

---

## 🧪 运行效果示例

### 示例一：预测未开赛比赛

**输入：**

```text
预测世界杯：阿根廷 vs 法国，专业数据分析版，但输出简洁一点。
```

**输出示例：**

```text
## 比赛预测：阿根廷 vs 法国

主预测比分：阿根廷 2-1 法国

参考概率：
- 胜平负：阿根廷胜 39% / 平 28% / 法国胜 33%
- 大小球：大2.5 46% / 小2.5 54%
- 双方进球：52%
- 晋级概率：阿根廷 53% / 法国 47%
- 爆冷概率：18%

简要依据：
- 阿根廷防守稳定性略好，法国进攻上限更高。
- 若首发阵容接近完整，比赛更可能是小比分胶着局。
- 淘汰赛环境下，常规时间平局概率会被抬高。

主要风险：
- 首发、伤病、红牌、点球和临场战术会明显改变结果。
- 本预测是数据分析，不是投注建议。
```

### 示例二：识别截图赛程

**输入：**

```text
这张截图里有几场世界杯比赛？帮我判断哪些已经踢完，只预测还没踢的。
```

**输出示例：**

```text
识别到 3 场比赛：

1. 阿根廷 vs 法国：未开赛，进入预测。
2. 巴西 vs 德国：已结束，实际比分 1-1，不做赛前预测。
3. 西班牙 vs 英格兰：未开赛，进入预测。

主预测：
- 阿根廷 2-1 法国
- 西班牙 1-1 英格兰
```

### 示例三：已结束比赛

**输入：**

```text
预测昨天的世界杯：巴西 vs 德国。
```

**输出示例：**

```text
## 比赛已结束：巴西 vs 德国

实际比分：巴西 1-1 德国

这场比赛已经结束，不再做赛前预测。
可以基于赛果、xG、阵容和关键事件做复盘，并把结果写入 match_results.csv。
```

---

## 🗂️ 仓库结构

```text
world-cup-skill/
├── README.md
├── docs/
│   ├── images/world-cup-banner.svg
│   ├── 快速开始.md
│   ├── 模块介绍.md
│   ├── 数据结构.md
│   ├── 数据来源.md
│   ├── 预测方法.md
│   └── 运行效果.md
├── examples/
│   ├── sample_matches.csv
│   ├── sample_prediction.md
│   └── sample_result_update.csv
└── skill/
    └── world-cup-skill/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/
        └── scripts/
```

---

## ⚠️ 免责声明

足球比赛具有高度随机性，世界杯短赛制尤其容易受到红牌、点球、伤病、天气、裁判尺度和临场战术影响。本项目仅用于数据分析、学习研究和赛前讨论，不提供投注建议，也不保证预测结果准确。
