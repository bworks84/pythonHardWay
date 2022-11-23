def break_words(sentence):
    '''This function will break up words for us.'''
    words = sentence.split(' ')
    return words


def sort_words(words):
    """Sort the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)


#print_first_word("You are here")


def print_last_word(words):
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
