import yfinance as yf
import akshare as ak
import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

DATA_DIR = "D:/3. 中山大学/5. 课件/6-数据分析与经济决策/team homework3/submissions/25PA/Team02-G03-黄金现货投资分析/data"

print("=" * 60)
print("开始获取数据...")
print("=" * 60)

# ============================================================
# 1. Yahoo Finance: COMEX Gold Futures (GC=F)
# ============================================================
print("\n[1/8] 获取 COMEX 黄金期货数据...")
gold_comex = yf.download("GC=F", start="2010-01-01", end="2025-05-16", progress=False)
gold_comex = gold_comex[["Close"]].rename(columns={"Close": "comex_gold"})
gold_comex.index = pd.to_datetime(gold_comex.index).tz_localize(None)
gold_comex.index.name = "date"
gold_comex.to_csv(f"{DATA_DIR}/comex_gold.csv")
print(f"  -> {len(gold_comex)} 条日数据, 范围 {gold_comex.index[0].date()} ~ {gold_comex.index[-1].date()}")

# ============================================================
# 2. Yahoo Finance: DXY (美元指数)
# ============================================================
print("\n[2/8] 获取 美元指数 DXY...")
dxy = yf.download("DX-Y.NYB", start="2010-01-01", end="2025-05-16", progress=False)
dxy = dxy[["Close"]].rename(columns={"Close": "dxy"})
dxy.index = pd.to_datetime(dxy.index).tz_localize(None)
dxy.index.name = "date"
dxy.to_csv(f"{DATA_DIR}/dxy.csv")
print(f"  -> {len(dxy)} 条日数据")

# ============================================================
# 3. Yahoo Finance: VIX
# ============================================================
print("\n[3/8] 获取 VIX 恐慌指数...")
vix = yf.download("^VIX", start="2010-01-01", end="2025-05-16", progress=False)
vix = vix[["Close"]].rename(columns={"Close": "vix"})
vix.index = pd.to_datetime(vix.index).tz_localize(None)
vix.index.name = "date"
vix.to_csv(f"{DATA_DIR}/vix.csv")
print(f"  -> {len(vix)} 条日数据")

# ============================================================
# 4. Yahoo Finance: 10Y Treasury Yield + S&P 500 + GLD ETF
# ============================================================
print("\n[4/8] 获取 美债10Y收益率 + 标普500 + GLD黄金ETF...")
multi = yf.download(["^TNX", "^GSPC", "GLD"], start="2010-01-01", end="2025-05-16", progress=False)
us10y = multi["Close"]["^TNX"].rename("us10y")
sp500 = multi["Close"]["^GSPC"].rename("sp500")
gld = multi["Close"]["GLD"].rename("gld_etf")

us10y.index = pd.to_datetime(us10y.index).tz_localize(None)
sp500.index = pd.to_datetime(sp500.index).tz_localize(None)
gld.index = pd.to_datetime(gld.index).tz_localize(None)

us10y.index.name = "date"; sp500.index.name = "date"; gld.index.name = "date"
us10y.to_csv(f"{DATA_DIR}/us10y.csv"); sp500.to_csv(f"{DATA_DIR}/sp500.csv"); gld.to_csv(f"{DATA_DIR}/gld_etf.csv")
print(f"  -> 美债10Y {len(us10y)} 条, 标普500 {len(sp500)} 条, GLD {len(gld)} 条")

# ============================================================
# 5. Yahoo Finance: SSE Composite (上证指数)
# ============================================================
print("\n[5/8] 获取 上证指数 + 沪深300...")
sse = yf.download("000001.SS", start="2010-01-01", end="2025-05-16", progress=False)
sse = sse[["Close"]].rename(columns={"Close": "sse_index"})
sse.index = pd.to_datetime(sse.index).tz_localize(None)
sse.index.name = "date"
sse.to_csv(f"{DATA_DIR}/sse_index.csv")

hs300 = yf.download("300750.SZ", start="2010-01-01", end="2025-05-16", progress=False)
# Use proper CSI 300 ETF
hs300 = yf.download("510300.SS", start="2012-06-01", end="2025-05-16", progress=False)
if len(hs300) > 0:
    hs300 = hs300[["Close"]].rename(columns={"Close": "hs300"})
    hs300.index = pd.to_datetime(hs300.index).tz_localize(None)
    hs300.index.name = "date"
    hs300.to_csv(f"{DATA_DIR}/hs300.csv")
print(f"  -> 上证指数 {len(sse)} 条, 沪深300 {len(hs300)} 条")

# ============================================================
# 6. akshare: 上海黄金交易所 Au99.99
# ============================================================
print("\n[6/8] 获取 上海金 Au99.99...")
try:
    sh_gold = ak.spot_golden_benchmark_sge()
    sh_gold = sh_gold[["date", "price"]].rename(columns={"price": "shanghai_gold"})
    sh_gold["date"] = pd.to_datetime(sh_gold["date"])
    sh_gold = sh_gold.set_index("date")
    sh_gold = sh_gold[sh_gold.index >= "2016-04-01"]
    sh_gold.to_csv(f"{DATA_DIR}/shanghai_gold.csv")
    print(f"  -> {len(sh_gold)} 条日数据 (上海金基准价)")
except Exception as e:
    print(f"  -> 上海金基准价获取失败: {e}")
    # Fallback: try Au99.99 spot
    try:
        sh_gold = ak.spot_price_sge(symbol="Au99.99")
        sh_gold = sh_gold[["date", "close"]].rename(columns={"close": "shanghai_gold"})
        sh_gold["date"] = pd.to_datetime(sh_gold["date"])
        sh_gold = sh_gold.set_index("date")
        sh_gold = sh_gold[sh_gold.index >= "2010-01-01"]
        sh_gold.to_csv(f"{DATA_DIR}/shanghai_gold.csv")
        print(f"  -> {len(sh_gold)} 条日数据 (Au99.99)")
    except Exception as e2:
        print(f"  -> Au99.99获取也失败: {e2}")

# ============================================================
# 7. akshare: 中国 CPI 月度数据
# ============================================================
print("\n[7/8] 获取 中国 CPI...")
try:
    china_cpi = ak.macro_china_cpi_yearly()
    # Try monthly CPI
    china_cpi = ak.macro_china_cpi_monthly()
    china_cpi = china_cpi.rename(columns={"日期": "date", "全国-当月": "china_cpi_yoy"})
    china_cpi["date"] = pd.to_datetime(china_cpi["date"])
    china_cpi = china_cpi.set_index("date")
    china_cpi = china_cpi[china_cpi.index >= "2010-01-01"]
    china_cpi.to_csv(f"{DATA_DIR}/china_cpi.csv")
    print(f"  -> {len(china_cpi)} 条月度数据")
except Exception as e:
    print(f"  -> 中国CPI获取失败: {e}")
    try:
        china_cpi = ak.macro_china_cpi_yearly()
        china_cpi = china_cpi.rename(columns={"日期": "date", "全国": "china_cpi_yoy"})
        china_cpi["date"] = pd.to_datetime(china_cpi["date"])
        china_cpi = china_cpi.set_index("date")
        china_cpi = china_cpi[china_cpi.index >= "2010-01-01"]
        china_cpi.to_csv(f"{DATA_DIR}/china_cpi.csv")
        print(f"  -> {len(china_cpi)} 条年度数据(fallback)")
    except Exception as e2:
        print(f"  -> 中国CPI全部失败: {e2}")

# ============================================================
# 8. FRED: TIPS 10Y real yield + US CPI
# ============================================================
print("\n[8/8] 获取 FRED 数据 (TIPS实际利率 + 美国CPI)...")
try:
    from fredapi import Fred
    fred = Fred(api_key="7e5eec87a6569c2d7ca6ac19b70e8f4b")
    
    tips = fred.get_series("DFII10", observation_start="2010-01-01", observation_end="2025-04-30")
    tips = pd.DataFrame({"tips_real_yield": tips})
    tips.index.name = "date"
    tips.index = pd.to_datetime(tips.index)
    tips.to_csv(f"{DATA_DIR}/tips_real_yield.csv")
    print(f"  -> TIPS实际利率 {len(tips)} 条日数据")
    
    us_cpi = fred.get_series("CPIAUCSL", observation_start="2010-01-01", observation_end="2025-04-30")
    us_cpi = pd.DataFrame({"us_cpi_index": us_cpi})
    us_cpi.index.name = "date"
    us_cpi.index = pd.to_datetime(us_cpi.index)
    us_cpi["us_cpi_yoy"] = us_cpi["us_cpi_index"].pct_change(12) * 100
    us_cpi.to_csv(f"{DATA_DIR}/us_cpi.csv")
    print(f"  -> 美国CPI {len(us_cpi)} 条月度数据")

    fed_funds = fred.get_series("DFF", observation_start="2010-01-01", observation_end="2025-04-30")
    fed_funds = pd.DataFrame({"fed_funds_rate": fed_funds})
    fed_funds.index.name = "date"
    fed_funds.index = pd.to_datetime(fed_funds.index)
    fed_funds.to_csv(f"{DATA_DIR}/fed_funds_rate.csv")
    print(f"  -> 联邦基金利率 {len(fed_funds)} 条日数据")

    gpr = fred.get_series("GEPUCURRENT", observation_start="2010-01-01", observation_end="2025-04-30")
    gpr = pd.DataFrame({"gpr_index": gpr})
    gpr.index.name = "date"
    gpr.index = pd.to_datetime(gpr.index)
    gpr = gpr.resample("M").last()
    gpr.to_csv(f"{DATA_DIR}/gpr_index.csv")
    print(f"  -> 地缘政治风险GPR指数 {len(gpr)} 条月度数据")

except Exception as e:
    print(f"  -> FRED数据获取失败: {e}")
    print("     请安装: pip install fredapi")
    print("     (需要免费FRED API key, 已在代码中提供测试key)")

print("\n" + "=" * 60)
print("数据获取完成！所有数据已保存到 data/ 目录")
print("=" * 60)
