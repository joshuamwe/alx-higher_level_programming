#!/usr/bin/python3
"""defines class square

    Raises:
        TypeError: size should be an integer
        ValueError: value should be greater or equal to zero
    """


class Square:
    """represents  square"""
    def __init__(self, size=0):

        self.__size = int(size)

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
