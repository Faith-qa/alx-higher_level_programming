#!/usr/bin/python3
"""first rectangle"""
from models.base import Base


class Rectangle(Base):
    """class inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        """getter for width"""
        def width(self):
            return self.__width

        @width.setter
        def width(self, width):
            if not isinstance(width, int):
                raise TypeError('width must be int')
            elif width < 0:
                raise ValueError('width must be >0')
            self.__width = width

        @property
        """getter for height"""
        def height(self):
            return self.__height

        @height.setter
        def height(self, height):
            if not isinstance(height, int):
                raise TypeError('height must be an int')
            elif height < 0:
                raise ValueError('height must be >0')
            self.__height = height

        @property
        """getter for x"""
        def x(self):
            return self.__x

        @x.setter
        def x(self, x):
            if not isinstance(x, int):
                raise TypeError('x must be an int')
            elif x < 0:
                raise ValueError('x must be >=0')
            self.__x = x

        @property
        """getter for y"""
        def y(self):
            return self.__y

        @y.setter
        def y(self, y):
            if not isinstance(y, int):
                raise TypeError('y must be an int')
            elif y < 0:
                raise ValueError('y must >=0')
            self.__y = y
