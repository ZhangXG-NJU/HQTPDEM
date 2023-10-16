# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 11:18:06 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import pandas as pd
import h5py
import os
import numpy as np
 
 
def read_atl06(fname):
    # Each beam is a group, strong beams are selected only here
    groups = ['/gt1l', '/gt2l', '/gt3l','/gt1r', '/gt2r', '/gt3r']
    
    # Loop trough beams
    for k, g in enumerate(groups):
        try:
            with h5py.File(fname, 'r') as fi:
                # Define the variables and construction, open the h5 files and check it out
                lat         = fi[g + '/land_ice_segments/latitude'][:]
                lon         = fi[g + '/land_ice_segments/longitude'][:]
                h_li        = fi[g + '/land_ice_segments/h_li'][:]
                h_li_sigma  = fi[g + '/land_ice_segments/h_li_sigma'][:]
                q_flag      = fi[g + '/land_ice_segments/atl06_quality_summary'][:]
                delta_time  = fi[g + '/land_ice_segments/delta_time'][:]
                dh_fit_dx   = fi[g + '/land_ice_segments/fit_statistics/dh_fit_dx'][:]
                dh_fit_dy   = fi[g + '/land_ice_segments/fit_statistics/dh_fit_dy'][:]                
                group       = np.full((lat.shape[0],1),g)
            
            result = pd.DataFrame()

            result['lon']        = lon
            result['lat']        = lat
            result['h_li']       = h_li
            result['h_li_sigma'] = h_li_sigma
            result['q_flag']     = q_flag
            result['delta_time'] = delta_time
            result['dh_fit_dx']  = dh_fit_dx
            result['dh_fit_dy']  = dh_fit_dy            
            result['group']      = group
            
            # Filter the data
            dropindex = np.where((np.array(result['h_li'].values) > 8850) | 
                                 (np.array(result['h_li'].values) < -422) | 
                                 (np.array(result['q_flag'].values) == 0) )
            dropindex = np.array(dropindex).flatten()
            result = result.drop(index=list(dropindex))
            ofilecsv = fname.replace('.h5', '_' + g[1:] + '.csv')
            #print('out ->', ofilecsv)
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
                read_atl06(file_name)
 

root_dir = r'E:\Zhang_XinGang\11_QPTDEM\03_data\atl06\2020_N25-45_E69-72'
readMultiH5(root_dir)
print('done')


