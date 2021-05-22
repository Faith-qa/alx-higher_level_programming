#!/usr/bin/python3
"""adds 2 integers"""

def add_integer(a,b=98):
    """
    returns the sum of 2 integers
    """
    for i in (a, b):
        if i == a:
            if isinstance(i, (int, float)):
                a = int(i)
            else:
                raise TypeError("a must be an integer")
        if i == b:
            if isinstance(i, (int, float)):
                b = int(i)
            else:
                raise TypeError("b must be an integer")
    
    return a + b