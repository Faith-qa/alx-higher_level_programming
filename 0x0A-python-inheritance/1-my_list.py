#!/usr/bin/python3
"""module of a class, MyList that inherits from list"""


class MyList(list):
    """inherits from the class list"""
    def print_sorted(self):
        """prints a list sorted in assending order"""
        print(sorted(self))
