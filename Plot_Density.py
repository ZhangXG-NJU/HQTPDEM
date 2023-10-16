import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import gaussian_kde

df = pd.read_csv(r"E:\Zhang_XinGang\11_QPTDEM\10_FigureV2\Figure Slope Val\06_test.csv")
#df = pd.read_csv(r"E:\Zhang_XinGang\11_QPTDEM\10_FigureV2\Figure Slope Val\13_test.csv")

# Define the labels and titles
x_labels  = ['e_ast', 'e_aw3', 'e_cop', 'e_tan', 'e_nas', 'e_srt', 'e_mrt', 'e_etc']
y_label   = 'cop_slo'
subtitles = ['ASTER GDEM V3', 'AW3D30 V3.2', 'COPDEM', 'TanDEM-X', 'NASADEM', 'SRTM V3', 'MERIT DEM', 'HQTPDEM']

fig, axes = plt.subplots(2, 4, figsize=(12, 8))

# Iterate through the subplots and plot the data
for i, x_label in enumerate(x_labels):
    x = df[x_label].values
    y = df[y_label].values

    # Calculate the point density
    xy = np.vstack([x, y])
    z = gaussian_kde(xy)(xy)

    # Sort the points by density
    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]

    # Set X and Y display ranges
    axes[i // 4, i % 4].set_xlim(-25, 25)  #-25, 25   -130, 130
    axes[i // 4, i % 4].set_ylim(0, 50)    #0, 50  0, 80

    # Scatter plot with density-based colors
    scatter = axes[i // 4, i % 4].scatter(x, y, c=z, cmap='Spectral', s=10, alpha=0.6)

    # Set subplot title
    axes[i // 4, i % 4].set_title(subtitles[i], fontsize=14, fontweight='bold', fontname='Microsoft YaHei')  # Modify font properties

    # Add grid lines
    axes[i // 4, i % 4].grid(True, linestyle='--', alpha=0.5)

    if i % 4 == 0:
        axes[i // 4, i % 4].set_ylabel('Slope (°)', fontsize=12, fontweight='bold', fontname='Microsoft YaHei')

# Add a colorbar
# cbar_ax = fig.add_axes([1, 0.15, 0.02, 0.7])
# cbar = fig.colorbar(scatter, cax=cbar_ax)
# cbar.ax.yaxis.set_tick_params(labelsize=12)  # Modify colorbar font size
# cbar.set_label('Density', fontsize=14, fontweight='bold', fontname='Microsoft YaHei')  # Modify colorbar label font properties

# Set axis labels and modify font properties
for ax in axes.flat:
    ax.set_xlabel('Error (m)', fontsize=12, fontweight='bold', fontname='Microsoft YaHei')
    #ax.set_ylabel('Slope (°)', fontsize=12, fontweight='bold', fontname='Microsoft YaHei')

plt.tight_layout()
plt.savefig('ATL08_Slope2.png', dpi=600)
plt.show()

