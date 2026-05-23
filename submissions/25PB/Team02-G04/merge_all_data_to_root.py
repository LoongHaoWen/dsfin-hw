# -*- coding: utf-8 -*-
"""
自动把 4 个中文命名子文件夹的 data/ 复制到 根目录 data/
Team02-G04 一键合并数据脚本
"""
import os
import shutil

# 根目录 data
ROOT_DATA = "./data"

# 适配你当前的【中文文件夹名】，直接复制使用
SUB_FOLDERS = [
    "Team02-G04-原油SC + PTA投资分析",
    "Team02-G04-螺纹钢RB、铁矿石I投资分析",
    "Team02-G04-碳酸锂期货LC投资分析",
    "Team02-G04-黄金现货投资分析"
]

# 安全创建根目录data（已存在不报错）
if not os.path.exists(ROOT_DATA):
    os.makedirs(ROOT_DATA)

# 遍历复制每个子文件夹的data文件
for sub in SUB_FOLDERS:
    src_data_path = os.path.join(sub, "data")
    if not os.path.exists(src_data_path):
        print(f"⚠️  跳过：{src_data_path} 文件夹不存在")
        continue

    # 遍历data内所有文件
    for file_name in os.listdir(src_data_path):
        src_file = os.path.join(src_data_path, file_name)
        dst_file = os.path.join(ROOT_DATA, file_name)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)
            print(f"✅ 已复制：{src_file} → {dst_file}")

print("\n🎉 全部合并完成！根目录data已包含所有子板块数据")