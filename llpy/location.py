from llpy import Base


class Location(Base):
    instance_name = ['location', 'locations']

    def __get_the(self, query):
        return Base.__get_the(self, query)
