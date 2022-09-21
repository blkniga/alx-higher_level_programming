#!/usr/bin/python3

def uppercase(string):
    s = ''
    for c in string:
        if chr(c) != range(97, 123):
            s = s + c
        else:
            s = s + (chr(c) - 32)
    print("{:s}".format(s))
