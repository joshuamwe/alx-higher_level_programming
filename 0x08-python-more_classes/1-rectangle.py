#!/usr/bin/python3
"""writes a class that defines a Rectangle
    with private instance width and height

    Raises:
        TypeError: Height and width must be integers
        ValueError: height and width must be >= 0

    Returns: Original values and reset values of height
        and width
    """


class Rectangle:
    """represents a triangle"""
    def __init__(self, width=0, height=0):
        """initiliaze a rectangle

        args:
            height(int): new value of height. Defaults to 0
            width(int): new value of width. Defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """returns height value of rectangle"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """sets new value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """returns width value of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets new value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
