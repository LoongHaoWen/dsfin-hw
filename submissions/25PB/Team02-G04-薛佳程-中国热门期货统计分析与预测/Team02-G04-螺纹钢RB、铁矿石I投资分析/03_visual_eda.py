import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

data_path = "./data_clean/final.csv"
plot_dir = "./plots"
os.makedirs(plot_dir, exist_ok=True)

df = pd.read_csv(data_path)
df["date"] = pd.to_datetime(df["date"])

# 1 价格时序
plt.figure(figsize=(14,6))
plt.plot(df.date, df.RB_close, label="RB Close")
plt.plot(df.date, df.IRON_close, label="Iron Close")
plt.title("RB vs Iron Price Trend")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{plot_dir}/01_price.png")
plt.close()

# 2 收益率直方图
fig, axes = plt.subplots(1,2,figsize=(12,5))
axes[0].hist(df.RB_ret, bins=80, alpha=0.7)
axes[1].hist(df.IRON_ret, bins=80, alpha=0.7)
axes[0].set_title("RB Return")
axes[1].set_title("Iron Return")
plt.tight_layout()
plt.savefig(f"{plot_dir}/02_hist.png")
plt.close()

# 3 KDE
plt.figure(figsize=(10,5))
sns.kdeplot(df.RB_ret.dropna(), fill=True, label="RB")
sns.kdeplot(df.IRON_ret.dropna(), fill=True, label="Iron")
plt.title("Kernel Density")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{plot_dir}/03_kde.png")
plt.close()

# 4 箱线图
fig, axes = plt.subplots(1,2,figsize=(10,5))
axes[0].boxplot(df.RB_ret.dropna(), vert=False)
axes[1].boxplot(df.IRON_ret.dropna(), vert=False)
axes[0].set_title("RB Boxplot")
axes[1].set_title("Iron Boxplot")
plt.tight_layout()
plt.savefig(f"{plot_dir}/04_box.png")
plt.close()

# 5 波动率
plt.figure(figsize=(14,6))
plt.plot(df.date, df.RB_vol20, label="RB Vol")
plt.plot(df.date, df.IRON_vol20, label="Iron Vol")
plt.title("20-Day Volatility")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{plot_dir}/05_vol.png")
plt.close()

# 6 相关性散点
corr = df.RB_close.corr(df.IRON_close)
plt.figure(figsize=(7,7))
plt.scatter(df.RB_close, df.IRON_close, s=6, alpha=0.5)
plt.title(f"Correlation = {corr:.2f}")
plt.tight_layout()
plt.savefig(f"{plot_dir}/06_corr.png")
plt.close()

# 7 热力图
corr_df = df[["RB_close","IRON_close","RB_ret","IRON_ret","RB_vol20","IRON_vol20"]].corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr_df, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap")
plt.tight_layout()
plt.savefig(f"{plot_dir}/07_heatmap.png")
plt.close()

print("✅ 7张图表已保存至 ./plots/")