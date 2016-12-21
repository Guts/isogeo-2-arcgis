# ------------------------------------------------------------------------------
# Name:         Isogeo to desktop GIS
# Purpose:      Load Isogeo metadata into a GIS desktop software
#
# Author:       Julien Moura (@geojulien)
#
# Python:       2.7.x with arcpy
# Created:      10/05/2015
# Updated:      28/05/2015
#
# Licence:      GPL 3
# -----------------------------------------------------------------------------

###############################################################################
########### Libraries #############
###################################

# Standard library
import ConfigParser  # to manipulate options.ini file

# 3rd party libraries
import arcpy
import pythonaddins

# custom modules
import arcpy_metadata as md

###############################################################################
############# Classes #############
###################################

class Pairing(object):
    """Implementation for Tools_addin.pairing_button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class Search(object):
    """Implementation for Tools_addin.search_button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class Settings(object):
    """Implementation for Tools_addin.settings_button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        """gfh """
        inputFeatureClass = raw_input('crie mon nom : ')
        print inputFeatureClass

class Sync(object):
    """Implementation for Tools_addin.sync_button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass
