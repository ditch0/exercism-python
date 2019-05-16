from __future__ import annotations


class Clock(object):
    def __init__(self, hours: int, minutes: int) -> None:
        self.__minutes = (hours * 60 + minutes) % (24 * 60)

    @property
    def hours(self) -> int:
        return int(self.__minutes / 60)

    @property
    def minutes(self) -> int:
        return self.__minutes % 60

    def __repr__(self) -> str:
        return '{:02d}:{:02d}'.format(self.hours, self.minutes)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Clock):
            return False

        return self.__minutes == other.__minutes

    def __add__(self, minutes: int) -> Clock:
        return Clock(self.hours, self.minutes + minutes)

    def __sub__(self, minutes: int) -> Clock:
        return Clock(self.hours, self.minutes - minutes)
