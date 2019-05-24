import itertools
from typing import List


def multiples_of(number: int, limit: int) -> List[int]:
    if number == 0:
        return [0]

    iterator = itertools.takewhile(
        lambda n: n < limit,
        itertools.count(number, number)
    )
    return list(iterator)


def sum_of_multiples(limit: int, numbers: List[int]) -> int:
    multiples = [
        multiples_of(number, limit)
        for number
        in numbers
    ]
    unique_multiples = set(itertools.chain(*multiples))
    return sum(unique_multiples)
