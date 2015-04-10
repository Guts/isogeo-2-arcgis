# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals
# ------------------------------------------------------------------------------
# Name:         Isogeo to desktop GIS
# Purpose:      Load Isogeo metadata into a GIS desktop software
#
# Author:       master ASIG de l'ENSG avec Julien Moura (@geojulien)
#
# Python:       2.7.x with arcpy
# Created:      10/09/2015
# Updated:      10/04/2015
#
# Licence:      GPL 3
# -----------------------------------------------------------------------------

_version = "0.1-alpha"

###############################################################################
########### Libraries #############
###################################

# Standard library
import ConfigParser  # to manipulate options.ini file

import logging      # log files
from logging.handlers import RotatingFileHandler

###############################################################################
############# Classes #############
###################################


class isogeo2desktop():
    def __init__(self):
        print('Get your metadata in your GIS!')

        # creation and configuration of log file
        # see: http://sametmax.com/ecrire-des-logs-en-python/
        self.logger = logging.getLogger()
        logging.captureWarnings(True)
        self.logger.setLevel(logging.DEBUG)  # all errors will be get
        log_form = logging.Formatter('%(asctime)s || %(levelname)s || %(message)s')
        logfile = RotatingFileHandler('isogeo2desktop.log', 'a', 5000000, 1)
        logfile.setLevel(logging.DEBUG)
        logfile.setFormatter(log_form)
        self.logger.addHandler(logfile)
        self.logger.info('\t\t ============== Isogeo to desktop =============')  # start
        self.logger.info('Version: {0}'.format(_version))

        # load settings
        self.load_settings()

        # 

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
            # self.logger.info('Last options loaded')
            return (def_share_id, def_token), (def_proxy_type, def_proxy_host,
                                               def_proxy_port, def_proxy_user,
                                               def_proxy_pswd)
        except:
            # log
            self.logger.info('First use: previous settings not found.')
            return None

    def save_settings(self):
        u"""
        save last options in order to make the next excution more easy
        """
        confile = 'options.ini'
        config = ConfigParser.RawConfigParser()
        # add sections
        config.add_section('basics')
        config.add_section('isogeo')
        config.add_section('proxy')

        # basics
        config.set('basics', 'tool_version', version)
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
        self.logger.info('Options saved')

        # End of function
        return config


###############################################################################
###### Stand alone program ########
###################################

if __name__ == '__main__':
    """ standalone execution for testing """
    app = isogeo2desktop()
