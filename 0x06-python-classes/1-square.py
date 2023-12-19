#!/usr/bin/python3
""" writes a class that defines a square
    with a private instance attribute size
    """


class Square:
    """ Defines the square and instances size """
    def __init__(self, size):
        self.__size = size
