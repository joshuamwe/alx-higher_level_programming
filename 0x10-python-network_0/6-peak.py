#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: A peak in the list of integers.
    """
    n = len(list_of_integers)

    """Check the edge cases"""
    if n == 0:
        return None
    elif n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)

    """Use binary search to find a peak"""
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
