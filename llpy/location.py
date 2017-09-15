import requests

from llpy import LLpyException, Base
from llpy.constants import URL


class Location(Base):
	instance_name = ['location', 'locations']
	def __get_the(self, query):
		return Base.__get_the(self, query)