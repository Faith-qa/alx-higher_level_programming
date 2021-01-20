#!/usr/bin/python3
"""
write to a file
"""


def write_file(filename="", text=""):
    """
    returns the number of characters that are written
    Args:
       filename(str) : name of the file
      text(str) : text to write
    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
