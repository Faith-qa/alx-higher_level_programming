#!/usr/bin/python3
"""
JSON represenationa
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using JSON rep
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(json.dumps(my_obj))
