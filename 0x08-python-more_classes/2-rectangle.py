#!/usr/bin/python3
"""writes a class that defines a rectangle with
    private instance attributes width and height

Raises:
    TypeError: both height and width must be integers
    ValueError: both height and width must be >= 0

Returns:
    values of height and width(new and original)
    rectangle area and perimeter
"""


class Rectangle:
    """represents a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes a rectangle

        args:
            width(int): new value of width. Defaults to 0.
            height(int): new value of height. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
