# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 10:35:46 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import os
os.environ['PROJ_LIB'] = r'C:\ProgramData\Anaconda3\envs\xdemmm\Library\share\proj'
os.environ['GDAL_DATA'] = r'C:\ProgramData\Anaconda3\envs\xdemmm\Library\share'

import xdem
import numpy as np
import datetime

def ntCog(start,end,path_tobeAli,setname):
    
    for i in range(start, end):
        
        try:
            i = str(i)
            print(setname+'_'+i+' started at: ' + str(datetime.datetime.now()))
            
            refpath = r'..\03_data\03_cop30\04_dem_filter_sub\cop30_'+i+'.tif'
            reference_dem = xdem.DEM(refpath)
            print('ref img imported at: '+ str(datetime.datetime.now()))
            
            refdata  = reference_dem.data
            reftrans = reference_dem.transform
            del reference_dem
            
            dem_to_be_aligned = xdem.DEM(path_tobeAli+i+'.tif')
            print('targ img imported at: ' + str(datetime.datetime.now()))
            
            aligdata  = dem_to_be_aligned.data
            aligtrans = dem_to_be_aligned.transform
            aligcrs   = dem_to_be_aligned.crs
            del dem_to_be_aligned
            
            nuth_kaab = xdem.coreg.NuthKaab()
            nuth_kaab.fit(refdata, aligdata, transform=reftrans)
            print('nk coreg fitted at: ' + str(datetime.datetime.now()))
            
            aligned_dem = xdem.DEM.from_array(
            	nuth_kaab.apply(aligdata, transform=aligtrans),transform=aligtrans, crs=aligcrs)
            print('dem aligned at: ' + str(datetime.datetime.now()))
            
            aligned_dem.save(setname+'_LocalCoreged_'+i+'.tif')
            print('dem saved at: ' + str(datetime.datetime.now()))
            
            del refdata,reftrans,aligdata,aligtrans,aligcrs,nuth_kaab,aligned_dem
        
        except: continue
    

#ntCog(19,25,r'..\03_data\01_aster\02_clip_sub\aster_','aster')
#ntCog(1,25,r'..\03_data\02_aw3d30\02_clip_sub\aw3d_','aw3d')
ntCog(6,10,r'..\03_data\04_nasadem\02_clip_sub\nasadem_','nasadem')
#ntCog(1,25,r'..\03_data\05_srtmv3\02_clip_sub\srtm_','srtm')