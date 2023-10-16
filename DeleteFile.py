# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 23:24:01 2022

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import os

aster_files  = os.listdir(r'F:\01_aster\00_raw\dem\\')
aster_LonLat = []

todel_files  = os.listdir(r'E:\Zhang_XinGang\11_QPTDEM\04_output\Archieve\sub\\')
todel_LonLat = []

for f in aster_files:
    f = f.split("V003_")
    try:
        f = f[1].split("_dem")
        aster_LonLat.append(f[0])
    except:
        continue

# =============================================================================
# for f in todel_files:
#     f = f.split("MLC30_")
#     try:
#         f = f[1].split("_MSK.tif")
#         todel_LonLat.append(f[0])
#     except:
#         continue
# =============================================================================

for f in todel_files:
    try:
        f = f.split("PDEM_")
        todel_LonLat.append(f[0])
    except:
        continue

for ll_aw in todel_LonLat:
    if(ll_aw in aster_LonLat):
        continue
    else:
        os.remove(r'E:\Zhang_XinGang\07_PT_DEM\FABDEM\\'+ll_aw+'_FABDEM_V1-0.tif')
    