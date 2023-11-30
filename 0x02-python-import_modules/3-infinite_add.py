#!/usr/bin/python3
if __name__ == "__main__":
    import sys

def add_arguments(*args):
    result = sum(int(arg) for arg in args)
    print(result)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_arguments(*arguments)
