#!/usr/bin/python3
'''This is a module with one method that looks up methods & attributes.'''


def lookup(obj):
    '''The method returns a list of available methods & attributes.

    Args:
        obj: The object passed in
    '''
    return obj.__dir__()
