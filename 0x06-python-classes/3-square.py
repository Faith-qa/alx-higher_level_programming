#!/usr/bin/python3
"""defining a square based on 2-square.py"""


class Square:
    """defines a square by size"""
    def __init__(self, size=0):
        """initializing size argument"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """returns the area of a square"""
        area = self.__size * self.__size
        return area
