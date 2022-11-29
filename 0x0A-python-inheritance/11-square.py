#!/usr/bin/python3
'''This is the module for a class Square.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is the square class"""

    def __init__(self, size):
        """This is the instantiation of the Square class.
        Args:
            size: The size of the square
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size
    
    def area(self):
        """This is the area method"""
        return self.__size * self.__size

    def __str__(self):
        """This is the string representation of the Square object"""
        return f'[Square] {self.__size}/{self.__size}'
