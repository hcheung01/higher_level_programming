#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """class defined"""

    def __init__(self, width=0, height=0):
        """Initialization method
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Setter Method of width
        Args:
            value(int): width of square
        Raises:
            TypeError: if width is not integer
            ValueError: if width is less than zero
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Getter Method of width"""
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Sets the height of the rectangle
        Args:
            value(int): height of square
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Getter Method of height"""
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')
        self.__height = value
