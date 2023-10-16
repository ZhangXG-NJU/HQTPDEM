# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:37:31 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""
import re
import os

path = r"E:\Zhang_XinGang\11_QPTDEM\03_data\02_aw3d30\12_asp_sub\\"

num = 1
for file in os.listdir(path):
    
    s = re.split('\_|\.',file)
    
    os.rename(os.path.join(path,file),path+'\\'+s[0]+'_'+s[1]+'_y'+str(int(s[3])+1)+'_x'+str(int(s[2])+1).zfill(2)+'.tif')
    num = num + 1