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
