# 中国热门期货统计分析与预测 —— Team02-G04
**数据分析与经济决策（ds2026）课程作业**

## 📋 项目基本信息
| 项目 | 内容 |
|---|---|
| 课程 | 数据分析与经济决策 ds2026 |
| 小组 | Team02-G04 |
| 研究方向 | 能源化工、地产基建、贵金属、新能源四大板块期货量化分析 |
| 组员 | 25210227 荣渝渝｜25210229 沈仕沐｜25210246 王丽娜｜25210257 吴玥｜25210271 连伊丽｜25210275 薛佳程｜25210285 易忠凯 |
| 主仓库 | https://github.com/zhongerhenglu/Statistical-Analysis-and-Prediction-of-China-s-Popular-Futures |
| 提交格式 | 严格遵循 lianxhcn/ds2026/homework/Team02 规范 |
| 完成日期 | 2026-05-23 |

---

## 📖 项目简介
本项目围绕**中国四大核心产业链期货**开展全流程量化分析：数据获取 → 标准化清洗 → 探索性分析 → 可视化 → 决策结论。

## 决策主体与选题摘要
本报告面向中国期货普通交易者与中小投资者，基于2010‑2026年四大板块期货数据，结合中国五年规划、货币财政政策、美联储全球资金成本，量化各品种阶段性投资性价比，为套利、趋势交易、风险管理提供可落地建议。

## 文件说明
- `report.md`：总分析报告正文
- `report.ipynb`：含代码、图表、统计结果
- `report.html`：网页可直接打开版
- `slides.md`/`slides.pdf`：课程顶层汇报PPT
- `data/`：数据获取与清洗脚本

## 研究目标
为交易者提供跨品种套利、趋势交易、风险管理的量化依据。

## 痛点
价格波动剧烈、极端行情频发、获利机会有限、主观决策风险高。

## 研究板块
研究时间：2010-01-01 — 2025-12-31（日度高频数据）
- 能源化工：原油 SC、PTA
- 地产基建：螺纹钢 RB、铁矿石 I
- 新能源：碳酸锂 LC、工业硅 SI
- 贵金属：沪金 AU

---
## 👥 任务分工
| 学号姓名 | 负责板块 | 核心任务 |
|---|---|---|
| 25210275 薛佳程 | 能源化工（SC+PTA） | 数据获取、代码整合、项目结构规范 |
| 25210271 连伊丽 | 能源化工（SC+PTA） | 可视化、统计检验、报告撰写 |
| 25210227 荣渝渝 | 地产基建（RB+Iron） | 数据采集、清洗、预处理 |
| 25210229 沈仕沐 | 地产基建（RB+Iron） | 分析、图表解读、决策结论 |
| 25210246 王丽娜 | 新能源（LC+SI） | 数据获取、指标构建、波动分析 |
| 25210257 吴玥 | 新能源（LC+SI） | 联动分析、报告整理、幻灯片制作 |
| 25210285 易忠凯 | 贵金属（AU） | 避险属性分析、统计检验、结论输出 |

---

## 📂 标准目录结构
submissions/25PB/Team02‑G04/  
├─ data/                         # 汇总总数据集  
├─ image/                        # 备用图片文件夹  
├─ output/  
│  └─ charts/                    # 分析输出图表  
│     ├─ fed_rate.png  
│     ├─ macro_liquidity.png  
│     ├─ profit_structure.png  
│     └─ trend_2010_2026.png  
├─ Team02‑G04‑原油SC + PTA投资分析/    # 子板块1  
│  ├─ charts/  
│  └─ data/  
├─ Team02‑G04‑碳酸锂期货LC投资分析/    # 子板块2  
├─ Team02‑G04‑螺纹钢RB、铁矿石I投资分析/# 子板块3  
│  └─ data_clean/  
├─ Team02‑G04‑黄金现货投资分析/        # 子板块4  
│  ├─ charts/  
│  └─ data/  
├─ merge_all_data_to_root.py     # 子板块数据合并脚本  
├─ readme.md                     # 项目说明、数据方法、文件清单  
├─ report.ipynb                  # 完整分析代码、数据处理、绘图  
├─ report.md                     # 研究报告文本版  
├─ report.html                   # 报告网页版  
├─ requirements.txt              # Python依赖包  
├─ slides.md                     # 汇报PPT源文件  
└─ Slides.pdf                    # 导出PDF汇报文件  

---
## 🔧 运行环境（可直接安装）
```bash
pip install -r requirements.txt

requirements.txt 内容
akshare>=1.12.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0

🚀 运行步骤（标准四步）

## 运行说明
```bash
pip install -r requirements.txt
python code/01_data_collect.py
python code/02_data_clean.py
python code/03_visual_eda.py
python code/04_analysis_conclusion.py
quarto render report.qmd

📌 提交规范符合性说明
✅ 每个模块均包含：决策主体 → 政策背景 → 数据 → 统计 → 可视化 → 结论 → 局限
✅ 代码命名规范：01/02/03/04 标准流程
✅ 图表规范：时序图、直方图、KDE、箱线图、波动率、散点图、热力图
✅ 文件规范：README + report.md + slides.md + slides.pdf
✅ 路径规范：纯相对路径，无中文乱码，可直接复现
✅ 分析规范：包含描述统计、偏度峰度、JB 检验、极端行情、相关性分析
📎 数据来源说明
所有数据均来自 akshare 公开免费接口，合规可复现，无付费数据、无侵权内容。





