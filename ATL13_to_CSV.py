# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 11:18:06 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import pandas as pd
import h5py
import os
import numpy as np
 
 
def read_atl13(fname):
    # Each beam is a group, strong beams are selected only here
    groups = ['/gt1l', '/gt2l', '/gt3l','/gt1r', '/gt2r', '/gt3r']
    
    # Loop trough beams
    for k, g in enumerate(groups):
        try:
            with h5py.File(fname, 'r') as fi:
                # Define the variables and construction, open the h5 files and check it out
                lat         = fi[g + '/segment_lat'][:]
                lon         = fi[g + '/segment_lon'][:]
                ht_ortho    = fi[g + '/ht_ortho'][:]
                ht_watsurf  = fi[g + '/ht_water_surf'][:]
                qf_bckgrd   = fi[g + '/qf_bckgrd'][:]
                qf_bias_em  = fi[g + '/qf_bias_em'][:]
                qf_bias_fit = fi[g + '/qf_bias_fit'][:]
                stdev_wtsf  = fi[g + '/stdev_water_surf'][:]
                delta_time  = fi[g + '/delta_time'][:]
                err_watsurf = fi[g + '/err_ht_water_surf'][:]
                group       = np.full((lat.shape[0],1),g)
            
            result = pd.DataFrame()

            result['lon']         = lon
            result['lat']         = lat
            result['ht_ortho']    = ht_ortho
            result['ht_watsurf']  = ht_watsurf
            result['qf_bckgrd']   = qf_bckgrd
            result['qf_bias_em']  = qf_bias_em
            result['qf_bias_fit'] = qf_bias_fit
            result['stdev_wtsf']  = stdev_wtsf
            result['delta_time']  = delta_time        
            result['err_watsurf'] = err_watsurf
            result['group']       = group
            
            # Filter the data
            dropindex = np.where((np.array(result['ht_ortho'].values)    > 8850)| 
                                 (np.array(result['ht_ortho'].values)    < -422)| 
                                 #(np.array(result['err_watsurf'].values) >  100)|
                                 (np.array(result['qf_bckgrd'].values)   ==   0)|
                                 (np.array(result['qf_bias_em'].values)  ==   3)|
                                 (np.array(result['qf_bias_em'].values)  ==  -3)|
                                 (np.array(result['qf_bias_fit'].values) ==   3)|
                                 (np.array(result['qf_bias_fit'].values) ==  -3)|                                 
                                 (np.array(result['stdev_wtsf'].values)  >    2))
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
                read_atl13(file_name)
 
 

readMultiH5(r'F:\03_data_Archieve\atl13\01_raw\2021')
print('done')

