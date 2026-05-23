# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.stats import norm
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 120

# ====================== 路径配置 ======================
data_path = "./data_clean/final.csv"
plot_dir = "./plots"
os.makedirs(plot_dir, exist_ok=True)

# ====================== 读取数据 ======================
df = pd.read_csv(data_path)
df["date"] = pd.to_datetime(df["date"])

# ====================== 1. 价格时序图 ======================
plt.figure(figsize=(14,6))
plt.plot(df["date"], df["SC_close"], label="SC Close", color="#1f77b4", linewidth=1.1)
plt.plot(df["date"], df["PTA_close"], label="PTA Close", color="#ff7f0e", linewidth=1.1)
plt.title("Price Trend: SC vs PTA", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{plot_dir}/01_price_trend.png", bbox_inches='tight')
plt.close()

# ====================== 2. 收益率分布直方图 + 拟合 ======================
fig, axes = plt.subplots(1,2,figsize=(14,5))
axes[0].hist(df["SC_ret"], bins=80, alpha=0.7, color="#1f77b4", density=True)
axes[1].hist(df["PTA_ret"], bins=80, alpha=0.7, color="#ff7f0e", density=True)
axes[0].set_title("SC Return Distribution")
axes[1].set_title("PTA Return Distribution")
for ax in axes:
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{plot_dir}/02_return_hist.png")
plt.close()

# ====================== 3. 核密度分布 KDE ======================
plt.figure(figsize=(10,5))
sns.kdeplot(df["SC_ret"], fill=True, color="#1f77b4", label="SC")
sns.kdeplot(df["PTA_ret"], fill=True, color="#ff7f0e", label="PTA")
plt.title("Kernel Density: Returns")
plt.xlabel("Log Return")
plt.ylabel("Density")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{plot_dir}/03_kde.png")
plt.close()

# ====================== 4. 箱线图（异常值） ======================
fig, axes = plt.subplots(1,2,figsize=(10,5))
axes[0].boxplot(df["SC_ret"].dropna(), vert=False, widths=0.7)
axes[1].boxplot(df["PTA_ret"].dropna(), vert=False, widths=0.7)
axes[0].set_title("SC Return Boxplot")
axes[1].set_title("PTA Return Boxplot")
for ax in axes:
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{plot_dir}/04_boxplot.png")
plt.close()

# ====================== 5. 20日波动率时序 ======================
plt.figure(figsize=(14,6))
plt.plot(df["date"], df["SC_vol20"], label="SC Volatility (20d)", color="#1f77b4")
plt.plot(df["date"], df["PTA_vol20"], label="PTA Volatility (20d)", color="#ff7f0e")
plt.title("20-Day Rolling Volatility")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{plot_dir}/05_volatility.png")
plt.close()

# ====================== 6. 相关性散点图 ======================
plt.figure(figsize=(8,8))
plt.scatter(df["SC_close"], df["PTA_close"], alpha=0.5, s=8)
corr = df[["SC_close","PTA_close"]].corr().iloc[0,1]
plt.title(f"Price Correlation: {corr:.2f}")
plt.xlabel("SC Close")
plt.ylabel("PTA Close")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{plot_dir}/06_corr_scatter.png")
plt.close()

# ====================== 7. 相关性热力图 ======================
corr_df = df[["SC_close","PTA_close","SC_vol20","PTA_vol20"]].corr()
plt.figure(figsize=(7,6))
sns.heatmap(corr_df, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(f"{plot_dir}/07_heatmap.png")
plt.close()

print("✅ 所有图表已保存至：./plots/")
print("📊 生成图表：")
print("1. 价格趋势图")
print("2. 收益率直方图")
print("3. 核密度图")
print("4. 箱线图")
print("5. 波动率趋势")
print("6. 价格散点图")
print("7. 相关性热力图")