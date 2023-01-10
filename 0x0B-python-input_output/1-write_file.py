#!/usr/bin/python3
"""This a module that deals with files & input / output operations"""


def write_file(filename="", text=""):
    '''A function that writes a text file
    & returns the number of characters written'''
    with open(filename, mode="w", encoding="UTF-8") as file:
        return file.write(text)
