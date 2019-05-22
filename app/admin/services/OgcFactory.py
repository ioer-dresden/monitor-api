from app.admin.services.WcsService import WcsService
from app.admin.services.WfsService import WfsService
from app.admin.services.WmsService import WmsService


class OgcFactory:
    def create_service(self,service,path=None):
        if service =='wms':
            return WmsService(path)
        elif service =='wcs':
            return WcsService(path)
        elif service=='wfs':
            return WfsService(path)