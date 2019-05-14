import functools
import re
from typing import Dict


def word_count(phrase: str) -> Dict[str, int]:
    words = re.findall(r'\d+|[a-z]+(?:\'[a-z]+)?', phrase.lower(), flags=re.IGNORECASE)

    def count_word(counts: Dict[str, int], word: str) -> Dict[str, int]:
        prev_count = counts.get(word, 0)
        counts[word] = prev_count + 1
        return counts

    return functools.reduce(count_word, words, {})
