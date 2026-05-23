import akshare as ak
import pandas as pd
import os

START = "20100101"
END = "20251231"

os.makedirs("./data_raw", exist_ok=True)

def get_fut(symbol):
    df = ak.futures_main_sina(symbol=symbol, start_date=START, end_date=END)
    df.columns = ["date", "open", "high", "low", "close", "volume", "amount", "oi"]
    return df

rb = get_fut("RB0")
i = get_fut("I0")

rb.to_csv("./data_raw/rb.csv", index=False)
i.to_csv("./data_raw/iron.csv", index=False)
print("✅ 螺纹钢 & 铁矿石数据获取完成（英文列名）")