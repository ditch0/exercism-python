import string


def rotate(text: str, key: int) -> str:
    encoded_chars = [encode_char(char, key) for char in list(text)]
    return ''.join(encoded_chars)


def encode_char(char: str, key: int) -> str:
    if char.isalpha():
        return encode_letter(char, key)
    else:
        return char


def encode_letter(letter: str, key: int) -> str:
    letter_index = string.ascii_lowercase.index(letter.lower())
    new_letter_index = (letter_index + key) % len(string.ascii_lowercase)
    new_letter = string.ascii_lowercase[new_letter_index]
    return new_letter if letter.islower() else new_letter.upper()
