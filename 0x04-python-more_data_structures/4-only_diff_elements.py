#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    for x in set_1:
        for y in set_2:
            if x != y:
                return set(x)
