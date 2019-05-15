from typing import List

_ORDINALS = {
    1:  'first',
    2:  'second',
    3:  'third',
    4:  'fourth',
    5:  'fifth',
    6:  'sixth',
    7:  'seventh',
    8:  'eighth',
    9:  'ninth',
    10: 'tenth',
    11: 'eleventh',
    12: 'twelfth',
}

_PRESENTS = {
    1:  'a Partridge in a Pear Tree',
    2:  'two Turtle Doves',
    3:  'three French Hens',
    4:  'four Calling Birds',
    5:  'five Gold Rings',
    6:  'six Geese-a-Laying',
    7:  'seven Swans-a-Swimming',
    8:  'eight Maids-a-Milking',
    9:  'nine Ladies Dancing',
    10: 'ten Lords-a-Leaping',
    11: 'eleven Pipers Piping',
    12: 'twelve Drummers Drumming',
}


def recite(start_verse: int, end_verse: int) -> List[str]:
    return [create_verse(n) for n in range(start_verse, end_verse + 1)]


def create_verse(number: int) -> str:
    day_number = _ORDINALS[number]
    presents = join(get_presents_for_day(number))
    return 'On the {} day of Christmas my true love gave to me: {}.'.format(day_number, presents)


def get_presents_for_day(number: int) -> List[str]:
    return [_PRESENTS[n] for n in range(number, 0, -1)]


def join(items: List) -> str:
    if len(items) < 2:
        return ''.join(items)

    return ', '.join(items[:-1]) + ', and ' + items[-1]
