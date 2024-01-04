#!/usr/bin/python3
"""writes a class that defines a rectangle with
    private instance attributes width and height

Raises:
    TypeError: both height and width must be integers
    ValueError: both height and width must be >= 0

Returns:
    values of height and width(new and original)
    rectangle area and perimeter

    Return the printable representation of the Rectangle.
"""


class Rectangle:
    """represents a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializes a rectangle

        args:
            width(int): new value of width. Defaults to 0.
            height(int): new value of height. Defaults to 0.
        """
        type(self).number_of_instances += 1
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

    def __str__(self):
        """Represents the rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """deletes rectangle instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
