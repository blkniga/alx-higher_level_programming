#!/usr/bin/python3
"""This is a module that deals with a Square"""


class Square:
    """This is a class that defines a Square with a public instance method"""

    def __init__(self, size=0):
        """This is an initialization method.

        Args:
            size: The size parameter.

        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    def area(self):
        """This is a method to return the current square area"""
        return size**2
