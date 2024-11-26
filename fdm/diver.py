#############################################################################
# Freediving Manager is a program to help to manage                         #
#            A Depth freediving Contest to manage start lists, results, ... #
# Authors: Bertrand Néron                                                   #
# Copyright (C) 2024  Bertrand Néron                                       #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                      #
# See the GNU General Public License for more details.                      #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program (COPYING).                                        #
# If not, see <https://www.gnu.org/licenses/>.                              #
#############################################################################

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
