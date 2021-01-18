#!/usr/bin/python3
"""module for lookup()"""


def lookup(obj):
    """returns a list of an object's available attributes."""
    return(dir(obj))
