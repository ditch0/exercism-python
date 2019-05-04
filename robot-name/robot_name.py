import random
import string


class Robot(object):
    used_names = set()

    def __init__(self):
        self.name = None
        self.reset()

    def reset(self) -> None:
        self.name = self.__generate_unique_name()

    @classmethod
    def __generate_unique_name(cls) -> str:
        while True:
            name = cls.__generate_name()
            if name not in cls.used_names:
                cls.used_names.add(name)
                return name

    @classmethod
    def __generate_name(cls) -> str:
        return cls.__generate_random_string(string.ascii_uppercase, 2) + cls.__generate_random_string(string.digits, 3)

    @staticmethod
    def __generate_random_string(chars: str, length: int) -> str:
        random_chars = random.choices(chars, k=length)
        return ''.join(random_chars)
