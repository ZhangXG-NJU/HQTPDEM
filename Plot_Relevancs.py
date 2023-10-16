# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 20:26:29 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

import numpy as np
import pandas as pd

file = r"E:\Zhang_XinGang\11_QPTDEM\11_testdata\Atl08_Pquery.csv"
data = pd.read_csv(file)

data.plot(kind = 'scatter',x = 'diff_cop', y = 'diff_nasa',alpha=0.05,s = 1)