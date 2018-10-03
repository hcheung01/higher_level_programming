#!/usr/bin/python3
class Square:
    """class square 6"""

    def __init__(self, size=0, position=(0, 0)):
        """initialization method"""
        self.size = size
        self.postion = position

    @property
    def size(self):
        """getter method"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """getter method"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) == tuple:
            if len(value) == 2:
                if value[0] and value[1] == int:
                    if value[0] and value[1]:
                        self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """return square area"""
        return (self.__size**2)

    def my_print(self):
        """prints to stdout square with the char #"""
        if not self.__size:
            print()
        if self.postion[1]:
            print()

        for row in range(self.__size):
            for col in range(self.__size):
                print("{}".format('#'), end="")
            print()
