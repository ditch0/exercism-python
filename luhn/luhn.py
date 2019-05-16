class Luhn(object):
    def __init__(self, card_num: str) -> None:
        self.__card_num = card_num

    def is_valid(self) -> bool:
        if not self.__has_valid_format():
            return False
        return self.__calculate_check_sum() % 10 == 0

    def __calculate_check_sum(self) -> int:
        def double(digit: int) -> int:
            doubled = digit * 2
            return doubled if doubled <= 9 else doubled - 9

        digits = [int(char) for char in self.__card_num if char.isdigit()]
        odd_digits = digits[::-2]  # odd from right
        even_digits = digits[-2::-2]  # even from right
        doubled_even_digits = [double(digit) for digit in even_digits]

        return sum(doubled_even_digits) + sum(odd_digits)

    def __has_valid_format(self) -> bool:
        return self.__has_only_valid_characters() and self.__get_digits_count() > 1

    def __has_only_valid_characters(self) -> bool:
        return all(char.isdigit() or char == ' ' for char in self.__card_num)

    def __get_digits_count(self) -> int:
        return len([char for char in self.__card_num if char.isdigit()])
