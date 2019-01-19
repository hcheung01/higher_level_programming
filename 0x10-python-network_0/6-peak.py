#!/usr/bin/python3
"""
Peak Module
"""


def find_peak(list_of_integers):
    """Find peak of a list"""

    if not len(list_of_integers):
        return None

    biggest = 0
    for i in range(len(list_of_integers)):
        if list_of_integers[i] > biggest:
            biggest = list_of_integers[i]
            if list_of_integers[i+1] and list_of_integers[i+1] <= biggest:
                return list_of_integers[i]
    return biggest
