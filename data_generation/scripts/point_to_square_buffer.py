# This helper script can be used to create square buffers from point based samples in QGIS. The size can be varied accordingly.

layer = iface.activeLayer()

feats = [ feat for feat in layer.getFeatures() ]

epsg = layer.crs().postgisSrid()

uri = "Polygon?crs=epsg:" + str(epsg) + "&field=id:integer&field=x:real&field=y:real&field=point_id:integer""&index=yes"

mem_layer = QgsVectorLayer(uri,
                           'square_buffer',
                           'memory')

prov = mem_layer.dataProvider()

for i, feat in enumerate(feats):
    point = feat.geometry().asPoint()
    new_feat = QgsFeature()
    new_feat.setAttributes([i, point[0], point[1], feat['class'], feat.id()])
    tmp_feat = feat.geometry().buffer(0.0005, -1).boundingBox().asWktPolygon()
    new_feat.setGeometry(QgsGeometry.fromWkt(tmp_feat))
    prov.addFeatures([new_feat])

QgsMapLayerRegistry.instance().addMapLayer(mem_layer)

# further details in https://gis.stackexchange.com/questions/210295/how-to-create-square-buffers-around-points-in-qgis-with-python
