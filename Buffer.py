# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:57:22 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import geopandas as gpd

raw  = gpd.read_file(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl06\02_Raw\atl06_2021+2022.shp")
print('files imported.')


#Buffer
buff = raw.buffer(0.010986092411341547,resolution=4)
buff = gpd.GeoDataFrame(crs=4326,geometry=buff)
print('Buffer Created.')

dissolved = buff.dissolve()
print('Dissolved.')

dissolved.to_file(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl06\02_Raw\atl06_2021+2022_Buffer.shp")
print('Buffer file saved.')


#Rebuffer
print('*******Rebuffer********')

Base     = gpd.read_file(r"E:\Zhang_XinGang\11_QPTDEM\02_bound\5_Union\Union.shp")
ReBuffer = Base.symmetric_difference(dissolved, align=True)
ReBuffer.to_file(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl06\02_Raw\atl06_2021+2022_ReBuffer.shp")
print('file saved.')






