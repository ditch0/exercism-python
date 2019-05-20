from typing import Tuple

EAST = 'east'
NORTH = 'north'
WEST = 'west'
SOUTH = 'south'


class Bearing:
    __BEARINGS = [NORTH, EAST, SOUTH, WEST]

    def __init__(self, value: str) -> None:
        self.__value = value

    def turn_right(self) -> None:
        self.__switch(1)

    def turn_left(self) -> None:
        self.__switch(-1)

    @property
    def value(self) -> str:
        return self.__value

    def __switch(self, delta: int) -> None:
        index = self.__BEARINGS.index(self.__value)
        new_index = (index + delta) % len(self.__BEARINGS)
        self.__value = self.__BEARINGS[new_index]


class Robot:
    def __init__(self, bearing: str = NORTH, x: int = 0, y: int = 0) -> None:
        self.__bearing = Bearing(bearing)
        self.__x = x
        self.__y = y

    def simulate(self, commands: str) -> None:
        for command in commands:
            self.__execute_command(command)

    def turn_right(self) -> None:
        self.__bearing.turn_right()

    def turn_left(self) -> None:
        self.__bearing.turn_left()

    def advance(self) -> None:
        if self.bearing == NORTH:
            self.__y += 1
        elif self.bearing == SOUTH:
            self.__y -= 1
        elif self.bearing == EAST:
            self.__x += 1
        elif self.bearing == WEST:
            self.__x -= 1

    @property
    def bearing(self) -> str:
        return self.__bearing.value

    @property
    def coordinates(self) -> Tuple[int, int]:
        return self.__x, self.__y

    def __execute_command(self, command: str) -> None:
        if command == 'L':
            self.turn_left()
        elif command == 'R':
            self.turn_right()
        elif command == 'A':
            self.advance()
