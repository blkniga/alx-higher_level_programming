#!/usr/bin/python3
"""This a module that deals with files & input / output operations"""
import json


def to_json_string(my_obj):
    '''A function that returns the JSON representation of an object (string)'''
    return json.dumps(my_obj)
