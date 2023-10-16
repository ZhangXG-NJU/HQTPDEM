# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:28:54 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import geopandas as gpd

raw = gpd.read_file(r"E:\Zhang_XinGang\11_QPTDEM\10_Figures\Figure3 Buffer Selection\atl08_2020.shp")
roi = gpd.read_file(r"E:\Zhang_XinGang\11_QPTDEM\10_Figures\Figure3 Buffer Selection\atl08_2021+2022_rebuffer.shp")
print('files imported.')

mask_clip = gpd.clip(raw,roi)
mask_clip = mask_clip[~mask_clip.is_empty]
print('files masked.')

mask_clip.to_file(r"E:\Zhang_XinGang\11_QPTDEM\10_Figures\Figure3 Buffer Selection\atl08_2020_inrebuffer.shp")
print('files saved.')
