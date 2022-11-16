#!/usr/bin/python3
"""This is a module that deals with a Square"""


class Square:
    """This is a class that defines a Square"""

    def __init__(self, size=0):
        """This is an initialization method.

        Args:
            size: The size parameter.

        """
        try:
            if size >= 0:
                self.__size = size
        except TypeError:
            print('size must be an integer')
        except ValueError:
            print('size must be >= 0')
