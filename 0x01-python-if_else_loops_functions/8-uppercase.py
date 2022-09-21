#!/usr/bin/python3
def uppercase(str):
    string = ''
    for c in str:
        u = ord(c) - 32
        string = string + chr(u)
    return string
