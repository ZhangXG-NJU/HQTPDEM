# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:54:18 2023

@author: Administrator
"""
import warnings
warnings.filterwarnings("ignore")

import os
import geopandas as gpd
import numpy as np

shp_dir = r"F:\gedi_l2a\02_raw\3601_3700"
out_dir = shp_dir

# Get a list of all shapefiles in the directory
shp_list = [file for file in os.listdir(shp_dir) if file.endswith('.shp')]

for shp_file in shp_list:
    # Read the shapefile into a GeoDataFrame
    data = gpd.read_file(os.path.join(shp_dir, shp_file))

    # Filter the data based on sensitivity > 0.95
    sensitive_data = data[data['senstiv'] > 0.96]
    sensitive_data = sensitive_data[sensitive_data['ele_bflag'] == 0]
    sensitive_data = sensitive_data[sensitive_data['dgrd_flag']  == 0]

    # Delete unnecessary columns
    cols_to_drop = ['q_flag', 'ele_bflag', 'dgrd_flag']
    sensitive_data.drop(columns=cols_to_drop, inplace=True)

    # Delete points where the absolute difference between ele_low and ele_high is greater than 10
    ele_diff = np.abs(sensitive_data['ele_low'] - sensitive_data['ele_high'])
    sensitive_data = sensitive_data[ele_diff <= 10]

    # Delete points where the absolute difference between dem and ele_low is greater than 70
    dem_ele_diff = np.abs(sensitive_data['dem'] - sensitive_data['ele_low'])
    sensitive_data = sensitive_data[dem_ele_diff <= 70]

    # Check if the filtered data is empty
    if len(sensitive_data) == 0:
        # If it is empty, delete the shapefile and its associated files
        prefix = os.path.splitext(shp_file)[0]
        for ext in ['cpg','fix','shp', 'shx', 'dbf', 'prj']:
            os.remove(os.path.join(shp_dir, f"{prefix}.{ext}"))
    else:
        # If it is not empty, write the filtered data to a new shapefile
        out_file = os.path.join(out_dir, shp_file)
        sensitive_data.to_file(out_file, driver='ESRI Shapefile')

        # Print the number of features in the original and filtered shapefiles
        print(f"Original: {len(data)} features. Filtered: {len(sensitive_data)} features.")
