import requests


class GatewayWrapperService:
    def __init__(self):
        self.url = 'http://localhost:3000/'

    def getSites(self):
        r = requests.get(self.url + 'sites/sites?run=0')

        if r.status_code == 200:
            return r.json()['data']

    def updateSite(self, site_id, data):
        r = requests.put(self.url + 'sites/sites/' + str(site_id), data)
