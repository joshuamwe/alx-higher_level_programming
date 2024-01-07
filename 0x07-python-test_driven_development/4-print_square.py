#!/usr/bin/python3
"""defines a function to print a square with character #"""


def print_square(size):
    """prints a square with character #

    Args:
        size (int): size length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
