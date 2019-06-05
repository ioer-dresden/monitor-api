# -*- coding: utf-8 -*-
import os
import sys
import sys
import unittest
import codecs

from app.admin.services.GeoSN import *
from app.admin.services.URL import *


class GeoSnTest(unittest.TestCase):
    def test_UpdateUrl(self):
        geosn = GeoSN("C:/Users/user/Downloads/geosn/")
        print(geosn.update())


    def test_RenameFiles(self):
        path = 'C:/Users/user/Downloads/geosn/'

        for filename in os.listdir(path):
            if not filename.endswith('.xml'): continue
            file = os.path.join(path, filename)
            id_ind = "test"
            service ="test"
            try:
                with open(file, "r", encoding="utf-8") as fr:
                    doc = xmltodict.parse(fr.read())
                    fr.close()
                    doc_ind = doc["gmd:MD_Metadata"]["gmd:identificationInfo"]["srv:SV_ServiceIdentification"][
                        "srv:containsOperations"]
                    url_id = doc["gmd:MD_Metadata"]["gmd:identificationInfo"]["srv:SV_ServiceIdentification"][
                        "srv:containsOperations"][0]["srv:SV_OperationMetadata"]["srv:connectPoint"][
                        "gmd:CI_OnlineResource"]["gmd:linkage"]["gmd:URL"]
                    id_ind = url_id.split("?")
                    id_ind = id_ind[1]
                    id_ind = id_ind.split("=")
                    id_ind = id_ind[1].split("_")
                    id_ind = id_ind[0]

                    for op in doc_ind:
                        # extract id from the url
                        node = \
                        op["srv:SV_OperationMetadata"]["srv:connectPoint"]["gmd:CI_OnlineResource"]["gmd:linkage"][
                            "gmd:URL"]
                        url = URL(node).extractUrl()
                        if url:
                            op["srv:SV_OperationMetadata"]["srv:connectPoint"]["gmd:CI_OnlineResource"]["gmd:linkage"][
                                "gmd:URL"] = url["res"]
                            service = url["service"]

                with open(os.path.join(path, "{}_{}.xml".format(id_ind,service)), "w+",encoding="utf-8") as fw:
                    out = xmltodict.unparse(doc, pretty=True)
                    fw.write(out)
                    fw.close()

                #os.remove(file)

            except IOError as e:
                print(e)
                #os.remove(file)