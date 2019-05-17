from typing import List


def is_divisible(number: int, divisor: int) -> bool:
    return number % divisor == 0


def prime_factors(number: int) -> List[int]:
    factors = []
    divisor = 2
    while number > 1:
        if is_divisible(number, divisor):
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return factors
