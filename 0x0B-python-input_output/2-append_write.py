#!/usr/bin/python3
"""This a module that deals with files & input / output operations"""


def append_write(filename="", text=""):
    '''A function that appends a string at the end of a text file
    & returns the number of characters added'''
    with open(filename, mode="a", encoding="UTF-8") as file:
        return file.write(text)
