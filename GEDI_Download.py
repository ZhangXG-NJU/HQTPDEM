# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 11:22:50 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

from pyGEDI import *

username='Zhang_XG'
password='XXX'

session=sessionNASA(username,password)

ul_lat= 25
ul_lon= 63
lr_lat= 45
lr_lon= 64

bbox=[ul_lat,ul_lon,lr_lat,lr_lon]

product_2A = 'GEDI02_A'
version    = '002'
outdir_2A  = '../03_data/GEDI_L2A/'+product_2A+'.'+version+'/'

gediDownload(outdir_2A,product_2A,version,bbox,session)