#!/usr/bin/python3
'''This is the module for a method checking instances.'''


def is_same_class(obj, a_class):
    """A method that checks if the object is an instance of, or
    if the object is an instance of a class that inherited from,
    the specified class

    Args:
        obj: The object to checked.
        a_class: The class to be checked against
    """
    if isinstance(obj, a_class) or type(obj) == a_class:
        return True
    else:
        return False
