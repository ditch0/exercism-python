from typing import List, Iterable


def flatten(iterable: Iterable) -> List:
    flat_list = []
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, str):
            flat_list += flatten(item)
        elif item is not None:
            flat_list.append(item)

    return flat_list
