# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:52:36 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import h5py
import pandas as pd
import numpy as np

path = r"F:\hagecpd\HAGECPD.mat"
data = h5py.File(path)

Elevation      = np.transpose(data['LJ_FProduct/Elevation'][:])
GElevation     = np.transpose(data['LJ_FProduct/GElevation'][:])
ID             = np.transpose(data['LJ_FProduct/ID'][:])
Lat            = np.transpose(data['LJ_FProduct/Lat'][:])
Lon            = np.transpose(data['LJ_FProduct/Lon'][:])
PeakNumber     = np.transpose(data['LJ_FProduct/PeakNumber'][:])
Shot           = np.transpose(data['LJ_FProduct/Shot'][:])
Time           = np.transpose(data['LJ_FProduct/Time'][:])
TopographyType = np.transpose(data['LJ_FProduct/TopographyType'][:])

result = pd.DataFrame()

result['Elevation']      = np.squeeze(Elevation)
result['GElevation']     = np.squeeze(GElevation)
result['ID']             = np.squeeze(ID)
result['Lat']            = np.squeeze(Lat)
result['Lon']            = np.squeeze(Lon)
result['PeakNumber']     = np.squeeze(PeakNumber)
result['Shot']           = np.squeeze(Shot)
result['Time']           = np.squeeze(Time)
result['TopographyType'] = np.squeeze(TopographyType)

# Filter the data
dropindex = np.where((np.array(result['Lat'].values) >  45)| 
                     (np.array(result['Lat'].values) <  25)| 
                     (np.array(result['Lon'].values) > 105)|                               
                     (np.array(result['Lon'].values) <  63))
dropindex = np.array(dropindex).flatten()
result = result.drop(index=list(dropindex))

ofilecsv = path.replace('.mat', '.csv')
print('out ->', ofilecsv)
result.to_csv(ofilecsv, index=None)
