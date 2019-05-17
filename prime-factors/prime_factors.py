from typing import List


def is_divisible(number: int, divisor: int) -> bool:
    return number % divisor == 0


def prime_factors(natural_number: int) -> List[int]:
    factors = []
    divisor = 2
    quotient = natural_number
    while True:
        if is_divisible(quotient, divisor):
            factors.append(divisor)
            quotient = quotient // divisor
        else:
            divisor += 1
        if quotient == 1:
            break

    return factors
