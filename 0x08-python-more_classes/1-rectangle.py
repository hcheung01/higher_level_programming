#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """class defined
    """

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
        """Get the width of Rectangle object

        Returns:
            Value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter Method of width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Returns height of Rectangle object

        Returns:
            Value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
