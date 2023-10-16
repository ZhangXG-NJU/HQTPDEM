import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#读取CSV文件
df = pd.read_csv(r"E:\Zhang_XinGang\11_QPTDEM\04_output\01_ControlPnt\02_3Topos\Topo_1.csv")

def printerr(data, actual, predicted):
    mae = np.mean(np.abs(actual - predicted))
    rmse = np.sqrt(np.mean((actual - predicted)**2))
    mse = np.mean((actual - predicted)**2)
    print(f"{data}: mae = {mae:.2f}, rmse = {rmse:.2f}, mse = {mse:.2f}")

printerr('aster', df['ele_cpnts'].values, df['ele_aster'].values)
printerr('aw3d', df['ele_cpnts'].values, df['ele_aw3d'].values)
printerr('cop', df['ele_cpnts'].values, df['ele_cop'].values)
printerr('tand', df['ele_cpnts'].values, df['ele_tand'].values)
printerr('nasa', df['ele_cpnts'].values, df['ele_nasa'].values)
printerr('srtm', df['ele_cpnts'].values, df['ele_srtm'].values)
printerr('merit', df['ele_cpnts'].values, df['ele_merit'].values)



df = df[df['dif_merit'] <= 150]
df = df[df['dif_merit'] >= -150]
df = df[df['dif_tand'] <= 150]
df = df[df['dif_tand'] >= -150]

#提取误差列
aster = df['dif_aster'].values
aw3d  = df['dif_aw3d' ].values
cop   = df['dif_cop'  ].values
tand  = df['dif_tand' ].values
nasa  = df['dif_nasa' ].values
srtm  = df['dif_srtm' ].values
merit = df['dif_merit'].values

colors = ["#2c7a79", "#b28343", "#ff6600", "#7a54a8", "#0052cc", "#ef9e9f", "#9dc183", "#f3d26f"]
titles = ['ASTER GDEM V3', 'AW3D30 V3.2', 'Copernicus DEM V2.1', 'TanDEM-X', 'NASADEM', 'SRTM V3','MERIT DEM']

#绘制直方图
sns.set_style("whitegrid")
sns.set(font="Microsoft YaHei", font_scale=1.5, style="whitegrid")
fig, axes = plt.subplots(1, 7, figsize=(42, 6))
plt.subplots_adjust(wspace=0.3, hspace=0.4)

for i, err in enumerate([aster, aw3d, cop, tand, nasa, srtm, merit]):
    sns.histplot(x=err, ax=axes[i], bins=1000, stat='density', color=colors[i])
    axes[i].set_title(titles[i], fontsize=23 ,fontweight='bold', pad=10) # 设置子图标题字体大小
    axes[i].set_xlabel('Error (m)', fontsize=22 ,fontweight='bold')        # 设置x轴标签字体大小
    axes[i].set_ylabel('Density', fontsize=22)      # 设置y轴标签字体大小
    axes[i].tick_params(axis='both', labelsize=22)  # 设置刻度标签字体大小和间距
    axes[i].grid(color='gray', linestyle='-', linewidth=1)
    axes[i].spines['top'].set_color('black')
    axes[i].spines['bottom'].set_color('black')
    axes[i].spines['left'].set_color('black')
    axes[i].spines['right'].set_color('black')
    for spine in axes[i].spines.values():
        spine.set_linewidth(2)

#设置所有子图的横纵坐标范围一致
xmin, xmax = -20, 20
ymin, ymax = 0, 0.2
for ax in axes:
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

plt.tight_layout()
plt.savefig('Topo1.png', dpi = 600)
plt.show()
