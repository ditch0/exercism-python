_SCORES = [
    (1,  set('aeioulnrst')),
    (2,  set('dg')),
    (3,  set('bcmp')),
    (4,  set('fhvwy')),
    (5,  set('k')),
    (8,  set('jx')),
    (10, set('qz')),
]


def score(word: str) -> int:
    return sum(_get_score_for_letter(letter) for letter in word)


def _get_score_for_letter(letter: str) -> int:
    lowercase_letter = letter.lower()

    for letter_score, letters in _SCORES:
        if lowercase_letter in letters:
            return letter_score

    return 0
