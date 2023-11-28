#!/usr/bin/python3
def uppercase(s):
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            ascii_value -= 32
        print("{}".format(chr(ascii_value)), end="")
    print()
