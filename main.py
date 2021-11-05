def reverse_words(text):
    """
    A function that reverses every word in a string of words.
    """
    # Splitting our string into words.
    words = text.split(" ")
    # ::-1 reverses a string and does it for every word in words
    new_words = [word[::-1] for word in words]
    # Adding every iteration from our list
    # It starts with nothing, adds 1 word, adds another one until the
    # iteration is done.
    sentence = " ".join(new_words)
    return sentence

