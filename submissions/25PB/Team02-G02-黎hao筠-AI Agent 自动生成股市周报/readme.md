# T-E2：AI Agent 自动生成股市周报（PDF + HTML）

> 课程：数据分析与经济决策（ds2026）｜小组：Team02

| 项目   | 链接                                                                                                                                                     |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GitHub | https://github.com/lizi586586-code/T-E2-AI-Agent-Automated-Stock-Market-Weekly-Report                                                                    |
| Pages  | https://htmlpreview.github.io/?https://github.com/lizi586586-code/T-E2-AI-Agent-Automated-Stock-Market-Weekly-Report/blob/main/output/weekly_report.html |

---

## 一、项目简介

本项目是 T-E2 作业，目标是构建一个自动化股市周报生成系统：自动拉取 A 股和美股关键指数数据，进行清洗、分析和可视化，最终生成排版精美的周报。

项目采用"数据层 → 分析层 → 可视化层"三层流水线架构，4 个 Jupyter Notebook 按编号顺序执行。

## 二、项目结构

```
Team02_小组作业/
├── readme.md                    ← 项目简介、分工说明、GitHub 链接
├── data_raw/                    ← 原始数据（直接获取，不做修改）
│   ├── A股原始数据.csv
│   └── 美股原始数据.csv
├── data_clean/                  ← 清洗后数据 + 分析结果
│   ├── A股清洗后数据.csv
│   ├── 美股清洗后数据.csv
│   ├── 周度涨跌幅汇总.csv
│   ├── 风险收益指标.csv
│   └── 相关性矩阵.csv
├── output/                      ← 图表输出
│   ├── 图表1_收盘价折线图.png
│   ├── 图表2_区间涨跌幅柱状图.png
│   ├── 图表3_中美日收益率散点图.png
│   └── 图表4_成交量占比饼图.png
├── 01_数据获取.ipynb            ← 数据获取
├── 02_数据清洗.ipynb            ← 数据清洗与整理
├── 03_实证分析.ipynb             ← 探索性/验证性分析
└── 04_可视化绘图.ipynb          ← 数据可视化
```

## 三、分工说明

本小组共完成两份作业。

| 组员（学号）             | 主要负责                                |
| ------------------------ | --------------------------------------- |
| 黎㵆筠（25210155）       | 项目统筹、代码框架与核心逻辑、最终审查  |
| 王佳（25210244）         | 负责数据获取、数据清洗模块              |
| 刘雄（25210196）         | 负责实证分析、统计方法设计模块          |
| <br />陈春洁（25210115） | 负责可视化绘图模块及数据验证            |
| 郑嘉豪（25210307）       | 负责AIagent周报数据获取、html设计模块   |
| 刘子瑜（25210198）       | 负责AIagent数据验证与 摘要 prompt 生成 |
| 黎沛鑫（25210156）       | 负责AIagent图表规范、结果解读           |
| 王占溪（25210249）       | 项目文档、GitHub Pages 部署             |

## 四、数据来源

- A 股指数：AKShare（`ak.stock_zh_index_daily`），上证指数、深证成指、沪深300、创业板指
- 美股指数：AKShare（`ak.index_us_stock_sina`），道琼斯工业、标普500、纳斯达克综合
- 数据区间：2026-05-11 至 2026-05-18（5 个交易日）

## 五、AI 工具使用说明

本项目使用以下 AI 工具辅助完成：

- **Claude Code**：代码编写、调试、Notebook 结构设计、Markdown 解读撰写
- **ChatGPT / 豆包**：思路讨论、prompt 优化

所有 AI 生成代码均经过本地运行验证，分析结论和解读文字体现了小组自身理解。

## 六、运行方式

```bash
# 1. 安装依赖
pip install akshare pandas numpy matplotlib

# 2. 按顺序运行 Notebook
jupyter notebook 01_数据获取.ipynb
jupyter notebook 02_数据清洗.ipynb
jupyter notebook 03_实证分析.ipynb
jupyter notebook 04_可视化绘图.ipynb
```
