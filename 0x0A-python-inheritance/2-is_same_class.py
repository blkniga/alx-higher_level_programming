#!/usr/bin/python3
'''This is the module for a method checking instances.'''


def is_same_class(obj, a_class):
    """A method that checks if the object is exactly an instance of
    a specified class.

    Args:
        obj: The object to checked.
        a_class: The class to be checked against
    """
    if type(obj) == a_class:
        return True
    else:
        return False
