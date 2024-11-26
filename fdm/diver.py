from enum import Enum, auto
from .rules import Discipline


class Gender(Enum):

    MALE = auto()
    FEMALE = auto()


class Diver:

    def __init__(self, first_name: str, last_name: str, gender: Gender, nationality: str, age: int = None) -> None:
        self.first_name = first_name.strip().capitalize()
        self.last_name = last_name.strip().capitalize()
        self.gender = gender
        self.nationality = nationality.strip().capitalize()
        self.age = age
        self._perfs = []


    def points_overall(self) -> int:
        perfs_per_discipline = {Discipline.CNF: [],
                               Discipline.FIM: [],
                               Discipline.CWT: [],
                               Discipline.CWTB: []
                              }
        for perf in self._perfs:
            perfs_per_discipline[perf.announce.discipline].append(perf.points)
        best_perfs = [max(v) for v in perfs_per_discipline.values() if v]
        points = sum(best_perfs) if best_perfs else 0
        return points

    def points_per_discipline(self, discipline: Discipline) -> int:
        selected_perf = [perf for perf in self.perfs if perf.discipline == discipline]
        points = max(selected_perf) if selected_perf else 0
        return points