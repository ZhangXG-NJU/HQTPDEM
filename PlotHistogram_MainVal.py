import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#读取CSV文件
df = pd.read_csv(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl06\07_Pquery\13_test.csv")
#df = pd.read_csv(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl08\07_Pquery\06_test.csv")

#提取误差列
errors = {
    'ASTER GDEM V3': (df['ast_bl'].values - df['lidar'].values),
    'AW3D30 V3.2'  : (df['aw3_bl'].values - df['lidar'].values),
    'COPDEM'       : (df['cop_bl'].values - df['lidar'].values),
    'TanDEM-X'     : (df['tan_bl'].values - df['lidar'].values),
    'NASADEM'      : (df['nas_bl'].values - df['lidar'].values),
    'SRTM V3'      : (df['srt_bl'].values - df['lidar'].values),
    'MERIT DEM'    : (df['mrt_bl'].values - df['lidar'].values),
    'HQTPDEM'      : (df['etc_bl'].values - df['lidar'].values)
}

colors = ["#2c7a79", "#b28343", "#ff6600", "#7a54a8", "#0052cc", "#ef9e9f", "#f3d26f", "#009900"]
titles = list(errors.keys())

# 绘制直方图
sns.set_style("whitegrid")
sns.set(font="Microsoft YaHei", font_scale=1.5, style="whitegrid")
fig, axes = plt.subplots(2, 4, figsize=(18, 9))  # Two rows, four columns
plt.subplots_adjust(wspace=0.3, hspace=0.4)

for i, (title, err) in enumerate(errors.items()):
    row = i // 4  # Determine the row for the subplot
    col = i % 4   # Determine the column for the subplot
    sns.histplot(x=err, ax=axes[row, col], bins='auto', stat='count', color=colors[i], binwidth=1)  #binwidth=1 0.2
    axes[row, col].set_title(titles[i], fontsize=20, fontweight='bold', pad=10)
    axes[row, col].set_xlabel('Error (m)', fontsize=19, fontweight='bold')
    axes[row, col].set_ylabel('ATL06 Point Number', fontsize=19, fontweight='bold') #ATL06 8
    axes[row, col].tick_params(axis='both', labelsize=19)
    axes[row, col].grid(color='lightgray', linestyle='-', linewidth=1)
    axes[row, col].spines['top'].set_color('black')
    axes[row, col].spines['bottom'].set_color('black')
    axes[row, col].spines['left'].set_color('black')
    axes[row, col].spines['right'].set_color('black')
    for spine in axes[row, col].spines.values():
        spine.set_linewidth(2)
    
    # Hide y-axis labels and ticks for all subplots except the leftmost ones
    if col != 0:
        axes[row, col].tick_params(axis='y', which='both', left=False, labelleft=False)
        axes[row, col].set_ylabel('')
    
    axes[row, col].set_xticks(np.arange(-30, 30.1, 10)) #-30, 30.1, 10   -6, 6.01, 3

# Set the same x and y limits for all subplots
xmin, xmax = -35, 35  #-35, 35    -6.5, 6.5
ymin, ymax = 0, 6500  #6500    11300
for ax in axes.flat:
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

# Adjust the layout and save the plot
plt.tight_layout()
plt.savefig('atl06.svg') #ATL06
plt.show()