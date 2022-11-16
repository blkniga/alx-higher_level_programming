#!/usr/bin/python3
"""This is a module that deals with a Square"""


class Square:
    """This is a class that defines a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """This is an initialization method.

        Args:
            size: The size parameter.

        """
        self.size = size
        self.position = position

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
    @property
    def position(self):
        """Returns the value of position"""
        return self.__position 

    @position.setter
    def position(self, value):
        """Sets the position attribute"""
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        """This is a method to return the current square area"""
        return self.__size**2

    def my_print(self):
        """This is a method that prints in the stdout the square in #"""
        if self.__size == 0:
            print('', end='\n')
        else:
            print('\n'*self.__position[1], end='')
            for i in range(self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
            
