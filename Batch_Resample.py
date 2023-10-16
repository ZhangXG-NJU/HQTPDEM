# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:07:47 2023

@author: Administrator
"""

from osgeo import gdal, osr
import os

# 输入和输出文件夹路径
input_folder = r"E:\Zhang_XinGang\11_QPTDEM\09_valid_data\04_Crop"
output_folder = r"E:\Zhang_XinGang\11_QPTDEM\09_valid_data\05_Resample"

# 目标分辨率
target_res = 0.00004629629   #约5m分辨率

# 定义目标投影坐标系
dst_srs = osr.SpatialReference()
dst_srs.ImportFromEPSG(4326)

# 循环遍历输入文件夹中的所有DEM文件
for filename in os.listdir(input_folder):
    if filename.endswith(".tif"):
        # 打开DEM文件
        input_path = os.path.join(input_folder, filename)
        ds = gdal.Open(input_path)

        # 获取原始分辨率
        src_res = ds.GetGeoTransform()[1]

        # 计算重采样因子
        res_factor = int(src_res / target_res)

        # 设置输出文件名和路径
        output_path = os.path.join(output_folder, filename)

        # 进行重采样
        gdal.Warp(output_path, ds, xRes=target_res, yRes=target_res, resampleAlg='bilinear',
                  dstSRS=dst_srs.ExportToWkt(), creationOptions=['COMPRESS=LZW'])

        print(f"{filename} 重采样完成")

print("全部重采样完成")