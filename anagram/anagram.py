from typing import List


def get_letters(word: str) -> List[str]:
    return sorted(list(word.lower()))


def is_anagram(word_a: str, word_b: str) -> bool:
    if word_a.lower() == word_b.lower():
        return False
    return get_letters(word_a) == get_letters(word_b)


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    return [c for c in candidates if is_anagram(word, c)]
