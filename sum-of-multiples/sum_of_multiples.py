from typing import List


def sum_of_multiples(limit: int, numbers: List[int]) -> int:
    return sum({
        multiple
        for number in numbers
        if number > 0
        for multiple in range(number, limit, number)
    })
