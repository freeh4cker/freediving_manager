from .rules import Remark, Card, Discipline


class Announce:

    def __init__(self):
        self.discipline = None
        self.depth = None
        self.dive_time = None
        self.bottom_time = None


class Performance:

    def __init__(self, announce: Announce, depth: int, remarks: list[Remark]) -> None:
        self._announce = announce
        self.depth = depth
        self.remarks = remarks
        self._points = None

    @property
    def points(self) -> int:
        return self._points


    @property
    def announce(self) -> Announce:
        return self._announce

    @property
    def discipline(self) -> Discipline:
        return self.announce.discipline

    def compute_points(self) -> int:
        """
        
        :return:
        """
        points = self.depth
        for remark in self.remarks:
            if remark.card == Card.RED:
                points = 0
                break
            if remark == Remark.UNDER_AP:
                points -= self._announce.depth - self.depth
            else:
                points *= remark.mult_penalty
                points -= remark.sub_penalty
        return max(0, points)

    def set_result(self, perf, remarks):
        pass


class Dive:

    def __init__(self, diver, announce: Announce) -> None:
        self.diver = diver
        self.announce = announce
        self.performance = None
        self.official_time = None
        self.lane = None


