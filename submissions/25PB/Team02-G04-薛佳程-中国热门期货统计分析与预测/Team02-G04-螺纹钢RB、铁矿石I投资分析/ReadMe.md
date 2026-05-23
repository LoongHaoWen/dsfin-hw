## 📋 项目基本信息
|项目|内容|
|---|---|
|课程|数据分析与经济决策（ds2026）|
|题目|地产基建期货（螺纹钢RB、铁矿石I）价格波动与联动决策分析|
|小组|第 4 组（Team02‑G04）|
|成员|25210227 荣渝渝｜25210229 沈仕沐｜25210246 王丽娜｜25210257 吴玥｜25210271 连伊丽｜25210275 薛佳程｜25210285 易忠凯|
|GitHub主仓库|https://github.com/zhongerhenglu/Statistical-Analysis-and-Prediction-of-China-s-Popular-Futures|
|提交目录|submissions/25PA/Team02-G04-RB-Iron|
|提交日期|2026‑05‑23|

## 👥 小组分工
|学号|任务|
|---|---|
|25210227 荣渝渝|数据获取、清洗、代码实现|
|25210229 沈仕沐|可视化、统计分析、结论撰写|
|其余成员|背景整理、格式校对、报告审核|

## 🎯 决策主体
面向**钢厂、基建企业、期货交易者、贸易商**，解决地产政策、基建周期下原料采购、套期保值、趋势交易的量化决策问题。

## 📌 研究背景
螺纹钢、铁矿石是地产基建产业链核心期货品种。铁矿石为上游原料，螺纹钢为下游成材，价格存在强成本传导。受地产调控政策、基建投资、进口政策、宏观周期影响，两品种波动剧烈，亟需量化规律支撑交易与套保决策。

## 📂 项目结构

Team02-G04-RB-Iron/
├── README.md
├── report.md
├── slides.md
├── slides.pdf
├── code/
│ ├── 01_data_collect.py
│ ├── 02_data_clean.py
│ ├── 03_visual_eda.py
│ └── 04_analysis_conclusion.py
├── data/
│ ├── data_raw/
│ └── data_clean/
└── output/
├── charts/
└── conclusion.txt


## 🔧 运行环境
```bash
pip install akshare pandas numpy matplotlib seaborn
python code/01_data_collect.py
python code/02_data_clean.py
python code/03_visual_eda.py
python code/04_analysis_conclusion.py

✅ 提交说明
已同步 main 分支，无版本冲突
数据来自 akshare 公开免费接口，可复现
全部分析基于统计事实，结论可验证