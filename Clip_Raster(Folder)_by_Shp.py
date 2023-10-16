# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 01:42:53 2023

@author: Administrator
"""

import glob
import os
import rasterio
from rasterio.mask import mask
import geopandas as gpd
from fiona.crs import from_epsg

def crop_dems_in_folder(dem_folder, roi_path, output_folder, compress=True):
    # 读取shapefile
    gdf = gpd.read_file(roi_path)

    # 确保shapefile的坐标系统与DEM一致
    #gdf = gdf.to_crs(from_epsg(4326))

    # 获取DEM文件列表
    dem_files = glob.glob(os.path.join(dem_folder, '*.tif'))

    for dem_path in dem_files:
        
        try:
            # 设置输出文件路径
            out_path = os.path.join(output_folder, os.path.basename(dem_path))
    
            # 读取DEM数据
            with rasterio.open(dem_path) as src:
                out_image, out_transform = mask(src, gdf.geometry,crop=True,nodata=-9999)
                out_meta = src.meta.copy()
    
            # 更新元数据
            out_meta.update({"driver": "GTiff",
                             "height": out_image.shape[1],
                             "width": out_image.shape[2],
                             "transform": out_transform,
                             "dtype": 'float32',
                             "nodata": -9999})
    
            # 是否压缩
            if compress:
                out_meta.update(compress='LZW')
    
            # 写入新的Raster文件
            with rasterio.open(out_path, "w", **out_meta) as dest:
                dest.write(out_image)
            print(os.path.basename(dem_path)+' cliped.')
        except:
            print('***'+os.path.basename(dem_path)+' Failed.***')
            continue

# 示例使用
dem_folder = r"E:\Zhang_XinGang\11_QPTDEM\04_output\XGBoost_ATL06"
roi_path = r"E:\Zhang_XinGang\11_QPTDEM\02_bound\13_RGI\03_main\03_RGI_Buffer.shp"
output_folder = r"E:\Zhang_XinGang\11_QPTDEM\04_output\XGBoost_ATL06_Clip"

crop_dems_in_folder(dem_folder, roi_path, output_folder, compress=True)