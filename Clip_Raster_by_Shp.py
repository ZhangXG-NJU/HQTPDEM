# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 22:13:10 2023

@author: Administrator
"""

import os
import rasterio
from rasterio.mask import mask
import geopandas as gpd
from fiona.crs import from_epsg

def crop_dem(dem_path, shapefile_path, output_path, compress=True):
    # 读取shapefile
    gdf = gpd.read_file(shapefile_path)

    # 确保shapefile的坐标系统与DEM一致
    #gdf = gdf.to_crs(from_epsg(4326))

    # 读取DEM数据
    with rasterio.open(dem_path) as src:
        out_image, out_transform = mask(src, gdf.geometry,crop=True,nodata=-9999)
        out_meta = src.meta.copy()
        out_image[out_image < -9999] = -9999

    # 更新元数据
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform,
                     "dtype": 'int16',  #uint8   float32  int16
                     "nodata": -9999})  #-9999   0

    # 是否压缩
    if compress:
        out_meta.update(compress='LZW')

    # 写入新的Raster文件
    with rasterio.open(output_path, "w", **out_meta) as dest:
        dest.write(out_image)

# 单个裁剪V1
dem_path = r"E:\Zhang_XinGang\11_QPTDEM\03_data\cop\cop_dem_270m_slo.tif"
roi_path = r"E:\Zhang_XinGang\11_QPTDEM\02_bound\13_RGI\03_main\03_RGI_Buffer.shp"
out_path = r"E:\Zhang_XinGang\11_QPTDEM\03_data\cop\cop_dem_270m_slo_RGI.tif"
crop_dem(dem_path, roi_path, out_path, compress=True)

# =============================================================================
# # 单个裁剪V2
# a = '02'  
# dem_path = r"F:\SRTM V3\04_coreg\srtm_egm08_coreg.tif"
# roi_path = f"E:/Zhang_XinGang/11_QPTDEM/09_valid_data/10_clip/A{a}/bound/Bound_A{a}.shp"
# out_path = f"E:/Zhang_XinGang/11_QPTDEM/09_valid_data/10_clip/A{a}/dem/A{a}_srt.tif"
# crop_dem(dem_path, roi_path, out_path, compress=True)
# =============================================================================

# =============================================================================
# # 批量裁剪
# dem_path = r"E:\Zhang_XinGang\11_QPTDEM\04_output\Archieve\ET_Main_Gaus075_Correct.tif"
# rois     = r"E:\Zhang_XinGang\11_QPTDEM\02_bound\15_output_grids"
# out_fold = r"E:\Zhang_XinGang\11_QPTDEM\04_output\Archieve\sub"
# 
# for roi in os.listdir(rois):
#     if roi.endswith(".shp"):
#         out_name = "HQTPDEM_" + os.path.splitext(roi)[0] + ".tif"  # 将扩展名更改为.tif
#         out_path = os.path.join(out_fold, out_name)
#         crop_dem(dem_path, os.path.join(rois, roi), out_path, compress=True)
#         print(roi)
# =============================================================================
