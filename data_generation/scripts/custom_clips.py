## This helper script can be modified to use in QGIS for custom clipping of large satellite imageries.

import os

rlayer = iface.activeLayer()

#raster layer
provider = rlayer.dataProvider()

input_raster_path = provider.dataSourceUri()

print input_raster_path

xsize = rlayer.rasterUnitsPerPixelX()
ysize = rlayer.rasterUnitsPerPixelY()

extent = rlayer.extent()

xmin_raster = extent.xMinimum()
ymax_raster = extent.yMaximum()

print xmin_raster, ymax_raster

n_rows = 4246
n_columns = 2375

row_init = 3
column_init = 3 

row_end = row_init + n_rows - 1
column_end = column_init + n_columns - 1

xmin = xmin_raster + (column_init - 1 ) * xsize
xmax = xmin_raster + (column_end) * xsize

ymin = ymax_raster - (row_end) * ysize
ymax = ymax_raster - (row_init - 1) * ysize

extent = " -projwin " + str(xmin) + " " + str(ymax) + " " + str(xmax) + " " + str(ymin) + " "

output_raster_path = "/home/deepank/Desktop/vae/satellite_imagery/clips/mum_clip2_rescaled_2.tif"

cmd = "gdal_translate " + extent + input_raster_path + " " + output_raster_path        

print cmd

os.system(cmd)
