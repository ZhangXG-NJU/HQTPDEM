# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 19:21:16 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import richdem as rd
from Geotiff_read_write import ReadGeoTiff,GetGeoInfo,CreateGeoTiff

data_arr, Ysize, Xsize = ReadGeoTiff(r"..\03_data\02_aw3d30\05_dem_sub\aw3d_dem_y1_x05.tif")
dem = rd.LoadGDAL(r"..\03_data\02_aw3d30\05_dem_sub\aw3d_dem_y1_x05.tif")

slope = rd.TerrainAttribute(dem, attrib='slope_riserun',zscale = 0.000010986092411341547)