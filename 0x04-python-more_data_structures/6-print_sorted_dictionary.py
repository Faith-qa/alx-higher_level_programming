#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_list = (sorted(a_dictionary))
    for keys in s_list:
        print("{}: {}".format(keys, a_dictionary[keys]))
