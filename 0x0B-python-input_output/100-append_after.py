#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    with open(filename, "r+", encoding="utf-8") as f:
        s = ""
        for line in f:
            s += line
            if search_string in line:
                s += new_string
        f.seek(0)
        f.write(s)
