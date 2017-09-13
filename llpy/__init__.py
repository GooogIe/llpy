import requests
from llpy.constants import URL

class LLpyException(Exception):
    def __init__(self, msg, full=None):
        super(LLpyException, self).__init__('Exception: ' + msg)
        if full:
            self.full_exc = full


class Base:
    def __init__(self, instance):
        raw = self.__get_the(instance)
        self.__parse(raw)

    def __get_the(self, instance):
        try:
            r = requests.get(URL + instance[0] + '/' + instance[1]).json()[instance[2]][0]
            return r
        except Exception as e:
            raise LLpyException('error in request', str(e))

    def __parse(self, raw):
        # TODO should be added some more
        try:
            if 'id' in raw:
                self.id = raw['id']
            if 'name' in raw:
                self.name = raw['name']
            if 'countryCode' in raw:
                self.countryCode = raw['countryCode']
            if 'abbrev' in raw:
                self.abbrev = raw['abbrev']
            if 'type' in raw:
                self.type = raw['type']
            if 'wikiURL' in raw:
                self.wikiURL = raw['wikiURL']
            if 'infoURLs' in raw:
                self.infoURLs = raw['infoURLs'] if raw['infoURLs'] else None

        except Exception as e:
            raise LLpyException('error while parsing', str(e))