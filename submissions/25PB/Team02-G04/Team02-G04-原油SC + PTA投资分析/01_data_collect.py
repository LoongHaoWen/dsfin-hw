import akshare as ak
import pandas as pd
import os

START = "20100101"
END = "20251231"

os.makedirs("./data_raw", exist_ok=True)

# 获取并保存为纯英文列名
def get_fut(symbol):
    df = ak.futures_main_sina(symbol=symbol, start_date=START, end_date=END)
    df.columns = ["date", "open", "high", "low", "close", "volume", "amount", "oi"]
    return df

sc = get_fut("SC0")
pta = get_fut("TA0")

sc.to_csv("./data_raw/sc.csv", index=False)
pta.to_csv("./data_raw/pta.csv", index=False)
print("✅ 数据获取完成（英文列名）")