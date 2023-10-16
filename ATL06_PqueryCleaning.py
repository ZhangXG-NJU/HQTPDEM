# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:33:30 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import geopandas as gpd
import numpy as np

atl06 = gpd.read_file(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl06\03_main\atl06.shp")
# dropindex = np.where((np.array(atl06['aster_dem'].values) == -9999)| 
#                      (np.array(atl06['h_li_sigma'].values) > 5    )|
#                      (np.array(atl06['cop_dem'].values)   == -9999))

dropindex = np.where (np.array(atl06['h_li_sigma'].values) > 5 )
dropindex = np.array(dropindex).flatten()
atl06     = atl06.drop(index=list(dropindex))

#atl06 = atl06.replace(-9999,0)

atl06.to_file(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl06\03_main\atl06_2.shp")



