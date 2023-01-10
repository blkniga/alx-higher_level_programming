#!/usr/bin/python3
"""This a module that deals with files & input / output operations"""


class Student:
    '''This is a class named student'''

    def __init__(self, first_name, last_name, age):
        '''The constructor method'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''A function that retrieves a dictionary representation
        of a Student instance'''
        return self.__dict__
