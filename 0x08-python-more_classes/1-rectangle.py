#!/usr/bin/python3
"""This defines the class Rectangle."""


class Rectangle:
    """Represents the class Rectangle."""
    def __init__(self, width=0, height=0):
        """Initialises the instance variables"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get/Set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
