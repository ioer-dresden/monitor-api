class URL:
    def __init__(self,_url):
        self.url = _url
        self.mapserver = "https://monitor.ioer.de/cgi-bin/"

    def extractUrl(self):
        service = False
        f = self.url.split("?")
        # extract the service
        try:
            if "wcs" in f[0]:
                service = "wcs"
            elif "wfs" in f[0]:
                service = "wfs"
            elif "wms" in f[0]:
                service = "wms"
            s = f[1].split("=")
            t = s[1].split("_")
            id = t[0]

            if service:
                return {"id":id,"service":service,"res":"{}{}?MAP={}_{}".format(self.mapserver,service,id,service)}
            else:
                return False
        except:
            return False
