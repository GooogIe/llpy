from llpy import Base


class Agency(Base):
    instance_name = ['agency', 'agencies']

    def __get_the(self, query):
        return Base.__get_the(self, query)


class AgencyType(Base):
    def __get_the(self, query):
        return Base.__get_the(self, query)