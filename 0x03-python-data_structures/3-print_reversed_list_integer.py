#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = reversed(my_list)
    for integer in l:
        print("{:d}".format(integer))
