from __future__ import  annotations
import datetime

from .diver import Diver
from .dive import Dive


class Contest:

    def __init__(self, name: str, date:datetime.date, warmup: int = 45, lines: int = 1) -> None:
        self.name = name
        self.date = date
        self.warmup = warmup
        self.lines = lines
        self._divers = set()
        self.days = []

    def add_diver(self, diver) -> None:
        self._divers.add(diver)

    def divers(self) -> set[Diver]:
        return self._divers.copy()

    def ranking(self, by_gender=True, by_discipline=True, by_nationality=False, nationality=None) -> list[Diver]:
        # by gender
        # by discipline
        # by nationality (corse pas corse pour les competitions regionales)
        pass

    def over_all(self, by_gender=True, nationality=None) -> list[Diver]:
        pass


class Day:

    def __init__(self, lines: int = 1):
        self.first_ot = None
        self.lines = lines
        self._dives = []

    def add_dive(self, dive: Dive) -> None:
        self._dives.append(dive)
