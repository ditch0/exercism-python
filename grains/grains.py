def square(number: int) -> int:
    ensure_square_number_is_valid(number)
    return 2 ** (number - 1)


def total(number: int) -> int:
    ensure_square_number_is_valid(number)
    return sum(square(n) for n in range(1, number + 1))


def ensure_square_number_is_valid(number: int):
    if number < 1 or number > 64:
        raise ValueError('Number must between 1 and 64')
