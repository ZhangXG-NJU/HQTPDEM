# -*- coding: utf-8 -*-

import os
import numpy             as     np
import rasterio          as     rio
import geopandas         as     gpd
import matplotlib.pyplot as     plt
from   rasterstats       import point_query

#pointData  = gpd.read_file(r"E:\Zhang_XinGang\11_QPTDEM\03_data\atl08\07_Pquery\06_test.shp")
pointData  = gpd.read_file(r"E:\Zhang_XinGang\11_QPTDEM\03_data\hagecpd\hagecpd_InBound.shp")

lons       = np.array(pointData['Lon'])
lats       = np.array(pointData['Lat'])
Topo       = np.array(pointData['Topography'])
lidarvalue  = np.array(pointData['GElevation'])

aw3_dem  = r"..\03_data\aw3\aw3_dem.tif"
# aw3_rou  = r"..\03_data\aw3\aw3_rou.tif"
# aw3_tri  = r"..\03_data\aw3\aw3_tri.tif"
# aw3_3ave = r"..\03_data\aw3\aw3_3ave.tif"
# aw3_stk  = r"..\03_data\aw3\aw3_stk.tif"
# aw3_slo  = r"..\03_data\aw3\aw3_slo_int.tif"
# aw3_asp  = r"..\03_data\aw3\aw3_asp.tif"

cop_dem   = r"..\03_data\cop\cop_dem2.tif"
# cop_rou   = r"..\03_data\cop\cop_rou.tif"
# cop_tri   = r"..\03_data\cop\cop_tri.tif"
# cop_3ave  = r"..\03_data\cop\cop_3ave.tif"
# cop_edm   = r"..\03_data\cop\cop_edm.tif"
# cop_slo   = r"..\03_data\cop\cop_slo.tif"
# cop_asp   = r"..\03_data\cop\cop_asp.tif"

tan_dem   = r"..\03_data\tan\tan_dem.tif"
# tan_rou   = r"..\03_data\tan\tan_rou.tif"
# tan_tri   = r"..\03_data\tan\tan_tri.tif"
# tan_3ave  = r"..\03_data\tan\tan_3ave.tif"
# tan_amp   = r"..\03_data\tan\tan_amp.tif"
# tan_slo   = r"..\03_data\tan\tan_slo.tif"
# tan_asp   = r"..\03_data\tan\tan_asp.tif"

nas_dem  = r"..\03_data\nas\nas_dem.tif"
# nas_rou  = r"..\03_data\nas\nas_rou.tif"
# nas_tri  = r"..\03_data\nas\nas_tri.tif"
# nas_3ave = r"..\03_data\nas\nas_3ave.tif"
# nas_num  = r"..\03_data\nas\nas_num.tif"
# nas_slo  = r"..\03_data\nas\nas_slo.tif"
# nas_asp  = r"..\03_data\nas\nas_asp.tif"

# fheight   = r"..\03_data\fheight\03_WtGcZero\WtGcZero_int16.tif"
# wc        = r"..\03_data\worldcover\resample\wc_resample.tif"

# sc1 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_177.tif"
# sc2 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_185.tif"
# sc3 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_193.tif"
# sc4 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_201.tif"
# sc5 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_209.tif"
# sc6 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_217.tif"
# sc7 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_225.tif"
# sc8 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_233.tif"
# sc9 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_241.tif"
# sc10 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_249.tif"
# sc11 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_257.tif"
# sc12 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_265.tif"
# sc13 = r"..\03_data\mod10a\04_clip\clip_proj_snowcover_273.tif"

# se1 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_177.tif"
# se2 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_185.tif"
# se3 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_193.tif"
# se4 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_201.tif"
# se5 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_209.tif"
# se6 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_217.tif"
# se7 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_225.tif"
# se8 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_233.tif"
# se9 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_241.tif"
# se10 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_249.tif"
# se11 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_257.tif"
# se12 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_265.tif"
# se13 = r"..\03_data\mod10a\04_clip\clip_proj_snowextent_273.tif"

ast_dem = r"E:\Zhang_XinGang\11_QPTDEM\03_data\ast\dem\aster_dem_full.tif"
srt_dem = r"E:\Zhang_XinGang\11_QPTDEM\03_data\srt\04_coreg\srtm_egm08_coreg.tif"
mrt_dem = r"E:\Zhang_XinGang\11_QPTDEM\03_data\mrt\03_egm08\merit_egm08.tif"
etc_dem  = r"E:\Zhang_XinGang\11_QPTDEM\04_output\Archieve\et_CSF33_C.tif"

#pquery_ast_bl = np.array(point_query(pointData['geometry'], ast_dem, interpolate='bilinear'))
#pquery_aw3_bl = np.array(point_query(pointData['geometry'], aw3_dem, interpolate='bilinear'))
pquery_cop_bl = np.array(point_query(pointData['geometry'], cop_dem, interpolate='bilinear'))
#pquery_tan_bl = np.array(point_query(pointData['geometry'], tan_dem, interpolate='bilinear'))
#pquery_nas_bl = np.array(point_query(pointData['geometry'], nas_dem, interpolate='bilinear'))
#pquery_srt_bl = np.array(point_query(pointData['geometry'], srt_dem, interpolate='bilinear'))
#pquery_mrt_bl = np.array(point_query(pointData['geometry'], mrt_dem, interpolate='bilinear'))
#pquery_etc_bl = np.array(point_query(pointData['geometry'], etc_dem, interpolate='bilinear'))

#pquery_sc1  = np.array(point_query(pointData['geometry'],sc1, interpolate='bilinear'))
#pquery_sc2  = np.array(point_query(pointData['geometry'],sc2, interpolate='bilinear'))
#pquery_sc3  = np.array(point_query(pointData['geometry'],sc3, interpolate='bilinear'))
#pquery_sc4  = np.array(point_query(pointData['geometry'],sc4, interpolate='bilinear'))
#pquery_sc5  = np.array(point_query(pointData['geometry'],sc5, interpolate='bilinear'))
#pquery_sc6  = np.array(point_query(pointData['geometry'],sc6, interpolate='bilinear'))
#pquery_sc7  = np.array(point_query(pointData['geometry'],sc7, interpolate='bilinear'))
#pquery_sc8  = np.array(point_query(pointData['geometry'],sc8, interpolate='bilinear'))
#pquery_sc9  = np.array(point_query(pointData['geometry'],sc9, interpolate='bilinear'))
#pquery_sc10 = np.array(point_query(pointData['geometry'],sc10,interpolate='bilinear'))
#pquery_sc11 = np.array(point_query(pointData['geometry'],sc11,interpolate='bilinear'))
#pquery_sc12 = np.array(point_query(pointData['geometry'],sc12,interpolate='bilinear'))
#pquery_sc13 = np.array(point_query(pointData['geometry'],sc13,interpolate='bilinear'))

# pquery_aw3dem  = np.array(point_query(pointData['geometry'],aw3_dem, interpolate='bilinear'))
# pquery_aw3rou  = np.array(point_query(pointData['geometry'],aw3_rou, interpolate='bilinear'))
# pquery_aw3slo  = np.array(point_query(pointData['geometry'],aw3_slo, interpolate='bilinear'))
# pquery_aw3tri  = np.array(point_query(pointData['geometry'],aw3_tri, interpolate='bilinear'))
# pquery_aw33ave = np.array(point_query(pointData['geometry'],aw3_3ave, interpolate='bilinear'))
# pquery_aw3asp  = np.array(point_query(pointData['geometry'],aw3_asp, interpolate='bilinear'))
#pquery_tanamp  = np.array(point_query(pointData['geometry'],tan_amp, interpolate='bilinear'))

#pquery_wc  = np.array(point_query(pointData['geometry'],wc, interpolate='bilinear'))
#pquery_fh  = np.array(point_query(pointData['geometry'],fheight, interpolate='bilinear'))


# def getFilePathes(Folder):
#     M_files = os.listdir(Folder)
#     Files_List = []
#     for items in M_files:
#         if os.path.splitext(items)[1] == '.tif':
#             Files_List.append(Folder+items)
#     return Files_List

# for f in getFilePathes(r"..\11_testdata\\"):
#     print(f)
#     pquery = np.array(point_query(pointData['geometry'],f))
#     pointData[f] = pquery
    
#pointData.to_csv(r"..\11_testdata\Atl08_Pquery.csv",index=False,encoding="utf-8")


