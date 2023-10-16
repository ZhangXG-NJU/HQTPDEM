import sys 
sys.path.append("..")

import os
os.environ['PROJ_LIB'] = r"C:\ProgramData\Anaconda3\Lib\site-packages\osgeo\data\proj"

import pandas as pd
import rasterio as rio
import xgboost as xgb
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from Geotiff_read_write import ReadGeoTiff, GetGeoInfo, CreateGeoTiff

# 读取CSV文件
df = pd.read_csv(r"..\..\03_data\atl06\08_pquery\05_withSC.csv")
df = shuffle(df).iloc[:, :]

# 分离 X 和 Y
X = df.iloc[:, 3:]
Y = df.iloc[:, 2]

# 定义XGBoost回归器
xgbr = xgb.XGBRegressor(objective='reg:squarederror',
                        n_jobs=-1,
                        n_estimators=800)

# 划分训练集和测试集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 训练模型
xgbr.fit(X_train, Y_train)

# 预测并计算 MAE、RMSE、MSE
y_pred = xgbr.predict(X_test)
mae = mean_absolute_error(Y_test, y_pred)
rmse = mean_squared_error(Y_test, y_pred, squared=False)
mse = mean_squared_error(Y_test, y_pred)

# 输出结果
print(f"Best Params: {xgbr.get_params()}, MAE: {mae}, RMSE: {rmse}, MSE: {mse}")

#将Geotiff读取并转为一维数组
def flat_tiff(file_path, band_num=1):
    with rio.open(file_path) as src:
        bandflatten = src.read(band_num).flatten()
    return bandflatten

#获取X值并获取GeoT等必要信息
def getSeries(x, y):
    XsMat = pd.DataFrame()
    
    #DEM COP-ASTER-AW3D-NASAcop_dem
    XsMat['aster_dem']  = flat_tiff(f"../../03_data/01_aster/dem_sub/aster_dem_y{y}_x{x}.tif")
    XsMat['aw3d_dem']   = flat_tiff(f"../../03_data/02_aw3d30/dem_sub/aw3d_dem_y{y}_x{x}.tif")
    XsMat['cop_dem']    = flat_tiff(f"../../03_data/03_cop30/dem_sub/cop_dem_y{y}_x{x}.tif")
    XsMat['nasa_dem']   = flat_tiff(f"../../03_data/04_nasadem/dem_sub/nasa_dem_y{y}_x{x}.tif")
    print('DEMs Imported.')
    
    #SLO ASTER-AW3D-COP-NASA
    XsMat['aster_slo']  = flat_tiff(f"../../03_data/01_aster/slo_sub/aster_slo_y{y}_x{x}.tif")
    XsMat['aw3d_slo']   = flat_tiff(f"../../03_data/02_aw3d30/slo_sub/aw3d_slo_y{y}_x{x}.tif")
    XsMat['cop_slo']    = flat_tiff(f"../../03_data/03_cop30/slo_sub/cop_slo_y{y}_x{x}.tif")
    XsMat['nasa_slo']   = flat_tiff(f"../../03_data/04_nasadem/slo_sub/nasa_slo_y{y}_x{x}.tif")
    print('SLOs Imported.')
    
    #ASP ASTER-AW3D-COP-NASA
    XsMat['aster_asp']  = flat_tiff(f"../../03_data/01_aster/asp_sub/aster_asp_y{y}_x{x}.tif")
    XsMat['aw3d_asp']   = flat_tiff(f"../../03_data/02_aw3d30/asp_sub/aw3d_asp_y{y}_x{x}.tif")
    XsMat['cop_asp']    = flat_tiff(f"../../03_data/03_cop30/asp_sub/cop_asp_y{y}_x{x}.tif")
    XsMat['nasa_asp']   = flat_tiff(f"../../03_data/04_nasadem/asp_sub/nasa_asp_y{y}_x{x}.tif")
    print('ASPs Imported.')
    
    #ROU ASTER-AW3D-COP-NASA
    XsMat['aster_rou']  = flat_tiff(f"../../03_data/01_aster/rou_sub/aster_rou_full_y{y}_x{x}.tif")
    XsMat['aw3d_rou']   = flat_tiff(f"../../03_data/02_aw3d30/rou_sub/aw3d_rou_y{y}_x{x}.tif")
    XsMat['cop_rou']    = flat_tiff(f"../../03_data/03_cop30/rou_sub/cop_rou_y{y}_x{x}.tif")
    XsMat['nasa_rou']   = flat_tiff(f"../../03_data/04_nasadem/rou_sub/nasa_rou_y{y}_x{x}.tif")
    print('ROUs Imported.')
    
    #TRI ASTER-AW3D-COP-NASA
    XsMat['aster_tri']  = flat_tiff(f"../../03_data/01_aster/tri_sub/aster_tri_full_y{y}_x{x}.tif")
    XsMat['aw3d_tri']   = flat_tiff(f"../../03_data/02_aw3d30/tri_sub/aw3d_tri_y{y}_x{x}.tif")
    XsMat['cop_tri']    = flat_tiff(f"../../03_data/03_cop30/tri_sub/cop_tri_y{y}_x{x}.tif")
    XsMat['nasa_tri']   = flat_tiff(f"../../03_data/04_nasadem/tri_sub/nasa_tri_y{y}_x{x}.tif")
    print('TRIs Imported.')
    
    #TPI ASTER-AW3D-COP-NASA
    XsMat['aster_3ave'] = flat_tiff(f"../../03_data/01_aster/3ave_sub/aster_3ave_y{y}_x{x}.tif")
    XsMat['aw3d_3ave']  = flat_tiff(f"../../03_data/02_aw3d30/3ave_sub/aw3d_3ave_y{y}_x{x}.tif")
    XsMat['cop_3ave']   = flat_tiff(f"../../03_data/03_cop30/3ave_sub/cop_3ave_y{y}_x{x}.tif")
    XsMat['nasa_3ave']  = flat_tiff(f"../../03_data/04_nasadem/3ave_sub/nasa_3ave_y{y}_x{x}.tif")
    print('TPIs Imported.')
    
    #AUX ASTER NUM - AW3D STK - COP30 EDM - WORLDCOVER -FHEIGHT
    XsMat['aster_num'] = flat_tiff(f"../../03_data/01_aster/num_sub/aster_num_y{y}_x{x}.tif")
    XsMat['cop30_edm']   = flat_tiff(f"../../03_data/03_cop30/edm_sub/cop_edm_y{y}_x{x}.tif")
    XsMat['aw3d30_stk']  = flat_tiff(f"../../03_data/02_aw3d30/stk_sub/aw3d_stk_y{y}_x{x}.tif")
    XsMat['wc']        = flat_tiff(f"../../03_data/worldcover/resample_sub/wc_y{y}_x{x}.tif")
    XsMat['fheight']   = flat_tiff(f"../../03_data/fheight/03_WtGcZero_sub/fheight_y{y}_x{x}.tif")
    print('AUXs Imported.')
    
    #MOD10A SC1-13 SE1-13
    XsMat['sc1']  = flat_tiff(f"../../03_data/mod10a/sc177_sub/sc177_y{y}_x{x}.tif")
    XsMat['sc2']  = flat_tiff(f"../../03_data/mod10a/sc185_sub/sc185_y{y}_x{x}.tif")
    XsMat['sc3']  = flat_tiff(f"../../03_data/mod10a/sc193_sub/sc193_y{y}_x{x}.tif")
    XsMat['sc4']  = flat_tiff(f"../../03_data/mod10a/sc201_sub/sc201_y{y}_x{x}.tif")
    XsMat['sc5']  = flat_tiff(f"../../03_data/mod10a/sc209_sub/sc209_y{y}_x{x}.tif")
    XsMat['sc6']  = flat_tiff(f"../../03_data/mod10a/sc217_sub/sc217_y{y}_x{x}.tif")
    XsMat['sc7']  = flat_tiff(f"../../03_data/mod10a/sc225_sub/sc225_y{y}_x{x}.tif")
    XsMat['sc8']  = flat_tiff(f"../../03_data/mod10a/sc233_sub/sc233_y{y}_x{x}.tif")
    XsMat['sc9']  = flat_tiff(f"../../03_data/mod10a/sc241_sub/sc241_y{y}_x{x}.tif")
    XsMat['sc10'] = flat_tiff(f"../../03_data/mod10a/sc249_sub/sc249_y{y}_x{x}.tif")
    XsMat['sc11'] = flat_tiff(f"../../03_data/mod10a/sc257_sub/sc257_y{y}_x{x}.tif")
    XsMat['sc12'] = flat_tiff(f"../../03_data/mod10a/sc265_sub/sc265_y{y}_x{x}.tif")
    XsMat['sc13'] = flat_tiff(f"../../03_data/mod10a/sc273_sub/sc273_y{y}_x{x}.tif")
    
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
    print('MOD10A Imported.')

    XsArray          = XsMat.iloc[:, :].values
    _, Ysize, Xsize  = ReadGeoTiff(f"../../03_data/01_aster/num_sub/aster_num_y{y}_x{x}.tif")
    GeoT, Projection = GetGeoInfo(f"../../03_data/01_aster/num_sub/aster_num_y{y}_x{x}.tif")
    return XsArray, Ysize, Xsize, GeoT, Projection

#使用模型预测输出值
def Train_Predict():
    for x in range(1,14):
        for y in range(1,7):
            x = str(x).zfill(2)
            y = str(y)
            try:
                XsArray, Ysize, Xsize, GeoT, Projection = getSeries(x,y)
                Xs_pred  = xgbr.predict(XsArray).reshape((Ysize, Xsize))
                filename = f"XGBoost_ATL06_y{y}x{x}"
                CreateGeoTiff(filename, Xs_pred, Xsize, Ysize, GeoT, Projection, -9999)
                print('*** y'+y+'x'+x+' created. ***')
            except: continue

Train_Predict()

