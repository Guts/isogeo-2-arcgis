# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals
# ------------------------------------------------------------------------------
# Name:         Matches table maintener
# Purpose:      Maintaining the match table between Isogeo IDs & local paths
#
# Author:       Julien Moura (@geojulien)
#
# Python:       2.7.x with arcpy
# Created:      10/04/2015
# Updated:      10/04/2015
#
# Licence:      GPL 3
# -----------------------------------------------------------------------------

###############################################################################
########### Libraries #############
###################################

# Standard library
from json import dump, load
import json
import time

# 3rd party libraries
import arcpy

###############################################################################
######### Global variables #########
###################################

# récupération du time
date = time.clock()


###############################################################################
########### Functions #############
###################################

def fill_full(id, idu, local_path, md_last_update):
    """
    TO DO
    """
    file = open("file.json", "a")
    line = {'date': date, 'line': {'ID': id,
                                   'IDU': idu,
                                   'local_Path': local_path,
                                   'Last_update': md_last_update
                                   }
            }
    json.dump(line, file, indent=4)
    file.close()

fill_full(arcpy.GetParameterAsText(0),
          arcpy.GetParameterAsText(1),
          arcpy.GetParameterAsText(2),
          'test')


###############################################################################
###### Stand alone program ########
###################################

if __name__ == '__main__':
    """ standalone execution for testing """
    pass
