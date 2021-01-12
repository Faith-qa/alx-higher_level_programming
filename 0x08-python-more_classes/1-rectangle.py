#!/usr/bin/python3
"""defining a rectangle based on 0-rectangle.py"""


class Rectangle:
    """defining the dimensions of the rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing a new rectangle.
        Args:
         width (int): the width ofthe rectangle
         height (int): the height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
            """get/set the height of the rectangle"""
            return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
