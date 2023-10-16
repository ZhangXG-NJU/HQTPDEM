import sys 
sys.path.append("..")

import os
os.environ['PROJ_LIB'] = r"C:\ProgramData\Anaconda3\Lib\site-packages\osgeo\data\proj"

import pandas as pd
import rasterio as rio
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from Geotiff_read_write import ReadGeoTiff, GetGeoInfo, CreateGeoTiff

# 读取CSV文件
df = pd.read_csv(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl06\07_Pquery\02A_Main_data_2times.csv")
df = shuffle(df).iloc[:, :]
print(df.columns)

# 分离 X 和 Y
X = df.iloc[:, 3:]
Y = df.iloc[:, 2]

et = ExtraTreesRegressor(n_estimators=200,n_jobs=-1)  #Attention!!!

# 划分训练集和测试集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=42)

# 训练模型
et.fit(X_train, Y_train)

# 预测并计算 MAE、RMSE、MSE
y_pred = et.predict(X_test)
mae = mean_absolute_error(Y_test, y_pred)
rmse = mean_squared_error(Y_test, y_pred, squared=False)

# 输出结果
print(f"Best Params: {et.get_params()}, MAE: {mae}, RMSE: {rmse}")

#将Geotiff读取并转为一维数组
def flat_tiff(file_path, band_num=1):
    with rio.open(file_path) as src:
        bandflatten = src.read(band_num).flatten()
    return bandflatten

#获取X值并获取GeoT等必要信息
def getSeries(x, y):
    x = str(x).zfill(2)
    y = str(y)
    XsMat = pd.DataFrame()
    #DEM
    XsMat['aw3d_dem']   = flat_tiff(f"../../03_data/aw3d/dem_sub/aw3d_dem_y{y}_x{x}.tif")
    XsMat['cop_dem']    = flat_tiff(f"../../03_data/cop/dem_sub/cop_dem_y{y}_x{x}.tif")
    XsMat['tan_dem']    = flat_tiff(f"../../03_data/tan/dem_sub/tan_dem_y{y}_x{x}.tif")
    XsMat['nasa_dem']   = flat_tiff(f"../../03_data/nasa/dem_sub/nasa_dem_y{y}_x{x}.tif")
    #SLO
    XsMat['aw3d_slo']   = flat_tiff(f"../../03_data/aw3d/slo_sub/aw3d_slo_y{y}_x{x}.tif")
    XsMat['cop_slo']    = flat_tiff(f"../../03_data/cop/slo_sub/cop_slo_y{y}_x{x}.tif")
    XsMat['tan_slo']    = flat_tiff(f"../../03_data/tan/slo_sub/tan_slo_y{y}_x{x}.tif")
    XsMat['nasa_slo']   = flat_tiff(f"../../03_data/nasa/slo_sub/nasa_slo_y{y}_x{x}.tif")
    #ASP
    XsMat['aw3d_asp']   = flat_tiff(f"../../03_data/aw3d/asp_sub/aw3d_asp_y{y}_x{x}.tif")
    XsMat['cop_asp']    = flat_tiff(f"../../03_data/cop/asp_sub/cop_asp_y{y}_x{x}.tif")
    XsMat['tan_asp']    = flat_tiff(f"../../03_data/tan/asp_sub/tan_asp_y{y}_x{x}.tif")
    XsMat['nasa_asp']   = flat_tiff(f"../../03_data/nasa/asp_sub/nasa_asp_y{y}_x{x}.tif")
    #ROU
    XsMat['aw3d_rou']   = flat_tiff(f"../../03_data/aw3d/rou_sub/aw3d_rou_y{y}_x{x}.tif")
    XsMat['cop_rou']    = flat_tiff(f"../../03_data/cop/rou_sub/cop_rou_y{y}_x{x}.tif")
    XsMat['tan_rou']    = flat_tiff(f"../../03_data/tan/rou_sub/tan_rou_y{y}_x{x}.tif")
    XsMat['nasa_rou']   = flat_tiff(f"../../03_data/nasa/rou_sub/nasa_rou_y{y}_x{x}.tif")
    #TRI
    XsMat['aw3d_tri']   = flat_tiff(f"../../03_data/aw3d/tri_sub/aw3d_tri_y{y}_x{x}.tif")
    XsMat['cop_tri']    = flat_tiff(f"../../03_data/cop/tri_sub/cop_tri_y{y}_x{x}.tif")
    XsMat['tan_tri']    = flat_tiff(f"../../03_data/tan/tri_sub/tan_tri_y{y}_x{x}.tif")
    XsMat['nasa_tri']   = flat_tiff(f"../../03_data/nasa/tri_sub/nasa_tri_y{y}_x{x}.tif")
    #TPI
    XsMat['aw3d_3ave']  = flat_tiff(f"../../03_data/aw3d/3ave_sub/aw3d_3ave_y{y}_x{x}.tif")
    XsMat['cop_3ave']   = flat_tiff(f"../../03_data/cop/3ave_sub/cop_3ave_y{y}_x{x}.tif")
    XsMat['tan_3ave']   = flat_tiff(f"../../03_data/tan/3ave_sub/tan_3ave_y{y}_x{x}.tif")
    XsMat['nasa_3ave']  = flat_tiff(f"../../03_data/nasa/3ave_sub/nasa_3ave_y{y}_x{x}.tif")
    #MASK
    XsMat['aw3d_stk']   = flat_tiff(f"../../03_data/aw3d/stk_sub/aw3d_stk_y{y}_x{x}.tif")
    XsMat['cop_edm']    = flat_tiff(f"../../03_data/cop/edm_sub/cop_edm_y{y}_x{x}.tif")
    XsMat['tan_amp']    = flat_tiff(f"../../03_data/tan/amp_sub/tan_amp_y{y}_x{x}.tif")    
    XsMat['nasa_num']   = flat_tiff(f"../../03_data/nasa/num_sub/nasa_num_y{y}_x{x}.tif") 
    #FH- WC
    XsMat['fheight']   = flat_tiff(f"../../03_data/fheight/03_WtGcZero_sub/fheight_y{y}_x{x}.tif")
    XsMat['wc']        = flat_tiff(f"../../03_data/worldcover/resample_sub/wc_y{y}_x{x}.tif")
    #MOD10A SE1-13
    XsMat['se1']  = flat_tiff(f"../../03_data/mod10a/se177_sub/se177_y{y}_x{x}.tif")
    XsMat['se2']  = flat_tiff(f"../../03_data/mod10a/se185_sub/se185_y{y}_x{x}.tif")
    XsMat['se3']  = flat_tiff(f"../../03_data/mod10a/se193_sub/se193_y{y}_x{x}.tif")
    XsMat['se4']  = flat_tiff(f"../../03_data/mod10a/se201_sub/se201_y{y}_x{x}.tif")
    XsMat['se5']  = flat_tiff(f"../../03_data/mod10a/se209_sub/se209_y{y}_x{x}.tif")
    XsMat['se6']  = flat_tiff(f"../../03_data/mod10a/se217_sub/se217_y{y}_x{x}.tif")
    XsMat['se7']  = flat_tiff(f"../../03_data/mod10a/se225_sub/se225_y{y}_x{x}.tif")
    XsMat['se8']  = flat_tiff(f"../../03_data/mod10a/se233_sub/se233_y{y}_x{x}.tif")
    XsMat['se9']  = flat_tiff(f"../../03_data/mod10a/se241_sub/se241_y{y}_x{x}.tif")
    XsMat['se10'] = flat_tiff(f"../../03_data/mod10a/se249_sub/se249_y{y}_x{x}.tif")
    XsMat['se11'] = flat_tiff(f"../../03_data/mod10a/se257_sub/se257_y{y}_x{x}.tif")
    XsMat['se12'] = flat_tiff(f"../../03_data/mod10a/se265_sub/se265_y{y}_x{x}.tif")
    XsMat['se13'] = flat_tiff(f"../../03_data/mod10a/se273_sub/se273_y{y}_x{x}.tif")
    print('All Imported.')

    XsArray          = XsMat.iloc[:, :].values
    _, Ysize, Xsize  = ReadGeoTiff(f"../../03_data/aw3d/dem_sub/aw3d_dem_y{y}_x{x}.tif")
    GeoT, Projection = GetGeoInfo(f"../../03_data/aw3d/dem_sub/aw3d_dem_y{y}_x{x}.tif")
    return XsArray, Ysize, Xsize, GeoT, Projection

#使用模型预测输出值
def Train_Predict():
    for x in range(1,14):
        for y in range(1,7):
            try:
                XsArray, Ysize, Xsize, GeoT, Projection = getSeries(x,y)
                Xs_pred  = et.predict(XsArray).reshape((Ysize, Xsize))
                filename = f"03_2TIMES_ET_ATL06_y{y}x{x}"
                CreateGeoTiff(filename, Xs_pred, Xsize, Ysize, GeoT, Projection, -9999)
                print('y'+str(y)+'x'+str(x).zfill(2)+' created.')
            except: continue

Train_Predict()
