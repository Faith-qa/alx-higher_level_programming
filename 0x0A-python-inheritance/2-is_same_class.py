#!/usr/bin/python3
"""module for 'is_same_class method"""


def is_same_class(obj, a_class):
    """function to check if object is instance of class
    Argument:
        obj: object to check
        a_class: specified class to check against
    Return:
       True if exactly an instance, otherwise false
    """
    return (type(obj) is a_class)
