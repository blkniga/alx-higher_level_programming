#!/usr/bin/python3
def best_score(a_dictionary):
    lst = []
    for value in a_dictionary.values():
        lst.append(value)
    lst.sort()
    high = lst.pop()

    for k, v in a_dictionary.items():
        if v == high:
            name = k
    return name
