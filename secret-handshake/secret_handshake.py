COMMANDS = ['wink', 'double blink', 'close your eyes', 'jump']


def commands(number):
    binary = f'{number:05b}'
    actions = [
        command
        for i, command
        in enumerate(COMMANDS)
        if binary[4 - i] == '1'
    ]

    if binary[0] == '1':
        actions.reverse()

    return actions


def secret_code(actions):
    commands_codes = [
        2 ** i
        for i, command
        in enumerate(COMMANDS)
        if command in actions
    ]

    if is_reversed(actions):
        commands_codes.append(2 ** 4)

    return sum(commands_codes)


def is_reversed(actions):
    return len(actions) > 1 and COMMANDS.index(actions[0]) > COMMANDS.index(actions[1])
