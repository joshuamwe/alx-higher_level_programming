#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a + b) * c - b

result = magic_calculation(70, 3, 4)
print(result)

