import requests

from llpy import LLpyException, Base
from llpy.constants import URL


class Agency(Base):
    def __get_the(self, agency):
        Base.__get_the(self, ['agency', agency, 'agencies'])

    def __parse(self, raw):
        Base.__parse(self, raw)

    def search(self, query):
        try:
            return requests.get(URL + 'agency?name=' + query).json()['agencies']
        except Exception as e:
            raise LLpyException('search', str(e))


class AgencyType(Base):
    def __get_the(self, agencytype):
        Base.__get_the(self, ['agencytype', agencytype, 'types'])