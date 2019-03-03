### This helper script is used in QGIS to clip the selected training samples from the satellite imagery.

import ogr
import subprocess


inraster = '/home/deepank/Desktop/vae/Satellite Image 2012/PROCESSED/Pleiades_DGPS/JPEG/pleaidestiff/jp22_stretched.tif'
inshape = '../square_buffer.shp'

print(inraster)

ds = ogr.Open(inshape)
print(ds)

lyr = ds.GetLayer(0)
print(lyr)


lyr.ResetReading()
ft = lyr.GetNextFeature()

print(ft)

while ft:

    id_name = ft.GetFieldAsString('id')
    print(id_name)

    class_name = ft.GetFieldAsString('point_id')
    print(class_name)

    outraster = inraster.replace('.tif', '_%s_%s.tif' % (id_name.replace(' ', '_'), class_name.replace(' ', '_')))    
    print(outraster)
    subprocess.call(['gdalwarp', inraster, outraster, '-cutline', inshape, 
                     '-crop_to_cutline', '-cwhere', "id = %s" % id_name])


    ft = lyr.GetNextFeature()


ds = None


# Following helper script is used to subdivide the contents of the folder into equal parts, if large number of clips are in single folder.

# i=0; 
# for f in *; 
# do 
#     d=dir_$(printf %03d $((i/20000+1))); 
#     mkdir -p $d; 
#     mv "$f" $d; 
#     let i++; 
# done

## Following helper script can be used to merge index shapefiles to one.

# for f in *.shp; do ogr2ogr -update -append merged.shp $f -f "ESRI Shapefile"; done;