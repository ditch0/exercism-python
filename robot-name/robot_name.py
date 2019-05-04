import random
import string


class Robot(object):
    used_names = set()

    def __init__(self):
        self.name = None
        self.reset()

    def reset(self) -> None:
        self.name = self.__generate_unique_name()

    def __generate_unique_name(self) -> str:
        while True:
            name = self.__generate_name()
            if name not in self.used_names:
                self.used_names.add(name)
                return name

    def __generate_name(self) -> str:
        return self.__generate_random_string(string.ascii_uppercase, 2) + self.__generate_random_string(string.digits, 3)

    def __generate_random_string(self, chars: str, length: int) -> str:
        random_chars = random.choices(chars, k=length)
        return ''.join(random_chars)
