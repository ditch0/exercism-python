import re
from typing import List


def decode(string: str) -> str:
    decoded_groups = [
        character * int(digits or 1)
        for digits, character
        in re.findall(r'(\d*)(\D)', string)
    ]
    return ''.join(decoded_groups)


def encode(string):
    char_groups = _split_to_repeating_character_groups(string)
    encoded_groups = [_encode_repeating_character_group(group) for group in char_groups]
    return ''.join(encoded_groups)


def _split_to_repeating_character_groups(string: str) -> List[str]:
    groups = []
    prev_char = None
    group = ''
    for char in string:
        if char == prev_char or prev_char is None:
            group += char
        else:
            groups.append(group)
            group = char
        prev_char = char
    else:
        if group:
            groups.append(group)

    return groups


def _encode_repeating_character_group(group: str) -> str:
    if len(group) == 1:
        return group
    return '{}{}'.format(len(group), group[0])
