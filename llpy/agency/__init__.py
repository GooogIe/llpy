import requests

from llpy.constants import URL


class Agency:
    def __init__(self, agency=None):
        self._agency = agency
        if agency is not None:
            self.agency_id = None
            self.agency_name = None
            self.agency_countryCode = None
            self.agency_abbrev = None
            self.agency_type = None
            self.agency_wikiURL = None
            self.agency_infoURLs = None

            self.__parse()

        else:
            try:
                self.agencies = requests.get(URL + 'agency').json()['agencies']
            except:
                raise Exception('error')

    def __parse(self):
        try:
            r = requests.get(URL + 'agency/' + self._agency).json()['agencies'][0]
        except:
            raise Exception('error in request')
        try:
            self.agency_id = r['id']
            self.agency_name = r['name']
            self.agency_countryCode = r['countryCode']
            self.agency_abbrev = r['abbrev']
            self.agency_type = r['type']
            self.agency_wikiURL = r['wikiURL']
            self.agency_infoURLs = r['infoURLs'] if r['infoURLs'] else None
        except:
            raise Exception

    def search(self, query):
        try:
            return requests.get(URL + 'agency?name=' + query).json()['agencies']
        except:
            raise Exception('error')
