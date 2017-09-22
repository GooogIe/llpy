import requests
from llpy.constants import URL


class LLpyException(Exception):
    def __init__(self, msg, full=None):
        super(LLpyException, self).__init__('Exception: ' + msg)
        if full:
            self.full_exc = full


class Base:
    instance_name = []

    def __init__(self, query=None, copy=None):
        """
        copy -- if you have raw variant of the object
        """
        self._inside = dict()
        raw = self.__get_the(query) if query else copy

        self.__parse(raw)

    # TODO should be added some more
    fields = ['id', 'name', 'countryCode', 'abbrev',
              'type', 'wikiURL', 'infoURLs', 'agencies',
              'relativeTime', 'duration', 'parentid',
              'imageURL', 'defaultPads', 'family',
              'mapURL', 'locationid', 'mapURL',
              'description', 'launch', 'infoURL',
              'events']

    def __getitem__(self, key):
        return self._inside[key]

    def __requester(self, request):
        """
        request is '/1' or '?mode=verbose'    ----   '/' or '?' is necessary
        instance is a list e.g.   ['agency', 'agencies']
        """
        try:
            r = requests.get(URL + self.instance_name[0] + request).json()[self.instance_name[1]]
            return r
        except Exception as e:
            raise LLpyException('error in request', str(e))

    def __get_the(self, request):
        """
        instance is a list e.g.   ['agency', 'agencies']
        request    'nasa' or 1
        may return a list of instances
        """
        return self.__requester('/' + request)

    def __get_specific(self, **kwargs):
        """
        to use requests as https://launchlibrary.net/1.2/mission?launchid=12
          or https://launchlibrary.net/1.2/launch?mode=verbose&next=1
        may return a list of instances
        """
        request = '?' + '&'.join([key + '=' + val for key, val in kwargs.items()])
        return self.__requester(request)

    def __parse(self, raw):
        try:
            for field in self.fields:
                if field in raw:
                    self._inside[field] = raw[field]
        except Exception as e:
            raise LLpyException('error while parsing', str(e))