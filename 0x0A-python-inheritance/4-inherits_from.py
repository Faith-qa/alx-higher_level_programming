#!/usr/bin/python3
"""
Checks for inheritance
"""


def inherits_from(obj, a_class):
    """ checks for inheritnace """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
