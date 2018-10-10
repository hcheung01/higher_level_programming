#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:
    """Class of Rectangle"""

    number_of_instances = 0

    """class defined"""
    def __init__(self, width=0, height=0):
        """Initialization method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Setter Method of width"""
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
        """Setter Method of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Getter Method of height"""
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')
        self.__height = value

    def area(self):
        """method to return area of width and height"""
        return self.__width * self.__height

    def perimeter(self):
        """method to return perimeter of width and height"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """method string object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for row in range(self.__height - 1):
            print("#" * self.__width)
        return ('#' * self.__width)

    def __repr__(self):
        """repr method"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """delete object/instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
