#!/usr/bin/python3

def uppercase(str):
    string = ''
    for c in str:
        string = string + (chr(c) - 32)
    return print(string)
