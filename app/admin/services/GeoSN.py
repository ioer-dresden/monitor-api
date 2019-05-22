# -*- coding: utf-8 -*-

from app.admin.interfaces.GeoSnService import GeoSnService
import xmltodict

# ToDo Weblaufwerk: https://monitor.ioer.de/ogc/  -> von Jörg erstellt auf Server ist es der Pfad: /srv/www/htdocs/monitor_ogc_xml/

class GeoSN(GeoSnService):

    def __init__(self):
        pass

    def update(self):
        pass

    def create(self, indicator, file_path=None):
        file = '../assets/1.xml'
        with open(file) as fd:
            doc = xmltodict.parse(fd.read())

        return doc

    def delete(self, file_path=None):
        pass
