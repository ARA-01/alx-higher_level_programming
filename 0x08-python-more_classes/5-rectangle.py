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

    def area(self):
        """Returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns the string representation of the Rectangle.

        Represent the Rectangle with # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle_str = []
        for i in range(self.__height):
            [rectangle_str.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle_str.append("\n")
        return ("".join(rectangle_str))

    def __repr__(self):
        """Return the string represnetation of the Rectangle."""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Prints a bye message for every deletion of the Rectangle."""
        print("Bye rectangle...")

