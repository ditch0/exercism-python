import itertools
import re


def decode(string: str) -> str:
    matches = re.findall(r'(\d*)(\D)', string)
    decoded_groups = [
        character * int(digits or 1)
        for digits, character
        in matches
    ]
    return ''.join(decoded_groups)


def encode(string):
    groups = [
        (character, len(list(group)))
        for character, group
        in itertools.groupby(string)
    ]
    encoded_groups = [
        f'{count if count > 1 else ""}{character}'
        for character, count
        in groups
    ]
    return ''.join(encoded_groups)
