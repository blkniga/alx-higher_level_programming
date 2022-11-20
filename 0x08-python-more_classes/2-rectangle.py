#!/usr/bin/python3
"""This is the module level documentation about the class Rectangle."""


class Rectangle:
    """This is a class definition of a Rectangle."""

    def __init__(self, width=0, height=0):
        """This is the initialization method for the class Rectangle.

        Args:
            width: This is the width of the rectangle.
            height: This is the height of the rectange.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This is the method for retriving the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """This is the method for retriving the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """This function returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """This function returns the perimeter of rectangle."""
        if self.__width or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
