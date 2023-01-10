#!/usr/bin/python3
"""This a module that deals with files & input / output operations"""
import json


def save_to_json_file(my_obj, filename):
    '''A function that writes an Object to a text file
    , using JSON representation'''
    with open(filename, mode="w", encoding="UTF-8") as file:
        json.dump(my_obj, file)
