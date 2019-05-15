from typing import List

SUBLIST = 'sublist'
SUPERLIST = 'superlist'
EQUAL = 'equal'
UNEQUAL = 'unequal'


def check_lists(first_list: List, second_list: List) -> str:
    first_contains_second = list_contains(first_list, second_list)
    second_contains_first = list_contains(second_list, first_list)

    if first_contains_second and second_contains_first:
        return EQUAL

    if first_contains_second:
        return SUPERLIST

    if second_contains_first:
        return SUBLIST

    return UNEQUAL


def list_contains(first_list: List, second_list: List) -> bool:
    if first_list == [] and second_list == []:
        return True

    for start_index in range(len(first_list)):
        end_index = start_index + len(second_list)
        if first_list[start_index:end_index] == second_list:
            return True

    return False
