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

    def __str__(self):
        return "[Square] ({}) {}/{} - {}". format(self.id, self.x, self.y,
                                                  self.width)

    @property
    def size(self):
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter to size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update arguments
        """
        attr = ['id', 'size', 'x', 'y']
        if args:
            for at, numb in zip(attr, args):
                setattr(self, at, numb)

        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)
