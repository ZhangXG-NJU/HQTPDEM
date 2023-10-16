# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:33:30 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import pandas as pd
import numpy as np

atl08     = pd.read_csv(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl08\08_pquery\01_atl08_pquery.csv"
                        ,delimiter=('|'),low_memory=False)
dropindex = np.where((np.array(atl08['aster_dem'].values) == 'None')| 
                     (np.array(atl08['cop_dem'].values)   == 'None'))
dropindex = np.array(dropindex).flatten()
atl08     = atl08.drop(index=list(dropindex))

atl08 = atl08.replace('None',0)

atl08.to_csv(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl08\08_pquery\02_atl08_Clean.csv",index=None)



