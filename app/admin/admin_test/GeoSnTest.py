import os
import sys
import unittest

from app.admin.services.GeoSN import *
from app.admin.services.URL import *


class GeoSnTest(unittest.TestCase):
    def test_UpdateUrl(self):
        path = 'C:/Users/user/Downloads/20190308_mds_ioer/'

        for filename in os.listdir(path):
            if not filename.endswith('.xml'): continue
            file = os.path.join(path, filename)
            try:
                with open(file,"r") as fr:
                    doc = xmltodict.parse(fr.read())
                    fr.close()
                    doc_ind = doc["gmd:MD_Metadata"]["gmd:identificationInfo"]["srv:SV_ServiceIdentification"]["srv:containsOperations"]
                    for op in doc_ind:
                        # extract id from the url
                        node = op["srv:SV_OperationMetadata"]["srv:connectPoint"]["gmd:CI_OnlineResource"]["gmd:linkage"]["gmd:URL"]
                        url = URL(node).extractUrl()
                        if url:
                            op["srv:SV_OperationMetadata"]["srv:connectPoint"]["gmd:CI_OnlineResource"]["gmd:linkage"]["gmd:URL"] = url["res"]

                with open(file,"w") as fw:
                    out = xmltodict.unparse(doc, pretty=True)
                    fw.write(out)
                    print(out)
                    fw.close()

            except:
                os.remove(file)
