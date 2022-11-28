#!/usr/bin/python3
'''This is the module for a class Rectangle.'''


class Rectangle(BaseGeometry):
    """This is the rectangle class"""

    def __init__(self, width, height):
        """This is the instantiation of the Rectangle class.

        Args:
            width: The width size
            height: The height size
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
