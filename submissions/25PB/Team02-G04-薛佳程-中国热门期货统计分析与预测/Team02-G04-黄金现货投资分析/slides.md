---
marp: true
theme: default
paginate: true
_paginate: false
size: 16:9
backgroundColor: "#F2EFEB"
style: |
  section {
    font-family: 'Microsoft YaHei', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    font-size: 34px;
    font-weight: 400;
    line-height: 1.4;
    padding: 0;
    background: #F2EFEB;
    color: #4A4540;
    overflow: hidden;
    page-break-inside: avoid;
  }

  section::after {
    content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    right: 42px;
    bottom: 16px;
    color: #8B857F;
    font-size: 0.5em;
    font-weight: 400;
  }

  /* ==================== COVER ==================== */
  section.cover {
    text-align: center;
    background: #7B8FA1 !important;
    color: #FFFFFF !important;
    padding: 80px 0 0 0;
  }
  section.cover::after { content: none; }
  section.cover h1 {
    font-weight: 900; font-size: 2.2em; color: #FFFFFF;
    margin: 0 0 0.12em 0; letter-spacing: 0.02em; line-height: 1.1;
  }
  section.cover .cov-sub {
    font-size: 0.75em; color: rgba(255,255,255,0.82);
    margin-bottom: 0.08em; letter-spacing: 0.04em;
  }
  section.cover .cov-en {
    font-size: 0.55em; font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
    color: rgba(255,255,255,0.45); letter-spacing: 0.07em;
    margin-bottom: 2.5em;
  }
  section.cover .cov-meta {
    font-size: 0.42em; font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
    color: rgba(255,255,255,0.3); letter-spacing: 0.05em;
  }

  /* ==================== DIVIDER ==================== */
  section.divider {
    text-align: center;
    background: #7B8FA1 !important;
    color: #FFFFFF !important;
    padding: 110px 0 0 0;
  }
  section.divider::after { content: none; }
  section.divider h1 {
    font-weight: 900; font-size: 2em; color: #FFFFFF;
    margin: 0 0 0.2em 0; letter-spacing: 0.02em; line-height: 1.15;
  }
  section.divider .div-en {
    font-size: 0.55em; font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
    color: rgba(255,255,255,0.45); letter-spacing: 0.07em;
  }

  /* ==================== END ==================== */
  section.end {
    text-align: center;
    background: #7B8FA1 !important;
    color: #FFFFFF !important;
    padding: 80px 0 0 0;
  }
  section.end::after { content: none; }
  section.end h1 {
    font-weight: 900; font-size: 3.2em; color: #FFFFFF;
    margin: 0 0 0.12em 0; letter-spacing: -0.02em;
    font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif; line-height: 1.1;
  }
  section.end .end-cn {
    font-size: 1.4em; color: rgba(255,255,255,0.78);
    margin-bottom: 1.8em; letter-spacing: 0.06em;
  }
  section.end .end-meta {
    font-size: 0.42em; font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
    color: rgba(255,255,255,0.3); letter-spacing: 0.05em;
  }

  /* ==================== CONTENT PAGES ==================== */
  h2 {
    font-size: 1.4em; font-weight: 900;
    color: #7B8FA1;
    margin: 0;
    padding: 0.02in 0.4in 0 0.4in;
    letter-spacing: 0.01em; line-height: 1.1;
  }
  h3 { font-size: 0.72em; font-weight: 700; color: #4A4540; margin: 0 0 0.25em 0; }
  h4 { font-size: 0.52em; font-weight: 600; color: #8B857F; margin: 0 0 0.1em 0; text-transform: uppercase; letter-spacing: 0.08em; }
  p  { margin: 0.08em 0; font-size: 0.6em; color: #4A4540; line-height: 1.45; }
  ul, ol { margin: 0.08em 0; padding-left: 1.1em; font-size: 0.6em; line-height: 1.55; color: #4A4540; }

  strong { color: #7B8FA1; font-weight: 700; }
  em     { color: #8B857F; font-style: normal; }

  .body { padding: 8px 0.4in 18px 0.4in; }
  .body-t { padding: 2px 0.35in 12px 0.35in; }
  .body-sm { padding: 2px 0.4in 14px 0.4in; }

  .xs { font-size: 0.42em; }
  .sm { font-size: 0.5em; }

  .g2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
  .g3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; }
  .g13 { display: grid; grid-template-columns: 1fr 2.2fr; gap: 18px; align-items: start; }
  .g22 { display: grid; grid-template-columns: 2fr 1fr; gap: 14px; align-items: start; }

  .card { background: #E6E2DC; border-radius: 8px; padding: 10px 14px; }
  .card-b { background: #DBD6D0; border-radius: 8px; padding: 8px 12px; }
  .card-g { background: #E6E0D5; border-radius: 8px; padding: 8px 12px; }

  .stat-box {
    text-align: center; background: #E6E2DC;
    border-radius: 8px; padding: 14px 10px 10px 10px;
  }
  .stat-num {
    font-size: 1.7em; font-weight: 900; color: #7B8FA1;
    line-height: 1; letter-spacing: -0.02em;
    font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
  }
  .stat-lbl {
    font-size: 0.45em; color: #8B857F; margin-top: 2px;
    font-weight: 500; text-transform: uppercase; letter-spacing: 0.06em;
  }

  table {
    width: 100%; border-collapse: collapse;
    margin: 0.08em 0; font-size: 0.5em;
  }
  table th {
    color: #8B857F; font-weight: 600;
    font-size: 0.78em; text-transform: uppercase; letter-spacing: 0.04em;
    padding: 3px 0; text-align: left; border-bottom: 2px solid #D5CFC8;
  }
  table td {
    padding: 4px 0; border-bottom: 1px solid #D5CFC8;
    color: #4A4540; font-size: 0.9em; font-weight: 500;
  }
  table tr:last-child td { border-bottom: none; }

  .chart { text-align: center; margin: 0; }
  .chart img { max-height: 460px !important; max-width: 100% !important; }

  .tag {
    display: inline-block; font-weight: 600; font-size: 0.42em;
    letter-spacing: 0.05em; text-transform: uppercase;
    padding: 3px 8px; border-radius: 4px;
    background: #DBD6D0; color: #7B8FA1;
    margin: 0 5px 5px 0;
  }

  .bline { width: 42px; height: 3px; background: #7B8FA1; margin: 8px 0 10px 0; }
  .sep { border: none; border-top: 1px solid #D5CFC8; margin: 6px 0; }

  /* compact layout for dual charts */
  .dual-chart { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; align-items: start; }
  .dual-chart img { max-height: 340px !important; max-width: 100% !important; }
---

<!-- _class: cover -->

# 黄金现货投资决策分析

<div class="cov-sub">
站在现在时点上，投资者是否应该买入黄金现货？
</div>

<div class="cov-en">
Gold Spot Investment Analysis for Chinese Retail Investors
</div>

<div class="cov-meta">
Data Analysis &amp; Economic Decisions · DS2026 &nbsp;|&nbsp; Team 02 — G03 &nbsp;|&nbsp; 2025.05
</div>

---

## 我们在帮谁 · 解决什么问题

<div class="body">

<div class="g13">

<div>

<div class="stat-num" style="font-size:2.2em">3</div>
<div class="stat-lbl">递进式决策问题</div>

<div class="bline"></div>

<div style="margin-top:10px">
<span class="tag">为谁分析</span>
<span class="tag">什么背景</span>
<span class="tag">如何决策</span>
</div>

</div>

<div>

**决策主体：中国中产家庭个人投资者**（可投资资产 50–500 万）

当前困境：银行存款利率 **1.1%** → 房地产持续下行 → A股宽幅震荡 → **"资产荒"**

<p style="font-size:0.65em; font-weight:700; margin-top:14px; color:#4A4540">三个核心决策问题：</p>

<div style="text-align:center;display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:6px">
<div class="card-b" style="padding:12px 10px">
  <div style="font-size:1.3em;font-weight:900;color:#7B8FA1">Q1</div>
  <p class="xs" style="margin:2px 0;font-weight:600">现在是否应该买入？</p>
  <p class="xs" style="color:#8B857F">金价已是历史最高，进场是"接盘"还是"上车"？</p>
</div>
<div class="card-b" style="padding:12px 10px">
  <div style="font-size:1.3em;font-weight:900;color:#7B8FA1">Q2</div>
  <p class="xs" style="margin:2px 0;font-weight:600">配置多少比例？</p>
  <p class="xs" style="color:#8B857F">5%、10%还是15%？不同偏好如何差异化？</p>
</div>
<div class="card-b" style="padding:12px 10px">
  <div style="font-size:1.3em;font-weight:900;color:#7B8FA1">Q3</div>
  <p class="xs" style="margin:2px 0;font-weight:600">何时应该卖出？</p>
  <p class="xs" style="color:#8B857F">建仓后需监测哪些信号做出卖出决策？</p>
</div>
</div>

</div>

</div>

</div>

---

## 宏观背景：三大结构性变化

<div class="body">

<div class="g3">

<div class="stat-box">
  <div class="stat-num">+170%</div>
  <p style="margin-top:4px; font-size:0.6em; font-weight:600; color:#4A4540">COMEX 金价涨幅</p>
  <p class="xs" style="color:#8B857F">2010 → 2025（15年）</p>
  <div style="margin-top:10px; padding-top:8px; border-top:1px solid #D5CFC8">
    <p class="xs" style="color:#8B857F; margin:0">复合年化增长率</p>
    <p style="font-size:0.85em; font-weight:800; color:#7B8FA1; margin:2px 0 0 0">~6.8% / year</p>
  </div>
</div>

<div class="stat-box">
  <div class="stat-num">>1,000t</div>
  <p style="margin-top:4px; font-size:0.6em; font-weight:600; color:#4A4540">全球央行年均购金</p>
  <p class="xs" style="color:#8B857F">2022 – 2024 连续三年</p>
  <div style="margin-top:10px; padding-top:8px; border-top:1px solid #D5CFC8">
    <p class="xs" style="color:#8B857F; margin:0">对比 2010–2021 均值</p>
    <p style="font-size:0.85em; font-weight:800; color:#B8963E; margin:2px 0 0 0">~450t → ~1,073t</p>
  </div>
</div>

<div class="stat-box">
  <div class="stat-num">525bp</div>
  <p style="margin-top:4px; font-size:0.6em; font-weight:600; color:#4A4540">美联储累计加息</p>
  <p class="xs" style="color:#8B857F">2022.3 → 2023.7</p>
  <div style="margin-top:10px; padding-top:8px; border-top:1px solid #D5CFC8">
    <p class="xs" style="color:#8B857F; margin:0">当前利率状态</p>
    <p style="font-size:0.85em; font-weight:800; color:#7B8FA1; margin:2px 0 0 0">4.25–4.50% → 降息中</p>
  </div>
</div>

</div>

<div class="bline" style="margin-top:14px"></div>

<div class="g2" style="gap:14px; margin-top:6px">
<div>
<p style="font-size:0.46em; font-weight:700; color:#7B8FA1; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:2px">核心文献</p>
<p class="sm">WGC Gold Demand Trends (2010-2025) · FOMC Statements · 人民银行 Q3 货币政策执行报告</p>
</div>
<div>
<p style="font-size:0.46em; font-weight:700; color:#7B8FA1; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:2px">中国投资者困境</p>
<p class="sm">存款实际负利率 (1.1% vs CPI 0.4%) · 房地产失锚 · A股震荡 · 人民币贬值预期</p>
</div>
</div>

</div>

---

## 数据来源与五维分析框架

<div class="body">

<div class="g2">

<div>

<h3>数据来源（全部免费公开）</h3>

| 来源 | 数据内容 | 频率 |
|------|---------|:---:|
| **yfinance** | COMEX · DXY · VIX · S&P 500 · SSE | 日 |
| **akshare** | 上海金 Au99.99 · 美债 10Y · 中美 CPI · 联邦基金利率 | 日/月 |
| **WGC** | 全球央行年度购金量 | 年 |

<div class="bline" style="width:36px;height:2px;margin:10px 0 6px 0"></div>
<p class="sm" style="color:#8B857F">2010-2025 月度数据，197 个月，19 个变量，100% 可复现</p>

</div>

<div>

<h3>五维分析框架</h3>

<table>
<tr><th>维度</th><th>分析内容</th><th>图表</th></tr>
<tr><td>价格定位</td><td>长期趋势 + 重大事件</td><td style="text-align:center">图1-2</td></tr>
<tr><td>驱动因素</td><td>实际利率 · 央行购金 · 美元</td><td style="text-align:center">图3-5</td></tr>
<tr><td>估值水平</td><td>金价/CPI · 收益分布</td><td style="text-align:center">图6</td></tr>
<tr><td>风险特征</td><td>波动率 · 最大回撤 · 利率周期</td><td style="text-align:center">图7-8</td></tr>
<tr><td>组合价值</td><td>滚动相关性 · 分散化</td><td style="text-align:center">图9</td></tr>
</table>

</div>

</div>

<div style="text-align:center; margin-top:12px">
  <span class="tag">月度频率</span>
  <span class="tag">2010 – 2025</span>
  <span class="tag">实际利率 = 名义利率 − CPI</span>
  <span class="tag">11 个核心变量</span>
</div>

</div>

---

## 图1 · 金价的历史坐标：台阶式上涨，加速突破

<div class="body-t">

<div class="chart">
  <img src="charts/fig1_gold_price_trend.png">
</div>

<div class="g2" style="margin-top:6px; gap:14px">
<div class="card-b">
  <p style="margin:0; font-size:0.42em">
    <strong>15 年 +170%，台阶式上涨。</strong>每轮重大危机（欧债、COVID、俄乌）后金价上一个新平台且不回前低。<strong>2024–2025 涨速显著快于历史任何时期</strong>——12个月内从 $2,300 跃至 $3,200+。
  </p>
</div>
<div class="card-g">
  <p style="margin:0; font-size:0.42em">
    <strong style="color:#B8963E">与央行购金时间窗口高度吻合。</strong>2022 年 11 月中国央行开始连续增持，此后 COMEX 金价从 ~$1,700 升至 $3,000+，涨幅超过 75%。
  </p>
</div>
</div>

</div>

---

## 图2 · 多资产年度收益对比 & 图5 · 美元与金价关系

<div class="body-t">

<div class="dual-chart">
  <div class="chart"><img src="charts/fig2_annual_returns.png"></div>
  <div class="chart"><img src="charts/fig5_dxy_vs_gold.png"></div>
</div>

<div class="g2" style="margin-top:4px; gap:14px">
<div class="card-b">
  <p style="margin:0; font-size:0.4em">
    <strong>黄金年均收益 6.4%，波动率 14.6%，Sharpe 0.44。</strong>低于 S&P 500 (11.1%) 但远高于上证综指 (2.6%)。黄金的核心优势在"守"——<strong>股市大跌年份（2018、2022）黄金保持正收益或跌幅显著更小</strong>，体现非对称避险属性。
  </p>
</div>
<div class="card-g">
  <p style="margin:0; font-size:0.4em">
    <strong style="color:#B8963E">美元与金价正在"脱钩"。</strong>全样本相关 −0.48，但 2024 年以来美元强势维持 (100+) 的同时金价大涨——黄金正摆脱对美元的"寄生"关系，定价逻辑更加多元。
  </p>
</div>
</div>

</div>

---

<!-- _class: divider -->

# 核心驱动因素分析

<div class="div-en">
Key Drivers: Real Yield, Central Bank, US Dollar
</div>

---

## 图3 · 核心驱动：实际利率 vs 金价

<div class="body-t">

<div class="chart">
  <img src="charts/fig3_real_yield_vs_gold.png">
</div>

<div class="g2" style="margin-top:6px; gap:14px">
<div class="card-b">
  <p style="margin:0; font-size:0.42em">
    全样本（2010–2025）相关系数约 <strong>−0.7 ~ −0.8</strong>，经典负相关关系整体成立。实际利率越低 → 持有黄金的机会成本越小 → 金价越高。实际利率每下降 1 个百分点，金价约上涨 $140。
  </p>
</div>
<div class="card-g">
  <p style="margin:0; font-size:0.42em">
    <strong style="color:#B8963E">2022 年后规律显著弱化。</strong>实际利率从 −1% 升至 2%+，金价不仅未跌反而大幅攀升（红点区域）。<strong>央行购金和去美元化正在"打破"传统的实际利率定价框架。</strong>
  </p>
</div>
</div>

</div>

---

## 图4 · 全球央行购金：前所未有的结构性需求

<div class="body-t">

<div class="chart">
  <img src="charts/fig4_cb_purchases.png">
</div>

<div class="g2" style="margin-top:6px; gap:14px">
<div class="card-b">
  <p style="margin:0; font-size:0.42em">
    <strong>2022-2024 年全球央行购金年均超千吨</strong>，较 2010-2021 年均值（约 450 吨）翻倍以上。这个结构性变化意味着：<strong>即使传统驱动因素（利率、美元）不利，央行购金本身构成独立的、持续的需求支柱。</strong>
  </p>
</div>
<div class="card-g">
  <p style="margin:0; font-size:0.42em">
    <strong style="color:#B8963E">主要买家：中国、波兰、印度、土耳其。</strong>中国央行自 2022 年 11 月恢复购金后已连续增持 18 个月（截至 2024 年 5 月），黄金储备占外汇储备比例从 3.6% 升至 4.9%，但仍远低于欧美水平（德国 77%，美国 72%）。
  </p>
</div>
</div>

</div>

---

## 图6 · 黄金现在贵不贵？—— 估值分析

<div class="body-t">

<div class="chart">
  <img src="charts/fig6_valuation.png">
</div>

<div class="g2" style="margin-top:6px; gap:14px">
<div class="card-b">
  <p style="margin:0; font-size:0.42em">
    <strong>贵，但不是泡沫。</strong>金价/CPI 比率处于历史 <strong>90%+ 分位</strong>——从通胀调整角度看确实处于偏贵区间。但高估值不是卖出的充分条件：<strong>"贵"可以维持较长时间</strong>，尤其在结构性需求（央行购金）持续支撑下。
  </p>
</div>
<div class="card-g">
  <p style="margin:0; font-size:0.42em">
    <strong style="color:#B8963E">月度波动 −5% ~ +6%，极端可达 ±8%。</strong>右图显示黄金单月涨跌分布——投资者需对这档波动有充分心理准备。央行年均 >1,000 吨购金提供了历史上不曾有的底部支撑。
  </p>
</div>
</div>

</div>

---

## 图7 · 风险特征 & 图9 · 组合分散化价值

<div class="body-t">

<div class="dual-chart">
  <div class="chart"><img src="charts/fig7_risk_metrics.png"></div>
  <div class="chart"><img src="charts/fig9_correlations.png"></div>
</div>

<div class="g2" style="margin-top:4px; gap:14px">
<div class="card-b">
  <p style="margin:0; font-size:0.4em">
    <strong>黄金年化波动率 12–20%，与标普 500 相当。</strong>历史上 12 个月内最大回撤达 <strong>−30.9%</strong>（2013 年）。"黄金抗跌"≠"黄金不跌"——投资者需有承受至少 15% 浮亏的心理准备。
  </p>
</div>
<div class="card-g">
  <p style="margin:0; font-size:0.4em">
    <strong style="color:#B8963E">黄金与股票长期低相关（−0.2~+0.4），是真正的组合分散工具。</strong>当前 Gold-S&P500 相关仅 −0.13，Gold-SSE 相关仅 +0.11。当股票大跌时，黄金未必跟随下跌。
  </p>
</div>
</div>

</div>

---

## 图8 · 不同利率环境下的黄金表现

<div class="body-t">

<div class="chart">
  <img src="charts/fig8_regime_returns.png">
</div>

<div class="g2" style="margin-top:6px; gap:14px">
<div class="card-b">
  <p style="margin:0; font-size:0.42em">
    <strong>反直觉发现：黄金在高利率环境中表现并不差。</strong>高利率往往伴随通胀或地缘风险，同样利好黄金。中等利率环境 (2.5-5%) 下黄金月均收益 <strong>+1.54%</strong>，为四个区间中最高。
  </p>
</div>
<div class="card-g">
  <p style="margin:0; font-size:0.42em">
    <strong style="color:#B8963E">当前定位（2025Q2）：联邦基金利率 4.25-4.50%。</strong>处于中等利率区间偏上、降息周期中途。历史上该阶段黄金月度收益偏正——<strong>降息预期本身构成黄金的利好因子。</strong>
  </p>
</div>
</div>

</div>

---

<!-- _class: divider -->

# 情景模拟与决策建议

<div class="div-en">
Scenario Analysis &amp; Investment Recommendations
</div>

---

## 图10 · 未来 12 个月情景模拟（蒙特卡洛，500 次）

<div class="body-t">

<div class="chart">
  <img src="charts/fig10_scenario_simulation.png">
</div>

<div class="g3" style="margin-top:6px">
<div class="card" style="text-align:center; padding:14px 14px; border-top:3px solid #7B9E8B">
  <h4 style="color:#7B9E8B; margin:0 0 3px 0; font-size:0.48em">乐观情景</h4>
  <p style="font-size:0.6em;font-weight:900;color:#7B9E8B;margin:2px 0">+17.1%</p>
  <p class="xs" style="margin:0; line-height:1.4">Fed 加速降息<br>地缘风险升级<br>央行大举购金</p>
</div>
<div class="card" style="text-align:center; padding:14px 14px; border-top:3px solid #7B8FA1">
  <h4 style="color:#7B8FA1; margin:0 0 3px 0; font-size:0.48em">基准情景</h4>
  <p style="font-size:0.6em;font-weight:900;color:#7B8FA1;margin:2px 0">+4.2%</p>
  <p class="xs" style="margin:0; line-height:1.4">Fed 温和降息<br>地缘风险维持<br>央行按节奏购金</p>
</div>
<div class="card" style="text-align:center; padding:14px 14px; border-top:3px solid #B8807A">
  <h4 style="color:#B8807A; margin:0 0 3px 0; font-size:0.48em">悲观情景</h4>
  <p style="font-size:0.6em;font-weight:900;color:#B8807A;margin:2px 0">−10.9%</p>
  <p class="xs" style="margin:0; line-height:1.4">通胀反弹<br>地缘风险消退<br>央行购金放缓</p>
</div>
</div>

<div style="text-align:center; margin-top:10px">
  <p style="font-size:0.55em; font-weight:700; color:#4A4540">
    关键发现：即使在乐观情景下，12 个月后仍有 5–10% 概率出现回调 → <strong style="color:#B8807A">分批建仓，不要一次性满仓</strong>
  </p>
</div>

</div>

---

## 加分项：多因子回归分析

<div class="body">

<div class="g22">

<div>

<h3>金价月度收益驱动因素</h3>

<table>
<tr><th>变量</th><th>全样本</th><th>Pre-2022</th><th>Post-2022</th></tr>
<tr><td><strong>常数项</strong></td><td>0.80**</td><td>0.58</td><td>1.13**</td></tr>
<tr><td>实际利率变化</td><td>−0.81</td><td>−1.40</td><td>−0.08</td></tr>
<tr><td><strong>美元收益率</strong></td><td>−0.97***</td><td>−0.89***</td><td>−1.22***</td></tr>
<tr><td>VIX 变化</td><td>0.02</td><td>0.01</td><td>0.06*</td></tr>
<tr><td>S&P 500 收益</td><td>−0.06</td><td>−0.06</td><td>0.09</td></tr>
</table>

<p class="xs" style="margin-top:6px;color:#8B857F">*** p<0.01 &nbsp; ** p<0.05 &nbsp; * p<0.1</p>

</div>

<div>

<h3>关键发现</h3>

<div class="stat-box" style="padding:14px 12px; margin-bottom:10px">
  <p style="font-size:0.52em; margin:0; text-align:left">
    <strong>R²: Full = 0.19, Pre-2022 = 0.16, Post-2022 = 0.39</strong>
  </p>
  <p class="xs" style="text-align:left; margin:4px 0 0 0">模型解释力有限——金价受危机"恐慌"驱动，难以被少数经济变量完全解释</p>
</div>

<div class="card-g" style="padding:12px 14px">
  <p style="font-size:0.5em; margin:0">
    <strong style="color:#B8963E">核心发现：美元收益率是全样本最显著的驱动因素（系数 −0.97，p<0.01）。</strong>但 2022 年后，实际利率的解释力从 −1.40 大幅下降至 −0.08（不再显著），印证结构性变化正在发生。
  </p>
</div>

</div>

</div>

</div>

---

## 核心结论

<div class="body">

<div class="g3">

<div class="card" style="text-align:center; padding:24px 18px; border-top:3px solid #7B8FA1">
  <div style="font-size:1.4em; font-weight:900; color:#7B8FA1; margin-bottom:4px; font-family:'Segoe UI','Microsoft YaHei',sans-serif">I</div>
  <h3 style="margin:0 0 6px 0; font-size:0.66em">贵 ≠ 要跌</h3>
  <p class="sm" style="line-height:1.6; color:#4A4540">
    估值处于 90%+ 历史分位<br>
    但央行年均 >1,000 吨购金<br>
    构成前所未有的结构性支撑<br>
    高估值可维持较长时间
  </p>
</div>

<div class="card" style="text-align:center; padding:24px 18px; border-top:3px solid #7B8FA1">
  <div style="font-size:1.4em; font-weight:900; color:#7B8FA1; margin-bottom:4px; font-family:'Segoe UI','Microsoft YaHei',sans-serif">II</div>
  <h3 style="margin:0 0 6px 0; font-size:0.66em">框架在改变</h3>
  <p class="sm" style="line-height:1.6; color:#4A4540">
    实际利率与金价的负相关<br>
    自 2022 年起显著弱化<br>
    传统的 TIPS 定价模型<br>
    需纳入央行购金等新变量
  </p>
</div>

<div class="card" style="text-align:center; padding:24px 18px; border-top:3px solid #7B8FA1">
  <div style="font-size:1.4em; font-weight:900; color:#7B8FA1; margin-bottom:4px; font-family:'Segoe UI','Microsoft YaHei',sans-serif">III</div>
  <h3 style="margin:0 0 6px 0; font-size:0.66em">分散化价值</h3>
  <p class="sm" style="line-height:1.6; color:#4A4540">
    与股票长期低相关<br>
    有效的组合风险分散工具<br>
    但波动不低（12–20%）<br>
    需做好 15%+ 回撤准备
  </p>
</div>

</div>

</div>

---

## 配置建议 & 风险管理

<div class="body">

<div class="g2">

<div class="card">

<h3>建议配置比例</h3>

| 投资者类型 | 黄金占比 | 逻辑 |
|:----------|:-------:|:-----|
| **保守型** · 追求保值 | **10 – 15%** | 替代低息存款，对抗通胀侵蚀 |
| **平衡型** · 兼顾收益与风险 | **5 – 10%** | 低相关性分散风险，5%即可起效 |
| **进取型** · 追求增长 | **0 – 5%** | 仅作尾部风险保险，不拖累收益 |

<div class="bline" style="width:36px;height:2px;margin:10px 0 6px 0"></div>

<p style="font-size:0.48em; line-height:1.6">
  <strong style="color:#B8807A">不建议：全部投入 · 加杠杆 · 一次性满仓</strong><br>
  <strong style="color:#7B9E8B">建议：分批建仓 · 定期再平衡 · 设定止盈止损线</strong>
</p>

</div>

<div class="card">

<h3>卖出信号监测清单</h3>

| 风险因素 | 触发条件 |
|---------|---------|
| Fed 政策转向 | 核心 PCE 连续 3 月反弹 |
| 央行需求减弱 | 中国人民银行连续 6 月未增持 |
| 地缘风险消退 | 俄乌停火协议 + 中东全面和平 |
| 美元大幅走强 | DXY 指数突破 110 |

<div class="bline" style="width:36px;height:2px;margin:10px 0 6px 0"></div>
<p class="sm" style="color:#8B857F">以上信号仅作为监测参考，不构成具体买卖时点的判断依据</p>

</div>

</div>

</div>

---

## 研究局限 & 未来方向

<div class="body">

<div class="g2">

<div class="card">

<h3>本研究局限性</h3>

<ul>
<li><strong>数据限缩：</strong>上海金仅覆盖 2016–2025，此前数据缺失</li>
<li><strong>方法局限：</strong>以描述统计为主，非因果推断；回归 R² 仅 0.19</li>
<li><strong>框架局限：</strong>历史规律可能因结构性变化（央行购金、去美元化）而失效</li>
<li><strong>适用局限：</strong>仅面向中等风险偏好的中国个人投资者</li>
<li><strong>变量缺失：</strong>未纳入比特币等替代资产的分流效应</li>
</ul>

</div>

<div class="card">

<h3>亟待进一步研究</h3>

<ul>
<li>黄金的"合理价格"如何估算？（需更复杂的定价模型）</li>
<li>数字资产（比特币）是否正在分流黄金的避险需求？</li>
<li>实物金 vs 黄金 ETF vs 黄金股：最优投资工具选择？</li>
<li>如何设计动态配置策略（何时加仓 / 何时减仓）？</li>
<li>中国个人投资者的行为金融特征如何影响黄金配置决策？</li>
</ul>

</div>

</div>

<div style="text-align:center; margin-top:22px">
  <p class="sm" style="color:#8B857F">
    本报告为"数据分析与经济决策 (DS2026)"课程小组作业。<br>
    <strong style="color:#B8807A">不构成任何形式的投资建议。投资有风险，入市需谨慎。</strong>
  </p>
</div>

</div>

---

<!-- _class: end -->

# THANKS

<div class="end-cn">
感谢聆听 · 欢迎提问
</div>

<div class="end-meta">
Team 02 — G03 · DS2026 &nbsp;|&nbsp; 中山大学岭南学院<br>
Data: yfinance · akshare · WGC · FRED
</div>
