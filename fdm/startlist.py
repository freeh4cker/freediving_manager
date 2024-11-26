from attr import dataclass


@dataclass
class Break:

    duration:int = 20


class Startlist:

    def __init__(self, day):
        self._day = day
        self._announces = []


    def divers(self):
        pass

    def insert_break(self, break_, index=-1):
        pass

    def deep_shallow(self):
        pass

    def shallow_deep(self):
        pass

    def shallow_deep_shallow(self, shallow_size=None):
        pass
