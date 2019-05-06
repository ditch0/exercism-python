def is_armstrong_number(number: int) -> bool:
    digits = [int(char) for char in list(str(number))]
    digits_count = len(digits)
    powers_of_digits = [digit ** digits_count for digit in digits]
    return sum(powers_of_digits) == number
