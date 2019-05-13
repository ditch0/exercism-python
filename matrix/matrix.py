from typing import List


class Matrix(object):
    def __init__(self, matrix_string: str):
        self.__data = self.__parse_from_string(matrix_string)

    def row(self, number: int) -> List[int]:
        index = number - 1
        return self.__data[index]

    def column(self, number: int) -> List[int]:
        index = number - 1
        return [row[index] for row in self.__data]

    @staticmethod
    def __parse_from_string(matrix_string: str) -> List[List[int]]:
        rows = matrix_string.split('\n')
        return [list(map(int, row.split())) for row in rows]
