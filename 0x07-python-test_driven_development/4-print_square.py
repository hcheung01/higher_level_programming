#!/usr/bin/python3
"""
Print Square
"""
def print_square(size):
    """Prints a square with the character #
    Parameters:
    size = row and column size

    Return: None
    """
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if isinstance(size, int) is False:
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')
    for row in range(size):
        print('#' * size)
