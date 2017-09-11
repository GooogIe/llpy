import requests

from llpy import LLpyException
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
            except Exception as e:
                raise LLpyException('agency', str(e))

    def __parse(self):
        try:
            r = requests.get(URL + 'agency/' + self._agency).json()['agencies'][0]
        except Exception as e:
            raise LLpyException('error in request', str(e))
        try:
            self.agency_id = r['id']
            self.agency_name = r['name']
            self.agency_countryCode = r['countryCode']
            self.agency_abbrev = r['abbrev']
            self.agency_type = r['type']
            self.agency_wikiURL = r['wikiURL']
            self.agency_infoURLs = r['infoURLs'] if r['infoURLs'] else None
        except Exception as e:
            raise LLpyException('error while parsing', str(e))

    def search(self, query):
        try:
            return requests.get(URL + 'agency?name=' + query).json()['agencies']
        except Exception as e:
            raise LLpyException('search', str(e))


class AgencyType:
    def __init__(self, agency_type=None):
        try:
            if agency_type:
                r = requests.get(URL + 'agencytype/' + agency_type).json()['types'][0]
                self.type_id = r['id']
                self.type_name = r['name']
            else:
                self.agency_types = requests.get(URL + 'agencytype/').json()['types']
        except Exception as e:
            raise LLpyException('agency type', str(e))
