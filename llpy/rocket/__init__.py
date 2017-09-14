import requests

from llpy import LLpyException, Base
from llpy.constants import URL


class Rocket(Base):
    def __get_the(self, query):
        Base.__get_the(self, ['rocket', query, 'rockets'])

    def search(self, query):
        try:
            return requests.get(URL + 'agency?name=' + query).json()['agencies']
        except Exception as e:
            raise LLpyException('search', str(e))


class RocketEvent(Base):
    def __get_the(self, query):
        Base.__get_the(self, ['rocketevent', query, ''])


class RocketFamily(Base):
    def __get_the(self, query):
        Base.__get_the(self, ['rocketfamily', query, 'RocketFamilies'])
