#!/usr/bin/python3

def uppercase(string):
    s = ''
    for c in string:
        if ord(c) != range(97, 123):
            s = s + c
        else:
            s = s + (chr(ord(c)) - 32)
    print("{:s}".format(s))
