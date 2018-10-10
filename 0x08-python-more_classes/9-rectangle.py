#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Class of Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
            raise ValueError('width must be >= 0')
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
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """method to return area of width and height"""
        return self.__width * self.__height

    def perimeter(self):
        """method to return perimeter of width and height"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle area"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with size for width and height"""
        if size:
            return cls(size, size)
        else:
            pass

    def __str__(self):
        """method string object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for row in range(self.__height - 1):
            print(str(self.print_symbol) * self.__width)
        return str(str(self.print_symbol) * self.__width)

    def __repr__(self):
        """repr method"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """delete object/instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
