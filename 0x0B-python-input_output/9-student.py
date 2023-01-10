#!/usr/bin/python3
"""This a module that deals with files & input / output operations"""


class Student:
    '''This is a class named student'''

    def __init__(self, first_name, last_name, age):
        '''The constructor method'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''A method that retrieves a
        dictionary representation of a Student instance'''

        if attrs is None:
            return self.__dict__
        else:
            d = {}
            for k, v in self.__dict__.items():
                for item in attrs:
                    if item == k:
                        d[k] = v
        return d
