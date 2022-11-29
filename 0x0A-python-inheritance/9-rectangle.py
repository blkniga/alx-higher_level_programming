#!/usr/bin/python3
'''This is the module for a class Rectangle.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is the rectangle class"""

    def __init__(self, width, height):
        """This is the instantiation of the Rectangle class.
        Args:
            width: The width size
            height: The height size
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """This is the area method"""
        return self.__width * self.__height
    
    def __str__(self):
        """This is the string representation of the Rectangle object"""
        return f'[Rectangle] {self.__width}/{self.__height}'
