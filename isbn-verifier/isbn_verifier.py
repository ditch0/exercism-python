import functools
import re
from typing import List


def extract_isbn_numbers(isbn: str) -> List[int]:
    def process_char(numbers: List[int], char: str) -> List[int]:
        if char.isdigit():
            numbers += [int(char)]
        elif char == 'X':
            numbers += [10]
        return numbers

    return functools.reduce(process_char, isbn, [])


def is_valid_isbn_format(isbn: str) -> bool:
    normalized_isbn = isbn.replace('-', '')
    return re.match(r'^\d{9}[\dX]$', normalized_isbn) is not None


def is_valid_isbn(isbn: str) -> bool:
    numbers = extract_isbn_numbers(isbn)
    checksum = sum(n * (10 - i) for (i, n) in enumerate(numbers))
    return checksum % 11 == 0


def verify(isbn: str) -> bool:
    return is_valid_isbn_format(isbn) and is_valid_isbn(isbn)
