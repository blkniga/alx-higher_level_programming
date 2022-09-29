#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for element in set(my_list):
        sum = sum + element
    return sum
