# -*- coding: utf-8 -*-

from app.admin.interfaces.GeoSnService import GeoSnService
import xmltodict

# ToDo Weblaufwerk: https://monitor.ioer.de/ogc/  -> von Jörg erstellt auf Server ist es der Pfad: /srv/www/htdocs/monitor_ogc_xml/

class GeoSN(GeoSnService):

    def __init__(self, _path='/srv/www/htdocs/monitor_ogc_xml/'):
        self.path = _path
        pass

    def update(self):
        pass

    def create(self, indicator):
        # schema file
        file = '../assets/geosn_schema.xml'
        with open(file) as fd:
            doc = xmltodict.parse(fd.read())

        return doc

    def delete(self):
        pass
