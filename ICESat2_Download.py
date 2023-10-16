# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 10:36:13 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import icepyx as ipx
import os
import shutil

for i in range(31,32):  #21-35
    try:
        E = i*3
        earthdata_uid = 'Zhang_XG'
        email = 'DG21270060@smail.nju.edu.cn'
        short_name = 'ATL06'
        date_range = ['2020-06-01','2020-11-01']
        
        spatial_extent = [E, 25, E+3, 45]
        region_a = ipx.Query(short_name, spatial_extent, date_range)
        #region_a.visualize_spatial_extent()
        
        #print(region_a.product)
        #print(region_a.product_version)
        #print(region_a.product_summary_info())
        #print(region_a.latest_version())
        print(region_a.avail_granules())
        #print(region_a.granules.avail)
        
        region_a.earthdata_login(earthdata_uid, email)
        region_a.order_granules()
        region_a.granules.orderIDs
        path = '../03_data/atl06/2020_N25-45_E'+str(E)+'-'+str(E+3)+'/'
        region_a.download_granules(path)
        
    except: continue

