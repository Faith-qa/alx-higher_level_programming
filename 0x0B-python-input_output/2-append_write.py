#!/usr/bin/python3
"""
Function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Appends string and returns the number of characters
    """
    chars_a = 0
    with open(filename, mode='a', encoding='utf-8') as a_file:
        chars_a = a_file.write(text)
        return chars_a
