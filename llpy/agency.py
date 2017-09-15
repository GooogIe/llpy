import requests

from llpy import LLpyException, Base
from llpy.constants import URL


class Agency(Base):
    instance_name = ['agency', 'agencies']
    def __get_the(self, query):
        return Base.__get_the(self, query)

    def search(self, query):
        try:
            return requests.get(URL + 'agency?name=' + query).json()['agencies']
        except Exception as e:
            raise LLpyException('search', str(e))


class AgencyType(Base):
    def __get_the(self, query):
        return Base.__get_the(self, query)