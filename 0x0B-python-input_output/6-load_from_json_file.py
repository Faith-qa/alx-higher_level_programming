#!/usr/bin/python3
"""
import json module
"""
import json


def load_from_json_file(filename):
    """create object from a JSON file"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        return json.load(a_file)
