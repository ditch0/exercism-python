import re
import string


def encode(plain_text: str) -> str:
    normalized_text = re.sub(r'[^a-z\d]+', '', plain_text.lower())
    encoded_text = translate(normalized_text)
    return add_space_after_every_nth_character(encoded_text, n=5)


def decode(ciphered_text: str) -> str:
    return translate(ciphered_text.replace(' ', ''))


def add_space_after_every_nth_character(text: str, n: int) -> str:
    chunks = [text[i:i+n] for i in range(0, len(text), n)]
    return ' '.join(chunks)


def translate(text: str) -> str:
    table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])
    return text.translate(table)
