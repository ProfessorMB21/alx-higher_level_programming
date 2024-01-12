#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the bigger integer value"""

    if isinstance(a_dictionary, dict):
        scores = list(a_dictionary.values())
        largest = scores[0]
        for i in range(len(scores)):
            if scores[i] > largest:
                largest = scores[i]
        return largest
    return None

