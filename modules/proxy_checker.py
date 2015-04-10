# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals
# ------------------------------------------------------------------------------
# Name:         Proxy checker
# Purpose:      Just a couple of functions to check various proxy configuration
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
import urllib2
import socket
import sys
import string
import os

# 3rd party libraries
import arcpy

###############################################################################
############ Functions ############
###################################

# execfile("parameters.py")

def is_bad_proxy(pip):
    """
    TO COMMENT
    """
    try:
        proxy_handler = urllib2.ProxyHandler({'http': pip})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req=urllib2.Request('http://www.example.com')  # change the URL to test here
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print 'Error code: ', e.code
        return e.code
    except Exception, detail:
        print "ERROR:", detail
        return True
    return False

def main():
    """
    TO COMMENT
    """
    socket.setdefaulttimeout(120)

    # two sample proxy IPs
    proxyList = ['10.0.4.2:3128', '{0}:{1}'.format(prox, port),
                 '{0}://{1}:{2}@{3}:{4}'.format(protocole, user, password, prox, port)]

    for currentProxy in proxyList:
        if is_bad_proxy(currentProxy):
            print "Bad Proxy %s" % (currentProxy)
            arcpy.AddMessage("Bad Proxy")
        else:
            print "%s is working" % (currentProxy)
            arcpy.AddMessage("is working")

###############################################################################
###### Stand alone program ########
###################################

if __name__ == '__main__':
    """ standalone execution for testing """
    pass
