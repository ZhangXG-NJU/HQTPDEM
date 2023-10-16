# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:23:21 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import richdem as rd
import numpy as np

beau = rd.LoadGDAL(r'E:\Zhang_XinGang\08_FusionTest\COP30.tif',no_data=-9999)

slope = rd.TerrainAttribute(beau, attrib='slope_riserun',zscale = 0.000010391473527418842)
rd.rdShow(slope, axes=False, cmap='jet', figsize=(8,5.5))