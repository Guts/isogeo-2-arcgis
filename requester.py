# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from __future__ import unicode_literals
#-------------------------------------------------------------------------------
# Name:        Requete
# Purpose:     Requête sur l'outil de catalogage ISOGEO
#
# Author:      Marie et Sana
#
# Created:     10/04/2015
#-------------------------------------------------------------------------------

import urllib2
import json
import datetime
import xml.etree.ElementTree as ET

# Proxy de l'ecole
proxy = urllib2.ProxyHandler({'http': 'http://10.0.4.2:3128'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)




class Requete:

    def __init__(self, forma, url_OpenCatalog):
        self.forma=forma
        self.url_OpenCatalog=url_OpenCatalog

    def __sharetoken__(self):

        # Isoler l'identifiant du partage
        share_id = self.url_OpenCatalog.rsplit('/')[4]

        # Isoler le token du partage
        share_token = self.url_OpenCatalog.rsplit('/')[5]

        return share_token

    def __authentification__(self):

        # Isoler l'identifiant du partage
        share_id = self.url_OpenCatalog.rsplit('/')[4]

        # Isoler le token du partage
        share_token = self.url_OpenCatalog.rsplit('/')[5]

        # Ecriture de la requête à l'API
        search_req =urllib2.Request('http://api.isogeo.com/v1.0/resources/search?ct={0}&s={1}&format%3A{2}'.format(share_token, share_id, self.forma))

        # Envoi de la requête dans une boucle de test pour prévenir les erreurs
        try:
            search_resp = urllib2.urlopen(search_req)
            search_rez = json.load(search_resp)
            return search_rez

        except urllib2.URLError, e:
            return e


    def __result__(self):

        search_rez= self.__authentification__()
        metadatas = search_rez.get('results')
        
        dictionnaire={}
        for md in metadatas:

            date = md.get('_modified')[:10]+' '+ md.get('_modified')[11:26]
            dateConver = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")


            tags = search_rez.get('tags')
            for tag in tags.keys():
                if tag.startswith('coordinate-system'):
                    srs = tags.get(tag)
                else:
                    pass

            dictionnaire[md.get('_id')] = md.get('title'), dateConver, srs
        return dictionnaire

    def __importxml__(self):

        # Retourne un fichier XML
        share_token=self.__sharetoken__()
        id = "78e4a2ce9a7d4b09a80eecd131130166"
        req_xml =urllib2.Request('http://api.isogeo.com/v1.0/resources/{0}.xml?token={1}'.format(id, share_token))

        rez_xml = urllib2.urlopen(req_xml)
        xml = rez_xml.read()
        return xml


# Se connecter au catalogue de l'utilisateur
url_OpenCatalog = "http://open.isogeo.com/s/2f6805ccda5f4ffcaaed9aaf813d5201/G5bfYn1icopkDvaBuh82ptlz5Da60"

# Critères de requêtes de l'utilisateur
forma ="shp"

essai=Requete(forma, url_OpenCatalog)

print essai.__authentification__()
#print essai.__result__()
#print essai.__importxml__()
