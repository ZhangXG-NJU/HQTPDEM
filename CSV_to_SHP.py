# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:10:37 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Point
import fiona

df = pd.read_csv(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl06\02_Raw\atl06_2020.csv")

print('file imported')

geometry = [Point(xy) for xy in zip(df.lon, df.lat)]
crs = {'init': 'epsg:4326'} 
geo_df = GeoDataFrame(df, crs=crs, geometry=geometry)

geo_df.to_file(driver='ESRI Shapefile', filename=r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl06\02_Raw\atl06_2020_GPD.shp")