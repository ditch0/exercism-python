import re


def starts_with_vowel(word: str) -> bool:
    return word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt'))


def extract_starting_consonant(word: str) -> str:
    for cluster in ['ch', 'sh', 'qu', 'squ', 'rh', 'sch', 'thr', 'th']:
        if word.startswith(cluster):
            return cluster
    return word[0]


def translate(text: str) -> str:
    return re.sub(r'\w+', lambda match: translate_word(match.group(0)), text)


def translate_word(word: str) -> str:
    if starts_with_vowel(word):
        return word + 'ay'
    else:
        starting_consonant = extract_starting_consonant(word)
        return word[len(starting_consonant):] + word[:len(starting_consonant)] + 'ay'
