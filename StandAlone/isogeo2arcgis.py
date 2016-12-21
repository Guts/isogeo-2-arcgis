# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from __future__ import (absolute_import, print_function, unicode_literals)

# ------------------------------------------------------------------------------
# Name:         Isogeo to ArcGIS
# Purpose:      Load Isogeo metadata into ArcGIS
#
# Author:       Julien Moura (@geojulien)
#
# Python:       2.7.9+ with arcpy
# Created:      10/09/2015
# Updated:      10/12/2016
#
# Licence:      GPL 3
# -----------------------------------------------------------------------------

_version = "0.2-alpha"

# ############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import ConfigParser  # to manipulate options.ini file
from os import path
import logging      # log files
from logging.handlers import RotatingFileHandler
from sys import exit, path as syspath, platform as opersys

# 3rd party libraries
from isogeo_pysdk import Isogeo
try:
    import arcpy
    from arcpy import env as enviro
    from arcpy import ImportMetadata_conversion as importMD
    import arcpy_metadata as arc_md
    print("Great! ArcGIS is well installed.")
except ImportError:
    print("ArcGIS isn't registered in the sys.path")
    syspath.append(r'C:\Program Files (x86)\ArcGIS\Desktop10.2\arcpy')
    syspath.append(r'C:\Program Files (x86)\ArcGIS\Desktop10.2\bin')
    syspath.append(r'C:\Program Files (x86)\ArcGIS\Desktop10.2\ArcToolbox\Scripts')
    try:
        from arcpy import env as enviro
        from arcpy import ImportMetadata_conversion as importMD
        print("ArcGIS has been added to Python path and then imported.")
    except:
        print("ArcGIS isn't installed on this computer")
        exit()

# ############################################################################
# ########## Log manager ###########
# ##################################

# creation and configuration of log file
logger = logging.getLogger()
logging.captureWarnings(True)
logger.setLevel(logging.DEBUG)  # all errors will be get
log_form = logging.Formatter("%(asctime)s || %(levelname)s "
                             "|| %(module)s || %(message)s")
logfile = RotatingFileHandler("LOG_isogeo2office.log", "a", 5000000, 1)
logfile.setLevel(logging.DEBUG)
logfile.setFormatter(log_form)
logger.addHandler(logfile)
logger.info('\t\t ============== Isogeo to ArcGIS =============')
logger.info('Version: {0}'.format(_version))

# ############################################################################
# ############ Classes #############
# ##################################


class IsogeoToArcGIS(object):
    """IsogeoToArcGIS class."""

    def __init__(self, lang="FR"):
        """Class initialization."""
        super(IsogeoToArcGIS, self).__init__()

        # ------------ VARIABLES ---------------------

        # -- functions
        # load settings
        self.load_settings()





        # save settings
        self.save_settings()

    def load_settings(self):
        u"""
        load settings from last execution
        """
        confile = 'options.ini'
        config = ConfigParser.RawConfigParser()
        try:
            config.read(confile)
            # authentification API Isogeo
            def_share_id = config.get('isogeo', 'def_share_id')
            def_token = config.get('isogeo', 'def_token')
            # proxy settings
            def_proxy_type = config.get('proxy', 'def_proxy_type')
            def_proxy_host = config.get('proxy', 'def_proxy_host')
            def_proxy_port = config.get('proxy', 'def_proxy_port')
            def_proxy_user = config.get('proxy', 'def_proxy_user')
            def_proxy_pswd = config.get('proxy', 'def_proxy_pswd')

            # log
            # logger.info('Last options loaded')
            return (def_share_id, def_token), (def_proxy_type, def_proxy_host,
                                               def_proxy_port, def_proxy_user,
                                               def_proxy_pswd)
        except:
            # log
            logger.info('First use: previous settings not found.')
            return None

    def save_settings(self):
        u"""
        save last options in order to make the next excution more easy
        """
        confile = r'options.ini'
        config = ConfigParser.RawConfigParser()

        # add sections
        config.add_section('basics')
        config.add_section('isogeo')
        config.add_section('proxy')

        # basics
        config.set('basics', 'tool_version', _version)
        config.set('basics', 'OS', opsys)
        config.set('basics', 'last_sync', lastsync)
        # isogeo
        config.set('isogeo', 'def_share_id', share_id)
        config.set('isogeo', 'def_token', token)
        # proxy
        config.set('proxy', 'def_proxy_type', proxy_type)
        config.set('proxy', 'def_proxy_host', proxy_host)
        config.set('proxy', 'def_proxy_port', proxy_port)
        config.set('proxy', 'def_proxy_user', proxy_user)
        config.set('proxy', 'def_proxy_pswd', proxy_pswd)

        # Writing the configuration file
        with open(confile, 'wb') as configfile:
            config.write(configfile)

        # log
        logger.info('Options saved')

        # End of function
        return config


###############################################################################
###### Stand alone program ########
###################################

if __name__ == '__main__':
    """ standalone execution for testing """
    # storing application parameters into an ini file
    settings_file = r"settings.ini"

    # testing ini file
    if not path.isfile(path.realpath(settings_file)):
        print("ERROR: to execute this script as standalone,"
              " you need to store your Isogeo application settings"
              " in a isogeo_params.ini file. You can use the template"
              " to set your own.")
        import sys
        sys.exit()
    else:
        pass

    # reading ini file
    config = ConfigParser.SafeConfigParser()
    config.read(settings_file)

    share_id = config.get('auth', 'app_id')
    share_token = config.get('auth', 'app_secret')

    # ------------ Real start ----------------
    proxies = {'http': 'http://s-olfeo1.cab.local:3129',
               'https': 'https://s-olfeo1.cab.local:3129'}
    # instanciating the class
    isogeo = Isogeo(client_id=share_id,
                    client_secret=share_token,
                    proxy=proxies
                    )

    # getting a token
    jeton = isogeo.connect()

    # let's search for metadatas!
    search = isogeo.search(jeton)
    print("Total count of metadatas shared: ", search.get("total"))
    print("Count of resources got by request: {}\n".format(len(search.get("results"))))

    # make a list of path
    # settings_dict = {s: dict(config.items(s)) for s in config.sections()}
##    path_dict = {md.get("name"): dict(config.items(md)) for md in search.get("results")}
    names_dict = {}
    for md_isogeo in search.get("results"):
        if md_isogeo.get("type")in ["vectorDataset", "rasterDataset"] and md_isogeo.get("name"):
            names_dict[md_isogeo.get("name")] = md_isogeo.get("abstract")
        else:
            pass

    # print(names_dict.keys()[8])
    print(names_dict.keys())
        

    # arcpy
    enviro.workspace = config.get('esri', 'sde_file')
    fcList = arcpy.ListFeatureClasses()
    for fc in fcList[:10]:
        # print(fc)
        # in names_dict.keys()
        if fc == "SIG.DSU_INCIDENT":
            src_md = arc_md.MetadataEditor(fc)
            print(src_md.title)
            ig_md = names_dict.get(fc)
            print(ig_md)




    
