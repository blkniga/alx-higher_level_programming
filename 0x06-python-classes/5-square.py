#!/usr/bin/python3
"""This is a module that deals with a Square"""


class Square:
    """This is a class that defines a Square with a public instance method
    & getter + setter"""

    def __init__(self, size=0):
        """This is an initialization method.

        Args:
            size: The size parameter.

        """
        self.size = size

    @property
    def size(self):
        """This is the getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """This is the setter"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
    
    def area(self):
        """This is a method to return the current square area"""
        return self.__size**2

    def my_print(self):
        """This is a method that prints in the stdout the square in #"""
        if self.__size = 0:
            print('', end='\n')
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#')
                    
