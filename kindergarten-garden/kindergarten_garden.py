from typing import List, Dict

_DEFAULT_STUDENTS = ['Alice', 'Bob', 'Charlie', 'David',
                     'Eve', 'Fred', 'Ginny', 'Harriet',
                     'Ileana', 'Joseph', 'Kincaid', 'Larry']

_PLANTS_NAMES = {
    'V': 'Violets',
    'C': 'Clover',
    'R': 'Radishes',
    'G': 'Grass',
}


class Garden(object):
    def __init__(self, diagram: str, students: List[str] = _DEFAULT_STUDENTS) -> None:
        plants = [char for char in diagram if char.isalpha()]

        self.__plants_by_students: Dict[str, List[str]] = {}
        for i, student in enumerate(sorted(students)):
            first_row_index = i * 2
            second_row_index = i * 2 + int(len(plants) / 2)
            first_row_plants = plants[first_row_index:first_row_index + 2]
            second_row_plants = plants[second_row_index:second_row_index + 2]
            self.__plants_by_students[student] = first_row_plants + second_row_plants

    def plants(self, student: str) -> List[str]:
        plants = self.__plants_by_students[student]
        return [_PLANTS_NAMES[plant] for plant in plants]
