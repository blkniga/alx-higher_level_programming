#!/usr/bin/python3
"""This a module that deals with files & input / output operations"""


def class_to_json(obj):
    '''A method that returns the dictionary description
    with simple data structure
    for JSON serialzation of an object'''
    return obj.__dict__
