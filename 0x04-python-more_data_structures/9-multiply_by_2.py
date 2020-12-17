#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dic = a_dictionary.copy()
    for value in n_dic:
        n_dic[value] *= 2
    return n_dic
