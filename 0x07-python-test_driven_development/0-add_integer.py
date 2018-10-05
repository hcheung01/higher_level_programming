#!/usr/bin/python3
"""Module to sum

add_integer: adds two integers and return

"""

def add_integer(a, b=98):
    """Return sum of a + b
    Args: a = int/float b = int/float
    """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return int(a + b)
