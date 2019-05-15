from dataclasses import dataclass
from typing import List


@dataclass
class Student:
    name: str
    grade: int


class School(object):
    def __init__(self) -> None:
        self.__students: List[Student] = []

    def add_student(self, name: str, grade: int) -> None:
        self.__students.append(Student(name, grade))

    def roster(self) -> List[str]:
        sorted_students = sorted(self.__students, key=lambda student: (student.grade, student.name))
        return [student.name for student in sorted_students]

    def grade(self, grade_number: int) -> List[str]:
        names = [student.name for student in self.__students if student.grade == grade_number]
        return sorted(names)
