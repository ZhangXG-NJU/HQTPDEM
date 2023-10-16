# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 11:18:06 2023

@author: Zhang_XG, Ph.D Cand., Nanjing Univ.
"""

import pandas as pd
import h5py
import os
import numpy as np
 
 
def read_atl08(fname):
    # Each beam is a group, strong beams are selected only here
    groups = ['/gt1l', '/gt2l', '/gt3l','/gt1r', '/gt2r', '/gt3r']
    
    # Loop trough beams
    for k, g in enumerate(groups):
        
        try:

            with h5py.File(fname, 'r') as fi:
                # Define the variables and construction, open the h5 files and check it out
                time        = fi[g + '/land_segments/delta_time'][:]
                lat         = fi[g + '/land_segments/latitude'][:]
                lon         = fi[g + '/land_segments/longitude'][:]
                dem         = fi[g + '/land_segments/terrain/h_te_best_fit'][:]
                dem_uncert  = fi[g + '/land_segments/terrain/h_te_uncertainty'][:]
                cnpy        = fi[g + '/land_segments/canopy/h_canopy'][:]
                cnpy_uncert = fi[g + '/land_segments/canopy/h_canopy_uncertainty'][:]
                group       = np.full((lat.shape[0],1),g)
            
            result = pd.DataFrame()

            result['time']        = time
            result['lon']         = lon
            result['lat']         = lat
            result['dem']         = dem
            result['dem_uncert']  = dem_uncert
            result['cnpy']        = cnpy
            result['cnpy_uncert'] = cnpy_uncert
            result['group']       = group
            
            
            # Filter the data
            dropindex = np.where((np.array(result['dem'].values) > 9000) | 
                                 (np.array(result['dem'].values) < -422) | 
                                 (np.array(result['dem_uncert'].values) >5))
            dropindex = np.array(dropindex).flatten()
            result = result.drop(index=list(dropindex))
            ofilecsv = fname.replace('.h5', '_' + g[1:] + '.csv')
            print('out ->', ofilecsv)
            result.to_csv(ofilecsv, index=None)
        except: continue
 
def readMultiH5(dir):
    # Iterate the dir, deal with all h5 files
    # For root_dir, sub_dir, files in os.walk(r'' + dir):
    for root_dir, sub_dir, files in os.walk(dir):
        for file in files:
            if file.endswith('h5'):
                # Absolute path
                file_name = os.path.join(root_dir, file)
                read_atl08(file_name)
 
 
readMultiH5(r"E:\Zhang_XinGang\29_OpenFund\04_Data\atl08\5000004402308\\")
