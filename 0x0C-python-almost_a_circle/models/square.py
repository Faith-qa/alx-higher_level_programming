#!/usr/bin/python3
"""
creating a square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a class that inherits from Rectangle
    """

    def __init__(self, size=int, x=0, y=0, id=None):
        """
        initializing attributes
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}". format(self.id, self.x, self.y,
                                                  self.width)

    @property
    def size(self):
        """
        getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter to size
        """
        self.__size = value
        self.width = self.height = value
