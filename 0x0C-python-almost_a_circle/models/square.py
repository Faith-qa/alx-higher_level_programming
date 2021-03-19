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
        return "[Square] ({}) {}/{} -{}/". format(self.id, self.x, self.y,
                                                  self.width, self.height)
