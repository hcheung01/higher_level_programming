#!/usr/bin/python3
class Square:
    """square class"""

    def __init__(self, size=0):
        """initialization method"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """square value"""
        return (self.__size**2)
