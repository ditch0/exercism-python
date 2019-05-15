from typing import List

_ORDINALS = [
    None,
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth',
]

_PRESENTS = [
    None,
    'a Partridge in a Pear Tree',
    'two Turtle Doves',
    'three French Hens',
    'four Calling Birds',
    'five Gold Rings',
    'six Geese-a-Laying',
    'seven Swans-a-Swimming',
    'eight Maids-a-Milking',
    'nine Ladies Dancing',
    'ten Lords-a-Leaping',
    'eleven Pipers Piping',
    'twelve Drummers Drumming',
]


def recite(start_verse: int, end_verse: int) -> List[str]:
    return [create_verse(n) for n in range(start_verse, end_verse + 1)]


def create_verse(number: int) -> str:
    day_number = _ORDINALS[number]
    presents = join(get_presents_for_day(number))
    return 'On the {} day of Christmas my true love gave to me: {}.'.format(day_number, presents)


def get_presents_for_day(number: int) -> List[str]:
    return _PRESENTS[number:0:-1]


def join(items: List) -> str:
    if len(items) < 2:
        return ''.join(items)

    return ', '.join(items[:-1]) + ', and ' + items[-1]
