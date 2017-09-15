import requests
from llpy.constants import URL


class LLpyException(Exception):
    def __init__(self, msg, full=None):
        super(LLpyException, self).__init__('Exception: ' + msg)
        if full:
            self.full_exc = full


class Base:
    def __init__(self, instance):
        self._inside = dict()
        raw = self.__get_the(instance)

        self.__parse(raw)

    # TODO should be added some more
    fields = ['id', 'name', 'countryCode', 'abbrev',
              'type', 'wikiURL', 'infoURLs', 'agencies',
              'relativeTime', 'duration', 'parentid',
              'imageURL', 'defaultPads', 'family',
              'mapURL', 'locationid', 'mapURL']


    def __getitem__(self, key):
        return self._inside[key]

    def __get_the(self, instance):
        try:
            r = requests.get(URL + instance[0] + '/' + instance[1]).json()[instance[2]][0]
            return r
        except Exception as e:
            raise LLpyException('error in request', str(e))

    def __parse(self, raw):
        try:
            for field in self.fields:
                if field in raw:
                    self._inside[field] = raw[field]
        except Exception as e:
            raise LLpyException('error while parsing', str(e))