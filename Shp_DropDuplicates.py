# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 17:17:02 2023

@author: Administrator
"""

import geopandas as gpd

# 读取shapefile文件
shapefile_path = r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl06+atl08_hagecpd\Merge.shp"
gdf = gpd.read_file(shapefile_path)

# 删除重复的数据行
gdf.drop_duplicates(subset=gdf.columns.drop('geometry'), keep='first', inplace=True)

# 保存去重后的shapefile
output_shapefile_path = r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl06+atl08_hagecpd\Merge2.shp"
gdf.to_file(output_shapefile_path)

print("处理完成，去重后的shapefile已保存为:", output_shapefile_path)