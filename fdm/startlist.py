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
