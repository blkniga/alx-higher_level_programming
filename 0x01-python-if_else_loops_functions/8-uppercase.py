#!/usr/bin/python3

def uppercase(string):
    s = ''
    for c in string:
        s = s + (chr(c) - 32)
    print("{}".format(s))
