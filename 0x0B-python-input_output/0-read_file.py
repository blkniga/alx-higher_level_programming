#!/usr/bin/python3
"""This a module that deals with files & input / output operations"""


def read_file(filename=""):
    '''A function that reads a text file & prints it to stdout'''
    with open(filename, mode="r", encoding="UTF-8") as file:
        print(file.read())
