from osgeo import gdal
import os

def crop_dem(input_file, output_file):
    # 打开DEM数据集
    dem_ds = gdal.Open(input_file)

    # 获取DEM数据集的投影和地理参考信息
    proj = dem_ds.GetProjection()
    geotransform = dem_ds.GetGeoTransform()
    no_data = dem_ds.GetRasterBand(1).GetNoDataValue()

    # 获取DEM数据集的宽度和高度
    width = dem_ds.RasterXSize
    height = dem_ds.RasterYSize

    # 从DEM数据集创建一个numpy数组
    dem_array = dem_ds.ReadAsArray()

    # 找到裁剪后的边界
    row_min, row_max = 0, height-1
    col_min, col_max = 0, width-1
    for i in range(height):
        if not all(dem_array[i,:] == dem_array[0,:]):
            row_min = i
            break
    for i in range(height-1, -1, -1):
        if not all(dem_array[i,:] == dem_array[height-1,:]):
            row_max = i
            break
    for i in range(width):
        if not all(dem_array[:,i] == dem_array[:,0]):
            col_min = i
            break
    for i in range(width-1, -1, -1):
        if not all(dem_array[:,i] == dem_array[:,width-1]):
            col_max = i
            break

    # 裁剪DEM数组
    cropped_dem_array = dem_array[row_min:row_max+1, col_min:col_max+1]

    # 创建一个新的GDAL数据集
    driver = gdal.GetDriverByName('GTiff')
    options = ['COMPRESS=LZW']
    dst_ds = driver.Create(output_file, 
                            cropped_dem_array.shape[1], 
                            cropped_dem_array.shape[0], 
                            1, 
                            gdal.GDT_Float32,
                            options=options)

    # 设置新数据集的投影和地理参考信息
    dst_ds.SetProjection(proj)
    dst_ds.SetGeoTransform((geotransform[0]+col_min*geotransform[1],
                            geotransform[1],
                            0,
                            geotransform[3]+row_min*geotransform[5],
                            0,
                            geotransform[5]))

    # 将裁剪后的DEM数组写入新数据集
    dst_ds.GetRasterBand(1).SetNoDataValue(no_data)
    dst_ds.GetRasterBand(1).WriteArray(cropped_dem_array)

    # 关闭数据集
    dem_ds = None
    dst_ds = None

def crop_dems_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".tif"):
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_folder, file)
                crop_dem(input_file, output_file)
                print(file)


input_folder = r"E:\Zhang_XinGang\11_QPTDEM\09_valid_data\03_egm08"
output_folder = r"E:\Zhang_XinGang\11_QPTDEM\09_valid_data\04_Crop"
crop_dems_in_folder(input_folder, output_folder)
