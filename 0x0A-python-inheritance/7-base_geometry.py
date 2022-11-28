#!/usr/bin/python3
'''This is the module for a class.'''


class BaseGeometry:
    """This is a class on geometry"""

    def area(self):
        """A method about an area of a class instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """The method validates and integer value.

        Args:
            name: A random string
            value: The integer value
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be an greater than 0")

