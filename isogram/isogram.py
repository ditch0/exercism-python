import re


def is_isogram(string: str) -> bool:
    return _get_letters_count(string) == _get_unique_letters_count(string)


def _get_letters_count(string: str) -> int:
    letters_only = _remove_non_letters(string)
    return len(letters_only)


def _get_unique_letters_count(string: str) -> int:
    letters_only = _remove_non_letters(string)
    unique_letters = set(letters_only.lower())
    return len(unique_letters)


def _remove_non_letters(string):
    return re.sub(r'[^a-z]', '', string, flags=re.IGNORECASE)
