CLOSING_BY_OPENING = {
    '(': ')',
    '[': ']',
    '{': '}',
}


def is_opening_bracket(char):
    return char in CLOSING_BY_OPENING.keys()


def is_closing_bracket(char):
    return char in CLOSING_BY_OPENING.values()


def is_pair(opening, closing):
    return CLOSING_BY_OPENING[opening] == closing


def is_paired(input_string):
    stack = []
    for char in input_string:
        if is_opening_bracket(char):
            stack.append(char)
        elif is_closing_bracket(char):
            if len(stack) == 0 or not is_pair(stack.pop(), char):
                return False

    return len(stack) == 0
