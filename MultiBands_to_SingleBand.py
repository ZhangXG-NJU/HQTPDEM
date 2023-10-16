# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:29:15 2023

@author: Administrator
"""

import os
from osgeo import gdal, osr

# 设置输入输出文件夹路径
input_folder = r"H:\11112"
output_folder = r"H:\11113"

# 定义空间参考
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)  # WGS84经纬度坐标系

# 遍历输入文件夹中的所有文件
for file_name in os.listdir(input_folder):
    # 检查文件是否是tif文件
    if file_name.endswith(".tif"):
        # 构建输入文件的完整路径
        input_file = os.path.join(input_folder, file_name)

        # 打开tif文件
        dataset = gdal.Open(input_file)

        # 提取每个波段并保存为单波段tif文件
        for band_num in range(1, dataset.RasterCount+1):
            # 构建输出文件的完整路径
            output_file = os.path.join(output_folder, file_name.replace(".tif", f"_B{band_num}.tif"))

            # 提取波段
            band = dataset.GetRasterBand(band_num)
            array = band.ReadAsArray()

            # 创建输出文件
            driver = gdal.GetDriverByName("GTiff")
            output_dataset = driver.Create(output_file, dataset.RasterXSize, dataset.RasterYSize, 1, band.DataType)

            # 将波段写入输出文件
            output_band = output_dataset.GetRasterBand(1)
            output_band.WriteArray(array)

            # 设置输出文件的投影和地理参考
            output_dataset.SetProjection(srs.ExportToWkt())
            output_dataset.SetGeoTransform(dataset.GetGeoTransform())

            # 关闭输出文件
            output_dataset = None

        # 关闭数据集
        dataset = None