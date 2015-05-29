# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals
# ------------------------------------------------------------------------------
# Name:         ArcGIS parameters
# Purpose:      Parameters needed for integration into ArcGIS UI
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
import sys
import string
import os

# 3rd party libraries
import arcpy

###############################################################################
######## Global variables #########
###################################

# Get the value of the input parameter

protocole = arcpy.GetParameterAsText(0)
prox = arcpy.GetParameterAsText(1)
port = arcpy.GetParameterAsText(2)
password = arcpy.GetParameterAsText(3)
user = arcpy.GetParameterAsText(4)
