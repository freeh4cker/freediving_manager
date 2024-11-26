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

from dataclasses import dataclass
from enum import Enum, auto


class Discipline(Enum):

    CNF = auto()
    CWT = auto()
    CWTB = auto()
    FIM = auto()


class Card(Enum):

    WHITE = 1
    YELLOW = 2
    RED = 3


@dataclass
class Penalty:

    card: Card
    reason: str
    mult_penalty: int
    sub_penalty: int


class Remark(Penalty, Enum):

    DQ_SP = Card.RED, 'DQ surface protocol', 0, 0
    DQ_BO_UW = Card.RED, 'DQ Black out under water', 0, 0
    DQ_BO_SURFACE = Card.RED, 'DQ Black out surface', 0, 0
    DQ_AIRWAYS = Card.RED, 'DQ Airways', 0, 0
    DQ_PULL = Card.RED, 'DQ Pull', 0, 0
    DQ_TOUCH = Card.RED, 'DQ Touch', 0, 0
    DQ_LATE = Card.RED, 'DQ Late start', 0, 0
    DQ_DOLPHIN = Card.RED, 'DQ dolphin kick', 0, 0
    DQ_CHECKIN = Card.RED, 'DQ Check-in',0 , 0
    EARLY = Card.YELLOW, 'Early start', 1, 5
    GRAB = Card.YELLOW, 'Grab', 1, 10
    LANYARD = Card.YELLOW, 'Lanyard', 1, 10
    NO_TAG = Card.YELLOW, 'No tag', 1 , 1
    UNDER_AP = Card.YELLOW, 'Under Announce Perf', 1, 0
    OK = Card.WHITE, 'Ok', 1, 0
