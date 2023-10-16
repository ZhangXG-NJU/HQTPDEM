# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:43:30 2023

@author: Administrator
"""

import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Open the DEM file using GDAL
dem_file = r"E:\Zhang_XinGang\11_QPTDEM\02_bound\10_DEM_Base\DEM_Base.tif"
ds = gdal.Open(dem_file)

# Get the elevation data as a NumPy array
elevation_array = ds.ReadAsArray()

# Create a meshgrid of the X and Y coordinates
x_size = ds.RasterXSize
y_size = ds.RasterYSize
x_range = np.arange(0, x_size)
y_range = np.arange(0, y_size)
x_coords, y_coords = np.meshgrid(x_range, y_range)

# Plot the DEM as a 3D surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x_coords, y_coords, elevation_array, cmap='terrain', linewidth=0, antialiased=False)

# Set the axis labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Elevation')
ax.set_xlim([0, x_size])
ax.set_ylim([0, y_size])
ax.set_zlim([np.min(elevation_array), np.max(elevation_array)])

# Add a colorbar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Save the figure
plt.savefig(r"E:\Zhang_XinGang\11_QPTDEM\02_bound\10_DEM_Base\DEM_Base111.tif")

# Show the figure
plt.show()