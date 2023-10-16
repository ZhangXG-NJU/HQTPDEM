# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 23:08:45 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import geopandas as gpd

Base  = gpd.read_file(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl08\02_csv\atl08_2021_ReBuffer.shp")
print('Union imported.')

Buffer = gpd.read_file(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl08\02_csv\atl08_2021_1kmBuffer.shp")
print('Buffer imported.')

ReBuffer = Base.symmetric_difference(Buffer, align=True)

ReBuffer.to_file(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl08\02_csv\atl08_2021_1km_ReBuffer.shp.shp")
print('file saved.')

