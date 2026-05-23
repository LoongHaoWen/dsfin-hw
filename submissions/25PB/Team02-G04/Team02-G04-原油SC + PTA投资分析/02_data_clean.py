import pandas as pd
import numpy as np
import os

os.makedirs("./data_clean", exist_ok=True)

sc = pd.read_csv("./data_raw/sc.csv")
pta = pd.read_csv("./data_raw/pta.csv")

def clean(df, prefix):
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.drop_duplicates("date")
    df = df.sort_values("date")
    df = df[(df["close"] > 0) & (df["volume"] >= 0)]
    df = df.dropna()

    df["ret"] = np.log(df["close"] / df["close"].shift(1))
    df["vol20"] = df["ret"].rolling(20).std()

    df = df.dropna()
    df.columns = [f"{prefix}_{c}" if c != "date" else "date" for c in df.columns]
    return df

sc_clean = clean(sc, "SC")
pta_clean = clean(pta, "PTA")

# 时间对齐（课程要求：inner join）
final = pd.merge(sc_clean, pta_clean, on="date", how="inner").dropna()
final.to_csv("./data_clean/final.csv", index=False)

print("✅ 清洗完成")
print(f"样本数：{len(final)}")
print(f"缺失值：{final.isnull().sum().sum()}")