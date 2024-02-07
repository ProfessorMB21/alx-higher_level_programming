#!/usr/bin/python3
""" Defines a function that prints text """

def text_indentation(text):
    """
    Prints text with two new lines after each of these characters
    Characters: `.', `?', `:`

    Args:
        text (str): A string of words

    Raises:
        TypeError: If text is not of type `str`
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for word in range(len(text)):
        if text[word] not in [":", ".", "?"]:
            print(text[word], end="")
        else:
            if text[word] == ' ':
                continue
            print(text[word], end="\n\n")


