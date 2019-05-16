def square_of_sum(count: int) -> int:
    return sum(range(count + 1)) ** 2


def sum_of_squares(count: int) -> int:
    squares = [number ** 2 for number in range(count + 1)]
    return sum(squares)


def difference(count: int) -> int:
    return abs(sum_of_squares(count) - square_of_sum(count))
