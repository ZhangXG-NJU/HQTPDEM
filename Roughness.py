# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:52:23 2023

@author: Zhang_XG, Ph.D, Nanjing Univ.
"""

#算法执行结果正确，但是只能保存为float64类型，改用QGIS实现

import os
os.environ['PROJ_LIB'] = r'C:\ProgramData\Anaconda3\envs\xdemmm\Library\share\proj'
os.environ['GDAL_DATA'] = r'C:\ProgramData\Anaconda3\envs\xdemmm\Library\share'


import xdem
import matplotlib.pyplot as plt

def plot_attribute(attribute, cmap, label=None, vlim=None):

    add_cb = True if label is not None else False

    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)

    if vlim is not None:
        if isinstance(vlim, (int, float)):
            vlims = {"vmin": -vlim, "vmax": vlim}
        elif len(vlim) == 2:
            vlims = {"vmin": vlim[0], "vmax": vlim[1]}
    else:
        vlims = {}

    attribute.show(ax=ax, cmap=cmap, add_cb=add_cb, cb_title=label, **vlims)

    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()

    plt.show()

#path      = r'E:\Zhang_XinGang\11_QPTDEM\03_data\01_aster\06_egm08\aster_egm08.tif'
path      = r'E:\Zhang_XinGang\08_FusionTest\COP30_small.tif'
dem       = xdem.DEM(path)
roughness = xdem.terrain.roughness(dem)

dem.show(cmap='coolwarm_r', cb_title="Elevation change (m)")
plot_attribute(roughness, "Oranges", "Roughness")


# Save to file
roughness.save(r'E:\Zhang_XinGang\08_FusionTest\COP30_small_ROUGHNESS_xdem.tif',dtype='uint16')