# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:59:07 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import os
from osgeo import gdal


def get_file_size(file_path):
    """获取文件占空间所少M"""
    fsize = os.path.getsize(file_path)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)


def progress(percent, msg, tag):
    """进度回调函数"""
    print(percent, msg, tag)


def compress(path, target_path):
    """使用gdal进行文件压缩"""
    dataset = gdal.Open(path)
    driver = gdal.GetDriverByName('GTiff')
    driver.CreateCopy(target_path, dataset, strict=1, options=["TILED=YES", "COMPRESS=LZW"])
    # strict=1表示和原来的影像严格一致，0表示可以有所调整
    # callback为进度回调函数
    # PACKBITS快速无损压缩，基于流
    # LZW针对像素点，黑白图像效果好
    del dataset

def getFilePathes(Folder):
    M_files = os.listdir(Folder)
    Files_List = []
    for items in M_files:
        if os.path.splitext(items)[1] == '.tif':
            Files_List.append(Folder+items)
    return Files_List

Path = r"H:\04_output\01_王卓第一次训练\ExtraTree9\\"
Files_List = getFilePathes(Path)

for f in Files_List:

    print(f)
    print("处理前", str(get_file_size(f)) + "MB")
    compress(f, f+"_cmp.tif")
    print("处理后", str(get_file_size(f+"_cmp.tif")) + "MB") 
    #os.remove(f)

