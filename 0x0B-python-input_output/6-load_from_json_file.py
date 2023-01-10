#!/usr/bin/python3
"""This a module that deals with files & input / output operations"""
import json


def load_from_json_file(filename):
    '''A function that creates an Object from a "JSON file" '''
    with open(filename, mode="r", encoding="UTF-8") as file:
        return json.load(file)
