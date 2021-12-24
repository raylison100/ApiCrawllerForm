import os
import requests


class GatewayWrapperService:
    def __init__(self):
        self.url = os.getenv('GATEWAY_URL')

    def getSites(self):
        r = requests.get(self.url + 'sites/sites?run=0')

        if r.status_code == 200:
            return r.json()['data']

    def updateSite(self, site_id, data):
        requests.put(self.url + 'sites/sites/' + str(site_id), data)

    def listSensitive(self):
        r = requests.get(self.url + 'sites/check-words/sensitive')

        if r.status_code == 200:
            return r.json()['data']

    def listPersonal(self):
        r = requests.get(self.url + 'sites/check-words/personal')

        if r.status_code == 200:
            return r.json()['data']

    def sedInput(self, data):
        requests.post(self.url + 'sites/inputs/', data)
