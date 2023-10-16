# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:25:45 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""


import numpy as np
import pandas as pd
import glob
import re
from tqdm import tqdm


dirpath = r'E:\Zhang_XinGang\29_OpenFund\04_Data\atl08\5000004402308\\'

csv_list = glob.glob(dirpath + '*.csv')
print('共发现%s个CSV文件'% len(csv_list))
for i in tqdm(csv_list):
    fr = open(i,'r',encoding='utf-8').read()
    with open(r'E:\Zhang_XinGang\29_OpenFund\04_Data\atl08\5000004402308\atl08.csv','a',encoding='utf-8') as f:
        f.write(fr)
print('合并完毕！')  

df = pd.read_csv(r'E:\Zhang_XinGang\29_OpenFund\04_Data\atl08\5000004402308\atl08.csv')
df = df.drop_duplicates(keep=False)
print('去重完毕！')
df.to_csv(r'E:\Zhang_XinGang\29_OpenFund\04_Data\atl08\5000004402308\atl082.csv',index=False,encoding="utf-8")