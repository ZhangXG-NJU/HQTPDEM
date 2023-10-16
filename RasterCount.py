# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:35:39 2023

@author: Administrator
"""

from osgeo import gdal
import numpy as np

# 打开GeoTIFF文件
file_path = r"E:\Zhang_XinGang\11_QPTDEM\03_data\wcv\resample\wcv_resample_withRGI.tif"
dataset = gdal.Open(file_path)

if dataset is None:
    print("无法打开GeoTIFF文件")
    exit()

# 读取GeoTIFF文件中的数据
band = dataset.GetRasterBand(1)  # 假设你处理的是第一个波段
data = band.ReadAsArray().astype('float64')
print('File imported.')

# 定义要统计的像元值列表
values_to_count = ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 100, 110])

# 初始化一个字典来存储像元值的数量
value_counts = {value: 0 for value in values_to_count}

# 统计像元值的数量
for value in values_to_count:
    value_counts[value] = np.sum(data == value)
    print(f"值 {value} 的像元数量：{value_counts[value]}")

# 关闭数据集
dataset = None