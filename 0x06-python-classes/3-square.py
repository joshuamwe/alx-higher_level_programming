#!/usr/bin/python3
"""defines a class square

    Raises:
        TypeError: size should be an integer
        ValueError: value of size always 0 or greater than 0

    Returns:
        Area: area of square for both original and initial size
    """


class Square:
    """represent a class square"""
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """determines and returns the area"""
        return (self.__size * self.__size)
