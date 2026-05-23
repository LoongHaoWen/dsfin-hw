import pandas as pd
import numpy as np
import os

os.makedirs("./data_clean", exist_ok=True)

rb = pd.read_csv("./data_raw/rb.csv")
iron = pd.read_csv("./data_raw/iron.csv")

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

rb_clean = clean(rb, "RB")
iron_clean = clean(iron, "IRON")

final = pd.merge(rb_clean, iron_clean, on="date", how="inner").dropna()
final.to_csv("./data_clean/final.csv", index=False)

print("✅ 清洗完成")
print("样本数：", len(final))
print("缺失值：", final.isnull().sum().sum())