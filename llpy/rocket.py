from llpy import Base


class Rocket(Base):
    instance_name = ['rocket', 'rockets']

    def __get_the(self, query):
        return Base.__get_the(self, query)


class RocketEvent(Base):
    instance_name = ['rocketevent', '']

    def __get_the(self, query):
        return Base.__get_the(self, query)


class RocketFamily(Base):
    instance_name = ['rocketfamily', 'RocketFamilies']

    def __get_the(self, query):
        return Base.__get_the(self, query)
