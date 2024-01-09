#!/usr/bin/python3
"""module prints to stdout content of a textfile"""


def read_file(filename=""):
    """opens and reads a textfile"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
