---
marp: true
theme: default
paginate: true
size: 16:9
math: mathjax
footer: "长鑫科技 Pre-IPO 估值专题 · 数据截至 2026-05-20 · 公开资料整理"
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;600;700&family=Noto+Sans+SC:wght@400;500;600;700&display=swap');

  :root {
    --report-blue: #1d4ed8;
    --report-blue-dark: #1e3a8a;
    --report-blue-light: #3b82f6;
    --report-indigo: #4f46e5;
    --navy: #0f172a;
    --ink: #334155;
    --slate: #64748b;
    --muted: #94a3b8;
    --line: #e2e8f0;
    --paper: #f8fafc;
    --panel: #f1f5f9;
    --gold: #b45309;
    --gold-bg: #fffbeb;
    --accent: #0ea5e9;
    --table-head: #1e293b;
    --shadow-sm: 0 1px 2px rgba(15, 23, 42, 0.05), 0 2px 8px rgba(30, 64, 175, 0.04);
    --shadow-md: 0 4px 16px rgba(30, 64, 175, 0.1), 0 1px 3px rgba(15, 23, 42, 0.06);
    --shadow-lg: 0 16px 40px rgba(15, 23, 42, 0.12), 0 4px 12px rgba(30, 64, 175, 0.08);
    --radius: 12px;
    --radius-sm: 8px;
  }

  section {
    font-family: "Noto Sans SC", "Microsoft YaHei", sans-serif;
    font-size: 19px;
    line-height: 1.48;
    color: var(--ink);
    background:
      radial-gradient(circle 320px at 98% 98%, rgba(59, 130, 246, 0.06) 0%, transparent 70%),
      radial-gradient(ellipse 80% 50% at 100% -10%, rgba(59, 130, 246, 0.07) 0%, transparent 55%),
      radial-gradient(ellipse 60% 40% at -5% 105%, rgba(30, 64, 175, 0.05) 0%, transparent 50%),
      linear-gradient(180deg, #ffffff 0%, var(--paper) 100%);
    padding: 48px 56px 36px;
    justify-content: flex-start;
    letter-spacing: 0.02em;
    position: relative;
    -webkit-font-smoothing: antialiased;
  }

  section:not(.lead):not(.closing):not(.appendix)::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, var(--report-blue-dark) 0%, var(--report-blue) 45%, var(--accent) 100%);
  }

  section:not(.lead):not(.closing):not(.appendix)::after {
    content: "";
    position: absolute;
    top: 18px;
    left: 56px;
    right: 56px;
    height: 1px;
    background: linear-gradient(90deg, var(--line) 0%, rgba(226, 232, 240, 0.3) 60%, transparent 100%);
  }

  header, footer {
    font-size: 9px;
    color: var(--muted);
    font-weight: 500;
    letter-spacing: 0.05em;
  }
  header {
    color: var(--slate);
    padding-left: 2px;
    border-left: 2px solid var(--report-blue-light);
    padding-left: 8px;
    margin-left: -2px;
  }
  footer {
    text-align: right;
    padding: 6px 10px 4px 16px;
    margin-right: -6px;
    opacity: 0.95;
    border-top: 1px solid rgba(226, 232, 240, 0.85);
    background: linear-gradient(180deg, transparent 0%, rgba(248, 250, 252, 0.92) 40%);
    font-variant-numeric: tabular-nums;
  }
  section.lead footer,
  section.closing footer { border: none; background: none; }

  h1, h2, h3, p, ul, ol { margin: 0; padding: 0; }

  h1, h2 {
    font-family: "Noto Serif SC", "SimSun", serif;
    color: var(--navy);
    font-weight: 700;
  }
  h1 { font-size: 1.32em; line-height: 1.3; }
  h2 {
    font-size: 1.06em;
    line-height: 1.35;
    margin-top: 8px;
    padding-bottom: 10px;
    border-bottom: none;
    position: relative;
  }
  h2::after {
    content: "";
    display: block;
    margin-top: 8px;
    height: 3px;
    width: 56px;
    border-radius: 999px;
    background: linear-gradient(90deg, var(--report-blue-dark) 0%, var(--report-blue) 55%, var(--accent) 100%);
  }

  .eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 0.54em;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: none;
    color: var(--report-blue-dark);
    background: linear-gradient(135deg, #eff6ff 0%, #ffffff 100%);
    border: 1px solid #bfdbfe;
    border-left: 3px solid var(--report-blue);
    padding: 6px 16px 6px 12px;
    border-radius: 999px;
    margin-bottom: 12px;
    font-family: "Noto Sans SC", sans-serif;
    box-shadow: var(--shadow-sm);
  }
  .eyebrow::before {
    content: "";
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--report-blue) 0%, var(--accent) 100%);
    flex-shrink: 0;
  }

  .section-no {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 1.75em;
    margin-right: 10px;
    font-family: "Noto Sans SC", sans-serif;
    font-size: 0.66em;
    font-weight: 700;
    color: #fff;
    background: linear-gradient(135deg, var(--report-blue-dark) 0%, var(--report-blue) 50%, var(--report-indigo) 100%);
    padding: 4px 10px;
    border-radius: 999px;
    vertical-align: middle;
    box-shadow: 0 2px 8px rgba(30, 64, 175, 0.28);
    letter-spacing: 0.04em;
  }

  .divider {
    display: none;
  }

  /* —— 封面 —— */
  section.lead {
    justify-content: center;
    align-items: stretch;
    padding: 0 !important;
    background:
      radial-gradient(ellipse 70% 80% at 85% 20%, rgba(59, 130, 246, 0.35) 0%, transparent 55%),
      radial-gradient(ellipse 50% 60% at 10% 90%, rgba(14, 165, 233, 0.15) 0%, transparent 50%),
      linear-gradient(145deg, #0a1628 0%, #0f2744 38%, #1e3a8a 72%, #1e40af 100%) !important;
    color: #ffffff !important;
    font-size: 22px;
  }
  section.lead::before,
  section.lead::after { display: none !important; }
  section.lead header,
  section.lead footer { display: none; }

  section.lead h1,
  section.lead h2,
  section.lead p,
  section.lead li,
  section.lead strong {
    color: #ffffff !important;
  }

  .lead-layout {
    display: grid;
    grid-template-columns: 8px 1fr;
    width: 100%;
    height: 100%;
    min-height: 100%;
    box-sizing: border-box;
    position: relative;
  }
  .lead-layout::after {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 48px 48px;
    pointer-events: none;
    opacity: 0.6;
  }
  .lead-bar {
    background: linear-gradient(180deg, #38bdf8 0%, #2563eb 50%, #1d4ed8 100%);
    box-shadow: 4px 0 28px rgba(37, 99, 235, 0.45);
  }
  .lead-panel {
    padding: 48px 64px 40px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-sizing: border-box;
    position: relative;
    z-index: 1;
  }
  .lead-panel::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent 0%, rgba(125, 211, 252, 0.45) 50%, transparent 100%);
  }
  .lead-kicker {
    display: inline-block;
    font-size: 14px !important;
    font-weight: 700 !important;
    letter-spacing: 0.16em;
    color: #e0f2fe !important;
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(125, 211, 252, 0.45);
    padding: 8px 20px;
    margin-bottom: 26px;
    border-radius: 999px;
  }
  section.lead h1 {
    font-family: "Noto Serif SC", "SimSun", serif !important;
    font-size: 32px !important;
    font-weight: 700 !important;
    line-height: 1.35 !important;
    letter-spacing: 0.04em !important;
    color: #ffffff !important;
    border: none !important;
    padding: 0 !important;
    margin: 0 !important;
    max-width: 92%;
    text-shadow: 0 2px 16px rgba(0, 0, 0, 0.22);
  }
  section.lead h1::after { display: none !important; }
  section.lead h2 {
    font-family: "Noto Serif SC", serif !important;
    font-size: 24px !important;
    font-weight: 600 !important;
    line-height: 1.38 !important;
    color: #fcd34d !important;
    border: none !important;
    padding: 0 !important;
    margin: 12px 0 0 0 !important;
    max-width: 92%;
  }
  section.lead h2::after { display: none !important; }
  .lead-hook {
    margin-top: 18px !important;
    font-size: 17px !important;
    line-height: 1.55 !important;
    color: #cbd5e1 !important;
    font-weight: 500 !important;
    max-width: 88%;
    padding: 10px 0 10px 16px;
    border-left: 3px solid rgba(251, 191, 36, 0.75);
    background: linear-gradient(90deg, rgba(255,255,255,0.04) 0%, transparent 100%);
    border-radius: 0 8px 8px 0;
  }
  .lead-meta {
    margin: 32px 0 0 0 !important;
    padding: 0 !important;
    list-style: none;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px 20px;
  }
  .lead-meta li {
    font-size: 15px !important;
    line-height: 1.45 !important;
    color: #f1f5f9 !important;
    padding: 12px 14px 12px 16px;
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(148, 163, 184, 0.35);
    border-radius: var(--radius);
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  }
  .lead-meta li:nth-child(1) { border-left: 3px solid #38bdf8; }
  .lead-meta li:nth-child(2) { border-left: 3px solid #fcd34d; }
  .lead-meta li:nth-child(3) { border-left: 3px solid #34d399; }
  .lead-meta li:nth-child(4) { border-left: 3px solid #a78bfa; }
  .lead-meta strong {
    display: block;
    font-size: 12px !important;
    letter-spacing: 0.08em;
    color: #7dd3fc !important;
    margin-bottom: 5px;
    font-weight: 700 !important;
    text-transform: uppercase;
  }

  /* —— 摘要 —— */
  .exec { font-size: 17px; padding-top: 4px; }
  .exec::after { display: none; }
  .rich-slide > .eyebrow + h2,
  .chart-slide > .eyebrow + h2 { margin-top: 2px; }
  .summary-box {
    margin-top: 12px;
    border: 1px solid var(--line);
    border-radius: var(--radius);
    background: #fff;
    box-shadow: var(--shadow-md);
    overflow: hidden;
  }
  .summary-box .box-title {
    background: linear-gradient(90deg, var(--table-head) 0%, #334155 100%);
    color: #fff;
    font-size: 0.7em;
    font-weight: 600;
    padding: 10px 16px;
    letter-spacing: 0.1em;
  }
  .summary-list {
    margin: 0;
    padding: 12px 16px 12px 36px;
    font-size: 0.86em;
    color: var(--ink);
  }
  .summary-list li {
    margin: 0;
    padding: 11px 6px 11px 6px;
    line-height: 1.5;
  }
  .summary-list li + li {
    border-top: 1px dashed rgba(226, 232, 240, 0.9);
  }
  .summary-list li::marker {
    color: var(--report-blue);
    font-weight: 700;
  }
  .summary-list strong { color: var(--report-blue-dark); font-weight: 600; }

  /* —— KPI 卡片 —— */
  .kpi-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 14px;
    border: none;
    background: transparent;
  }
  .kpi {
    padding: 14px 16px;
    border: 1px solid var(--line);
    border-radius: var(--radius);
    box-shadow: var(--shadow-sm);
    background: linear-gradient(180deg, #ffffff 0%, #fafbfc 100%);
    border-top: 3px solid var(--report-blue);
    position: relative;
  }
  .kpi:nth-child(even) {
    border-top-color: var(--accent);
  }
  .kpi .label {
    font-size: 0.66em;
    color: var(--slate);
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
  }
  .kpi .value {
    display: block;
    margin-top: 6px;
    font-size: 1.28em;
    font-weight: 700;
    color: var(--report-blue-dark);
    font-family: "Noto Serif SC", serif;
    line-height: 1.2;
    font-variant-numeric: tabular-nums;
    -webkit-text-fill-color: unset;
    background: none;
  }
  .kpi .note {
    display: block;
    margin-top: 5px;
    font-size: 0.62em;
    color: var(--muted);
    line-height: 1.35;
  }
  .cols {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 12px;
    font-size: 0.85em;
    color: var(--ink);
  }
  .col-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 14px 16px;
    box-shadow: var(--shadow-sm);
    border-top: none;
    position: relative;
    overflow: hidden;
  }
  .col-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--report-blue) 0%, var(--accent) 100%);
  }
  .col-card h3 {
    font-family: "Noto Serif SC", serif;
    font-size: 0.8em;
    font-weight: 700;
    color: var(--navy);
    margin: 4px 0 10px 0;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--line);
  }
  .col-card h3::after { display: none; }
  .cols ul { margin: 0; padding-left: 1.1em; }
  .cols li { margin: 6px 0; line-height: 1.44; }

  .flow-hint {
    margin-top: 14px;
    padding: 12px 14px 12px 16px;
    background: linear-gradient(135deg, var(--gold-bg) 0%, #fff 100%);
    font-size: 0.75em;
    color: var(--slate);
    border: 1px solid #fde68a;
    border-left: 4px solid var(--gold);
    border-radius: var(--radius-sm);
    box-shadow: var(--shadow-sm);
  }
  .flow-hint strong {
    color: var(--gold);
    font-weight: 700;
  }

  /* —— 正文块 —— */
  .rich-slide { font-size: 17px; }
  .report-brief {
    margin-top: 12px;
    padding: 14px 18px;
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    border: 1px solid var(--line);
    border-left: 4px solid var(--report-blue);
    border-radius: 0 var(--radius) var(--radius) 0;
    font-size: 0.83em;
    color: var(--ink);
    line-height: 1.54;
    text-align: justify;
    box-shadow: var(--shadow-sm);
  }
  .report-brief strong { color: var(--navy); }
  .insight-strip {
    margin-top: 14px;
    padding: 12px 14px 12px 16px;
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: var(--radius-sm);
    font-size: 0.79em;
    color: var(--slate);
    line-height: 1.5;
    position: relative;
  }
  .insight-strip::before {
    content: "◆";
    position: absolute;
    left: 8px;
    top: 12px;
    font-size: 0.5em;
    color: var(--report-blue);
    line-height: 1;
  }
  .insight-strip strong {
    color: var(--navy);
    padding-left: 10px;
  }
  .insight-strip ul { margin: 8px 0 0 10px; padding-left: 1.1em; }
  .insight-strip li { margin: 5px 0; }

  /* —— 图表页 —— */
  .chart-slide {
    padding: 32px 44px 24px;
    font-size: 15px;
    background:
      radial-gradient(ellipse 100% 60% at 50% 0%, rgba(59, 130, 246, 0.08) 0%, transparent 70%),
      linear-gradient(180deg, #ffffff 0%, var(--paper) 100%);
  }
  .chart-slide::after { display: none; }
  .chart-slide .eyebrow { margin-bottom: 8px; }
  .chart-slide h2 {
    font-size: 0.9em;
    border-bottom: none;
    padding-bottom: 0;
    margin-top: 0;
  }
  .chart-slide h2::after {
    width: 36px;
    height: 2px;
    margin-top: 6px;
  }
  .fig-head {
    margin-top: 6px;
    padding: 8px 14px;
    background: linear-gradient(90deg, #f8fafc 0%, #ffffff 100%);
    border: 1px solid #e2e8f0;
    border-left: 3px solid var(--report-blue);
    border-radius: var(--radius-sm);
    box-shadow: var(--shadow-sm);
  }
  .fig-caption {
    font-size: 0.68em;
    color: var(--navy);
    line-height: 1.34;
  }
  .fig-caption strong {
    font-family: "Noto Serif SC", serif;
    color: var(--report-blue);
    margin-right: 6px;
  }
  .chart-layout {
    --chart-h: 300px;
    --chart-img-max: 288px;
    display: grid;
    grid-template-columns: minmax(0, 1.24fr) minmax(0, 0.76fr);
    gap: 14px;
    margin-top: 8px;
    align-items: stretch;
  }

  .chart-figure {
    min-width: 0;
    height: var(--chart-h);
    display: flex;
    align-items: center;
  }
  .chart-wrap {
    position: relative;
    width: 100%;
    height: var(--chart-h);
    margin: 0;
    padding: 14px 16px;
    box-sizing: border-box;
    background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
    border: 1px solid #cbd5e1;
    border-radius: 16px;
    box-shadow: var(--shadow-md), inset 0 1px 0 rgba(255, 255, 255, 0.9);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: visible;
  }
  .chart-wrap::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    border-radius: 14px 14px 0 0;
    background: linear-gradient(90deg, var(--report-blue-dark) 0%, var(--report-blue) 50%, var(--accent) 100%);
  }
  .chart-wrap img.chart-img,
  .chart-wrap > p > img {
    display: block;
    margin: 0 auto;
    width: auto !important;
    height: auto !important;
    max-width: 100% !important;
    max-height: var(--chart-img-max) !important;
    object-fit: contain !important;
    object-position: center center;
  }
  .chart-wrap > p {
    margin: 0;
    width: 100%;
    text-align: center;
    line-height: 0;
  }

  .interpret {
    display: flex;
    flex-direction: column;
    height: var(--chart-h);
    font-size: 0.62em;
    line-height: 1.36;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    background: #fff;
    box-shadow: var(--shadow-md);
    overflow: hidden;
  }
  .interpret-title {
    flex-shrink: 0;
    background: linear-gradient(90deg, var(--report-blue-dark) 0%, var(--report-blue) 60%, var(--report-blue-light) 100%);
    color: #fff;
    padding: 9px 14px;
    font-size: 0.82em;
    font-weight: 600;
    letter-spacing: 0.1em;
  }
  .interp-block {
    flex: 1;
    padding: 7px 10px 8px;
    border: none;
    border-bottom: 1px solid #f1f5f9;
    background: #fff;
  }
  .interp-block:last-child {
    border-bottom: none;
    background: linear-gradient(180deg, var(--gold-bg) 0%, #fffef7 100%);
  }
  .interp-block .label {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 0.8em;
    font-weight: 700;
    margin-bottom: 3px;
    color: var(--report-blue-dark);
    font-family: "Noto Serif SC", serif;
  }
  .interp-block .label::before {
    content: "";
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: var(--report-blue);
    flex-shrink: 0;
  }
  .interp-block:last-child .label::before { background: var(--gold); }
  .interp-block p {
    margin: 0;
    color: var(--ink);
    text-align: justify;
    line-height: 1.34;
  }
  .interp-block em {
    color: var(--report-blue-dark);
    font-style: normal;
    font-weight: 600;
  }

  /* —— 结论 —— */
  .verdict { font-size: 17px; }
  .verdict .point {
    margin-top: 10px;
    padding: 12px 14px 12px 18px;
    background: #fff;
    border-radius: var(--radius-sm);
    border: 1px solid var(--line);
    border-left: 4px solid var(--report-blue);
    font-size: 0.83em;
    color: var(--ink);
    line-height: 1.44;
    box-shadow: var(--shadow-sm);
    text-align: justify;
    position: relative;
  }
  .verdict .point:nth-child(2) { border-left-color: var(--accent); }
  .verdict .point:nth-child(3) { border-left-color: var(--gold); }
  .verdict .point b {
    color: var(--navy);
    font-weight: 700;
    font-family: "Noto Serif SC", serif;
  }

  .disclaimer {
    font-size: 0.58em;
    color: var(--slate);
    margin-top: 12px;
    padding: 8px 12px;
    border: 1px dashed var(--line);
    border-radius: var(--radius-sm);
    text-align: left;
    background: rgba(248, 250, 252, 0.8);
    font-style: normal;
    line-height: 1.45;
  }

  /* —— 收尾 —— */
  .closing {
    text-align: center;
    justify-content: center;
    padding: 44px 52px;
    background:
      radial-gradient(ellipse 80% 60% at 50% 100%, rgba(59, 130, 246, 0.08) 0%, transparent 60%),
      linear-gradient(180deg, #ffffff 0%, var(--paper) 100%) !important;
  }
  .closing::before, .closing::after { display: none; }
  .closing-inner {
    width: 100%;
    padding: 56px 52px 48px;
    box-sizing: border-box;
    background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    box-shadow: var(--shadow-lg);
    position: relative;
  }
  .closing-inner::after {
    content: "";
    position: absolute;
    bottom: -24px;
    left: 50%;
    transform: translateX(-50%);
    width: 120px;
    height: 4px;
    border-radius: 999px;
    background: linear-gradient(90deg, transparent, var(--report-blue-light), transparent);
    opacity: 0.5;
  }
  .closing-inner::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--report-blue-dark) 0%, var(--report-blue) 50%, var(--accent) 100%);
    border-radius: var(--radius) var(--radius) 0 0;
  }
  .closing-tag {
    display: inline-block;
    font-size: 0.58em;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: var(--report-blue-dark);
    background: linear-gradient(135deg, #eff6ff 0%, #fff 100%);
    border: 1px solid #bfdbfe;
    padding: 8px 20px;
    border-radius: 999px;
    margin-bottom: 24px;
    box-shadow: var(--shadow-sm);
  }
  .closing-inner h1 {
    font-family: "Noto Serif SC", serif;
    color: var(--navy);
    font-size: 1.65em;
    font-weight: 700;
    letter-spacing: 0.08em;
  }
  .closing-inner h1::after { display: none; }
  .closing-inner p {
    margin-top: 18px;
    font-size: 0.88em;
    color: var(--slate);
    line-height: 1.55;
  }
  .closing-inner strong { color: var(--navy); }

  table {
    font-size: 0.79em;
    border-collapse: separate;
    border-spacing: 0;
    width: 100%;
    margin-top: 12px;
    border: 1px solid var(--line);
    border-radius: var(--radius-sm);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
  }
  th {
    background: linear-gradient(180deg, #334155 0%, var(--table-head) 100%);
    color: #fff;
    font-weight: 600;
    padding: 10px 14px;
    text-align: left;
    border: none;
    border-bottom: 2px solid var(--report-blue);
    letter-spacing: 0.04em;
  }
  td {
    padding: 8px 14px;
    border: none;
    border-bottom: 1px solid var(--line);
    color: var(--ink);
    background: #fff;
  }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: var(--panel); }
  code {
    font-size: 0.85em;
    background: var(--panel);
    padding: 1px 5px;
    border-radius: 2px;
    color: var(--navy);
    border: 1px solid var(--line);
  }

  .toc-slide table { font-size: 0.77em; margin-top: 12px; box-shadow: var(--shadow-md); }
  .toc-slide table td:last-child { color: var(--ink); line-height: 1.48; }
  .toc-slide table td:first-child {
    width: 76px;
    font-weight: 700;
    color: #fff;
    background: linear-gradient(135deg, var(--report-blue) 0%, var(--report-blue-light) 100%);
    text-align: center;
    border-right: 1px solid rgba(255,255,255,0.2);
  }
  .toc-slide table tr:nth-child(even) td:first-child {
    background: linear-gradient(135deg, var(--report-blue-dark) 0%, var(--report-blue) 100%);
  }

  .data-slide { font-size: 17px; }
  .data-slide table { font-size: 0.75em; }
  .data-slide th { font-size: 0.94em; }
  .data-slide td[style*="text-align"] { font-variant-numeric: tabular-nums; }

  .scenario-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
  }
  .scenario-card {
    background: #fff;
    border: 1px solid var(--line);
    border-top: 4px solid var(--report-blue);
    border-radius: var(--radius);
    padding: 18px 14px;
    text-align: center;
    box-shadow: var(--shadow-md);
    transition: none;
  }
  .scenario-card.conservative {
    border-top-color: #64748b;
    background: linear-gradient(180deg, #f8fafc 0%, #fff 100%);
  }
  .scenario-card.neutral {
    border-top-color: var(--report-blue);
    background: linear-gradient(180deg, #eff6ff 0%, #fff 100%);
  }
  .scenario-card.optimistic {
    border-top-color: #d97706;
    background: linear-gradient(180deg, var(--gold-bg) 0%, #fff 100%);
  }
  .scenario-card .tag {
    font-size: 0.7em;
    font-weight: 700;
    color: var(--slate);
    letter-spacing: 0.05em;
  }
  .scenario-card .num {
    display: block;
    margin-top: 10px;
    font-family: "Noto Serif SC", serif;
    font-size: 1.38em;
    font-weight: 700;
    color: var(--report-blue-dark);
  }
  .scenario-card.optimistic .num { color: #b45309; }
  .scenario-card .sub {
    display: block;
    margin-top: 8px;
    font-size: 0.62em;
    color: var(--muted);
    line-height: 1.35;
  }

  .file-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 12px;
    font-size: 0.71em;
  }
  .file-card {
    background: #fff;
    border: 1px solid var(--line);
    border-radius: var(--radius-sm);
    padding: 12px 14px;
    line-height: 1.42;
    color: var(--ink);
    box-shadow: var(--shadow-sm);
  }
  .file-card b { color: var(--navy); display: block; margin-bottom: 5px; }

---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _backgroundColor: #0f2744 -->
<!-- _color: #ffffff -->

<div class="lead-layout">

<div class="lead-bar"></div>

<div class="lead-panel">

# 数据分析与经济决策-第二次小组作业

## 科创板上市前的估值再定价研究--长鑫科技集团股份有限公司

<p class="lead-hook">收入高增 · 盈利修复 · 一级定价走廊与同业锚交叉验证</p>

<ul class="lead-meta">
<li><strong>报告日期</strong>2026 年 5 月</li>
<li><strong>数据截止</strong>2026-05-20（上会稿）</li>
<li><strong>陈述时长</strong>约 10 分钟</li>
<li><strong>资料来源</strong>上交所 · akshare · 公开报道</li>
</ul>

</div>

</div>

---

<!-- _class: exec rich-slide -->

<span class="eyebrow">摘要</span>

## <span class="section-no">一</span>核心观点

<div class="report-brief">
<strong>研报定位</strong>：面向 Pre-IPO 定价与板块联动判断，将长鑫科技置于「<em>高成长存储制造</em>」与「<em>政策背书战略资产</em>」双重标签下考察；结论强调<strong>可复核数字</strong>而非单一估值公式。
</div>

<div class="summary-box">
<div class="box-title">摘 要 · 四条主线</div>
<ol class="summary-list">

<li><strong>基本面（图 1、表 1）</strong>：营收 2023—2025 由 91 亿增至 618 亿，增速远超同业均值；2025 年归母净利首次转正（+18.7 亿），但 2022—2025 累计亏损约 409 亿，盈利质量仍取决于 DRAM 价格与产能利用率。</li>

<li><strong>结构与全球（图 6—7）</strong>：LPDDR 2025 年约 407 亿、DDR 约 195 亿，产品组合向移动端倾斜；美光与 A 股半导体指数同向不同步，国内情绪不能替代全球合约价信号。</li>

<li><strong>市场定价（图 3、图 8—9）</strong>：存储链 Beta 普遍高于 1；IPO 受理事件窗 CAR 方向为正但统计不显著，提示消息或已在辅导阶段部分定价。</li>

<li><strong>估值锚（图 2、图 4—5、表 3）</strong>：一级走廊 1,282—1,584 亿与 PS 回归隐含 1,636 亿构成共识带；收入×PE 情景（8/15/25 倍）给出 4,944—15,450 亿上界参考，须与盈利预测及摊薄后股本联动修正。</li>

</ol>
</div>

<p class="disclaimer">说明：本报告基于公开披露与行情数据整理，仅供研究交流，不构成任何投资建议。</p>

---

<!-- _class: rich-slide toc-slide -->

<span class="eyebrow">目录</span>

## <span class="section-no">二</span>报告结构

| 篇章 | 主要内容 |
|:--:|:--|
| 一 | 核心观点（摘要） |
| 二—八 | 研究框架、财务事实、交易背景、政策环境、方法与四维框架 |
| 图 1—10 | 基本面 · 产品结构 · 估值走廊 · ROE · 收入路径 · PS 回归 · 全球对照 · Beta · 事件研究 |
| 表 1—3 | 财务序列 · 政策要点 · 估值情景敏感性 |
| 九—十 | 综合判断与局限 |

<div class="insight-strip">
<strong>阅读提示</strong>：前半部分建立「事实—政策—方法」共识，后半部分用十张图完成交叉验证；若时间有限，可优先保留图 1、2、4、5 与表 3。
<ul>
<li>财务事实页强调<strong>收入跃迁与亏损存量</strong>的并存，避免仅用 PS 横向比较。</li>
<li>图表页采用「左图右评」：左侧完整展示图表，右侧为三层经济解读。</li>
</ul>
</div>

---

<!-- _class: rich-slide -->

<span class="eyebrow">研究框架</span>

## <span class="section-no">三</span>研究问题：定价权握在谁手里？

<div class="report-brief">
<strong>核心命题</strong>：在盈利尚未稳定、但收入已具全球量级的前提下，<em>谁</em>在为长鑫的市值买单——一级战略投资者、二级板块资金，还是政策预期下的「隐含担保」？本报告用三条证据链回答：① 招股书可验证事实；② 同业 ROE/Beta 与 PS 锚；③ 事件窗与回归模型的可复核输出。
</div>

<div class="cols">

<div class="col-card">

### 一级市场

跟投与战略配售面对的不是「当前 PE」，而是<strong>未来 2—3 年 DRAM 景气路径</strong>是否已被折进 1,300—1,600 亿走廊；若 2026Q1 高增不可持续，上沿定价的安全边际极薄。

### 二级市场

上市瞬间将触发存储链<strong>资金再配置</strong>：高 Beta 标的对指数有放大效应，但事件研究显示异常收益并不显著，二级更应关注发行折价与解禁节奏而非「题材脉冲」。

</div>

<div class="col-card">

### 产业与政策

「自主可控」提供估值<strong>下限期权</strong>，但不能自动抵消 409 亿量级累计亏损与持续 Capex；政策溢价须与毛利率、折旧摊销同屏观察。

### 本报告方法

以招股说明书、行情与同业数据为基础，经清洗与量化模型交叉验证，避免「只给结论、不给依据」的简报缺陷。

</div>

</div>

---

<!-- _class: rich-slide -->

<span class="eyebrow">基本面</span>

## <span class="section-no">四</span>财务概览：收入具全球量级，盈利处修复初期

<div class="report-brief">
<strong>经济解读</strong>：公司已完成从「烧钱换份额」到「份额换现金流」的第一阶段跃迁——收入三年复合增速极高，但归母净利 2025 年仅小幅转正，说明<strong>价格与利用率</strong>仍是利润弹性的主因；2026Q1 单季收入 508 亿若不能全年化，则当前估值隐含的是景气高位假设。
</div>

<div class="kpi-grid">

<div class="kpi">
<span class="label">2025 年营业收入</span>
<span class="value">618 亿元</span>
<span class="note">较 2024 年 242 亿约 +156%</span>
</div>

<div class="kpi">
<span class="label">2026 年一季度</span>
<span class="value">508 亿元</span>
<span class="note">单季接近 2024 全年水平</span>
</div>

<div class="kpi">
<span class="label">2025 年归母净利润</span>
<span class="value">+18.7 亿元</span>
<span class="note">2024 年仍为 -71 亿元</span>
</div>

<div class="kpi">
<span class="label">历史累计净亏损</span>
<span class="value">约 409 亿元</span>
<span class="note">2022—2025，招股书口径</span>
</div>

</div>

<div class="insight-strip">
<strong>三点关注</strong>：① 收入规模已支持「全球第四」叙事，但 ROE 尚未稳定；② 研发费用率由约 50% 降至 15%，规模效应显现；③ 累计亏损存量仍是下行周期中的「隐性杠杆」。
</div>

---

<!-- _class: data-slide rich-slide -->

<span class="eyebrow">基本面</span>

## <span class="section-no">表1</span>关键财务指标序列（招股书口径）

| 报告期 | 营业收入 | 归母净利润 | 研发费用 | 研发费用率 |
|:--|--:|--:|--:|--:|
| 2023 | 90.9 亿 | -163.4 亿 | 45.2 亿 | 49.7% |
| 2024 | 241.8 亿 | -71.4 亿 | 46.1 亿 | 19.1% |
| 2025 | 618.0 亿 | +18.7 亿 | 95.9 亿 | 15.5% |
| 2026Q1 | 508.0 亿 | +247.6 亿* | — | — |

<div class="report-brief">
<strong>表解读</strong>：2024—2025 年出现「收入跳升 + 亏损收窄」的典型周期复苏形态；2026Q1 营收与净利同步冲高，需对照附注区分<strong>经常性经营利润</strong>与一次性因素。研发费用绝对额仍上升（95.9 亿），显示技术投入未因盈利转正而收缩，对长期毛利率形成刚性支撑亦构成短期压力。
</div>

<p class="report-brief" style="margin-top:8px;font-size:0.78em;">*2026Q1 归母净利须结合附注区分经常性因素。</p>

---

<!-- _class: rich-slide -->

<span class="eyebrow">交易背景</span>

## <span class="section-no">五</span>募资规模与一级市场心理价位

<div class="report-brief">
<strong>交易解读</strong>：拟募资约 295 亿元反映产能与研发继续扩张的决心；一级市场 1,282—1,584 亿走廊相当于以 2024 年收入为锚的 <strong>5—7 倍 PS</strong>，已提前计入 2025—2026 年收入跃迁预期，故二级定价更似「验证」而非「发现」。
</div>

<div class="kpi-grid">

<div class="kpi">
<span class="label">拟募集资金</span>
<span class="value">约 295 亿元</span>
<span class="note">科创板受理（2025-12-30）</span>
</div>

<div class="kpi">
<span class="label">报道估值走廊</span>
<span class="value">1,282—1,584 亿</span>
<span class="note">约 5.3—6.6× 2024 年收入 PS</span>
</div>

<div class="kpi">
<span class="label">产业地位（招股书）</span>
<span class="value">全球第四</span>
<span class="note">中国 DRAM 出货量第一</span>
</div>

<div class="kpi">
<span class="label">定价逻辑检验</span>
<span class="value">三条线</span>
<span class="note">收入增速 · 亏损收敛 · 板块 Beta</span>
</div>

</div>

<div class="insight-strip">
<strong>定价含义</strong>：全球第四 / 国内第一份额支撑「战略资产」叙事；但若发行定价靠近走廊上沿，投资者承担的实质是<strong>DRAM 景气均值回归</strong>与<strong>资本开支峰值</strong>的双重风险。
</div>

<p class="report-brief" style="margin-top:8px;font-size:0.78em;">注：估值走廊来自公开媒体报道区间，非交易所成交价格。</p>

---

<!-- _class: rich-slide -->

<span class="eyebrow">宏观与产业</span>

## <span class="section-no">六</span>政策托底与周期波动并存

<div class="report-brief">
<strong>宏观叙事</strong>：政策端提供税收优惠与自主可控预期，构成估值「软下限」；市场端则受全球 DRAM 合约价、库存周期与美联储利率路径制约。长鑫定价须在<strong>政策期权</strong>与<strong>商品周期</strong>之间取交集，而非简单叠加。
</div>

<div class="cols">

<div class="col-card">

### 制度环境

国发〔2020〕8 号与「十四五」信息化规划强化存储自主可控 → 降低有效税率、改善融资可得性，形成<strong>长期估值下限</strong>。

### 资本事件轴

辅导备案 → 受理 → 2026-05 上会稿：信息分批释放，一级价格往往在申报—上会阶段即形成锚定。

</div>

<div class="col-card">

### 行业节奏

DRAM 合约价与库存周期决定短期收入弹性；A 股半导体指数与 MU <strong>同向但不同步</strong>，须防「国内情绪过热、全球基本面转弱」的错位。

### 对本项目含义

政策溢价可解释 PS 高于成熟制造，但无法单独解释<strong>持续亏损后的转正幅度</strong>——盈利质量才是二级承接的关键。

</div>

</div>

---

<!-- _class: data-slide rich-slide -->

<span class="eyebrow">政策环境</span>

## <span class="section-no">表2</span>政策与产业背景要点

| 政策 / 文件 | 经济含义 |
|:--|:--|
| 国发〔2020〕8 号（集成电路） | 税收优惠与产业协同 → 降低有效税率、支撑长期 Capex |
| 「十四五」国家信息化规划 | 存储器等关键环节自主可控 → **战略期权**计入估值 |
| 科创板 IPO 受理（2025-12-30） | 拟募资约 295 亿元；信息披露节奏影响一级定价预期 |
| Omdia 出货量口径（招股书） | 中国 DRAM 出货量第一、全球第四 → 份额叙事支撑 PS 锚 |

---

<!-- _class: rich-slide -->

<span class="eyebrow">研究方法</span>

## <span class="section-no">七</span>证据链与数据复现路径

<div class="report-brief">
<strong>方法说明</strong>：本简报不做黑箱估值。CAPM、事件研究、OLS 与 PS 回归均为<strong>示意性量化</strong>，样本受限处（如仅 3 个年报）已明示，避免过度拟合叙事。
</div>

| 数据模块 | 官方 / 公开来源 |
|:--|:--|
| 公司财务 | 上交所招股说明书 PDF（结构化解析） |
| A 股行情与指数 | akshare（沪深300、科创50、半导体指数） |
| 同业财务 | 同花顺摘要（8 家可比公司） |
| 全球对照 | 美光 MU 年报（SEC 披露汇总） |

---

<!-- _class: rich-slide -->

<span class="eyebrow">分析框架</span>

## <span class="section-no">八</span>四维分析框架：从事实到定价

<div class="insight-strip">
<strong>框架逻辑</strong>：先确认「量」（收入与结构）→ 再检验「质」（盈利与研发）→ 继而测算「市场风险」（Beta 与事件）→ 最后收敛至「价格走廊」（一级 PS 与回归交叉）。四维任一环节弱化，估值结论即需下调置信度。
</div>

<div class="kpi-grid">

<div class="kpi">
<span class="label">① 成长</span>
<span class="value" style="font-size:1em;">营收 & 结构</span>
<span class="note">DDR / LPDDR · 2026Q1 脉冲</span>
</div>

<div class="kpi">
<span class="label">② 盈利</span>
<span class="value" style="font-size:1em;">拐点 & 刚性</span>
<span class="note">归母净利 · 研发费用率</span>
</div>

<div class="kpi">
<span class="label">③ 市场</span>
<span class="value" style="font-size:1em;">Beta & ROE</span>
<span class="note">板块情绪 · 同业分化</span>
</div>

<div class="kpi">
<span class="label">④ 定价</span>
<span class="value" style="font-size:1em;">锚 & 敏感性</span>
<span class="note">走廊价 · PS 回归 · 收入×PE</span>
</div>

</div>

<div class="flow-hint">
<strong>图表导读</strong>：图 1—5 为核心定价链；图 6—10 补充产品结构、全球对照、Beta 与事件研究；表 3 给出收入×PE 敏感性。
</div>

---

<!-- _class: chart-slide -->

<span class="eyebrow">图表分析</span>

## <span class="section-no">图1</span>营收与盈利：从份额扩张到现金流修复

<div class="fig-head">
<p class="fig-caption"><strong>图 1</strong> 长鑫科技营业收入与归母净利润（2021—2026Q1）；左轴营收、右轴归母净利润，单位：亿元</p>
</div>

<div class="chart-layout">

<div class="chart-figure">
<div class="chart-wrap">

<img class="chart-img" src="./data/output/fig1_cxkj_revenue_profit.png" alt="图1" />

</div>
</div>

<div class="interpret">
<div class="interpret-title">图表点评</div>

<div class="interp-block">
<span class="label">一、读图</span>
<p>2023—2025 营收由 <em>91 → 242 → 618 亿元</em>；归母净利由 <em>-163 → -71 → +18.7 亿元</em>，2025 年首次站上盈亏线。</p>
</div>

<div class="interp-block">
<span class="label">二、含义</span>
<p>公司已进入收入<strong>指数型扩张</strong>阶段，但利润对价格与产能利用率仍高度敏感；<em>409 亿元</em> 量级累计亏损意味着一轮下行周期即可显著侵蚀 2025 年盈利修复。</p>
</div>

<div class="interp-block">
<span class="label">三、启示</span>
<p>估值不应仅锚定收入 PS，须同步跟踪<strong>毛利与折旧</strong>；2026Q1 单季收入 508 亿提示景气高位，亦放大周期反转风险。</p>
</div>

</div>

</div>

---

<!-- _class: chart-slide -->

<span class="eyebrow">图表分析</span>

## <span class="section-no">图2</span>一级市场估值走廊：预期定价主导

<div class="fig-head">
<p class="fig-caption"><strong>图 2</strong> 一级市场报道估值区间与参考点（非二级市场成交价格，单位：亿元）</p>
</div>

<div class="chart-layout">

<div class="chart-figure">
<div class="chart-wrap">

<img class="chart-img" src="./data/output/fig6_valuation_range.png" alt="图2" />

</div>
</div>

<div class="interpret">
<div class="interpret-title">图表点评</div>

<div class="interp-block">
<span class="label">一、读图</span>
<p>区间大致覆盖 <em>1,282—1,584 亿元</em>，对应 2024 年收入约 <em>5.3—6.6 倍 PS</em>；下限贴近 2024 年末交易参考，上限反映 2026 年初媒体报道高位。</p>
</div>

<div class="interp-block">
<span class="label">二、含义</span>
<p>一级市场已在<strong>盈利尚未稳定</strong>阶段给出「成熟成长股」量级的 PS，隐含对 2025—2026 收入高增及份额持续提升的<strong>前置定价</strong>。</p>
</div>

<div class="interp-block">
<span class="label">三、启示</span>
<p>二级上市定价大概率<strong>参照该走廊</strong>而非 DRAM 现货日度波动；若发行定价靠近上沿，留给二级资金的赔率取决于盈利能否<strong>兑现并维持</strong>。</p>
</div>

</div>

</div>

---

<!-- _class: chart-slide -->

<span class="eyebrow">图表分析</span>

## <span class="section-no">图3</span>同业 ROE 比较：产业链内部分化显著

<div class="fig-head">
<p class="fig-caption"><strong>图 3</strong> A 股半导体产业链可比公司净资产收益率（8 家可比公司，2020—2026）</p>
</div>

<div class="chart-layout">

<div class="chart-figure">
<div class="chart-wrap">

<img class="chart-img" src="./data/output/fig5_roe_peer.png" alt="图3" />

</div>
</div>

<div class="interpret">
<div class="interpret-title">图表点评</div>

<div class="interp-block">
<span class="label">一、读图</span>
<p>设备（北方华创、中微）、制造（中芯、华润微）与存储/设计标的 ROE <strong>路径分化</strong>；2024 年前后多数同业 ROE 修复，波动幅度小于纯存储设计龙头。</p>
</div>

<div class="interp-block">
<span class="label">二、含义</span>
<p>长鑫尚未纳入可比序列，但上市后将面临「<em>高 Beta 存储</em>」与「<em>政策背书制造</em>」的双重标签；市场可能给予高于传统 IDM 的 PS，同时要求更高的盈利可见度。</p>
</div>

<div class="interp-block">
<span class="label">三、启示</span>
<p>不宜用单一行业 PE 中位数套用；建议按<strong>产业链位置 + ROE 稳定性</strong>分层估值。存储链 CAPM Beta 多显著大于 1，板块情绪对长鑫定价有<strong>放大器效应</strong>。</p>
</div>

</div>

</div>

---

<!-- _class: chart-slide -->

<span class="eyebrow">图表分析</span>

## <span class="section-no">图4</span>收入路径：披露高增与线性外推的张力

<div class="fig-head">
<p class="fig-caption"><strong>图 4</strong> 营业收入实际值与 OLS 趋势外推（灰色虚线为模型外推，<strong>非公司指引</strong>）</p>
</div>

<div class="chart-layout">

<div class="chart-figure">
<div class="chart-wrap">

<img class="chart-img" src="./data/output/fig7_revenue_ols_forecast.png" alt="图4" />

</div>
</div>

<div class="interpret">
<div class="interpret-title">图表点评</div>

<div class="interp-block">
<span class="label">一、读图</span>
<p>年报拟合斜率约 <em>+264 亿元/年</em>（R²≈0.94，但样本仅 3 年，p≈0.15）；2026Q1 单季 508 亿显著高于线性外推的季度化水平。</p>
</div>

<div class="interp-block">
<span class="label">二、含义</span>
<p>若将 Q1 简单年化，收入体量已处于<strong>极端景气假设</strong>；DRAM 行业存在均值回归，线性外推更适合做<strong>敏感性上下界</strong>，不宜视为管理层预测。</p>
</div>

<div class="interp-block">
<span class="label">三、启示</span>
<p>收入×PE 情景（8/15/25 倍 → 约 4,944—15,450 亿）展示的是<strong>「若收入维持」</strong>的市值空间，而非基准情形；定价应引入<strong>价格周期 + 产能利用率</strong>折现。</p>
</div>

</div>

</div>

---

<!-- _class: chart-slide -->

<span class="eyebrow">图表分析</span>

## <span class="section-no">图5</span>PS 回归交叉验证：与走廊同量级

<div class="fig-head">
<p class="fig-caption"><strong>图 5</strong> 存储产业链市值—营收对数回归与长鑫隐含点（红星为 2024 年收入对应隐含市值）</p>
</div>

<div class="chart-layout">

<div class="chart-figure">
<div class="chart-wrap">

<img class="chart-img" src="./data/output/fig7_peer_ps_regression.png" alt="图5" />

</div>
</div>

<div class="interpret">
<div class="interpret-title">图表点评</div>

<div class="interp-block">
<span class="label">一、读图</span>
<p>对数回归隐含市值约 <em>1,636 亿元</em>，对应 PS 约 <em>6.8×</em>（基于 2024 年 242 亿收入）；模型 R² 仅 <em>0.08</em>，拟合度弱。</p>
</div>

<div class="interp-block">
<span class="label">二、含义</span>
<p>尽管统计拟合一般，<strong>经济结论</strong>仍清晰：市场历史上愿意为存储龙头的收入规模支付 <em>6× 左右 PS</em>，与报道走廊 <em>1,282—1,584 亿</em> <strong>相互印证</strong>。</p>
</div>

<div class="interp-block">
<span class="label">三、启示</span>
<p>宜将 1,300—1,650 亿视为<strong>共识带</strong>而非精确公允值；若 2025 年 618 亿收入在二级获得认可，静态 PS 可下移，但<strong>盈利质量与可持续 Capex</strong>将决定能否撑住估值。</p>
</div>

</div>

</div>

---

<!-- _class: chart-slide -->

<span class="eyebrow">图表分析</span>

## <span class="section-no">图6</span>产品结构：LPDDR 占比抬升

<div class="fig-head">
<p class="fig-caption"><strong>图 6</strong> DDR 与 LPDDR 系列收入构成</p>
</div>

<div class="chart-layout">

<div class="chart-figure">
<div class="chart-wrap">

<img class="chart-img" src="./data/output/fig2_product_mix.png" alt="图6" />

</div>
</div>

<div class="interpret">
<div class="interpret-title">图表点评</div>

<div class="interp-block">
<span class="label">一、读图</span>
<p>2025 年 LPDDR 约 <em>407 亿元</em>、DDR 约 <em>195 亿元</em>；2024 年对应约 <em>198 亿 / 32 亿</em>，LPDDR 增速显著高于 DDR。</p>
</div>

<div class="interp-block">
<span class="label">二、含义</span>
<p>收入结构向<strong>移动与嵌入式</strong>场景倾斜，有助于平滑部分 PC/服务器 DRAM 周期波动，但高端制程与验证周期仍决定毛利质量。</p>
</div>

<div class="interp-block">
<span class="label">三、启示</span>
<p>估值叙事可从「纯周期存储」部分转向「结构升级」；须跟踪 LPDDR 在主流手机厂商与服务器端的<strong>认证与份额</strong>兑现节奏。</p>
</div>

</div>

</div>

---

<!-- _class: chart-slide -->

<span class="eyebrow">图表分析</span>

## <span class="section-no">图7</span>全球对照：美光与 A 股半导体指数

<div class="fig-head">
<p class="fig-caption"><strong>图 7</strong> 美光（MU）与 A 股半导体指数走势对照（归一化）</p>
</div>

<div class="chart-layout">

<div class="chart-figure">
<div class="chart-wrap">

<img class="chart-img" src="./data/output/fig4_mu_vs_semiconductor.png" alt="图7" />

</div>
</div>

<div class="interpret">
<div class="interpret-title">图表点评</div>

<div class="interp-block">
<span class="label">一、读图</span>
<p>MU 与半导体指数<strong>同向但不同步</strong>；全球 DRAM 定价与 A 股情绪存在传导时滞。</p>
</div>

<div class="interp-block">
<span class="label">二、含义</span>
<p>长鑫上市定价无法仅看国内指数；须将<strong>全球合约价/现货价</strong>与 MU 盈利周期纳入情景分析。</p>
</div>

<div class="interp-block">
<span class="label">三、启示</span>
<p>建议建立「MU 盈利 surprise → A 股存储 Beta → 长鑫发行溢价」的<strong>联动监测表</strong>，作为申购策略辅助。</p>
</div>

</div>

</div>

---

<!-- _class: chart-slide -->

<span class="eyebrow">图表分析</span>

## <span class="section-no">图8</span>系统性风险：存储链 CAPM Beta

<div class="fig-head">
<p class="fig-caption"><strong>图 8</strong> 可比公司相对沪深300 / 科创50 的 Beta 估计</p>
</div>

<div class="chart-layout">

<div class="chart-figure">
<div class="chart-wrap">

<img class="chart-img" src="./data/output/fig7_capm_beta_dual_benchmark.png" alt="图8" />

</div>
</div>

<div class="interpret">
<div class="interpret-title">图表点评</div>

<div class="interp-block">
<span class="label">一、读图</span>
<p>兆易创新、澜起、君正、韦尔等 Beta 约 <em>1.3—1.4</em>（相对沪深300）；多数估计 <strong>p&lt;0.05</strong>，系统性风险高于市场。</p>
</div>

<div class="interp-block">
<span class="label">二、含义</span>
<p>存储/设计链对大盘波动<strong>放大器</strong>明显；长鑫上市后大概率归入高 Beta 集群，估值折现率对无风险利率更敏感。</p>
</div>

<div class="interp-block">
<span class="label">三、启示</span>
<p>一级定价已隐含成长溢价时，二级需关注<strong>利率与板块资金</strong>双向挤压；不宜在半导体指数 CAR 高位追涨发行。</p>
</div>

</div>

</div>

---

<!-- _class: chart-slide -->

<span class="eyebrow">图表分析</span>

## <span class="section-no">图9</span>事件研究：IPO 消息是否已被定价

<div class="fig-head">
<p class="fig-caption"><strong>图 9</strong> 两条官方 IPO 节点 × 两类资产 CAR（实线=半导体指数，虚线=存储同业；基准=沪深300）</p>
</div>

<div class="chart-layout">

<div class="chart-figure">
<div class="chart-wrap">

<img class="chart-img" src="./data/output/fig7_event_study_car_detailed.png" alt="图9" />

</div>
</div>

<div class="interpret">
<div class="interpret-title">图表点评</div>

<div class="interp-block">
<span class="label">一、读图</span>
<p>四条曲线同轴对比：<em>辅导备案</em>两端 CAR 接近 0（约 -0.5%）；<em>IPO 受理</em>半导体 <em>+6.5%</em>、存储同业 <em>+5.1%</em>（事件窗末端标注）。</p>
</div>

<div class="interp-block">
<span class="label">二、含义</span>
<p>受理节点有<strong>方向性正向反应</strong>，但 AR 检验 <strong>p≈0.15</strong>（不显著）→ 超额收益难以与大盘噪音区分，消息或已部分前置定价。</p>
</div>

<div class="interp-block">
<span class="label">三、启示</span>
<p>不宜用单事件 CAR 外推上市溢价；须结合<strong>发行折价、配售结构、解禁日历</strong>与多事件联合检验。</p>
</div>

</div>

</div>

---

<!-- _class: data-slide -->

<span class="eyebrow">估值敏感性</span>

## <span class="section-no">表3</span>收入×PE 情景市值（示意，非投资建议）

<div class="report-brief" style="margin-top:6px;font-size:0.78em;">基于 2025 年营业收入 618.0 亿元</div>

<div class="scenario-grid">

<div class="scenario-card conservative">
<span class="tag">保守情景 · PE 8×</span>
<span class="num">约 4,944 亿</span>
<span class="sub">收入锚定 · 未修正盈利质量</span>
</div>

<div class="scenario-card neutral">
<span class="tag">中性情景 · PE 15×</span>
<span class="num">约 9,270 亿</span>
<span class="sub">对应乐观情绪上限参考</span>
</div>

<div class="scenario-card optimistic">
<span class="tag">乐观情景 · PE 25×</span>
<span class="num">约 15,450 亿</span>
<span class="sub">极端景气假设 · 慎用</span>
</div>

</div>

<div class="insight-strip" style="margin-top:10px;">
<strong>交叉验证</strong>：一级报道走廊 1,282—1,584 亿（约 5—7× PS）与 PS 回归隐含 1,636 亿更接近「Pre-IPO 共识带」；上表 PE 情景须待盈利预测与股本摊薄后修正。
</div>

---

<!-- _class: verdict -->

<span class="eyebrow">结论与研判</span>

## <span class="section-no">九</span>综合判断

<div class="point"><b>高 β 成长阶段</b><br>收入与份额指标具全球意义；累计亏损与资本开支意味着下行风险仍可能被低估。</div>

<div class="point"><b>估值锚已在一级市场成型</b><br>约 1,300—1,600 亿元区间与 PS 回归相互印证，定价的是战略期权 + 成长，而非稳定自由现金流。</div>

<div class="point"><b>二级市场联动需审慎</b><br>存储链 Beta 高于大盘；IPO 事件窗异常收益多不显著。收入×PE 敏感性（2025 收入）：8/15/25 倍 → 约 4,944 / 9,270 / 15,450 亿元。</div>

<p class="disclaimer">上述 PE 情景须待盈利预测修正 · 不构成投资建议</p>

---

<!-- _class: rich-slide -->

<span class="eyebrow">风险与展望</span>

## <span class="section-no">十</span>研究局限与后续议程

<div class="cols">

<div class="col-card">

### 主要局限

- 未上市，缺高频毛利、产能利用率、合约价
- 未展开 DCF；部分回归样本仅 3 个年报
- 一级估值来自媒体报道，非成交价格

</div>

<div class="col-card">

### 建议深化

- DRAM 现货/合约价 + 产能利用率情景
- 申购定价博弈与解禁对板块资金的冲击
- 分部 DCF（盈亏平衡产能假设）

</div>

</div>

---

<!-- _class: closing -->
<!-- _paginate: false -->

<div class="closing-inner">

<p class="closing-tag">长鑫科技 Pre-IPO 估值专题</p>

# 感谢聆听

<p>欢迎就假设参数、情景设定与模型口径进一步讨论</p>

</div>
