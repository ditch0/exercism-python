def hey(phrase: str) -> str:
    is_silence = phrase == '' or phrase.isspace()
    is_shouting = phrase.isupper()
    is_question = phrase.rstrip().endswith('?')

    if is_silence:
        return 'Fine. Be that way!'

    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"

    if is_shouting:
        return 'Whoa, chill out!'

    if is_question:
        return 'Sure.'

    return 'Whatever.'
