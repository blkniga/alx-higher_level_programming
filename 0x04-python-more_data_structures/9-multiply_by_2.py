#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary = {}
    for k, v in a_dictionary.items():
        dictionary[k] = v*2
    return dictionary
