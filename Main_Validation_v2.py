# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:50:37 2023

@author: Administrator
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 读取CSV文件，保留DEMs
df = pd.read_csv(r"E:\Zhang_XinGang\11_QPTDEM\10_FigureV2\Figure Slope Val\ATL08_0-5.csv")

# 创建度量函数
def evaluate_metrics(target, predictions, label):
    mae = mean_absolute_error(target, predictions)
    rmse = np.sqrt(mean_squared_error(target, predictions))
    r2 = r2_score(target, predictions)
    
    # 使用字符串格式化保留小数点后三位
    mae_str = f'{mae:.2f}'
    rmse_str = f'{rmse:.2f}'
    r2_str = f'{r2:.10f}'
    
    return f'{label} MAE: {mae_str}  RMSE: {rmse_str}  R2: {r2_str}'


# bilinear度量
bl_columns = ['ast_bl', 'aw3_bl', 'cop_bl', 'tan_bl', 'nas_bl', 'srt_bl', 'mrt_bl', 'etc_bl']
for column in bl_columns:
    print(evaluate_metrics(df['lidar'], df[column], column))