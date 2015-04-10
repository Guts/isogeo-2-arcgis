import arcpy
from arcpy import env
env.workspace = "c:/data/data.gdb"
arcpy.ImportMetadata_conversion ("c:/data/streams.shp","FROM_FGDC","streams")
