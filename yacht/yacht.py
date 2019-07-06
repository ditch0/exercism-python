from collections import Counter

YACHT = 'yacht'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'full_house'
FOUR_OF_A_KIND = 'four_of_a_kind'
LITTLE_STRAIGHT = 'little_straight'
BIG_STRAIGHT = 'big_straight'
CHOICE = 'choice'


def count_yacht(dice):
    if all(n == dice[0] for n in dice):
        return 50
    else:
        return 0


def count_same_numbers(dice, number):
    return sum(n for n in dice if n == number)


def count_ones(dice):
    return count_same_numbers(dice, 1)


def count_twos(dice):
    return count_same_numbers(dice, 2)


def count_threes(dice):
    return count_same_numbers(dice, 3)


def count_fours(dice):
    return count_same_numbers(dice, 4)


def count_fives(dice):
    return count_same_numbers(dice, 5)


def count_sixes(dice):
    return count_same_numbers(dice, 6)


def count_full_house(dice):
    counts = set(Counter(dice).values())
    if counts == {2, 3}:
        return sum(dice)
    else:
        return 0


def count_four_of_a_kind(dice):
    for n, count in Counter(dice).items():
        if count >= 4:
            return n * 4
    return 0


def count_little_straight(dice):
    if sorted(dice) == [1, 2, 3, 4, 5]:
        return 30
    else:
        return 0


def count_big_straight(dice):
    if sorted(dice) == [2, 3, 4, 5, 6]:
        return 30
    else:
        return 0


def count_choice(dice):
    return sum(dice)


def get_counter(category):
    try:
        return globals()[f'count_{category}']
    except KeyError:
        raise ValueError(f'Unsupported category: {category}')


def score(dice, category):
    counter = get_counter(category)
    return counter(dice)
