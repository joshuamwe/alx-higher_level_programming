#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    res = []
    tri = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(tri[y] + tri[y - 1])
        tri = row
        res.append(row)
    return res
