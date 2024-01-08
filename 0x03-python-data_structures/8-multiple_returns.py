#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character"""

    result = ()
    if len(sentence) == 0:
        result = (len(sentence), None)
        return result

    result = (len(sentence), sentence[0])
    return result

