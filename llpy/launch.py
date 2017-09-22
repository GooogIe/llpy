from llpy import Base

from llpy.rocket import Rocket


class Launch(Base):
    instance_name = ['launch', 'launches']

    def __get_the(self, query):
        return Base.__get_the(self, query)

    def __parse(self, raw):
        Base.__parse(self, raw)
        self._inside['rocket'] = Rocket(copy=raw['rocket'])
        # TODO add other special fields
