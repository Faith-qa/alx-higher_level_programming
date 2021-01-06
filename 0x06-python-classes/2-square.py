#!/usr/bin/python3
"""defines a class square based on 1-square.py"""


class Square:
    """initializing size as an argument"""
    def __init__(self, size=0):
        """initializing new square with the size argument"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
