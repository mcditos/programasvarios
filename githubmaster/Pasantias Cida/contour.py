from osgeo import gdal
from osgeo.gdalconst import *
from numpy import *
from osgeo import ogr

#Primero se lee la data grd
data_elevacion= gdal.Open( "/usr/cbarrios/Documentos/Gerardo/vallesdeltuyhillshade/raster_combinado.grd", GA_ReadOnly)
banda_raster = data_elevacion.GetRasterBand(1)

#Generacion de la capa para las lineas de nivel
ogr_ds = ogr.GetDriverByName("ESRI Shapefile").CreateDataSource("lineas de nivel.shp")
contour_shp = ogr_ds.CreateLayer('lineas de nivel')

#Se definen los campos (atributos de la capa), uno de enteros(la cantidad de lineas) y uno de reales que representara las alturas
field_defn = ogr.FieldDefn("ID", ogr.OFTInteger)
contour_shp.CreateField(field_defn)
field_defn = ogr.FieldDefn("elev", ogr.OFTReal)
contour_shp.CreateField(field_defn)

#Generate Contourlines
gdal.ContourGenerate(banda_raster, 100, 0, [], 0, 0, contour_shp, 0, 1)

#se elimina la data para dejar solo las lineas de contorno 

ogr_ds = None
del ogr_ds
