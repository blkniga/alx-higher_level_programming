#!/usr/bin/python3
"""This is a module features a function which adds two integers"""


def add_integer(a, b=98):
    """This is a funtion that adds two integers.

    Args:
        a: This is the first parameter
        b: This is the second parameter

    Returns:
        An addition of two integers
    """
    if type(a) != int or type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int or type(b) != float:
        raise TypeError("b must be an integer")
    elif type(a) == float:
        a = int(a)
    elif type(b) == float:
        b = int(b)
    else:
        return a + b
