#!/usr/bin/python3

"""Square class"""


class Square:
    """ Square class with size attribute"""
    def __init__(self, size=0):
        """
        Initializes Square class
        size: size of Square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns area of Square
        """
        return self.__size ** 2
