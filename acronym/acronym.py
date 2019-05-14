import re
from typing import List


def abbreviate(phrase: str) -> str:
    words = _split_to_words(phrase)
    first_letters = [word[0] for word in words]
    uppercase_first_letters = [letter.upper() for letter in first_letters]
    return ''.join(uppercase_first_letters)


def _split_to_words(phrase: str) -> List[str]:
    return re.findall(r'\d+|[a-z]+(?:\'[a-z]+)?', phrase.lower(), flags=re.IGNORECASE)
