import requests

from llpy import LLpyException, Base
from llpy.constants import URL


class Agency(Base):
    def __get_the(self, query):
        return Base.__get_the(self, ['agency', query, 'agencies'])

    def search(self, query):
        try:
            return requests.get(URL + 'agency?name=' + query).json()['agencies']
        except Exception as e:
            raise LLpyException('search', str(e))


class AgencyType(Base):
    def __get_the(self, query):
        return Base.__get_the(self, ['agencytype', query, 'types'])