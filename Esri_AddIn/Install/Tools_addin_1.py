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

###############################################################################
############# Classes #############
###################################

class Settings(object):
    """Implementation for Tools_addin.settings_button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False

    # def onClick(self):
    #     """gfh """
    #     layer_files = pythonaddins.OpenDialog('Select Layers', True, r'C:\\Users\\antoine.audusseau\\Documents\\GIS_Data', 'Add')
    #     mxd = arcpy.mapping.MapDocument('current')
    #     df = pythonaddins.GetSelectedTOCLayerOrDataFrame()
    #     if not isinstance(df, arcpy.mapping.Layer):
    #         for layer_file in layer_files:
    #             layer = arcpy.mapping.Layer(layer_file)
    #             arcpy.mapping.AddLayer(df, layer)
    #     else:
    #         pythonaddins.MessageBox('Select a data frame', 'INFO', 0)

    def onClick(self):
        """gfh """
        inputFeatureClass = raw_input('crie mon nom : ')
        print inputFeatureClass

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
