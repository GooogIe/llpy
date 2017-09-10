from llpy.constants import URL
import requests


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
            # TODO: return a dict with all agencies
            pass

    def __parse(self):
        r = requests.get(URL + 'agency/' + self._agency).json()['agencies'][0]
        if r:
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
        else:
            raise Exception
