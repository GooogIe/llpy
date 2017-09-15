import requests

from llpy import LLpyException, Base
from llpy.constants import URL


class Location(Base):
    def __get_the(self, query):
        return Base.__get_the(self, ['location', query, 'locations'])

    def search(self, query):
        try:
            return requests.get(URL + 'agency?name=' + query).json()['agencies']
        except Exception as e:
            raise LLpyException('search', str(e))