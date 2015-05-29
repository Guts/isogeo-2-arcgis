# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals
# ------------------------------------------------------------------------------
# Name:         XML importer
# Purpose:      Writing metadata in local storage from the XML imported
#
# Author:       Julien Moura (@geojulien)
#
# Python:       2.7.x
# Created:      10/04/2015
# Updated:      10/04/2015
#
# Licence:      GPL 3
# -----------------------------------------------------------------------------

###############################################################################
########### Libraries #############
###################################

# 3rd party libraries
import arcpy
from arcpy import env

###############################################################################
############ Main program ############
###################################

arcpy.ImportMetadata_conversion ("c:/data/streams.shp","FROM_FGDC","streams")


###############################################################################
###### Stand alone program ########
###################################

if __name__ == '__main__':
    """ standalone execution for testing """
    pass
