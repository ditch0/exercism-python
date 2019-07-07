import math
from itertools import combinations


def is_divisible(number, divisor):
    return number % divisor == 0


def at_least_one_is_divisible(a, b, divisor):
    return is_divisible(a, divisor) or is_divisible(b, divisor)


def triplets_with_sum(number):
    triplets = set()
    numbers = range(5, number, 5) if is_divisible(number, 25) else range(1, number)
    for a, b in combinations(numbers, 2):
        if a + b >= number:
            continue
        if not at_least_one_is_divisible(a, b, divisor=3):
            continue
        if not at_least_one_is_divisible(a, b, divisor=4):
            continue

        c = math.sqrt(a ** 2 + b ** 2)
        if int(c) != c:
            continue
        if a + b + c == number:
            triplets.add(tuple(sorted([a, b, int(c)])))
    return triplets
