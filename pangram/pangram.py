import string


def is_pangram(sentence: str) -> bool:
    lowercase_sentence = sentence.lower()
    for letter in string.ascii_lowercase:
        if letter not in lowercase_sentence:
            return False

    return True
